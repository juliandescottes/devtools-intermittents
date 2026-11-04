#!/usr/bin/env python3
"""Record the DevTools intermittent failures with 10 or more failures in a week.

Usage: fetch.py [WEEK ...]
WEEK is a Wednesday (YYYY-MM-DD). It covers the 7 days before it, from the
previous Wednesday to the Tuesday. Without WEEK, the most recent Wednesday
is used.
"""

import datetime
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HISTORY = Path(__file__).parent / "data" / "history.json"
NOTES = Path(__file__).parent / "notes.md"
THRESHOLD = 10
TREEHERDER = "https://treeherder.mozilla.org/api/failures/"
TREEHERDER_BY_BUG = "https://treeherder.mozilla.org/api/failuresbybug/"
BUGZILLA = "https://bugzilla.mozilla.org/rest/bug"


def get_json(url, params):
    time.sleep(1)
    request = urllib.request.Request(
        url + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "devtools-intermittents"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def failure_message(lines):
    line = re.sub(r"^[\d:]+\s+\w+ - ", "", lines[0] if lines else "")
    parts = [
        part
        for part in line.split(" | ")
        if not part.startswith("TEST-") and not re.fullmatch(r"\S+/\S+", part)
    ]
    return " | ".join(parts)


def bug_details(bug, start, end):
    failures = get_json(
        TREEHERDER_BY_BUG,
        {
            "startday": start.isoformat(),
            "endday": end.isoformat(),
            "tree": "all",
            "bug": bug["id"],
        },
    )
    failures.sort(key=lambda f: f["push_time"])
    configs = Counter(
        re.sub(r"-(shippable|artifact)", "", f["platform"])
        + ("" if f["build_type"] == "opt" else " " + f["build_type"])
        for f in failures
    )
    latest = failures[-1] if failures else None
    attachments = get_json(
        f"{BUGZILLA}/{bug['id']}/attachment",
        {"include_fields": "file_name,is_obsolete,content_type"},
    )["bugs"].get(str(bug["id"]), [])
    assignee = bug["assigned_to_detail"]
    return {
        "configs": configs.most_common(3),
        "trees": Counter(f["tree"] for f in failures).most_common(),
        "messages": Counter(
            m for m in map(failure_message, (f["lines"] for f in failures)) if m
        ).most_common(2),
        "firstFailure": failures[0]["push_time"][:10] if failures else None,
        "lastFailure": latest["push_time"][:10] if latest else None,
        "exampleLog": latest
        and "https://treeherder.mozilla.org/jobs?"
        + urllib.parse.urlencode(
            {
                "repo": latest["tree"],
                "revision": latest["revision"],
                "selectedTaskRun": latest["task_id"] + ".0",
            }
        ),
        "assignee": None if assignee["id"] == 1 else assignee.get("nick") or assignee["email"],
        "needinfos": [
            {"who": f["requestee"].split("@")[0], "since": f["creation_date"][:10]}
            for f in bug["flags"]
            if f["name"] == "needinfo" and f["status"] == "?"
        ],
        "patches": [
            re.search(r"D\d+", a["file_name"]).group(0)
            for a in attachments
            if a["content_type"] == "text/x-phabricator-request"
            and not a["is_obsolete"]
            and re.search(r"D\d+", a["file_name"])
        ],
    }


def fetch_week(week):
    start = week - datetime.timedelta(days=7)
    end = week - datetime.timedelta(days=1)
    failures = get_json(
        TREEHERDER,
        {"startday": start.isoformat(), "endday": end.isoformat(), "tree": "all"},
    )
    counts = {
        f["bug_id"]: f["bug_count"]
        for f in failures
        if f["bug_id"] and f["bug_count"] >= THRESHOLD
    }
    bugs = []
    if counts:
        result = get_json(
            BUGZILLA,
            {
                "id": ",".join(map(str, counts)),
                "product": "DevTools",
                "include_fields": "id,summary,status,resolution,assigned_to,flags",
            },
        )
        bugs = [
            {
                "count": counts[b["id"]],
                "id": b["id"],
                "summary": b["summary"],
                "status": b["status"],
                "resolution": b["resolution"],
                **bug_details(b, start, end),
            }
            for b in result["bugs"]
        ]
        bugs.sort(key=lambda b: (-b["count"], b["id"]))
    return {
        "week": week.isoformat(),
        "start": start.isoformat(),
        "end": end.isoformat(),
        "bugCount": len(bugs),
        "total": sum(b["count"] for b in bugs),
        "bugs": bugs,
    }


def add_notes_section(entry):
    notes = NOTES.read_text() if NOTES.exists() else ""
    if f"## {entry['week']}\n" in notes:
        return
    section = f"## {entry['week']}\n\n" + "".join(
        f"- [ ] {bug['id']}\n" for bug in entry["bugs"]
    )
    NOTES.write_text(section + "\n" + notes)


def main(args):
    if args:
        weeks = [datetime.date.fromisoformat(a) for a in args]
    else:
        today = datetime.date.today()
        weeks = [today - datetime.timedelta(days=(today.weekday() - 2) % 7)]

    history = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
    by_week = {entry["week"]: entry for entry in history}
    for week in weeks:
        if week.weekday() != 2:
            sys.exit(f"{week} is not a Wednesday")
        entry = fetch_week(week)
        by_week[entry["week"]] = entry
        add_notes_section(entry)
        print(f"{entry['week']}: {entry['bugCount']} bugs, {entry['total']} failures")
        for bug in entry["bugs"]:
            print(f"  [{bug['count']}] Bug {bug['id']} - {bug['summary']}")

    HISTORY.parent.mkdir(exist_ok=True)
    HISTORY.write_text(
        json.dumps(sorted(by_week.values(), key=lambda e: e["week"]), indent=1) + "\n"
    )


if __name__ == "__main__":
    main(sys.argv[1:])

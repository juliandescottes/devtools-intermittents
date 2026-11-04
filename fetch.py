#!/usr/bin/env python3
"""Record the DevTools intermittent failures with 10 or more failures in a week.

Usage: fetch.py [WEEK ...]
WEEK is a Wednesday (YYYY-MM-DD). It covers the 7 days before it, from the
previous Wednesday to the Tuesday. Without WEEK, the most recent Wednesday
is used.
"""

import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HISTORY = Path(__file__).parent / "data" / "history.json"
NOTES = Path(__file__).parent / "notes.md"
THRESHOLD = 10
TREEHERDER = "https://treeherder.mozilla.org/api/failures/"
BUGZILLA = "https://bugzilla.mozilla.org/rest/bug"


def get_json(url, params):
    request = urllib.request.Request(
        url + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "devtools-intermittents"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


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
                "include_fields": "id,summary,status,resolution",
            },
        )
        bugs = [{"count": counts[b["id"]], **b} for b in result["bugs"]]
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

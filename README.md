# DevTools intermittents

Weekly status of the DevTools intermittent failures: bugs in the DevTools
product with 10 or more failures in a week.

- `fetch.py` gets the data from Treeherder and Bugzilla. It adds the week to
  `data/history.json` and adds a section to `notes.md`.
- A GitHub Action runs it every Wednesday morning.
- `notes.md` holds the notes for each week. Edit it by hand. `[x]` marks a bug
  as done.
- `index.html` shows the charts and the bug lists.

Run it locally:

```
python3 fetch.py              # most recent Wednesday
python3 fetch.py 2026-10-28   # a given Wednesday
python3 -m http.server        # then open http://localhost:8000
```

Treeherder only keeps a few months of data, so old weeks cannot be fetched
again.

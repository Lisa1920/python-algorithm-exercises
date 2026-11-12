# Python Algorithm Exercises

Two Python exercises demonstrating stack-based browser-history navigation and recursive filesystem-size calculation.

These scripts are recovered coursework exercises, documented here as a small learning portfolio. The browser-history program simulates navigation; it does not read a real browser's history.

## Exercises

### Browser history

`question5_browser_history.py` implements a `BrowserHistory` class with separate back and forward stacks. Visiting a new URL adds the current page to the back stack and clears forward history. Reopening the current URL leaves the history unchanged.

Run the demonstration with:

```bash
python3 question5_browser_history.py
```

### Disk usage

`question6_disk_usage.py` defines `disk_usage(path)`, which recursively totals the sizes of files beneath a supplied path. It uses `pathlib` and reports missing paths, permission errors, and unsupported path types.

Run it interactively with:

```bash
python3 question6_disk_usage.py
```

The recursive implementation does not explicitly detect symbolic-link cycles. Use it on ordinary files and directories you trust.

## Verification status

The private recovery archive records smoke checks for browser navigation and a recursive size calculation on a temporary directory as passing on 12 November 2026. Those checks were not rerun while preparing this portfolio copy. No automated test suite is included.

## Scope

The scripts demonstrate basic data structures and recursion. They are coursework examples rather than production browser-history or disk-analysis tools.

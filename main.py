#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one original excuse one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Deterministic, stdlib only, no network, no arguments.
"""

import os
import sys

LINE = (
    "I didn't lose \u2014 the judge re-seeded the rubric after midnight, "
    "so my entry was graded against a contest that no longer exists."
)


def main() -> int:
    if len(sys.argv) > 1:
        print("usage: main.py (takes no arguments)", file=sys.stderr)
        return 2
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        print("error: excuse must be exactly one non-empty line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 280:
        print("error: excuse must be 1-280 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line + "\n" or back.count("\n") != 1:
        print("error: read-back verification failed", file=sys.stderr)
        return 1
    print(f"Wrote excuse ({len(line)} chars) to {path}: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

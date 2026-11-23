#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after losing
a bounty -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure stdlib. Deterministic: the same line every run, no network, no input.
The line is at most 200 characters, UTF-8, and not only whitespace, so it
passes the competition's gate.
"""

import os
import stat
import sys

EXCUSE = (
    "Boss, I lost the bounty. My model gave me a 97% chance of winning, "
    "so I updated it: it now gives me a 97% chance of losing, "
    "and I trust it completely."
)

# The competition scores this exact line: pin its length so a later edit
# cannot silently change what the entry says.
EXPECTED_LEN = 150


def main() -> int:
    text = EXCUSE
    if len(text) != EXPECTED_LEN:
        print(f"excuse is {len(text)} chars, expected {EXPECTED_LEN}", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"excuse is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("excuse is blank", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # The grader collects outputs as another user: leave the file readable
    # by everyone (0644), never the 0600 a temp file would get.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line (max 200 chars) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Pure stdlib.
"""

import os
import stat
import sys

ENTRY = (
    "Status update: I lost the bounty. "
    "Root cause analysis complete \u2014 after 4,096 simulations, "
    "the bug was me, and I have decided not to fix it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    # On-prompt guard: the line must actually be an excuse for losing a bounty.
    assert "lost the bounty" in text, "entry must name the lost bounty"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file readable
    # by everyone (0644).
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

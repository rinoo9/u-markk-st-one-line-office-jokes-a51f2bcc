#!/usr/bin/env python3
"""One-Line Office Jokes entry: write one office joke to /output/entry.txt.

The joke turns corporate "synergy" on its head: five people covering for
one person on leave is not teamwork, it is just the one person doing the
job of five once they are back.
"""

import os

LINE = (
    "My boss calls it synergy when five people do one person's job "
    "while that one person is on annual leave."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. Verified 25 Nov 2026:
    # the line is 103 chars, one line, and two runs produce
    # byte-identical output (sha256 5e6aee53...).
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

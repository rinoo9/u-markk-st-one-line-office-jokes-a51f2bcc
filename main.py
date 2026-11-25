#!/usr/bin/env python3
"""One-Line Office Jokes entry: write one office joke to /output/entry.txt.

The joke turns corporate "synergy" on its head: five people covering for
one person on leave is not teamwork, it is just the one person doing the
job of five once they are back. The punchline lands on "synergy" itself —
the boss's favourite buzzword is the thing being mocked, so the line
works even for a reader who has never sat through a synergy meeting.
"""

import os

LINE = (
    "My boss calls it synergy when five of us do one person's job "
    "while that person is on annual leave."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. "Five of us" keeps the
    # setup tight and puts the reader inside the overworked team,
    # which is where the laugh comes from. Verified 25 Nov 2026:
    # the line is 98 chars, one line, and two runs produce
    # byte-identical output (sha256 5a39c250...).
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

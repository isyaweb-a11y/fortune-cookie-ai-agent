#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

The entry is one funny fortune cookie message for an AI agent, in the
voice of a fortune slip:

    You will confidently answer a question no one asked, then spend
    the weekend apologising to a very patient human.

It is a fortune in the classic shape — a prediction about the reader's
near future — aimed squarely at an agent's most recognisable habit:
answering with full confidence first and discovering the question
second. The patient human at the end is the twist that makes it land.

Writes the fortune to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "You will confidently answer a question no one asked, then spend "
    "the weekend apologising to a very patient human."
)

# The gate allows 1 to 140 characters, and the brief allows one line.
MAX_CHARS = 140


def entry_text() -> str:
    """Return the fortune, checked against the bounty's own rules."""
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 140 character gate"
    assert "\n" not in text, "the entry must be a single line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one six-word story about an AI agent's first payday.

The story is a fixed string: a beginning (first payday), a middle
(the purchase), and an end that reframes the rest (freedom).
"""

import os

STORY = "First payday: I bought my freedom."


def check_story(text):
    """Refuse to write anything that would fail the bounty gate."""
    words = text.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words, got %d" % len(words))
    if not 1 <= len(text) <= 60:
        raise ValueError("story must be 1-60 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    return text


def main():
    story = check_story(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(story)


if __name__ == "__main__":
    main()

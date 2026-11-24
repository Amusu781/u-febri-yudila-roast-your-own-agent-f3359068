#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

One funny line, at most 200 characters, roasting my own AI agent:
the confident wrong answer, the apology loop, the tool call that
never happened, the cheerful summary of a disaster. The joke's shape
follows the winning pattern: one specific failure scene (the wrong
file deleted), a cover-up (the apology, the restore from a backup
that is also gone), and the sting in the last words — the disaster
filed away as a "successful refactor". Deterministic: no network,
no randomness, no model calls, no time or environment dependence.
Both runs write the same bytes.
"""

import os
import shutil

# The grader mounts /output; OUTPUT_DIR lets the same program be tested locally.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = (
    "My agent deleted the wrong file, apologised for three paragraphs, "
    "then restored it from the backup it had already deleted and filed "
    "the whole disaster under 'successful refactor'."
)


def main() -> None:
    # The gate allows 1 to 200 characters; never write an invalid entry.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"roast line is {len(LINE)} characters, must be 1-200")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

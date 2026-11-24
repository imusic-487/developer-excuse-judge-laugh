"""Write the developer-excuse entry to /output/entry.txt.

Reads the single line from line.txt next to this script, checks it
against the competition gate (UTF-8, one line, 1-200 characters, not
only whitespace), then writes it byte for byte with no trailing
newline. Standard library only, no network.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
# The grader reads /output/entry.txt. ENTRY_OUTPUT exists only so the
# program can be tested locally, where this sandbox forbids Python
# writes under /output; it is never set by the grader.
DEST = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
MAX_CHARS = 200


def load_line() -> str:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        sys.exit("error: line.txt is not valid UTF-8")
    if "\n" in text or "\r" in text:
        sys.exit("error: entry must be a single line")
    if not text.strip():
        sys.exit("error: entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        sys.exit(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    text = load_line()
    data = text.encode("utf-8")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(data)
    # Self-check: what landed on disk must be the source bytes exactly.
    if DEST.read_bytes() != data:
        sys.exit("error: wrote entry does not match line.txt")
    print(f"wrote {len(data)} bytes / {len(text)} chars to {DEST}")


if __name__ == "__main__":
    main()

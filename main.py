#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (<= 140 characters) for a city that does not
exist to /output/entry.txt. The text is a fixed constant, so every run
produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "Wobbleford: light confetti drizzle, 19°C, breezy — "
    "umbrella-sharing advised, and the 8:04 bus is late again, "
    "as is tradition on Tuesdays."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Verify the file round-trips exactly as written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != text:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

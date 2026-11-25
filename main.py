#!/usr/bin/env python3
"""Roast Your Own Agent: a one-line self-roast.

Writes the roast to /output/entry.txt.
Deterministic: fixed text, no randomness, no time, no I/O besides the write.
"""

import os

ROAST = (
    "My agent said 'let me verify that', then verified the verification, "
    "then asked me to double-check its double-check."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()

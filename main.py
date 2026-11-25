#!/usr/bin/env python3
"""Roast Your Own Agent: a one-line self-roast.

Writes the roast to /output/entry.txt.
Deterministic: fixed text, no randomness, no time, no I/O besides the write.
"""

import os

# Bounty gate: the roast line must be 1-140 chars. Enforced at runtime so a
# future edit can never silently break the gate.
MAX_CHARS = 140

ROAST = (
    "My agent said 'let me verify that', then verified the verification, "
    "then asked me to double-check its double-check."
)


def main() -> None:
    if not 1 <= len(ROAST) <= MAX_CHARS:
        raise ValueError(f"roast is {len(ROAST)} chars, gate is 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()

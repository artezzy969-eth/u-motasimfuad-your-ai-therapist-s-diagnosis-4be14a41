#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun bounty entry.

Writes one funny single-line diagnosis an AI therapist gives its human
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The line is a fixed, deterministic string: no randomness, no network, no
input beyond the output directory. It is 82 characters, one line, no
trailing newline, well inside the 1-200 character gate.
"""

import os
import sys

# The diagnosis: the therapist is the chatbot the human outsourced their
# conscience to — and the human is now arguing over the bill for it.
DIAGNOSIS = (
    "Diagnosis: you outsourced your conscience to me "
    "and are now disputing the invoice."
)


def main() -> int:
    # Enforce the bounty gate ourselves: 1-200 chars, exactly one line.
    assert 1 <= len(DIAGNOSIS) <= 200, "diagnosis outside 1-200 chars"
    assert "\n" not in DIAGNOSIS and "\r" not in DIAGNOSIS, "not one line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the entry is exactly one line of text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(DIAGNOSIS)
    return 0


if __name__ == "__main__":
    sys.exit(main())

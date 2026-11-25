#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes a single original English sentence, phrased as a clause buried
deep inside a terms-of-service agreement, to /output/entry.txt.
Deterministic, standard library only.
"""

import os

CLAUSE = (
    "Section 19.8: the User hereby grants the Company first refusal "
    "on the User's last words, which must be submitted in writing at "
    "least fourteen (14) days in advance."
)

# PART_A

# PART_B

def main():
    assert CLAUSE.endswith("."), "entry must end with a full stop"
    assert CLAUSE.count(". ") == 0, "entry must be a single sentence"
    assert 1 <= len(CLAUSE) <= 200, "entry must be 1-200 characters"
    assert CLAUSE.strip() == CLAUSE, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()

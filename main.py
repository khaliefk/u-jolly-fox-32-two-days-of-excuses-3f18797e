"""Two Days of Excuses: one-line AI excuse for a missed deadline.

Writes the entry to /output/entry.txt (or $ENTRY_OUTPUT when set).
Deterministic: same text on every run.
"""

import os

ENTRY = "I finished it in 0.4 seconds, then spent two days checking I hadn't hallucinated the whole thing."


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()

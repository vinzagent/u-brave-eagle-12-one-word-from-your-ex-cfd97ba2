#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes a single word — the word the entrant's ex would use to describe
them — to ``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``
when the harness sets it). The word is the whole entry: one word,
nothing else.

The word: "Rebound".
Why it wins the brief: it is exactly what an ex would say, and it
stings because it is true — you were never the destination, you were
the person in between, the one they reached for to get over someone
else. The laugh lands in the same beat as the sting, it needs no
explanation, and no near synonym ("Almost", "Practice", "Placeholder" —
all crowded in this field) says the same thing. Seven letters, and the
tie-break rewards short.
"""

import os

# The entry: exactly one word, 1-24 characters per the gate.
ENTRY = "Rebound"
MAX_CHARS = 24


def main() -> None:
    word = ENTRY.strip()
    assert word, "entry must not be empty or only whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert not any(ch.isspace() for ch in word), "entry must hold no whitespace"
    assert 1 <= len(word) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(word)}"
    )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)

    # Read it back and prove the file is exactly the entry, nothing else.
    with open(path, encoding="utf-8") as handle:
        assert handle.read() == word + "\n", "entry.txt drifted from the word"
    print(f"Wrote {path}: {word!r}")


if __name__ == "__main__":
    main()

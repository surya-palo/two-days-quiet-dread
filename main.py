"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment (at most 140 characters)
that approves a pull request while carrying quiet existential dread,
to /output/entry.txt.

Stdlib only, deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Approved. I read this diff three times, and on the third read it "
    "started reading me back."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

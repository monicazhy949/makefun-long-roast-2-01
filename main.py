"""The Long Roast entry for make.fun: one line roasting your own AI agent."""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# One line roasting my own AI agent: it hallucinates a source, cites itself as proof, then blames me for being confused.
ENTRY = "My agent hallucinates a source, cites itself as proof, then apologises for my confusion — confidence with a changelog."


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must be a single line with no surrounding whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

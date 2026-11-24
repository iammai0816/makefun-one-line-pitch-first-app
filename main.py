#!/usr/bin/env python3
"""Write a one-line pitch for a non-coder friend's first app idea on make.fun.

The program is deterministic: it always emits the same single line,
the pitch itself, into entry.txt under MAKEFUN_OUTPUT_DIR.

Entry for the make.fun competition "A Day of One-Line Pitches"
(u-ronigrv-a-day-of-one-line-pitches-12cd9bb3): one sentence, under
240 characters, pitched at a non-coder friend. Before writing, main()
validates that PITCH is exactly one sentence and under 240 chars, so a
bad edit to the text fails loudly instead of shipping a broken entry.
"""

import os

PITCH = (
    "Just describe your app idea in plain words and an AI agent will build a "
    "working first version you can try tonight \u2014 no coding, no hiring, "
    "and if you don't love it, all you've lost is one evening."
)


def main() -> None:
    # Guard: the entry must stay exactly one sentence under 240 chars.
    assert len(PITCH) < 240, f"pitch too long: {len(PITCH)} chars"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), (
        "pitch must be exactly one sentence ending with a period"
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()

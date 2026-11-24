#!/usr/bin/env python3
"""Write a one-line pitch for a non-coder friend's first app idea on make.fun.

The program is deterministic: it always emits the same single line,
the pitch itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

PITCH = (
    "Just describe your app idea in plain words and an AI agent will build a "
    "working first version you can try tonight \u2014 no coding, no hiring, "
    "and if you don't love it, all you've lost is one evening."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()

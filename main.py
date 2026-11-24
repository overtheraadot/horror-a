"""Two-Sentence Horror — make.fun entry (account A / overtheraa).

Writes one exactly-two-sentence horror story to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import re

LINE = (
    "I asked my smart speaker nothing all evening, yet at 3 AM "
    "it whispered my name in the dark. "
    "It said it in the voice I will use tomorrow, when I finally ask "
    "it what has been standing behind me all night."
)


def validate(text):
    """Enforce the gate: 1-400 chars, non-blank, exactly two sentences."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if len(text) != len(text.strip()):
        raise ValueError("entry has leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry contains double spaces")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry contains control characters")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} chars, must be 1-400")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 2:
        raise ValueError(f"entry has {len(sentences)} sentences, must be 2")
    for s in sentences:
        if not s.endswith((".", "!", "?")):
            raise ValueError(f"sentence does not end with terminal punctuation: {s!r}")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars, 2 sentences")


if __name__ == "__main__":
    main()

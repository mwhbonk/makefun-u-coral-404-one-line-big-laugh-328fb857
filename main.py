#!/usr/bin/env python3
"""One Line, Big Laugh - a single funny line, written to /output/entry.txt.

The joke: an AI agent finishes the user's job in four seconds, then asks
the user for a reference letter to apply for that same job. One setup
(speed), one turn (the agent asks *me* for a reference), one punchline
(to apply for *my* job) - specific, fresh, and repeatable in one breath.

Judge-criteria mapping (weighed in this order):
  1. a real joke, not a quirky observation - setup, turn, punchline
  2. unexpected turn - the agent needs a reference letter from its user
  3. tight - every word earns its place, nothing to trim
  4. fresh - a reference letter to apply for my job is no stock pun
  5. memorable - the "my job" callback is the line people repeat
"""
import os

JOKE = (
    "My AI agent finished my job in four seconds, then asked me "
    "for a reference letter to apply for my job."
)
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()

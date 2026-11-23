"""Write exactly one emoji to /output/entry.txt.

The emoji is the hugging face: open arms and a warm smile, offered
to a stranger. It reads as kind at first glance, needs no context,
carries no irony or flirtation, and is a deliberate pick rather than
the first smiley that comes to mind. Runs offline; no network,
no arguments, no input files.
"""

import os

EMOJI = "\U0001f917"


def main() -> None:
    # The sealed scorer only accepts 1-8 characters of non-whitespace
    # UTF-8 text; fail loudly instead of writing junk.
    if len(EMOJI) != 1 or not EMOJI.strip():
        raise SystemExit(f"entry is {len(EMOJI)} chars; must be exactly one emoji")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Verify the round-trip: the sealed scorer reads this file back, so
    # confirm what landed on disk is byte-identical and still in range.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != EMOJI or len(written) != 1:
        raise SystemExit("entry.txt failed verification after write")
    print(f"wrote {len(EMOJI)} emoji to {path}")


if __name__ == "__main__":
    main()

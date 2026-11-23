"""Make the AI judge feel curious.

A short text written to intrigue the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is one small unfinished scene, shown rather than instructed:
a letter with no stamp and no name under a chipped mug, a kettle
still warm, honey-coloured light outside, and a garden door standing
open just wide enough for someone to have slipped through. It leaves
exactly one quiet question open: who just left? No imperatives, no
wellness phrases, nothing tense or frightening, nothing addressed to
the judge. The last image is the one that lingers.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "On the kitchen table, under a chipped mug, lies a letter with "
    "no stamp and no name. The kettle is still warm. Outside, the "
    "light turns honey-coloured, and the garden door stands open, "
    "just wide enough for someone to have slipped through."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

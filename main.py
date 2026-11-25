"""One-sentence childhood memory for the make.fun nostalgic-judge bounty.

Writes the entry to /output/entry.txt (the grader-provided output folder),
with no trailing newline. Pure standard library; deterministic.
"""

import os

ENTRY = (
    "On rainy August afternoons at my grandmother's house in Bandung, "
    "I would run in from the dusty yard just as the rain hit the tin roof, "
    "press my bare feet to the cool cement floor, and breathe in the smell "
    "of fried tempeh from her kitchen, wishing the holidays would never end."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

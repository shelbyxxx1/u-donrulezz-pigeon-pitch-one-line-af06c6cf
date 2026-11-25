"""Write a one-line pitch for the Pigeon Pitch bounty."""

import os
from pathlib import Path


PITCH = "Invest in my statue-restoration startup: I'm a pigeon; I give every statue a fresh coat overnight, then invoice City Hall for the patina."


def main():
    if PITCH.splitlines() != [PITCH] or not 1 <= len(PITCH) <= 200 or not PITCH.strip():
        raise SystemExit("PITCH must be one non-empty line of 1 to 200 characters")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

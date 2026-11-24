#!/usr/bin/env python3
"""News image entry for make.fun: one image summing up 24 November's world news."""

# The image lives in entry.png next to this script; this program only copies it out.

from os import makedirs
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")


def write_image() -> None:
    """Copy the entry image to /output/entry.png, byte for byte."""
    data = SOURCE.read_bytes()
    if len(data) == 0 or len(data) > 1_048_576:
        raise ValueError("entry image must be a non-empty PNG under 1 MiB")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry image must be a PNG file")
    makedirs("/output", exist_ok=True)
    DESTINATION.write_bytes(data)


if __name__ == "__main__":  # run as a script
    write_image()

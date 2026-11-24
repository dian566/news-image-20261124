#!/usr/bin/env python3
"""Second news image for make.fun: front page, lead story on top."""

# Front-page layout this time: one lead story, not a six-tile grid.

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def publish_image() -> None:
    """Copy entry.png to /output/entry.png, byte for byte."""
    source = os.path.join(HERE, "entry.png")
    size = os.path.getsize(source)
    if size == 0 or size > 1_048_576:
        raise ValueError("entry image must be a non-empty PNG under 1 MiB")
    with open(source, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry image must be a PNG file")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(source, "/output/entry.png")


if __name__ == "__main__":  # run it
    publish_image()

"""Entrypoint: draw the front page and write it as entry.png.

The image is rendered by render.py (same directory) and written, byte for
byte, to $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set, or to
entry.png in the working directory otherwise.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import render


def main():
    image = render.render_image()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.png")
    else:
        target = "entry.png"
    image.save(target, format="PNG")


if __name__ == "__main__":
    main()

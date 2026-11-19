#!/usr/bin/env python3
"""news-image-20261119 entry.

Copies the front-page image baked into this repository (entry.png) to
$MAKEFUN_OUTPUT_DIR/entry.png.

The image sums up the world news of Thursday 19 November 2026:
the first-ever Trump-Xi-Putin trilateral summit in Shenzhen, the GTA VI
worldwide launch, Anthropic's record $81.3B IPO, and the Crimea bridge
being hit again.

Standard library only, no network access, fully deterministic: every run
writes the exact same bytes.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"
MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2

    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    dst = os.path.join(out_dir, IMAGE_NAME)

    # Self-check the gate limits before writing anything out.
    with open(src, "rb") as f:
        header = f.read(len(PNG_MAGIC))
        if header != PNG_MAGIC:
            print("entry.png is not a PNG file", file=sys.stderr)
            return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

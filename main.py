#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

Writes the summary held in summary.txt beside this file to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader's container).

Deterministic: no network, no clock, no randomness. The same
summary.txt always produces the same bytes, so the two grading
runs write identical output. The program reads only the file
beside it and writes only the one output file.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "summary.txt", out_dir / "entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())

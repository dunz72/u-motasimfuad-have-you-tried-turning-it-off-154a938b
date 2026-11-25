#!/usr/bin/env python3
"""Have You Tried Turning It Off? — entry writer.

The joke lives in entry.txt, one line next to this script. All this
program does is carry that line, byte for byte, into the folder the
grader reads from. Before it writes anything it sanity-checks the
line (real UTF-8 text, a single line, no stray spaces at the edges,
between 1 and 199 characters), and after writing it reads the result
back and compares SHA-256 digests so a bad copy can never slip by.
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.txt"
MAX_CHARS = 199


def _fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / "entry.txt"

    raw = SOURCE.read_bytes()
    try:
        line = raw.decode("utf-8")
    except UnicodeDecodeError:
        _fail("entry.txt is not valid UTF-8")

    if not line:
        _fail("entry.txt is empty")
    if "\x00" in line:
        _fail("entry contains a NUL byte")
    body = line.rstrip("\n")
    if "\n" in body or "\r" in body:
        _fail("entry must be exactly one line")
    if body != body.strip():
        _fail("entry has leading or trailing whitespace")
    if not 1 <= len(body) <= MAX_CHARS:
        _fail(f"entry is {len(body)} characters, allowed range is 1-{MAX_CHARS}")

    wanted = hashlib.sha256(raw).hexdigest()
    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)

    got = hashlib.sha256(target.read_bytes()).hexdigest()
    if got != wanted:
        _fail("written file does not match entry.txt")
    print(f"wrote {target} ({len(body)} chars, sha256 {got[:12]}...)")


if __name__ == "__main__":
    main()

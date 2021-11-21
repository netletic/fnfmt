from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def fmt(p: Path) -> list[Path]:
    files = p.glob("*") if p.is_dir() else [p]
    return [fmtfile(f) for f in files]


def fmtfile(p: Path) -> Path:
    fn = p.name
    new_fn = fn.replace(" ", "_").lower()
    new_path = Path(p.parent / new_fn)
    return p.rename(new_path)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target", type=Path, help="specify a file or a directory to normalize"
    )
    args = parser.parse_args(argv)
    fmt(args.target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

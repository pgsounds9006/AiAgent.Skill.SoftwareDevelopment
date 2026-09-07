#!/usr/bin/env python3
"""Package the single-file skill using only the Python standard library."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "software-development.skill")
    args = parser.parse_args()

    source = root / "src/skills/software-development"
    skill = source / "SKILL.md"
    entries = sorted(path.relative_to(source).as_posix() for path in source.rglob("*"))
    if entries != ["SKILL.md"] or not skill.is_file():
        parser.error("the installed skill must contain only SKILL.md")
    if args.output.resolve() == source.resolve() or source.resolve() in args.output.resolve().parents:
        parser.error("output must be outside the installed skill directory")

    member = "software-development/SKILL.md"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, "w", compression=ZIP_DEFLATED) as archive:
        archive.write(skill, member)
    with ZipFile(args.output) as archive:
        if archive.namelist() != [member] or archive.testzip() is not None:
            raise RuntimeError("package integrity check failed")
        if archive.read(member) != skill.read_bytes():
            raise RuntimeError("packaged skill differs from its source")
    print(f"Packaged and verified {args.output}")


if __name__ == "__main__":
    main()

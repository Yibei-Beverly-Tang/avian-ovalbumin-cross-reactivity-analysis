"""Command-line interface for project validation tasks."""

from __future__ import annotations

import argparse
from pathlib import Path

from .registry import validate_registry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="avian-ova")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser(
        "validate-sources", help="validate source provenance records"
    )
    validate.add_argument(
        "--registry",
        type=Path,
        default=Path("data/source_registry.csv"),
        help="path to the source registry CSV",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "validate-sources":
        errors = validate_registry(args.registry)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"Source registry is valid: {args.registry}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())


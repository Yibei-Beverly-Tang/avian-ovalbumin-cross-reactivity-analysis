"""Command-line interface for project validation tasks."""

from __future__ import annotations

import argparse
from pathlib import Path

from .catalogue import load_candidates, write_catalogue
from .checksums import validate_checksums
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
    catalogue = subparsers.add_parser(
        "build-catalogue",
        help="build the verified sequence catalogue from a frozen UniProt TSV",
    )
    catalogue.add_argument("snapshot", type=Path, help="frozen UniProt TSV")
    catalogue.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="directory for catalogue, exclusion log, and FASTA outputs",
    )
    checksums = subparsers.add_parser(
        "verify-checksums", help="verify frozen data files against SHA-256"
    )
    checksums.add_argument(
        "--manifest",
        type=Path,
        default=Path("data/checksums.sha256"),
        help="path to the checksum manifest",
    )
    checksums.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="project root used to resolve manifest paths",
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
    if args.command == "build-catalogue":
        candidates = load_candidates(args.snapshot)
        included, excluded = write_catalogue(
            candidates,
            args.output_dir / "verified_sequence_catalogue.csv",
            args.output_dir / "sequence_exclusion_log.csv",
            args.output_dir / "verified_sequences.fasta",
            args.snapshot.as_posix(),
        )
        print(
            f"Catalogue built from {len(candidates)} candidates: "
            f"{included} included, {excluded} excluded"
        )
        return 0
    if args.command == "verify-checksums":
        errors = validate_checksums(args.manifest, args.root)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"Checksums are valid: {args.manifest}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

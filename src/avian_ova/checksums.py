"""Validate frozen data files against a SHA-256 manifest."""

from __future__ import annotations

import hashlib
from pathlib import Path


def validate_checksums(manifest: Path, root: Path) -> list[str]:
    """Return errors for malformed, missing, or changed manifest entries."""

    errors: list[str] = []
    seen_paths: set[str] = set()
    for line_number, raw_line in enumerate(
        manifest.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("  ", maxsplit=1)
        if len(parts) != 2:
            errors.append(f"line {line_number}: expected HASH<two spaces>PATH")
            continue
        expected, relative_name = parts
        if len(expected) != 64 or any(
            character not in "0123456789abcdef" for character in expected
        ):
            errors.append(f"line {line_number}: invalid SHA-256 digest")
            continue
        relative = Path(relative_name)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"line {line_number}: path must stay within project root")
            continue
        if relative_name in seen_paths:
            errors.append(f"line {line_number}: duplicate path {relative_name!r}")
            continue
        seen_paths.add(relative_name)
        path = root / relative
        if not path.is_file():
            errors.append(f"line {line_number}: file is missing: {relative_name}")
            continue
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            errors.append(
                f"line {line_number}: checksum mismatch for {relative_name}"
            )
    if not seen_paths:
        errors.append("checksum manifest contains no file entries")
    return errors

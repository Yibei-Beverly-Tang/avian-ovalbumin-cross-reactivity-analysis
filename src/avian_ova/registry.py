"""Validation for the project's public-source provenance registry."""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_FIELDS = (
    "source_id",
    "resource",
    "record_id",
    "organism",
    "evidence_type",
    "url",
    "retrieved_on",
    "verification_status",
    "notes",
)

ALLOWED_STATUSES = {"verified_reference", "verified_included", "excluded"}


def validate_registry(path: Path) -> list[str]:
    """Return human-readable validation errors for a source registry."""

    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(REQUIRED_FIELDS):
            errors.append(
                "header must exactly match: " + ",".join(REQUIRED_FIELDS)
            )
            return errors

        seen_ids: set[str] = set()
        row_count = 0
        for line_number, row in enumerate(reader, start=2):
            row_count += 1
            prefix = f"line {line_number}"
            for field in REQUIRED_FIELDS:
                if not row[field].strip():
                    errors.append(f"{prefix}: {field} is empty")

            source_id = row["source_id"].strip()
            if source_id in seen_ids:
                errors.append(f"{prefix}: duplicate source_id {source_id!r}")
            seen_ids.add(source_id)

            parsed = urlparse(row["url"].strip())
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{prefix}: url must be an absolute HTTPS URL")

            try:
                retrieved = date.fromisoformat(row["retrieved_on"].strip())
                if retrieved > date.today():
                    errors.append(f"{prefix}: retrieved_on is in the future")
            except ValueError:
                errors.append(f"{prefix}: retrieved_on must use YYYY-MM-DD")

            status = row["verification_status"].strip()
            if status not in ALLOWED_STATUSES:
                errors.append(
                    f"{prefix}: verification_status {status!r} is not allowed"
                )

        if row_count == 0:
            errors.append("registry must contain at least one source record")

    return errors


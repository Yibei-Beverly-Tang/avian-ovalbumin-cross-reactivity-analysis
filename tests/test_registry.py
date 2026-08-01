from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from avian_ova.registry import REQUIRED_FIELDS, validate_registry


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RegistryTests(unittest.TestCase):
    def test_project_registry_is_valid(self) -> None:
        errors = validate_registry(PROJECT_ROOT / "data/source_registry.csv")
        self.assertEqual(errors, [])

    def test_duplicate_and_insecure_source_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=REQUIRED_FIELDS)
                writer.writeheader()
                row = {
                    "source_id": "same",
                    "resource": "Example",
                    "record_id": "1",
                    "organism": "Example species",
                    "evidence_type": "test record",
                    "url": "http://example.org/1",
                    "retrieved_on": "2025-01-01",
                    "verification_status": "verified_included",
                    "notes": "validator fixture; not project evidence",
                }
                writer.writerow(row)
                writer.writerow(row)

            errors = validate_registry(path)
            self.assertTrue(any("absolute HTTPS" in error for error in errors))
            self.assertTrue(any("duplicate source_id" in error for error in errors))


if __name__ == "__main__":
    unittest.main()


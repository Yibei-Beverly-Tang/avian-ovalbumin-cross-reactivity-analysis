from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from avian_ova.checksums import validate_checksums


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ChecksumTests(unittest.TestCase):
    def test_project_data_checksums_are_valid(self) -> None:
        errors = validate_checksums(
            PROJECT_ROOT / "data/checksums.sha256", PROJECT_ROOT
        )
        self.assertEqual(errors, [])

    def test_changed_file_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "record.txt"
            data.write_text("original", encoding="utf-8")
            digest = hashlib.sha256(data.read_bytes()).hexdigest()
            manifest = root / "checksums.sha256"
            manifest.write_text(
                f"{digest}  record.txt\n", encoding="utf-8"
            )
            data.write_text("changed", encoding="utf-8")
            errors = validate_checksums(manifest, root)
            self.assertTrue(any("checksum mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

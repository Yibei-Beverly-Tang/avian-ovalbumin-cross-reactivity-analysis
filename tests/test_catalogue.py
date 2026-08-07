from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from avian_ova.catalogue import (
    Candidate,
    exclusion_reasons,
    load_candidates,
    write_catalogue,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = (
    PROJECT_ROOT
    / "data/raw/uniprot_reviewed_avian_ovalbumin_2026-08-07.tsv"
)


class CatalogueTests(unittest.TestCase):
    def test_frozen_snapshot_has_expected_decisions(self) -> None:
        candidates = load_candidates(SNAPSHOT)
        decisions = {
            candidate.accession: exclusion_reasons(candidate)
            for candidate in candidates
        }
        self.assertEqual(len(candidates), 7)
        self.assertEqual(
            {accession for accession, reasons in decisions.items() if not reasons},
            {"P01012", "O73860", "Q6V115", "P19104", "E2RVI8"},
        )
        self.assertIn("paralogue", " ".join(decisions["P01014"]))
        self.assertIn("paralogue", " ".join(decisions["P01013"]))

    def test_declared_length_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.tsv"
            header = "\t".join(
                (
                    "Entry",
                    "Entry Name",
                    "Reviewed",
                    "Protein names",
                    "Organism",
                    "Organism (ID)",
                    "Length",
                    "Sequence",
                    "Protein families",
                )
            )
            path.write_text(
                header
                + "\nX1\tX\treviewed\tOvalbumin\tExample bird\t1\t2\tAAA\t"
                "Serpin family, Ov-serpin subfamily\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "does not match"):
                load_candidates(path)

    def test_ambiguous_residue_is_excluded(self) -> None:
        candidate = Candidate(
            accession="X1",
            entry_name="TEST_BIRD",
            reviewed="reviewed",
            protein_names="Ovalbumin",
            organism="Example bird",
            taxonomy_id="1",
            length=386,
            sequence="A" * 385 + "X",
            protein_families="Serpin family, Ov-serpin subfamily",
        )
        self.assertTrue(
            any("ambiguous residues" in reason for reason in exclusion_reasons(candidate))
        )

    def test_builder_writes_auditable_outputs(self) -> None:
        candidates = load_candidates(SNAPSHOT)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            included_count, excluded_count = write_catalogue(
                candidates,
                output / "included.csv",
                output / "excluded.csv",
                output / "sequences.fasta",
                SNAPSHOT.as_posix(),
            )
            self.assertEqual((included_count, excluded_count), (5, 2))
            with (output / "included.csv").open(
                newline="", encoding="utf-8"
            ) as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 5)
            self.assertTrue(all(len(row["sequence_sha256"]) == 64 for row in rows))
            fasta = (output / "sequences.fasta").read_text(encoding="utf-8")
            self.assertEqual(fasta.count(">"), 5)


if __name__ == "__main__":
    unittest.main()

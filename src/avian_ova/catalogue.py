"""Build the evidence-gated avian ovalbumin sequence catalogue."""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path


EXPECTED_FIELDS = (
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

MIN_LENGTH = 350
MAX_LENGTH = 425
STANDARD_AMINO_ACIDS = frozenset("ACDEFGHIKLMNPQRSTVWY")


@dataclass(frozen=True)
class Candidate:
    accession: str
    entry_name: str
    reviewed: str
    protein_names: str
    organism: str
    taxonomy_id: str
    length: int
    sequence: str
    protein_families: str


def load_candidates(path: Path) -> list[Candidate]:
    """Load a UniProt TSV snapshot and reject malformed source data."""

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != list(EXPECTED_FIELDS):
            raise ValueError(
                "UniProt snapshot header must exactly match: "
                + ", ".join(EXPECTED_FIELDS)
            )

        candidates: list[Candidate] = []
        seen_accessions: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            accession = row["Entry"].strip()
            if not accession:
                raise ValueError(f"line {line_number}: accession is empty")
            if accession in seen_accessions:
                raise ValueError(
                    f"line {line_number}: duplicate accession {accession!r}"
                )
            seen_accessions.add(accession)

            sequence = row["Sequence"].strip().upper()
            try:
                declared_length = int(row["Length"].strip())
            except ValueError as error:
                raise ValueError(
                    f"line {line_number}: length must be an integer"
                ) from error
            if declared_length != len(sequence):
                raise ValueError(
                    f"line {line_number}: declared length {declared_length} "
                    f"does not match sequence length {len(sequence)}"
                )

            candidates.append(
                Candidate(
                    accession=accession,
                    entry_name=row["Entry Name"].strip(),
                    reviewed=row["Reviewed"].strip(),
                    protein_names=row["Protein names"].strip(),
                    organism=row["Organism"].strip(),
                    taxonomy_id=row["Organism (ID)"].strip(),
                    length=declared_length,
                    sequence=sequence,
                    protein_families=row["Protein families"].strip(),
                )
            )
    if not candidates:
        raise ValueError("UniProt snapshot contains no candidate records")
    return candidates


def exclusion_reasons(candidate: Candidate) -> list[str]:
    """Return all documented reasons that prevent catalogue inclusion."""

    reasons: list[str] = []
    name = candidate.protein_names.casefold()
    if candidate.reviewed.casefold() != "reviewed":
        reasons.append("record is not UniProtKB reviewed")
    if not name.startswith("ovalbumin"):
        reasons.append("recommended protein name is not ovalbumin")
    if "ovalbumin-related" in name:
        reasons.append("record is an ovalbumin-related paralogue")
    if "ov-serpin subfamily" not in candidate.protein_families.casefold():
        reasons.append("record lacks Ov-serpin subfamily annotation")
    if not MIN_LENGTH <= candidate.length <= MAX_LENGTH:
        reasons.append(
            f"sequence length {candidate.length} is outside "
            f"the predefined {MIN_LENGTH}-{MAX_LENGTH} residue window"
        )
    invalid = sorted(set(candidate.sequence) - STANDARD_AMINO_ACIDS)
    if invalid:
        reasons.append(
            "sequence contains non-standard or ambiguous residues: "
            + "".join(invalid)
        )
    return reasons


def _sequence_sha256(sequence: str) -> str:
    return hashlib.sha256(sequence.encode("ascii")).hexdigest()


def write_catalogue(
    candidates: list[Candidate],
    included_path: Path,
    excluded_path: Path,
    fasta_path: Path,
    source_snapshot: str,
) -> tuple[int, int]:
    """Write deterministic included, excluded, and FASTA outputs."""

    included_path.parent.mkdir(parents=True, exist_ok=True)
    excluded_path.parent.mkdir(parents=True, exist_ok=True)
    fasta_path.parent.mkdir(parents=True, exist_ok=True)

    included_fields = (
        "accession",
        "entry_name",
        "organism",
        "taxonomy_id",
        "review_status",
        "length",
        "sequence_sha256",
        "source_snapshot",
        "verification_status",
        "inclusion_reason",
    )
    excluded_fields = (
        "accession",
        "entry_name",
        "organism",
        "taxonomy_id",
        "review_status",
        "length",
        "protein_names",
        "source_snapshot",
        "verification_status",
        "exclusion_reason",
    )

    included: list[Candidate] = []
    excluded: list[tuple[Candidate, list[str]]] = []
    for candidate in candidates:
        reasons = exclusion_reasons(candidate)
        if reasons:
            excluded.append((candidate, reasons))
        else:
            included.append(candidate)

    with included_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=included_fields)
        writer.writeheader()
        for candidate in included:
            writer.writerow(
                {
                    "accession": candidate.accession,
                    "entry_name": candidate.entry_name,
                    "organism": candidate.organism,
                    "taxonomy_id": candidate.taxonomy_id,
                    "review_status": candidate.reviewed,
                    "length": candidate.length,
                    "sequence_sha256": _sequence_sha256(candidate.sequence),
                    "source_snapshot": source_snapshot,
                    "verification_status": "verified_included",
                    "inclusion_reason": (
                        "reviewed UniProtKB record explicitly named ovalbumin; "
                        "complete canonical sequence within predefined length window"
                    ),
                }
            )

    with excluded_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=excluded_fields)
        writer.writeheader()
        for candidate, reasons in excluded:
            writer.writerow(
                {
                    "accession": candidate.accession,
                    "entry_name": candidate.entry_name,
                    "organism": candidate.organism,
                    "taxonomy_id": candidate.taxonomy_id,
                    "review_status": candidate.reviewed,
                    "length": candidate.length,
                    "protein_names": candidate.protein_names,
                    "source_snapshot": source_snapshot,
                    "verification_status": "excluded",
                    "exclusion_reason": "; ".join(reasons),
                }
            )

    with fasta_path.open("w", encoding="utf-8", newline="\n") as handle:
        for candidate in included:
            handle.write(
                f">{candidate.accession}|{candidate.entry_name}|"
                f"{candidate.organism}|taxon:{candidate.taxonomy_id}\n"
            )
            for start in range(0, len(candidate.sequence), 60):
                handle.write(candidate.sequence[start : start + 60] + "\n")

    return len(included), len(excluded)

# Avian Ovalbumin Cross-Reactivity Analysis

[![Data policy: traceable public records](https://img.shields.io/badge/data-traceable%20public%20records-2ea44f)](data/README.md)
[![Status: verified sequence catalogue](https://img.shields.io/badge/status-verified%20sequence%20catalogue-blue)](ROADMAP.md)

Comparative sequence, epitope, and structural analysis of avian ovalbumins for
**potential** allergenic cross-reactivity.

## Research question

How strongly are experimentally observed chicken ovalbumin epitopes conserved
among verified avian ovalbumin homologues, and are the conserved regions
accessible in available experimental or predicted structures?

Sequence or structural similarity can support a hypothesis of potential
cross-reactivity. It cannot establish clinical cross-allergy without suitable
experimental or clinical evidence.

## Data integrity policy

- Only records retrieved from identifiable public databases are included.
- Every raw record must retain its accession, source URL, retrieval date, and
  database provenance.
- Experimental structures and predicted structures are kept distinct.
- IEDB assay records will be preserved at assay level; aggregate counts will
  never be presented as independent subjects or experiments.
- Missing values remain missing. They are not imputed unless a later analysis
  explicitly documents and justifies an imputation method.
- Demonstration or simulated measurements are not accepted as biological
  evidence in this repository.
- Computational findings are labelled as predictions or inferences, not as
  clinical conclusions.

Version 0.2.0 contains a conservative primary catalogue of five complete,
reviewed avian ovalbumins. All candidate records, inclusion decisions, rejected
paralogues, retrieval metadata, and sequence checksums remain auditable.

## Verified sequence catalogue

| UniProtKB record | Organism | Length | Role |
|---|---|---:|---|
| P01012 | *Gallus gallus* | 386 | Chicken reference |
| O73860 | *Meleagris gallopavo* | 386 | Included homologue |
| Q6V115 | *Coturnix coturnix* | 383 | Included homologue |
| P19104 | *Coturnix japonica* | 383 | Included homologue |
| E2RVI8 | *Dromaius novaehollandiae* | 386 | Included homologue |

Two reviewed search hits, P01013 and P01014, are retained in the exclusion log
because they are ovalbumin-related X/Y paralogues rather than target
ovalbumins. See [`docs/sequence_catalogue.md`](docs/sequence_catalogue.md) for
the complete inclusion protocol and limitations.

The experimental chicken structure 1OVA remains registered separately as the
structural reference. See [`data/source_registry.csv`](data/source_registry.csv)
for machine-readable provenance.

## Planned outputs

- verified avian ovalbumin sequence catalogue;
- pairwise identity and multiple-sequence alignment;
- assay-level experimentally observed epitope table;
- epitope conservation matrix across included species;
- structure provenance and confidence table;
- surface-accessibility and spatial epitope maps;
- evidence-quality and uncertainty report;
- fully reproducible figures, tables, and tests.

## Quick validation

Requires Python 3.10 or later and no third-party packages:

```bash
python -m avian_ova.cli validate-sources
python -m avian_ova.cli verify-checksums
python -m unittest discover -s tests -v
```

For a source checkout without installation:

```bash
PYTHONPATH=src python -m avian_ova.cli validate-sources
PYTHONPATH=src python -m avian_ova.cli verify-checksums
PYTHONPATH=src python -m unittest discover -s tests -v
```

Rebuild the processed catalogue from the frozen UniProtKB response:

```bash
PYTHONPATH=src python -m avian_ova.cli build-catalogue \
  data/raw/uniprot_reviewed_avian_ovalbumin_2026-08-07.tsv
```

## Project status

Version 0.2.0 completes the verified-sequence-catalogue milestone with a frozen
UniProtKB release 2026_02 snapshot, explicit inclusion rules, five included
sequences, a two-record exclusion log, deterministic FASTA/CSV generation,
checksums, automated tests, and continuous integration. It does not yet claim
comparative cross-species or epitope results. Progress is tracked in
[`ROADMAP.md`](ROADMAP.md).

The planned analysis uses separate global-sequence, epitope, physicochemical,
structural, post-translational, and empirical-evidence layers. The definitions
and the gate for any future composite model are specified in
[`docs/scoring_framework.md`](docs/scoring_framework.md). No unvalidated
“clinical risk score” is produced.

## Primary public resources

- [UniProt](https://www.uniprot.org/)
- [Immune Epitope Database (IEDB)](https://www.iedb.org/)
- [RCSB Protein Data Bank](https://www.rcsb.org/)
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)

## License

Code is released under the MIT License. Source databases and individual records
remain subject to their respective terms and citation requirements.

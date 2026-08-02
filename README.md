# Avian Ovalbumin Cross-Reactivity Analysis

[![Data policy: traceable public records](https://img.shields.io/badge/data-traceable%20public%20records-2ea44f)](data/README.md)
[![Status: protocol and validation scaffold](https://img.shields.io/badge/status-protocol%20scaffold-blue)](ROADMAP.md)

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

The initial registry contains only two independently verified chicken
ovalbumin reference records. Additional species will be added only after their
protein identity and provenance pass the inclusion protocol.

## Verified starting records

| Resource | Record | Evidence type | Organism |
|---|---|---|---|
| UniProtKB | P01012 | Protein sequence and annotation | *Gallus gallus* |
| RCSB PDB | 1OVA | X-ray structure, 1.95 A | *Gallus gallus* |

See [`data/source_registry.csv`](data/source_registry.csv) for machine-readable
provenance and [`docs/research_protocol.md`](docs/research_protocol.md) for the
planned inclusion and analysis procedure.

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
python -m unittest discover -s tests -v
```

For a source checkout without installation:

```bash
PYTHONPATH=src python -m avian_ova.cli validate-sources
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Project status

Version 0.1.1 establishes the research protocol, provenance registry, source
validator, automated tests, and continuous-integration workflow. It does not
yet claim comparative cross-species results. Progress is tracked in
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

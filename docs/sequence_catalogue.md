# Verified sequence catalogue protocol

## Scope

Version 0.2.0 establishes a conservative catalogue of complete, reviewed avian
ovalbumin sequences. It is intentionally narrower than the set of all records
returned by a text search. This first comparison set prioritises protein
identity and traceability over taxonomic breadth.

## Frozen candidate query

The candidate snapshot was retrieved from the UniProtKB REST API on 2026-08-07
using UniProt release 2026_02:

```text
(reviewed:true) AND (protein_name:ovalbumin) AND (taxonomy_id:8782)
```

Taxonomy identifier 8782 represents Aves and includes descendant taxa. The
query returned seven records. The unmodified response fields used by the
catalogue builder are preserved in
[`data/raw/uniprot_reviewed_avian_ovalbumin_2026-08-07.tsv`](../data/raw/uniprot_reviewed_avian_ovalbumin_2026-08-07.tsv),
with release and query metadata in the adjacent JSON file.

## Inclusion rules

A candidate is included only when all of the following are true:

1. the UniProtKB record is reviewed;
2. the recommended protein name begins with `Ovalbumin`;
3. the recommended protein name does not identify an `ovalbumin-related`
   protein, which would mix paralogues with the target orthologue set;
4. UniProt assigns the record to the Ov-serpin subfamily;
5. the canonical sequence contains only the 20 standard amino-acid symbols;
6. sequence length is 350–425 residues.

The length window is a completeness screen centred on the 386-residue chicken
reference. It is not evidence of protein identity by itself. Future unreviewed
records require an additional, separately versioned protocol and will never be
silently merged into this reviewed set.

## Decisions

Five records pass all rules:

| Accession | Organism | Length | Decision |
|---|---|---:|---|
| P01012 | *Gallus gallus* | 386 | Included; reference |
| O73860 | *Meleagris gallopavo* | 386 | Included |
| Q6V115 | *Coturnix coturnix* | 383 | Included |
| P19104 | *Coturnix japonica* | 383 | Included |
| E2RVI8 | *Dromaius novaehollandiae* | 386 | Included |

Two reviewed search hits are excluded:

| Accession | Annotation | Length | Reason |
|---|---|---:|---|
| P01014 | Ovalbumin-related protein Y | 388 | Paralogous ovalbumin-related protein |
| P01013 | Ovalbumin-related protein X | 232 | Paralogous protein and outside completeness window |

The machine-readable catalogue records a SHA-256 digest for each included
sequence. The exclusion log retains every rejected candidate and all applicable
reasons.

## Reproduction

```bash
PYTHONPATH=src python -m avian_ova.cli build-catalogue \
  data/raw/uniprot_reviewed_avian_ovalbumin_2026-08-07.tsv
```

This command recreates:

- `data/processed/verified_sequence_catalogue.csv`;
- `data/processed/sequence_exclusion_log.csv`;
- `data/processed/verified_sequences.fasta`.

## Limitations

- Reviewed UniProtKB coverage is taxonomically sparse and biased toward a few
  well-studied birds.
- Common and Japanese quail are retained as distinct traceable database
  records even though their sequences are highly similar.
- The catalogue establishes sequence identity and provenance only. It does not
  establish immunological or clinical cross-reactivity.
- No unreviewed prediction, genome-derived fragment, isoform, or ovalbumin X/Y
  paralogue is used in the primary comparison set.

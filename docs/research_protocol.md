# Research protocol

## Objective

Measure sequence and experimentally observed epitope conservation among
verified avian ovalbumin homologues, then describe their structural context.
The analysis estimates molecular similarity; it does not diagnose allergy or
estimate an individual's clinical risk.

## Inclusion units

### Protein records

A candidate protein may be included only when:

1. the source database supplies a stable accession and organism assignment;
2. the record is explicitly annotated as ovalbumin, not merely as a generic
   serpin or an ovalbumin-related paralogue;
3. sequence length and coverage are sufficient for coordinate mapping;
4. fragment, isoform, and sequence-conflict status are retained;
5. the record can be retrieved reproducibly.

Reviewed records are preferred. An unreviewed record requires an explicit
evidence note and must remain distinguishable in all outputs.

### Epitope records

An epitope may be included only when its IEDB record, source antigen, assay type,
qualitative outcome, host, and reference remain traceable. Linear epitopes must
map unambiguously to the selected P01012 sequence version. Failed or ambiguous
mappings are recorded in an exclusion table rather than silently discarded.

### Structures

Experimental PDB structures and predicted AlphaFold models form separate
evidence classes. Experimental method and resolution are retained for PDB
entries. Model confidence and low-confidence regions are retained for AlphaFold
entries. Structural comparisons exclude or flag unresolved/low-confidence
coordinates.

## Planned analysis

1. Freeze source snapshots and calculate file checksums.
2. Validate protein identity and sequence completeness.
3. Align verified sequences and publish alignment parameters.
4. Map assay-supported linear epitopes onto the reference alignment.
5. Calculate exact and substitution-aware conservation separately.
6. Map epitopes onto structures and calculate solvent accessibility.
7. Report evidence class, uncertainty, exclusions, and missingness alongside
   every comparative output.

## Interpretation boundary

Conserved sequence and accessible structure are mechanistic indicators only.
Clinical cross-reactivity additionally depends on immune recognition, exposure,
processing, abundance, patient population, and other factors not established by
sequence/structure comparison alone.


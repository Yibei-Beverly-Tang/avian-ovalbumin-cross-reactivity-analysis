# Roadmap

The roadmap is evidence-gated: an analysis stage is completed only after its
inputs, validation, and limitations are documented.

## v0.1.0 — Reproducible foundation

- [x] Define the research question and non-clinical interpretation boundary.
- [x] Establish source-provenance and data-integrity requirements.
- [x] Add a machine-readable source registry.
- [x] Add a standard-library source-registry validator.
- [x] Add automated tests and continuous integration.

## v0.2.0 — Verified sequence catalogue

- [ ] Define taxonomic and protein-identity inclusion rules.
- [ ] Retrieve candidate avian ovalbumin records from UniProt.
- [ ] Preserve raw responses and retrieval metadata.
- [ ] Exclude fragments, unreviewed identity conflicts, and non-ovalbumin
      paralogues using documented rules.
- [ ] Publish the verified sequence catalogue and exclusion log.

## v0.3.0 — Comparative sequence analysis

- [ ] Generate a reproducible multiple-sequence alignment.
- [ ] Calculate pairwise identity with an explicitly defined denominator.
- [ ] Map chicken P01012 coordinates to included homologues.
- [ ] Report alignment uncertainty and coverage.

## v0.4.0 — Experimental epitope evidence

- [ ] Retrieve relevant IEDB records with a reproducible query and snapshot.
- [ ] Separate B-cell, T-cell, MHC-ligand, positive, and negative assays.
- [ ] Deduplicate biological epitopes without losing assay-level evidence.
- [ ] Map valid linear epitopes to P01012 and document rejected mappings.

## v0.5.0 — Epitope conservation

- [ ] Calculate residue-level and whole-epitope conservation.
- [ ] Report exact matches separately from conservative substitutions.
- [ ] Generate the species-by-epitope conservation matrix.
- [ ] Avoid converting sequence conservation into a clinical risk score.

## v0.6.0 — Structural context

- [ ] Catalogue experimental structures and AlphaFold predictions separately.
- [ ] Retain resolution or model-confidence metadata.
- [ ] Calculate solvent accessibility using a documented method.
- [ ] Produce three-dimensional epitope maps and uncertainty annotations.

## v0.7.0 — Evidence synthesis

- [ ] Classify each conclusion by evidence type and traceability.
- [ ] Generate a limitations and evidence-gap report.
- [ ] Add a reproducible release snapshot with checksums.
- [ ] Complete independent validation of all tables and figures.


# Roadmap

The roadmap is evidence-gated: an analysis stage is completed only after its
inputs, validation, and limitations are documented.

## Analysis architecture

The project will report interpretable components rather than a single opaque
clinical-risk score:

1. global sequence conservation;
2. experimentally supported epitope conservation;
3. amino-acid substitution and physicochemical-change annotations;
4. structure confidence, relative solvent accessibility, local geometry, and
   optional electrostatic-surface comparison;
5. experimentally annotated and motif-level post-translational features;
6. independent empirical cross-reactivity evidence, when available.

These components may be combined into a calibrated prediction model only if a
sufficient independent dataset with experimentally measured cross-reactivity
labels is identified and a validation protocol is fixed in advance. Otherwise,
they remain separate hypothesis-generating features.

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

- [ ] Generate a reproducible MAFFT multiple-sequence alignment.
- [ ] Calculate global pairwise identity with an explicitly defined
      denominator and gap policy.
- [ ] Map chicken P01012 coordinates to included homologues.
- [ ] Produce a second, epitope-restricted alignment layer.
- [ ] Report exact epitope identity separately from BLOSUM62 similarity and
      explicit charge, polarity, size, and hydrophobicity changes.
- [ ] Treat BLOSUM62 as an evolutionary substitution score, not a validated
      antibody-binding or clinical cross-reactivity score.
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
- [ ] Keep B-cell and T-cell evidence, assay outcome, host, and MHC context
      separate in all summaries.
- [ ] Avoid converting sequence conservation into a clinical risk score.

## v0.6.0 — Structural context

- [ ] Catalogue experimental structures and AlphaFold predictions separately.
- [ ] Retain resolution or model-confidence metadata.
- [ ] Calculate absolute SASA and residue-normalized relative SASA (RSA) using
      a documented MaxASA scale.
- [ ] Predefine exposed/buried sensitivity analyses instead of treating one
      RSA cutoff (for example 25%) as biological ground truth.
- [ ] Compare local epitope-patch geometry only where coordinate mapping and
      structural confidence are adequate; report atom selection and alignment
      method with patch RMSD.
- [ ] Add APBS/PDB2PQR electrostatic comparison as an optional, parameter-fixed
      analysis after checking missing atoms, protonation assumptions, ionic
      strength, grid spacing, and structure confidence.
- [ ] Produce three-dimensional epitope maps and uncertainty annotations.

## v0.7.0 — Post-translational and structural-stability features

- [ ] Map experimentally annotated glycosylation sites separately from scanned
      N-X-S/T sequence motifs.
- [ ] Label motif gains/losses as glycosylation potential, not evidence of
      glycan occupancy or glycan composition.
- [ ] Map experimentally annotated disulfide bonds and report conservation of
      the participating cysteines.
- [ ] Do not infer heat stability or allergenicity direction from motif or
      cysteine conservation alone.

## v0.8.0 — Evidence synthesis and delivery

- [ ] Classify each conclusion by evidence type and traceability.
- [ ] Build a phylogenetic tree annotated with the separate molecular features
      and any independently measured cross-reactivity evidence.
- [ ] Produce a static comparison report before considering a Streamlit or
      Gradio interface.
- [ ] If a composite model is attempted, preregister its labels, training and
      held-out validation split, calibration metric, and external-validation
      requirement; otherwise do not publish a “risk score”.
- [ ] Generate a limitations and evidence-gap report.
- [ ] Add a reproducible release snapshot with checksums.
- [ ] Complete independent validation of all tables and figures.

# Interpretable feature and scoring framework

## Purpose

This document specifies how molecular comparison features will be reported
without overstating their relationship to clinical cross-reactivity.

## Feature layer 1: global sequence comparison

For every pair of included proteins, report alignment coverage, exact identity,
similarity, gap fraction, and the denominator used for each percentage. Global
identity is descriptive and is not itself an immune-response probability.

## Feature layer 2: experimentally supported epitope comparison

IEDB records are retained at assay level and separated by B-cell, T-cell, and
MHC-ligand evidence, positive/negative outcome, host, reference, and relevant
restriction information. Only reference-mapped residues contribute to an
epitope conservation result.

For each mapped linear epitope, report:

- exact residue identity;
- alignment coverage and gaps;
- BLOSUM62 substitution score;
- counts of charge reversal, polarity change, aromaticity change, side-chain
  size class change, and hydrophobicity class change;
- residue-level structure accessibility when a suitable structure exists.

BLOSUM62 reflects observed evolutionary substitutions. It is not described as
an “immune matrix” or as a validated antibody-affinity model.

## Feature layer 3: structural context

Experimental and predicted structures are never pooled without provenance.
Absolute SASA is reported in square angstroms. Relative SASA is calculated by
normalizing to a named per-residue MaxASA scale. An RSA threshold is an analysis
convention rather than biological ground truth, so primary tables retain the
continuous RSA value and sensitivity summaries may compare multiple predefined
cutoffs.

Patch RMSD is reported only when the same mapped epitope patch has adequate
coordinate coverage and confidence in both structures. The atom set,
superposition region, missing residues, and model confidence are recorded.

APBS/PDB2PQR electrostatics are optional. Comparisons require fixed force-field,
pH/protonation, ionic-strength, dielectric, grid, and alignment settings.
Electrostatic similarity remains a computational feature unless independently
validated against measured binding or inhibition data.

## Feature layer 4: post-translational features

Database-annotated glycosylation is distinct from an N-X-S/T motif scan. A motif
indicates sequence potential only; it does not demonstrate occupancy, glycan
composition, or immunologic effect. Likewise, conserved cysteines and annotated
disulfide pairs are structural features, not direct evidence of heat stability
or allergenic potency.

## Evidence layer 5: empirical cross-reactivity

Where publications report inhibition, binding, challenge, or clinical outcomes,
the measurement type, population, sample size, units, comparator, uncertainty,
and source location must be retained. Measurements with incompatible endpoints
are not silently combined.

## Composite-model gate

A composite cross-reactivity model may be developed only after identifying a
sufficient labelled dataset and fixing:

1. the biological endpoint being predicted;
2. inclusion and independence rules;
3. feature definitions and missing-data handling;
4. training, calibration, and held-out validation partitions;
5. discrimination and calibration metrics;
6. external validation and uncertainty reporting.

Until those requirements are met, the project presents a multidimensional
feature profile and evidence table, not a clinical “risk score”.

## Method references

- Katoh K, Standley DM. MAFFT Multiple Sequence Alignment Software Version 7.
  *Molecular Biology and Evolution*. 2013;30:772–780.
  <https://doi.org/10.1093/molbev/mst010>
- Henikoff S, Henikoff JG. Amino acid substitution matrices from protein
  blocks. *PNAS*. 1992;89:10915–10919.
  <https://doi.org/10.1073/pnas.89.22.10915>
- Tien MZ et al. Maximum Allowed Solvent Accessibilities of Residues in
  Proteins. *PLOS ONE*. 2013;8:e80635.
  <https://doi.org/10.1371/journal.pone.0080635>
- Mitternacht S. FreeSASA: An open source C library for solvent accessible
  surface area calculations. *F1000Research*. 2016;5:189.
  <https://doi.org/10.12688/f1000research.7931.1>
- Jurrus E et al. Improvements to the APBS biomolecular solvation software
  suite. *Protein Science*. 2018;27:112–128.
  <https://doi.org/10.1002/pro.3280>
- IEDB Query API and assay-level exports:
  <https://help.iedb.org/hc/en-us/articles/4402872882189-Immune-Epitope-Database-Query-API-IQ-API>

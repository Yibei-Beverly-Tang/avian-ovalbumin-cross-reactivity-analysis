# Data directory

## Directory layout

- `raw/` contains frozen, unmodified public-database responses and retrieval
  metadata.
- `processed/` contains deterministic outputs produced from the raw snapshots.
- `source_registry.csv` contains the project-wide provenance registry.

The version 0.2.0 sequence snapshot and its inclusion rules are documented in
[`docs/sequence_catalogue.md`](../docs/sequence_catalogue.md).

## Current contents

`source_registry.csv` is the authoritative registry of source records reviewed
by the project. Version 0.2.0 also provides the frozen UniProtKB candidate
snapshot, a verified five-record sequence catalogue, a two-record exclusion
log, FASTA sequences, and a SHA-256 manifest. It does not yet contain
comparative epitope or clinical results.

## Required provenance

Every accepted record must contain:

- a repository-unique source identifier;
- database/resource name;
- stable database accession or record identifier;
- organism;
- evidence type;
- HTTPS source URL;
- ISO retrieval date;
- verification status;
- explanatory notes where needed.

Raw responses are stored separately from processed tables. Retrieval metadata
records the API query and UniProt release, while `checksums.sha256` detects
changes to frozen inputs and generated outputs.

## Prohibited practices

- inventing values to complete missing fields;
- silently replacing unavailable records;
- treating predicted structures as experimental structures;
- presenting simulated data as measured biological data;
- reporting computational similarity as demonstrated clinical cross-allergy.

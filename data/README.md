# Data directory

## Current contents

`source_registry.csv` is the authoritative registry of source records accepted
into the project. Version 0.1.0 contains metadata only; it does not contain a
cross-species sequence dataset or comparative biological results.

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

Raw data downloaded in later releases will be stored separately from processed
tables. A download manifest will record URL, retrieval timestamp, file checksum,
and the script version that produced each snapshot.

## Prohibited practices

- inventing values to complete missing fields;
- silently replacing unavailable records;
- treating predicted structures as experimental structures;
- presenting simulated data as measured biological data;
- reporting computational similarity as demonstrated clinical cross-allergy.


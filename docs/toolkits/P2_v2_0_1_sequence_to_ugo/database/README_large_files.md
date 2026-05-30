# Large Sequence-to-UGO database files

The full Sequence-to-UGO protein search database and full sequence-to-orthogroup lookup table are not stored directly in the GitHub repository because they exceed GitHub's single-file size limit.

Large files excluded from GitHub:

- UGO_11species_protein_search_database_v1.fa
- UGO_11species_protein_search_database_v1.fa.gz
- UGO_11species_protein_search_database_v1.dmnd
- UGO_sequence_to_orthogroup_lookup_v1.tsv

These files are included in the full release package and will be archived with the Zenodo release DOI.

The GitHub repository retains:

- scripts/run_sequence_to_UGO.sh
- scripts/map_sequence_hits_to_UGO.py
- examples/example_query_proteins.fa
- example_results/example_sequence_to_UGO_result.tsv
- database/UGO_orthogroup_to_candidate_module_lookup_v1.tsv
- database/UGO_sequence_to_candidate_module_lookup_v1.tsv
- database/UGO_sequence_to_ugo_toolkit_metadata_v1.json

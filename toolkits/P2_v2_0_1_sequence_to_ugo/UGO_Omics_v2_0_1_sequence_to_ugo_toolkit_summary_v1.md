# UGO-Omics v2.0.1 Sequence-to-UGO Toolkit summary

Generated on: 2026-05-29 20:47:01

## Purpose

This step creates a Sequence-to-UGO Toolkit that maps user protein sequences to UGO-Omics orthogroups, candidate modules, UGO scores, biological discovery cases, and validation-priority annotations.

## Database

- Species represented: 11
- Protein sequences: 408906
- Candidate orthogroups: 8
- Candidate protein records: 375
- DIAMOND database status: not_built

## Main outputs

- database/UGO_11species_protein_search_database_v1.fa
- database/UGO_11species_protein_search_database_v1.fa.gz
- database/UGO_11species_protein_search_database_v1.dmnd
- database/UGO_sequence_to_orthogroup_lookup_v1.tsv
- database/UGO_orthogroup_to_candidate_module_lookup_v1.tsv
- database/UGO_sequence_to_candidate_module_lookup_v1.tsv
- scripts/run_sequence_to_UGO.sh
- scripts/map_sequence_hits_to_UGO.py
- examples/example_query_proteins.fa
- example_results/example_sequence_to_UGO_result.tsv

## Interpretation

This toolkit makes UGO-Omics usable when a user starts with a protein sequence. It is a candidate-prioritization and hypothesis-generation workflow, not functional validation.

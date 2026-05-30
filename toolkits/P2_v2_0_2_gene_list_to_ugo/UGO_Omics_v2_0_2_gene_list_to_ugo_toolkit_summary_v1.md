# UGO-Omics v2.0.2 Gene-list-to-UGO Toolkit summary

Generated on: 2026-05-29 21:13:25

## Purpose

This step creates a Gene-list-to-UGO Toolkit that maps DEG, QTL, GWAS, and manually curated gene lists to UGO-Omics orthogroups, candidate modules, UGO scores, biological discovery cases, and validation-priority annotations.

## Database

- Candidate orthogroups: 8
- Candidate gene/protein records: 375
- Example input IDs: 7

## Main outputs

- database/UGO_candidate_gene_lookup_compact_v1.tsv
- database/UGO_orthogroup_to_candidate_module_lookup_v1.tsv
- scripts/gene_list_to_UGO.py
- scripts/run_gene_list_to_UGO.sh
- examples/example_gene_list.txt
- example_results/example_gene_list_to_UGO.matched_genes.tsv
- example_results/example_gene_list_to_UGO.module_summary.tsv
- example_results/example_gene_list_to_UGO.unmatched_genes.tsv

## Interpretation

This toolkit makes UGO-Omics usable when a user starts with a DEG, QTL, GWAS, or candidate gene list. It is a candidate-prioritization and hypothesis-generation workflow, not functional validation.

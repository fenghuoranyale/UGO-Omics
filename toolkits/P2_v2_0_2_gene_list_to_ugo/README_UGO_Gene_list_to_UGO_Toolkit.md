# UGO-Omics v2.0.2 Gene-list-to-UGO Toolkit

## Purpose

This toolkit maps user gene lists to UGO-Omics orthogroups and candidate modules.

It is designed for users who start from:

- DEG lists;
- QTL interval genes;
- GWAS peak candidate genes;
- manually curated candidate genes;
- species-specific homolog lists.

## Main outputs

The toolkit writes three files:

- matched_genes.tsv
- module_summary.tsv
- unmatched_genes.tsv

## Quick start

Run this command from the toolkit directory:

    bash scripts/run_gene_list_to_UGO.sh examples/example_gene_list.txt example_results/example_gene_list_to_UGO

## Interpretation

The most useful output is module_summary.tsv. It summarizes which UGO candidate modules are represented in the user's input gene list and ranks modules by input-gene support and validation-priority score.

## Current compact database size

- Candidate orthogroups: 8
- Candidate gene/protein records: 375

## Full mode versus compact mode

Compact mode uses the candidate gene lookup included in GitHub Pages.

Full mode additionally uses the full sequence-to-orthogroup lookup from the v2.0.1 Sequence-to-UGO release archive:

    P2_v2_0_1_sequence_to_ugo/database/UGO_sequence_to_orthogroup_lookup_v1.tsv

Full mode can map genes outside the prioritized candidate modules to UGO orthogroups. Compact mode focuses on prioritized UGO candidate modules.

## Claim calibration

Gene-list-to-UGO is a candidate-prioritization and hypothesis-generation workflow. Matched modules should not be interpreted as functional validation.

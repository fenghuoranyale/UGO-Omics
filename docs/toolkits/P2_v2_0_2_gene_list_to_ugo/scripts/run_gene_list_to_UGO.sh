#!/bin/bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
    echo "Usage:"
    echo "  bash run_gene_list_to_UGO.sh gene_list.txt output_prefix"
    echo
    echo "Example:"
    echo "  bash run_gene_list_to_UGO.sh ../examples/example_gene_list.txt ../example_results/example_gene_list_to_UGO"
    exit 1
fi

GENE_LIST="$1"
OUT_PREFIX="$2"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLKIT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DB_DIR="${TOOLKIT_DIR}/database"

CANDIDATE_GENE_LOOKUP="${DB_DIR}/UGO_candidate_gene_lookup_compact_v1.tsv"
CANDIDATE_LOOKUP="${DB_DIR}/UGO_orthogroup_to_candidate_module_lookup_v1.tsv"
MAPPER="${SCRIPT_DIR}/gene_list_to_UGO.py"

FULL_LOOKUP="${TOOLKIT_DIR}/../P2_v2_0_1_sequence_to_ugo/database/UGO_sequence_to_orthogroup_lookup_v1.tsv"

if [ -f "${FULL_LOOKUP}" ]; then
    python3 "${MAPPER}" \
        --genes "${GENE_LIST}" \
        --candidate_gene_lookup "${CANDIDATE_GENE_LOOKUP}" \
        --candidate_lookup "${CANDIDATE_LOOKUP}" \
        --full_lookup "${FULL_LOOKUP}" \
        --out_prefix "${OUT_PREFIX}"
else
    echo "Full sequence-to-orthogroup lookup not found."
    echo "Running compact candidate-only mode."
    python3 "${MAPPER}" \
        --genes "${GENE_LIST}" \
        --candidate_gene_lookup "${CANDIDATE_GENE_LOOKUP}" \
        --candidate_lookup "${CANDIDATE_LOOKUP}" \
        --out_prefix "${OUT_PREFIX}"
fi

echo "Done."
echo "Matched genes: ${OUT_PREFIX}.matched_genes.tsv"
echo "Module summary: ${OUT_PREFIX}.module_summary.tsv"
echo "Unmatched genes: ${OUT_PREFIX}.unmatched_genes.tsv"

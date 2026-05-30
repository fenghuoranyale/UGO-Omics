#!/bin/bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
    echo "Usage:"
    echo "  bash run_sequence_to_UGO.sh query_proteins.fa output_prefix"
    echo
    echo "Example:"
    echo "  bash run_sequence_to_UGO.sh ../examples/example_query_proteins.fa ../example_results/my_query"
    exit 1
fi

QUERY_FASTA="$1"
OUT_PREFIX="$2"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLKIT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DB_DIR="${TOOLKIT_DIR}/database"

DB_FASTA="${DB_DIR}/UGO_11species_protein_search_database_v1.fa"
DB_DMND="${DB_DIR}/UGO_11species_protein_search_database_v1.dmnd"
LOOKUP="${DB_DIR}/UGO_sequence_to_orthogroup_lookup_v1.tsv"
MAPPER="${SCRIPT_DIR}/map_sequence_hits_to_UGO.py"

HITS="${OUT_PREFIX}.diamond_hits.tsv"
RESULT="${OUT_PREFIX}.sequence_to_UGO.tsv"

if ! command -v diamond >/dev/null 2>&1; then
    echo "ERROR: diamond is not available in PATH."
    echo "Please load or install DIAMOND first, then rerun."
    exit 1
fi

if [ ! -f "${DB_DMND}" ]; then
    echo "DIAMOND database not found. Building ${DB_DMND}"
    diamond makedb --in "${DB_FASTA}" -d "${DB_DMND%.dmnd}"
fi

echo "Running DIAMOND blastp"

diamond blastp \
    -q "${QUERY_FASTA}" \
    -d "${DB_DMND}" \
    -o "${HITS}" \
    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore \
    --max-target-seqs 25 \
    --evalue 1e-5 \
    --threads 8

echo "Mapping hits to UGO-Omics"

python3 "${MAPPER}" \
    --hits "${HITS}" \
    --lookup "${LOOKUP}" \
    --out "${RESULT}" \
    --top 5 \
    --min_pident 25 \
    --min_bitscore 50

echo "Done"
echo "Raw hits: ${HITS}"
echo "UGO result: ${RESULT}"

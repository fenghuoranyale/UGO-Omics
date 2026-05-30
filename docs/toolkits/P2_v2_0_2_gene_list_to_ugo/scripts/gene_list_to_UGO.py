#!/usr/bin/env python3

import argparse
import csv
from collections import defaultdict
from pathlib import Path

def safe(x):
    return "" if x is None else str(x).strip()

def clean_id(x):
    x = safe(x)
    if not x:
        return ""
    if x.startswith(">"):
        x = x[1:]
    x = x.split()[0]
    return x.strip()

def read_gene_list(path):
    genes = []
    seen = set()

    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            token = clean_id(line.split()[0].split(",")[0])

            if token and token not in seen:
                seen.add(token)
                genes.append(token)

    return genes

def read_tsv(path):
    with open(path, newline="", encoding="utf-8", errors="ignore") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def build_candidate_lookup(candidate_lookup_path):
    og_to_candidate = {}

    for r in read_tsv(candidate_lookup_path):
        og = safe(r.get("orthogroup"))
        if og:
            og_to_candidate[og] = r

    return og_to_candidate

def add_key(lookup, key, row):
    key = clean_id(key)

    if key:
        lookup.setdefault(key, []).append(row)

def build_gene_lookup(candidate_gene_lookup_path, full_lookup_path=None):
    lookup = {}

    # Compact candidate-level lookup.
    for r in read_tsv(candidate_gene_lookup_path):
        add_key(lookup, r.get("gene_id"), r)
        add_key(lookup, r.get("protein_id"), r)
        add_key(lookup, r.get("ugo_protein_id"), r)

    # Optional full lookup. This can be large and is distributed through the release archive/Zenodo.
    if full_lookup_path and Path(full_lookup_path).exists():
        for r in read_tsv(full_lookup_path):
            add_key(lookup, r.get("gene_id"), r)
            add_key(lookup, r.get("protein_id"), r)
            add_key(lookup, r.get("ugo_protein_id"), r)

    return lookup

def write_tsv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, delimiter="\t", fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})

def main():
    parser = argparse.ArgumentParser(description="Map DEG/QTL/GWAS gene lists to UGO-Omics orthogroups and candidate modules.")

    parser.add_argument("--genes", required=True, help="Input gene list, one gene/protein ID per line.")
    parser.add_argument("--candidate_gene_lookup", required=True, help="Compact candidate gene/protein lookup.")
    parser.add_argument("--candidate_lookup", required=True, help="Orthogroup-to-candidate-module lookup.")
    parser.add_argument("--out_prefix", required=True, help="Output prefix.")
    parser.add_argument("--full_lookup", default="", help="Optional full sequence-to-orthogroup lookup from the release archive.")

    args = parser.parse_args()

    input_genes = read_gene_list(args.genes)
    og_to_candidate = build_candidate_lookup(args.candidate_lookup)
    gene_lookup = build_gene_lookup(args.candidate_gene_lookup, args.full_lookup)

    matched_rows = []
    unmatched_rows = []

    for q in input_genes:
        hits = gene_lookup.get(q, [])

        if not hits:
            unmatched_rows.append({
                "input_id": q,
                "status": "unmatched",
                "note": "No direct gene/protein match in provided UGO lookup."
            })
            continue

        for h in hits:
            og = safe(h.get("orthogroup"))
            cand = og_to_candidate.get(og, {})

            candidate_function = safe(h.get("candidate_function")) or safe(cand.get("candidate_function"))
            benchmark_module = safe(h.get("benchmark_module")) or safe(cand.get("benchmark_module"))
            candidate_tier = safe(h.get("candidate_tier")) or safe(cand.get("candidate_tier"))
            ugo_score = safe(h.get("ugo_score")) or safe(cand.get("ugo_score"))
            validation_priority_score = safe(h.get("validation_priority_score")) or safe(cand.get("validation_priority_score"))
            validation_priority_class = safe(h.get("validation_priority_class")) or safe(cand.get("validation_priority_class"))
            biological_discovery_case = safe(h.get("biological_discovery_case")) or safe(cand.get("biological_discovery_case"))
            suggested_validation_system = safe(h.get("suggested_validation_system")) or safe(cand.get("suggested_validation_system"))
            suggested_assay = safe(h.get("suggested_assay")) or safe(cand.get("suggested_assay"))

            if candidate_function:
                interpretation = "Matched prioritized UGO candidate module."
            elif og:
                interpretation = "Matched UGO orthogroup, but not currently a prioritized candidate module."
            else:
                interpretation = "Matched lookup entry without orthogroup annotation."

            matched_rows.append({
                "input_id": q,
                "matched_gene_id": safe(h.get("gene_id")),
                "matched_protein_id": safe(h.get("protein_id")),
                "ugo_protein_id": safe(h.get("ugo_protein_id")),
                "species": safe(h.get("species")),
                "orthogroup": og,
                "species_present_11": safe(h.get("species_present_11")),
                "candidate_function": candidate_function,
                "benchmark_module": benchmark_module,
                "candidate_tier": candidate_tier,
                "ugo_score": ugo_score,
                "validation_priority_score": validation_priority_score,
                "validation_priority_class": validation_priority_class,
                "biological_discovery_case": biological_discovery_case,
                "suggested_validation_system": suggested_validation_system,
                "suggested_assay": suggested_assay,
                "UGO_interpretation": interpretation
            })

    module_counter = defaultdict(lambda: {
        "input_gene_count": 0,
        "matched_records": 0,
        "orthogroup": "",
        "candidate_function": "",
        "benchmark_module": "",
        "candidate_tier": "",
        "ugo_score": "",
        "validation_priority_score": "",
        "validation_priority_class": "",
        "biological_discovery_case": "",
        "suggested_validation_system": "",
        "example_input_ids": []
    })

    seen_gene_module = set()

    for r in matched_rows:
        key = r["orthogroup"] or "NA_orthogroup"
        module_counter[key]["orthogroup"] = r["orthogroup"]
        module_counter[key]["candidate_function"] = r["candidate_function"]
        module_counter[key]["benchmark_module"] = r["benchmark_module"]
        module_counter[key]["candidate_tier"] = r["candidate_tier"]
        module_counter[key]["ugo_score"] = r["ugo_score"]
        module_counter[key]["validation_priority_score"] = r["validation_priority_score"]
        module_counter[key]["validation_priority_class"] = r["validation_priority_class"]
        module_counter[key]["biological_discovery_case"] = r["biological_discovery_case"]
        module_counter[key]["suggested_validation_system"] = r["suggested_validation_system"]
        module_counter[key]["matched_records"] += 1

        gm = (r["input_id"], key)
        if gm not in seen_gene_module:
            module_counter[key]["input_gene_count"] += 1
            seen_gene_module.add(gm)

        if len(module_counter[key]["example_input_ids"]) < 8:
            module_counter[key]["example_input_ids"].append(r["input_id"])

    module_rows = []
    for key, v in module_counter.items():
        module_rows.append({
            "orthogroup": v["orthogroup"],
            "candidate_function": v["candidate_function"],
            "benchmark_module": v["benchmark_module"],
            "candidate_tier": v["candidate_tier"],
            "input_gene_count": v["input_gene_count"],
            "matched_records": v["matched_records"],
            "ugo_score": v["ugo_score"],
            "validation_priority_score": v["validation_priority_score"],
            "validation_priority_class": v["validation_priority_class"],
            "biological_discovery_case": v["biological_discovery_case"],
            "suggested_validation_system": v["suggested_validation_system"],
            "example_input_ids": ";".join(v["example_input_ids"])
        })

    def score_value(x):
        try:
            return float(x)
        except Exception:
            return 0.0

    module_rows = sorted(
        module_rows,
        key=lambda r: (
            -int(r.get("input_gene_count") or 0),
            -score_value(r.get("validation_priority_score")),
            -score_value(r.get("ugo_score")),
            r.get("candidate_function", "")
        )
    )

    matched_cols = [
        "input_id",
        "matched_gene_id",
        "matched_protein_id",
        "ugo_protein_id",
        "species",
        "orthogroup",
        "species_present_11",
        "candidate_function",
        "benchmark_module",
        "candidate_tier",
        "ugo_score",
        "validation_priority_score",
        "validation_priority_class",
        "biological_discovery_case",
        "suggested_validation_system",
        "suggested_assay",
        "UGO_interpretation"
    ]

    module_cols = [
        "orthogroup",
        "candidate_function",
        "benchmark_module",
        "candidate_tier",
        "input_gene_count",
        "matched_records",
        "ugo_score",
        "validation_priority_score",
        "validation_priority_class",
        "biological_discovery_case",
        "suggested_validation_system",
        "example_input_ids"
    ]

    unmatched_cols = [
        "input_id",
        "status",
        "note"
    ]

    write_tsv(args.out_prefix + ".matched_genes.tsv", matched_rows, matched_cols)
    write_tsv(args.out_prefix + ".module_summary.tsv", module_rows, module_cols)
    write_tsv(args.out_prefix + ".unmatched_genes.tsv", unmatched_rows, unmatched_cols)

    print("Input IDs:", len(input_genes))
    print("Matched input IDs:", len(set(r["input_id"] for r in matched_rows)))
    print("Unmatched input IDs:", len(unmatched_rows))
    print("Matched records:", len(matched_rows))
    print("Matched modules:", len(module_rows))
    print("Wrote:", args.out_prefix + ".matched_genes.tsv")
    print("Wrote:", args.out_prefix + ".module_summary.tsv")
    print("Wrote:", args.out_prefix + ".unmatched_genes.tsv")

if __name__ == "__main__":
    main()

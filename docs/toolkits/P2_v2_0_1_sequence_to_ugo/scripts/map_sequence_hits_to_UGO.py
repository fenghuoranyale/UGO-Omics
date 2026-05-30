#!/usr/bin/env python3

import argparse
import csv

def safe(x):
    return "" if x is None else str(x).strip()

def load_lookup(path):
    lookup = {}

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for r in reader:
            keys = [
                safe(r.get("search_database_header")),
                safe(r.get("ugo_protein_id")),
                safe(r.get("protein_id")),
                safe(r.get("gene_id")),
            ]

            header = safe(r.get("search_database_header"))
            if header:
                keys.append(header.split()[0])

            for key in keys:
                if key:
                    lookup[key] = r

    return lookup

def subject_keys(sseqid):
    sseqid = safe(sseqid)
    keys = [sseqid]

    if "|" in sseqid:
        parts = sseqid.split("|")
        keys.append(parts[0])

        for part in parts:
            if part.startswith("protein="):
                keys.append(part.replace("protein=", "", 1))
            if part.startswith("gene="):
                keys.append(part.replace("gene=", "", 1))

    return keys

def parse_evalue(x):
    try:
        return float(x)
    except Exception:
        return 999.0

def main():
    parser = argparse.ArgumentParser(description="Map DIAMOND/BLAST tabular hits to UGO-Omics candidate modules.")
    parser.add_argument("--hits", required=True)
    parser.add_argument("--lookup", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--min_pident", type=float, default=25.0)
    parser.add_argument("--min_bitscore", type=float, default=50.0)
    args = parser.parse_args()

    lookup = load_lookup(args.lookup)
    hits_by_query = {}

    with open(args.hits, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue

            parts = line.rstrip("\n").split("\t")
            if len(parts) < 12:
                continue

            qseqid = parts[0]
            sseqid = parts[1]
            pident = float(parts[2])
            length = int(float(parts[3]))
            evalue = parts[10]
            bitscore = float(parts[11])

            if pident < args.min_pident or bitscore < args.min_bitscore:
                continue

            rec = None
            for key in subject_keys(sseqid):
                if key in lookup:
                    rec = lookup[key]
                    break

            if rec is None:
                continue

            row = {
                "query_id": qseqid,
                "hit_subject_id": sseqid,
                "pident": pident,
                "alignment_length": length,
                "evalue": evalue,
                "bitscore": bitscore,
                "hit_species": rec.get("species", ""),
                "hit_gene_id": rec.get("gene_id", ""),
                "hit_protein_id": rec.get("protein_id", ""),
                "hit_orthogroup": rec.get("orthogroup", ""),
                "species_present_11": rec.get("species_present_11", ""),
                "candidate_function": rec.get("candidate_function", ""),
                "benchmark_module": rec.get("benchmark_module", ""),
                "candidate_tier": rec.get("candidate_tier", ""),
                "ugo_score": rec.get("ugo_score", ""),
                "validation_priority_score": rec.get("validation_priority_score", ""),
                "validation_priority_class": rec.get("validation_priority_class", ""),
                "biological_discovery_case": rec.get("biological_discovery_case", ""),
                "suggested_validation_system": rec.get("suggested_validation_system", ""),
                "suggested_assay": rec.get("suggested_assay", ""),
            }

            hits_by_query.setdefault(qseqid, []).append(row)

    out_rows = []

    for q, rows in hits_by_query.items():
        rows = sorted(rows, key=lambda r: (-float(r["bitscore"]), parse_evalue(r["evalue"])))

        for rank, r in enumerate(rows[:args.top], 1):
            r["hit_rank"] = rank

            if r["candidate_function"]:
                r["UGO_interpretation"] = "Matched UGO candidate module; inspect validation-priority fields and species-specific homologs."
            elif r["hit_orthogroup"]:
                r["UGO_interpretation"] = "Matched UGO 11-species orthogroup, but not currently in prioritized candidate modules."
            else:
                r["UGO_interpretation"] = "No UGO orthogroup annotation recovered for this hit."

            out_rows.append(r)

    fieldnames = [
        "query_id",
        "hit_rank",
        "hit_subject_id",
        "pident",
        "alignment_length",
        "evalue",
        "bitscore",
        "hit_species",
        "hit_gene_id",
        "hit_protein_id",
        "hit_orthogroup",
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
        "UGO_interpretation",
    ]

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, delimiter="\t", fieldnames=fieldnames)
        writer.writeheader()
        for r in out_rows:
            writer.writerow(r)

    print(f"Wrote {args.out}")
    print(f"Queries with mapped hits: {len(hits_by_query)}")
    print(f"Output rows: {len(out_rows)}")

if __name__ == "__main__":
    main()

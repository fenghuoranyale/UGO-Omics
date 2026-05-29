# UGO-Omics MP submission-ready package

## Purpose

This package contains the current Molecular Plant-oriented UGO-Omics submission materials, including the MP-polished manuscript, final Figure 1–6 order, Supplementary Figure S1, public-ready Supplementary Tables S6–S9, static website, JSON browser layers, and Figure 4/5 source materials.

## Main evidence layers

UGO-Omics integrates:

1. A six-species expression-backed underground-organ analytical core.
2. A 51-species broad underground-organ resource layer.
3. A 9-species expanded OrthoFinder backbone.
4. Candidate expansion traceability across newly added broad-layer species.
5. Known-module benchmark recovery at a conservative gene-family/pathway-module level.
6. A static website exposing species, candidate, orthogroup, candidate expansion, and benchmark recovery layers.

## Key quantitative results

- 9-species expanded OrthoFinder backbone: 26,459 orthogroups.
- Orthogroups present in all 9 species: 7,346.
- Orthogroups present in at least 8 species: 10,223.
- Prioritized candidate orthogroups remapped to expanded backbone: 8/8.
- Prioritized candidates traceable in at least one newly added broad-layer species: 8/8.
- Curated benchmark modules recovered by prioritized candidates: 11/15.
- Candidate-benchmark recovery links: 30.

## Final figure order

- Figure 1: UGO-Omics workflow and data architecture.
- Figure 2: Candidate prioritization funnel.
- Figure 3: Prioritized candidate heatmap.
- Figure 4: Candidate traceability in the 9-species expanded backbone.
- Figure 5: Known-module benchmark recovery.
- Figure 6: Website interface and browsable layers.
- Supplementary Figure S1: Conservative benchmark recovery multipanel.

## Directory structure

- manuscript/
  - MP-polished consistency-checked manuscript and editorial notes.
- figures/
  - Final Figure 1–6 and Supplementary Figure S1 in PDF/PNG format.
- supplementary_tables/
  - Public-ready Supplementary Tables S6–S9.
- website/
  - Static website with Species Browser, Candidate Expansion, and Benchmark Recovery pages.
- json/
  - Website JSON data layers.
- source_tables/
  - Figure source tables, captions, and final figure-order decision table.

## Website local viewing

From the `website/` directory, run:

python3 -m http.server 8899

Then open:

http://localhost:8899

## Public release note

Before submission or publication, replace repository placeholders with the final public repository URL, DOI, and deployed website link.

## Claim calibration

Candidate and benchmark layers should be interpreted as prioritized, traceable, and module-level recovery evidence. They should not be described as functionally proven regulators unless direct functional validation is later added.

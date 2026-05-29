# UGO-Omics

UGO-Omics is an expression-backed orthogroup resource for comparative underground-organ biology.

UGO-Omics integrates public underground-organ transcriptomes, reference annotations, organ-associated expression scoring, cross-species orthogroup inference, candidate prioritization, benchmark recovery, and a static website. The resource supports comparative analysis across rhizome, tuber/stolon, storage-root, root-crown, bulb, corm, and related underground-organ systems.

## Main evidence layers

UGO-Omics includes:

1. A six-species expression-backed underground-organ analytical core.
2. A 51-species broad underground-organ resource layer.
3. A 9-species expanded OrthoFinder backbone.
4. Candidate expansion traceability across newly added broad-layer species.
5. Known-module benchmark recovery at a conservative gene-family/pathway-module level.
6. A static website exposing species, candidate, orthogroup, candidate expansion, benchmark recovery, and download layers.

## Key quantitative results

- 9-species expanded OrthoFinder backbone: 26,459 orthogroups.
- Orthogroups present in all 9 species: 7,346.
- Orthogroups present in at least 8 species: 10,223.
- Prioritized candidate orthogroups remapped to expanded backbone: 8/8.
- Prioritized candidates traceable in at least one newly added broad-layer species: 8/8.
- Curated benchmark modules recovered by prioritized candidates: 11/15.
- Candidate-benchmark recovery links: 30.

## Repository structure

- `docs/`
  - Static website for GitHub Pages.
- `data/json/`
  - JSON browser layers used by the website.
- `manuscript_support/manuscript/`
  - MP-polished manuscript draft.
- `manuscript_support/figures/`
  - Final Figures 1–6 and Supplementary Figure S1.
- `manuscript_support/supplementary_tables/`
  - Public-ready Supplementary Tables S6–S9.
- `manuscript_support/source_tables/`
  - Figure source tables, captions, and figure-order decision table.

## Website

After GitHub Pages is enabled, the website will be available at:

https://fenghuoranyale.github.io/UGO-Omics/

## Citation

A Zenodo DOI will be added after the first archived release.

## Claim calibration

Candidate and benchmark layers should be interpreted as prioritized, traceable, and module-level recovery evidence. They should not be described as functionally proven regulators unless direct functional validation is later added.

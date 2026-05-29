# UGO-Omics

UGO-Omics is an application-oriented cross-species platform for underground-organ candidate discovery and transfer.

## Website

- Web platform: https://fenghuoranyale.github.io/UGO-Omics/
- Public repository: https://github.com/fenghuoranyale/UGO-Omics

## What UGO-Omics does

UGO-Omics supports four user-facing discovery workflows:

1. **Check a Gene**  
   Query a gene ID, orthogroup, gene family, or annotation keyword to evaluate whether it belongs to a UGO candidate module.

2. **Find Candidates by Organ**  
   Select an underground-organ type such as rhizome, tuber, storage root, bulb, corm, root crown, or stolon to retrieve prioritized candidate modules.

3. **Find Candidates by Species**  
   Select a species to view candidate modules with homologous members in that species.

4. **Prioritize Validation Targets**  
   Generate a ranked shortlist of candidate modules for functional follow-up, including suggested validation systems and assays.

## Resource layers

UGO-Omics currently integrates:

- a six-species expression-backed analytical core;
- an 11-species high-confidence transfer backbone;
- a 51-species broad underground-organ resource layer.

The 11-species backbone contains 30121 orthogroups, including 7378 represented in all 11 species. All 8 prioritized candidate modules were remapped to this backbone, and 7 were traceable in both newly added species, Panicum virgatum and Dioscorea rotundata.

## Public repository contents

This public repository contains:

- `docs/`: GitHub Pages website source;
- `docs/json/`: JSON data layers used by the web platform;
- `data/`: reusable data layers;
- `resources/`: figures, source tables, and supplementary tables;
- `CITATION.cff`;
- `LICENSE`.

The public repository is limited to the public website, reusable data layers, figures, source tables, and supplementary resources.

## Claim calibration

UGO-Omics is a candidate-prioritization and hypothesis-generation platform. Candidate traceability, UGO scores, and validation-priority rankings should not be interpreted as functional validation.

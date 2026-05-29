# UGO-Omics reveals conserved gene modules underlying plant underground organ development and regeneration

Generated on: 2026-05-28 22:02:34

## Highlights

- UGO-Omics integrates underground-organ expression, orthogroups, benchmark recovery, and web exploration.
- A six-species backbone assigns 208,448 genes to 25,195 orthogroups across major underground-organ systems.
- Lotus and ginger rhizome data strengthen six of eight prioritized candidate orthogroups.
- Conserved candidates include cell-wall remodeling, developmental transcription factor, meristem/regrowth, and stress-resilience modules.
- A static website enables candidate, orthogroup, benchmark, and download exploration.


# Abstract

Underground organs such as rhizomes, tubers, stolons, bulbs, corms, storage roots, and root crowns enable plants to persist, store resources, regenerate after disturbance, and adapt to seasonal or stressful environments. Despite their ecological and agricultural importance, comparative molecular resources for underground-organ biology remain fragmented across species, organ types, and experimental systems. Here we present UGO-Omics, an expression-backed orthogroup resource for comparative underground-organ biology. UGO-Omics integrates public transcriptomes, reference annotations, organ-associated expression scoring, cross-species orthogroup inference, candidate prioritization, benchmark recovery, and a static web interface. The initial analytical core links six species spanning rhizome, tuber/stolon, and storage-root contexts, and a broader 51-species layer extends the resource across major underground-organ categories. Candidate prioritization identified conserved modules associated with cell-wall remodeling, meristem and regrowth programs, developmental transcriptional regulation, hormone-related regulation, and stress resilience. To test whether prioritized candidates could be projected beyond the original analytical core, we constructed a 9-species expanded OrthoFinder backbone by adding Beta vulgaris, Brassica rapa, and Musa acuminata. This expanded backbone contained 26,459 orthogroups, including 7,346 represented in all nine species. All eight prioritized candidate orthogroups were remapped to the expanded backbone, and all eight retained homologous members in at least one newly added broad-layer species. A conservative known-module benchmark recovered 11 of 15 curated underground-organ or storage-organ modules among prioritized candidates, including meristem/regrowth, hormone regulation, cell-wall remodeling, bud branching, developmental transition, NAC-related regulation, and hypoxia/stress-resilience modules. UGO-Omics therefore provides a reusable framework for transferring candidate modules across underground-organ systems and for generating testable hypotheses in comparative plant developmental, regenerative, and storage-organ biology.

# Introduction

Underground organs are among the most important yet least systematically compared structures in plant biology. Rhizomes, tubers, stolons, bulbs, corms, storage roots, and root crowns contribute to clonal propagation, carbohydrate storage, vegetative persistence, stress survival, and regeneration after disturbance. These traits shape ecological resilience in wild species and agronomic performance in crops, yet their molecular basis is usually studied within individual species or organ types. As a result, it remains difficult to distinguish broadly recurrent underground-organ modules from lineage-specific or organ-specific programs.

Comparative omics offers a route to identify shared and divergent molecular components across underground-organ systems. However, simple gene-level comparisons are limited by differences in gene annotation, genome quality, expression datasets, and organ terminology. Orthogroup-centered analysis can partially overcome these challenges by linking species-specific genes through evolutionary correspondence, allowing expression and functional evidence to be summarized across diverse species. This is especially useful for underground organs, where homologous or functionally analogous structures may differ in developmental origin, morphology, and ecological role.

UGO-Omics was designed as a resource-plus-discovery framework for this problem. The current analysis uses a deeply processed six-species expression-backed core spanning tuber/stolon, storage-root or taproot, and rhizome contexts. This core is not intended to represent the final taxonomic breadth of the platform; rather, it provides a rigorous implementation in which reference resources, RNA-seq quantification, organ-associated scoring, orthogroup construction, candidate tracking, benchmark recovery, and website-ready data layers can be evaluated end to end. The framework is designed to support later broad-layer expansion across additional underground-organ-bearing species.

A key challenge for rhizome biology is distinguishing robust rhizome-associated signals from species-specific or dataset-specific patterns. To address this, we incorporated lotus and ginger as independent rhizome systems and used them to test whether candidate orthogroups originally prioritized from the core analysis were supported by additional rhizome evidence. We further evaluated candidate interpretability through conservative benchmark recovery, focusing on biological modules expected to contribute to underground-organ initiation, growth, storage, stress resilience, and regeneration. Together, these analyses establish UGO-Omics as both a browsable resource and a hypothesis-generating framework for underground-organ biology.


# Results

## UGO-Omics links underground-organ transcriptomes to a comparative orthogroup framework

UGO-Omics was designed to address a central limitation in underground-organ biology: relevant transcriptomic and genomic resources exist across multiple species, but they are rarely organized into a shared comparative framework. We therefore built a resource structure that connects public underground-organ transcriptomes, reference annotations, gene-level expression evidence, orthogroup inference, candidate prioritization, benchmark recovery, and web-based exploration. The analytical core includes six species representing rhizome, tuber/stolon, and storage-root or taproot contexts, while a broader 51-species layer records candidate taxa and resource status across rhizome, tuber, bulb, corm, storage-root, root-crown, and stolon systems.

Across the six-species framework, UGO-Omics mapped gene-level evidence onto orthogroups and used underground-organ-associated expression scores to prioritize conserved candidate modules. This design allowed candidates to be evaluated at the orthogroup level rather than as isolated gene lists from individual species. The resulting resource therefore separates three related but distinct layers: expression support within underground-organ datasets, cross-species orthogroup membership, and candidate interpretability through functional annotation and benchmark modules.

## Candidate prioritization identifies conserved modules supported by rhizome evidence

The candidate prioritization workflow started from 227,847 input genes or proteins, of which 208,448 were assigned to 25,195 orthogroups. The six-species backbone included 7,533 orthogroups represented across all six species and 99 single-copy orthogroups. Rhizome evidence from lotus and ginger identified 6,924 rhizome-supported orthogroups, including benchmark-supported modules and a larger poorly annotated candidate space.

Tracking the prioritized candidate set into the six-species backbone identified eight main candidate orthogroups. Six of these gained high-confidence lotus or ginger rhizome support. These candidates included modules associated with xyloglucan cell-wall remodeling, early nodulin-like meristem or regrowth activity, bHLH-like and MYB-like transcriptional regulation, non-symbiotic hemoglobin-linked stress resilience, carotenoid cleavage dioxygenase or hormone-related regulation, and NAC-like transcriptional regulation. Together, these results show that UGO-Omics prioritizes biologically interpretable modules while also preserving candidates that may represent less-characterized underground-organ biology.

## A 9-species expanded backbone supports candidate transfer beyond the analytical core

To test whether prioritized UGO-Omics candidate modules remained traceable beyond the original six-species analytical core, we constructed a 9-species expanded OrthoFinder backbone by adding three broad-layer species with high-confidence proteome resources: Beta vulgaris, Brassica rapa, and Musa acuminata. These species were selected because genome annotation, protein FASTA, and GFF3 resources were available and could be processed into longest-protein-per-gene datasets.

The 9-species OrthoFinder run produced 26,459 orthogroups, including 7,346 orthogroups represented in all nine species and 10,223 represented in at least eight species. All nine proteomes contributed substantially to the expanded backbone, with 23,231 to 64,644 genes per species assigned to orthogroups. The expanded backbone therefore provides a usable comparative framework rather than a sparse or species-biased extension.

We next remapped the eight prioritized UGO candidate orthogroups from the six-species core onto the 9-species expanded backbone using member-gene overlap. All eight prioritized candidates were successfully mapped to 9-species orthogroups, and all eight retained homologous members in at least one newly added broad-layer species. Several candidates, including xyloglucan cell-wall remodeling, early nodulin-like meristem/regrowth, bHLH-like and MYB-like transcriptional regulators, non-symbiotic hemoglobin, carotenoid cleavage dioxygenase, and NAC-like candidates, were represented across all six core species and all three newly added species. These results show that the prioritized UGO-Omics candidate space is not restricted to the original analytical core and can be projected onto an expanded cross-species backbone for candidate transfer.

## Prioritized candidates recover curated underground-organ benchmark modules

To evaluate whether prioritized UGO-Omics candidates recovered expected biological layers for underground-organ and storage-organ biology, we curated a conservative benchmark set of 15 gene-family or pathway modules. These modules included meristem identity, regenerative meristem activity, auxin signaling and transport, gibberellin and brassinosteroid regulation, sugar transport, starch biosynthesis, cell-wall remodeling, tuberization or phase transition, mobile developmental signaling, bud outgrowth, NAC-related developmental and stress regulation, and hypoxia or stress resilience. We treated these entries as family- or pathway-level benchmarks rather than as broad functional regulators across underground-organ systems.

The prioritized candidate set recovered 11 of 15 benchmark modules, producing 30 candidate-benchmark recovery links. Recovered modules included cell-wall remodeling, meristem and regenerative growth, bud outgrowth, phase transition or tuberization, hormone regulation, NAC-related developmental and stress regulation, and hypoxia or stress resilience. Four modules—LBD/ASL lateral organ rooting, PIN/AUX-LAX auxin transport, sugar transport, and starch biosynthesis—were not recovered by the prioritized candidate set. These non-recovered modules are not interpreted as absent from UGO-Omics overall, because this analysis tested only the prioritized candidate set rather than all expanded orthogroups. Together, the benchmark recovery analysis shows that prioritized UGO-Omics candidates capture multiple expected biological modules while also highlighting benchmark layers that may require broader orthogroup-level mining beyond the current top candidate set.

## A static website exposes candidate, orthogroup, species, expansion, and benchmark layers

To make the resource reusable, we implemented UGO-Omics as a static HTML/JavaScript website powered by compact JSON files. The website includes pages for species browsing, candidate browsing, benchmark summaries, top orthogroups, downloads, candidate expansion, and known-module benchmark recovery. The Species Browser exposes the 51-species broad underground-organ resource layer, including organ category, clade, resource triage, and candidate use case. The Candidate Expansion page exposes the 9-species candidate traceability analysis, and the Benchmark Recovery page exposes curated known-module recovery results. This structure makes the resource portable and easy to host, while preserving transparent links between expression evidence, orthogroups, candidate prioritization, benchmark recovery, and downloadable data layers.

# Discussion

UGO-Omics addresses a persistent gap in plant biology: underground organs are central to persistence, regeneration, storage, and adaptation, but their molecular resources remain scattered across species and organ types. Rather than treating each transcriptome as an isolated gene list, UGO-Omics organizes underground-organ evidence into an orthogroup-centered framework. This structure allows candidate modules to be compared across rhizome, tuber/stolon, storage-root, and related underground-organ systems, while retaining species-specific evidence and annotation.

A major strength of the current resource is that candidate prioritization is supported by multiple complementary layers. The six-species analytical core provides expression-backed orthogroup discovery. Lotus and ginger rhizome evidence strengthens several prioritized candidates. The 9-species expanded backbone shows that all eight prioritized candidate orthogroups remain traceable beyond the original analytical core. Finally, the curated benchmark analysis shows that prioritized candidates recover 11 of 15 expected underground-organ or storage-organ modules at a conservative family or pathway level. These layers are mutually reinforcing: expression evidence identifies candidates, orthogroups make them transferable, benchmark recovery calibrates biological plausibility, and the website makes the results reusable.

The candidate modules highlighted by UGO-Omics are consistent with a view of underground organs as integrated developmental, regenerative, storage, and stress-resilience systems. Cell-wall remodeling candidates may contribute to organ elongation, swelling, or tissue expansion. Meristem and transcriptional-regulatory candidates are consistent with underground bud activity, shoot-like developmental programs, and regrowth potential. Hormone-related candidates may link underground-organ initiation and developmental transitions to auxin, gibberellin, brassinosteroid, or carotenoid-derived pathways. Non-symbiotic hemoglobin and NAC-like candidates suggest that underground organs may also rely on stress-resilience and low-oxygen response modules. These interpretations remain hypotheses, but they provide concrete targets for future functional and comparative studies.

The benchmark recovery analysis also clarifies what the current prioritized candidate set does not yet capture. LBD/ASL lateral organ rooting, PIN/AUX-LAX auxin transport, sugar transport, and starch biosynthesis modules were not recovered among the eight prioritized candidates. This does not mean these processes are absent from UGO-Omics. Instead, it indicates that the current top candidate set is enriched for developmental, regulatory, cell-wall, and stress-resilience modules, whereas storage metabolism and transport layers may require broader mining of the expanded orthogroup resource. This distinction is important because a useful resource should identify strong candidates while also revealing where additional targeted searches are needed.

UGO-Omics should be interpreted as a candidate-prioritization and comparative resource, not as functional validation of individual regulators. The current framework prioritizes orthogroups, tracks candidate modules across species, and recovers expected biological benchmark layers. Experimental validation, perturbation studies, and species-specific developmental analyses will be required to test the functions of individual genes. This claim calibration is especially important for large cross-species resources, where homology, annotation, and expression support can generate strong hypotheses but cannot by themselves establish gene function.

The current implementation is intentionally portable. A static website backed by JSON files allows the resource to be deployed without a complex server environment and makes it easier to archive, mirror, and update. Future versions can extend the broad species layer, integrate additional underground-organ transcriptomes, add QTL and GWAS tracks, and support richer gene-level search across expanded orthogroups. The current release establishes the core framework: expression-backed underground-organ evidence, orthogroup-centered candidate transfer, benchmark recovery, and reusable web access. This provides a foundation for comparative underground-organ biology and for identifying candidate modules that may underlie persistence, regeneration, storage, and adaptation across plants.

# Methods

## RNA-seq quantification

Transcript abundance was estimated using Salmon v1.4.0. For each species, a Salmon transcriptome index was generated from the corresponding transcript FASTA file using `salmon index -t <transcript_fasta> -i <index_dir> -p <threads>`. RNA-seq libraries were quantified with automatic library-type detection (`-l A`) and selective-alignment-based mapping validation (`--validateMappings`). Paired-end libraries were quantified using `-1 <read1> -2 <read2>`, whereas single-end libraries were quantified using `-r <reads>`. Quantification was performed with the available thread count specified for each run. Successful quantification was defined by the presence of a non-empty `quant.sf` file in the Salmon output directory; runs with missing FASTQ files, incurrent paired-end files, or missing `quant.sf` outputs were excluded from downstream expression scoring.

## Gene-level expression summarization

Transcript-level Salmon TPM estimates were summarized to gene-level TPM values using transcript-to-gene mappings derived from the corresponding genome annotation. For each gene, TPM values from all transcripts assigned to that gene were summed within each sample to generate a gene-level expression matrix. These gene-level TPM matrices were used for target-versus-control organ scoring.

## Rhizome-associated gene scoring

For lotus and ginger, rhizome-associated expression was quantified by comparing curated rhizome samples against non-rhizome control organs. For each gene, the mean and median TPM were calculated separately across target rhizome samples and control samples. Target-versus-control log2 fold change was calculated as:

log2FC = log2((target_mean_TPM + 0.1) / (control_mean_TPM + 0.1))

Rhizome specificity was calculated as:

specificity = target_mean_TPM / (target_mean_TPM + control_mean_TPM)

when the sum of target and control mean TPM values was greater than zero. Detection consistency was calculated as the fraction of target rhizome samples with TPM ≥ 1. The final rhizome association score was calculated as:

organ_score = log2(target_mean_TPM + 1) × (1 + max(log2FC, 0)) × specificity × target_detection_fraction

Genes were classified as high-confidence rhizome-associated genes if they satisfied all of the following criteria: target mean TPM ≥ 2.0, log2FC ≥ 1.0, rhizome specificity ≥ 0.50, and target detection fraction ≥ 0.5. Genes with target mean TPM ≥ 2.0 and log2FC ≥ 0.5, but not meeting all high-confidence criteria, were classified as moderate rhizome-associated genes. Genes with target mean TPM ≥ 2.0 but weaker enrichment were classified as expressed in rhizome, and all remaining genes were classified as low or not rhizome-associated. These classifications were used for downstream orthogroup-level rhizome support.

## Six-species orthogroup inference

Orthogroups were inferred using OrthoFinder v2.5.4. For each species, one longest protein isoform per gene was retained as the input proteome. OrthoFinder was run on the six-species longest-protein directory using:

orthofinder -f <input_proteome_directory> -o <output_directory> -t <threads> -a <threads>

where `<threads>` corresponded to the allocated CPU count. The resulting `Orthogroups.tsv`, `Orthogroups.GeneCount.tsv`, and comparative genomics statistics were used to define the six-species orthogroup backbone.

## Candidate tracking across orthogroup versions

Because adding lotus and ginger required rebuilding the orthogroup backbone, candidate orthogroup identifiers were not assumed to be stable across framework versions. Candidate continuity was therefore determined using member-gene overlap. For each previously prioritized candidate orthogroup, member genes present in the expanded six-species analysis were identified, and the expanded orthogroup containing the largest number of overlapping genes was selected as the best match. The overlap fraction was calculated as the best overlap count divided by the number of mappable member genes in the original candidate orthogroup. Candidates with partial orthogroup splitting were retained with caution when their biological annotation and support pattern remained consistent.

## Lotus and ginger orthogroup support

High-confidence and moderate rhizome-associated genes from lotus and ginger were mapped onto the expanded six-species orthogroups. For each orthogroup, we counted the number of lotus and ginger genes, high-confidence rhizome-associated genes, and moderate rhizome-associated genes. Orthogroups were classified as having both-species high-confidence support, lotus-only high-confidence support, ginger-only high-confidence support, moderate lotus/ginger support, or no lotus/ginger rhizome support. Candidate tiers were updated based on the original candidate status, orthogroup continuity, lotus/ginger high-confidence support, benchmark recovery, and whether the orthogroup showed evidence of splitting.

## Conservative benchmark module recovery

Benchmark module recovery was performed using a conservative, boundary-aware keyword matching strategy applied to gene annotations within lotus- and ginger-supported orthogroups. Benchmark modules included developmental transcriptional regulation, meristem/bud/regrowth, stress resilience, cell-wall remodeling, hormone-related regulation, carbohydrate storage metabolism, transport, and a no-benchmark-keyword class. Short ambiguous terms were excluded, and keyword matches were evaluated using conservative pattern matching rather than unrestricted substring matching. For each orthogroup, matched keyword counts were summarized by module, and the primary benchmark module was selected as the module with the highest keyword hit count. If no benchmark keyword was detected, the orthogroup was assigned to the no-benchmark-keyword class. For candidate orthogroups, benchmark evidence scores combined benchmark keyword hits with lotus and ginger rhizome-support counts.

## Data and code availability

The analysis generated tab-delimited candidate tables, rhizome-associated gene score tables, benchmark recovery tables, compact JSON files, manuscript figures, and a static website. Before submission, these files should be deposited in a stable public repository, and the manuscript should include accession numbers for raw RNA-seq datasets, genome and annotation sources, code repository links, and a versioned data DOI.

Sample and accession metadata are provided in Supplementary Table S1. Reference genome and annotation resources are provided in Supplementary Table S2. Conservative benchmark modules and keyword rules are provided in Supplementary Table S3. Website JSON schema fields are provided in Supplementary Table S4. The reproducible workflow and final script order are summarized in Supplementary Table S5. The 9-species expanded OrthoFinder summary and per-species representation are provided in Supplementary Table S6. Candidate expansion traceability and Figure 4 source data are provided in Supplementary Table S7. The curated known-module benchmark seed and recovery tables are provided in Supplementary Tables S8a and S8b. The website page, JSON-layer, and figure/source asset manifest is provided in Supplementary Table S9.

# Data and website availability

The UGO-Omics static website, JSON browser layers, figure source tables, orthogroup summaries, candidate expansion outputs, benchmark recovery tables, and public-ready release package will be made available through a public repository before publication. The current website implementation includes Species Browser, Candidate Expansion, Benchmark Recovery, Candidate Browser, Benchmark Summary, Top Orthogroups, and Downloads pages.

# Figure legends

# Figure 1. UGO-Omics workflow and data architecture

UGO-Omics integrates public underground-organ transcriptomes, reference annotations, organ-associated expression scoring, six-species orthogroup construction, candidate tracking, benchmark recovery, expanded candidate transfer, and web-based exploration. The framework links species representing tuber/stolon, storage-root or taproot, and rhizome contexts. Gene-level expression evidence is mapped onto orthogroups, prioritized into candidate modules, evaluated using rhizome support and benchmark recovery, and exposed through candidate, orthogroup, species, benchmark, expansion, and download browsers.

# Figure 2. UGO-Omics candidate prioritization funnel

Candidate prioritization in the UGO-Omics framework. The six-species analysis started from 227,847 input genes or proteins, of which 208,448 were assigned to 25,195 orthogroups. The backbone included 7,533 orthogroups with all six species represented and 99 single-copy orthogroups. Lotus and ginger rhizome evidence identified 6,924 rhizome-supported orthogroups, including benchmark-supported modules and a large poorly annotated candidate pool. Tracking the prioritized candidate set identified eight main candidates, six of which gained high-confidence lotus or ginger rhizome support.

# Figure 3. Prioritized UGO candidates strengthened by lotus and ginger rhizome evidence

Candidate heatmap showing lotus and ginger rhizome support for prioritized UGO candidate orthogroups after mapping candidates onto the six-species orthogroup backbone. Rows represent tracked candidate orthogroups and representative functions. Columns show the number of high-confidence and moderate-support rhizome-associated genes from lotus and ginger, together with conservative benchmark evidence scores. Six of eight prioritized candidates gained high-confidence lotus or ginger rhizome support, including candidates associated with xyloglucan cell-wall remodeling, bHLH- and MYB-like transcriptional regulation, early nodulin-like meristem/regrowth activity, and non-symbiotic hemoglobin-linked stress resilience.

# Figure 4. Candidate traceability in the 9-species expanded UGO-Omics backbone

Prioritized UGO-Omics candidate orthogroups were remapped from the six-species core onto a 9-species expanded OrthoFinder backbone containing three newly added broad-layer species: Beta vulgaris, Brassica rapa, and Musa acuminata. Rows represent prioritized candidate orthogroups and their representative functions. Columns show species-level gene counts within the mapped 9-species orthogroup. Green cells indicate candidate traceability in newly added broad-layer species, blue cells indicate presence in the original deep-core species, and grey cells indicate absence. All eight prioritized candidates were successfully remapped to the expanded backbone and retained homologous members in at least one newly added species, supporting candidate transfer beyond the original six-species analytical core.

# Figure 5. Known-module benchmark recovery by prioritized UGO-Omics candidates

Recovery of curated benchmark modules related to underground-organ development, storage-organ biology, hormone regulation, cell-wall remodeling, bud/regrowth processes, and stress resilience. Bars indicate the number of prioritized candidate orthogroups linked to each benchmark module. Dark green indicates direct module recovery, light green indicates broader module-level recovery, and grey indicates benchmark modules not recovered by the prioritized candidate set. The analysis is interpreted conservatively at the gene-family or pathway-module level rather than as evidence that individual candidate genes have been functionally validated. Prioritized UGO-Omics candidates recovered 11 of 15 curated benchmark modules, including cell-wall remodeling, meristem/regrowth, hormone regulation, developmental transition, bud branching, NAC-related developmental/stress regulation, and hypoxia/stress resilience modules.

# Figure 6. UGO-Omics website interface and browsable data layers

Static website interface for UGO-Omics. The website includes browsable layers for species resources, prioritized candidates, orthogroups, candidate expansion, benchmark recovery, and downloads. The Species Browser summarizes the 51-species broad underground-organ resource layer. The Candidate Expansion page links prioritized candidate orthogroups to the 9-species expanded backbone. The Benchmark Recovery page displays curated known-module recovery results. The interface is implemented as a static HTML/JavaScript site powered by compact JSON files.

# Supplementary Figure S1. Conservative benchmark recovery of UGO-Omics underground-organ modules

Conservative benchmark recovery among lotus- and ginger-supported orthogroups. Panels summarize the number of lotus/ginger-supported orthogroups assigned to each benchmark module, the number of high-confidence lotus and ginger rhizome-associated genes represented in each benchmark module, and benchmark module assignments for prioritized UGO candidate orthogroups. This conservative benchmark confirms that prioritized candidates recover expected underground-organ-associated modules, including cell-wall remodeling, developmental transcriptional regulation, meristem/regrowth, stress resilience, and hormone regulation. The large poorly annotated class represents orthogroups with weak annotation, lineage-specific patterns, or potentially novel underground-organ associations.

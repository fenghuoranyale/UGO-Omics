# UGO-Omics reveals a recurrent regeneration–resilience toolkit across underground-organ systems

# Abstract

Underground organs such as rhizomes, tubers, storage roots, corms, and related structures enable perennial persistence, vegetative propagation, resource storage, stress survival, and post-disturbance regrowth across plant lineages. Despite their biological and agricultural importance, underground-organ research remains fragmented across species, organ types, and omics resources, limiting cross-system comparison and candidate discovery. Here, we present UGO-Omics, a cross-species, evolution-informed discovery platform for underground-organ biology. UGO-Omics integrates a 51-species underground-organ atlas, an 11-species high-confidence analytical backbone, orthogroup-based candidate transfer, researcher-facing query workflows, and an independent BUSCO-based phylogenetic framework. By mapping candidate modules onto this framework, UGO-Omics identifies recurrent module-level signals associated with meristem/regrowth, stress resilience, hormone-related developmental switching, developmental transcriptional regulation, and cell-wall remodeling. A known-category recovery benchmark supports the credibility of the module-prioritization framework, recovering expected biological categories linked to underground-organ development and persistence. Integrating phylogenetic dispersion, benchmark recovery, recurrence strength, and species-level support reveals a candidate regeneration–resilience core toolkit recurring across phylogenetically divergent underground-organ systems. We propose that morphologically distinct underground organs may repeatedly recruit conserved developmental, survival, regulatory, and structural-remodeling modules through module-level convergence and regulatory redeployment. UGO-Omics provides a reusable platform and evolutionary framework for prioritizing candidate genes and modules underlying underground-organ diversification, persistence, and regeneration.

# Significance

Underground organs are central to plant survival, regeneration, vegetative propagation, and crop productivity, but their study has lacked a unified cross-species omics framework. UGO-Omics addresses this gap by integrating a broad 51-species atlas, an 11-species high-confidence analytical backbone, phylogenetic context, researcher-facing query tools, benchmark recovery, and biological discovery modules. The platform suggests that diverse underground organs may repeatedly recruit a conserved regeneration–resilience toolkit, providing a new framework for studying underground-organ evolution and function.

# Introduction

Underground organs are central to the persistence and productivity of many plant lineages [REF_UNDERGROUND_IMPORTANCE_01; REF_BUD_BANK_REGENERATION_01]. Rhizomes, tubers, storage roots, corms, bulbs, root crowns, and related structures allow plants to survive unfavorable seasons, store resources, propagate vegetatively, and regenerate after disturbance [REF_RHIZOME_REVIEW_01; REF_STORAGE_ORGANS_01]. These traits are especially relevant to perenniality, stress tolerance, post-fire or post-grazing recovery, and yield-related storage organs in crops. Yet, compared with aboveground developmental systems, underground organs remain poorly integrated across species and organ types.

A central difficulty is that underground organs are morphologically and developmentally diverse [REF_ORGAN_NON_EQUIVALENCE_01]. Rhizomes are typically stem-derived, storage roots are root-derived, tubers can arise from stem or root contexts, and corm-like or crown-like structures may involve additional shoot-axis or transition-zone programs. This diversity makes it difficult to treat underground organs as a single homologous structure. At the same time, these organs share recurring functional demands: they must maintain or reactivate growth potential, survive stress, switch developmental states, remodel tissues, and coordinate storage or regrowth. These shared demands suggest that underground-organ evolution may be better studied at the level of conserved functional modules than at the level of organ morphology alone [REF_DEEP_HOMOLOGY_01; REF_CONVERGENCE_01; REF_REGULATORY_REDEPLOYMENT_01].

Recent advances in comparative genomics, transcriptomics, and orthogroup-based analysis create an opportunity to build a broader framework for underground-organ biology [REF_COMPARATIVE_GENOMICS_01; REF_ORTHOFINDER_01]. However, available data remain scattered across species-specific studies, crop-focused resources, and organ-specific datasets. Researchers often lack a practical way to move from a candidate sequence, gene list, species, or organ question to a cross-species underground-organ context. This gap limits both resource reuse and the discovery of candidate modules that may be recurrently associated with underground-organ diversification.

Here, we present UGO-Omics, a cross-species, evolution-informed discovery platform for underground-organ biology. UGO-Omics combines a broad 51-species underground-organ atlas with an 11-species high-confidence analytical backbone, orthogroup-based candidate transfer, researcher-facing query workflows, and an independent BUSCO-based phylogenetic framework. Rather than presenting underground organs as a single equivalent organ class, UGO-Omics uses a tiered design to separate atlas breadth, analytical depth, and evolutionary interpretation.

Using this framework, we identify recurrent candidate modules associated with meristem/regrowth, stress resilience, hormone-related developmental switching, developmental transcriptional regulation, and cell-wall remodeling. We further integrate module recurrence, phylogenetic dispersion, known-category benchmark recovery, and species-level support into a high-priority biological discovery case. These analyses support a hypothesis in which morphologically distinct underground organs repeatedly recruit a conserved regeneration–resilience toolkit through module-level convergence and regulatory redeployment. UGO-Omics therefore provides both a reusable community resource and a conceptual framework for studying underground-organ evolution, function, and candidate gene prioritization.

# Results

UGO-Omics was developed to transform fragmented underground-organ datasets into a comparative, evolution-informed discovery framework. We organized the platform around three connected goals: first, to assemble a broad underground-organ atlas spanning diverse species and organ systems; second, to define a high-confidence analytical backbone for orthogroup-based candidate transfer and module-level comparison; and third, to provide a practical interface through which researchers can query sequences, gene lists, species resources, and organ-focused datasets. The resulting framework links data integration, phylogenetic context, benchmark recovery, and biological discovery into a unified platform for underground-organ research.


## Construction of UGO-Omics as a cross-species underground-organ platform

UGO-Omics integrates underground-organ resources across species, organs, candidate modules, orthogroups, and user-facing workflows (Figure 1). The platform was designed to address a central limitation in underground-organ biology: relevant datasets exist across many systems, but they are difficult to compare because they differ in species, organ identity, data type, and annotation depth. To overcome this limitation, UGO-Omics uses a tiered architecture that separates broad resource coverage from high-confidence comparative analysis.

The broad layer consists of a 51-species underground-organ atlas, which captures taxonomic and organ-level diversity across rhizomes, tubers, storage roots, corm-like structures, root/hypocotyl storage systems, and related underground organs. This layer provides atlas breadth and resource discoverability. In contrast, the 11-species analytical backbone was selected to support orthogroup-based transfer, candidate-module analysis, phylogenetic interpretation, and user-facing discovery workflows. This separation allows UGO-Omics to retain broad biological scope while focusing detailed comparative inference on a curated high-confidence subset.

The platform architecture connects omics resources, orthogroup mapping, module scoring, benchmark recovery, and candidate prioritization (Figure 1D). Thus, UGO-Omics is not organized as a static collection of files, but as a structured discovery framework for moving from underground-organ datasets to candidate modules and testable biological hypotheses.


## A high-confidence 11-species backbone provides evolutionary context for candidate-module analysis

To place the high-confidence backbone into an evolutionary framework, we reconstructed an independent BUSCO-based phylogenetic context for the 11 species (Figure 2). Because strict single-copy overlap across all 11 species was limited by duplicated BUSCO recovery in several proteomes, we used a relaxed 9-of-11 BUSCO matrix as the main phylogenetic dataset. This matrix included 531 BUSCO loci and 279,498 amino-acid sites, with missing species for individual loci coded as gaps. A stricter 10-of-11 BUSCO matrix was retained as a sensitivity analysis.

The BUSCO tree provides an independent phylogenetic scaffold for interpreting species-level candidate-module recurrence across the 11-species backbone (Figure 2B). Importantly, this tree is used as an evolutionary context rather than as a definitive reconstruction of underground-organ origins. This distinction is central to the UGO-Omics framework, because the underground organs included in the atlas are morphologically and developmentally diverse. The phylogeny therefore supports module-level comparison across divergent species without requiring assumptions of strict organ-level homology.

We next overlaid candidate-module occurrence onto this phylogenetic context. The resulting framework links the 51-species atlas, the 11-species backbone, the BUSCO species tree, and the candidate module matrix into a single evolution-informed view (Figure 2). This integrated structure provides the basis for asking whether underground-organ systems share recurrent functional modules across phylogenetically divergent species.


## Researcher-facing workflows enable sequence-, gene-list-, species-, and organ-based discovery

UGO-Omics was designed for practical reuse by researchers who may enter the platform with different types of questions. The interface therefore includes four primary entry points: Sequence-to-UGO, Gene-list-to-UGO, Resource Finder, and Organ Kits (Figure 3). These workflows allow users to begin with a protein sequence, a candidate gene list, a species or dataset query, or an underground-organ category.

Sequence-to-UGO connects a protein FASTA query to UGO orthogroups and candidate module context. Gene-list-to-UGO maps user-provided gene sets to orthogroup and module summaries, allowing candidate lists from independent studies to be interpreted in an underground-organ framework. Resource Finder supports species-level resource discovery, while Organ Kits group resources and examples around organ categories such as rhizomes, tubers, storage roots, and related systems. Demo Results and Use Cases provide reviewer- and user-facing examples of expected inputs and outputs.

Together, these workflows make UGO-Omics a reusable discovery platform rather than a passive data viewer. They allow users to move from common research inputs to cross-species candidate context, recurrence signals, downloadable resources, and testable hypotheses (Figure 3D).

## Conserved candidate modules recur across phylogenetically divergent underground-organ systems

We next asked whether the UGO backbone contained recurrent candidate-module signals across phylogenetically divergent species. Candidate modules were mapped onto the BUSCO phylogenetic context and summarized as species-level module occurrence across the 11-species backbone (Figure 2C). This analysis focused on module-level recurrence rather than on direct organ-level homology, because the underground organs represented in UGO-Omics arise from diverse developmental contexts.

Five prioritized modules were retained for the main evolutionary framework: meristem/regrowth, stress resilience, hormone-related regulation, developmental transcriptional regulation, and cell-wall remodeling. Four of these modules—meristem/regrowth, stress resilience, hormone-related regulation, and developmental transcriptional regulation—were detected across all 11 backbone species and spanned both monocot and eudicot representatives. The cell-wall remodeling module showed a more restricted distribution but was also detected across both major clades.

These patterns suggest that underground-organ systems may share recurrent module-level features despite differences in organ morphology and developmental origin. The broad recurrence of regeneration-, stress-, hormone-, and regulatory-associated modules provides a candidate molecular basis for comparing underground organs across species. In contrast, the more restricted distribution of the cell-wall remodeling module suggests that structural remodeling may represent a supporting or context-dependent component rather than a universal core module.


## UGO-Omics supports a regeneration–resilience toolkit model

To interpret the recurrent module signals, we developed a regeneration–resilience toolkit model for underground-organ diversification (Figure 4). This model begins from the observation that underground organs are not necessarily equivalent structures. Rhizomes, tubers, storage roots, corm-like stems, and root/hypocotyl storage structures can arise from different organ contexts. Therefore, repeated underground-organ evolution should not be assumed to reflect repeated evolution of the same organ.

Instead, UGO-Omics supports a module-level model in which distinct underground organs may repeatedly recruit conserved functional programs. In this framework, meristem/regrowth modules contribute to growth reactivation and regenerative potential [REF_PLANT_REGENERATION_01]; stress-resilience modules support persistence under unfavorable conditions [REF_STRESS_RESILIENCE_01]; hormone-related modules mediate developmental-state switching [REF_HORMONE_DORMANCY_01]; developmental transcription-factor modules provide regulatory control; and cell-wall remodeling modules contribute to tissue expansion and structural reorganization [REF_CELL_WALL_REMODELING_01].

This interpretation reframes underground-organ convergence as a problem of module-level deep homology and regulatory redeployment. The same broad functional toolkit may be activated in different anatomical contexts, producing distinct underground organs with partially shared developmental and physiological capacities. Thus, UGO-Omics provides a hypothesis-generating model for how underground organs may diversify without requiring strict organ-level homology.


## Known-category recovery benchmark supports module-level candidate prioritization

A key question for any discovery platform is whether its prioritization logic recovers expected biological signals. To evaluate this, we constructed a known-category recovery benchmark representing processes expected to be relevant to underground-organ development and persistence (Figure 5A,B). The benchmark included categories related to meristem/bud regrowth, hormone-mediated developmental-state switching, stress survival, transcriptional network control, structural remodeling, storage metabolism, and organ identity or patterning.

The current five-module mechanism layer recovered nine of ten benchmark items overall and all nine current-scope benchmark items. Recovered categories included meristem/bud regrowth, hormone-mediated developmental-state switching, stress survival, transcriptional network control, structural remodeling, and organ identity or patterning. The only non-recovered benchmark category was storage metabolism, which was intentionally retained as a future expansion target because storage-metabolism modules are not yet represented as a primary component of the current five-module model.

This benchmark supports the credibility of UGO-Omics at the category/module level. It shows that the current prioritization framework recovers expected biological processes while also identifying a clear direction for future expansion. Importantly, this benchmark is not interpreted as functional validation of individual genes; rather, it evaluates whether the platform captures biologically plausible module categories relevant to underground-organ systems.


## A high-impact discovery case identifies a recurrent regeneration–resilience core toolkit

Finally, we integrated module recurrence, phylogenetic dispersion, benchmark recovery, and species-level support into a high-impact biological discovery case (Figure 5C,D). Each prioritized module was evaluated using an integrated discovery score that combined recurrence strength, monocot/eudicot dispersion, benchmark support, and species breadth. This synthesis identified four core discovery modules: meristem/regrowth, stress resilience, hormone-related regulation, and developmental transcriptional regulation.

Each core module was detected across all 11 backbone species, spanned monocot and eudicot representatives, and recovered expected benchmark categories. Together, these modules define a candidate regeneration–resilience core toolkit. The cell-wall remodeling module formed a supporting structural component, with a more restricted but cross-lineage distribution.

This discovery case provides the central biological output of UGO-Omics. It suggests that diverse underground-organ systems may repeatedly recruit a conserved core toolkit linking regenerative growth, stress survival, developmental-state switching, and regulatory control. Cell-wall remodeling may then contribute structural remodeling capacity in a subset of contexts. The resulting model generates a prioritized set of candidate modules for future functional, developmental, and evolutionary testing.


## UGO-Omics links platform utility with evolutionary hypothesis generation

Together, the UGO-Omics framework links resource integration, phylogenetic context, user-facing workflows, benchmark recovery, and biological discovery. Figure 1 defines the platform architecture, Figure 2 places the analytical backbone into evolutionary context, Figure 3 demonstrates usability, Figure 4 presents the regeneration–resilience toolkit model, and Figure 5 supports the model through benchmark recovery and integrated discovery scoring.

This combined structure is important because underground-organ biology requires both practical resources and conceptual synthesis. A platform that only collects datasets would not explain how underground organs can be compared across divergent species and organ contexts. Conversely, a conceptual model without reusable tools would have limited community value. UGO-Omics addresses both needs by providing a reusable discovery platform and a candidate evolutionary framework for underground-organ diversification.

# Discussion

UGO-Omics addresses a long-standing gap in underground-organ biology: the lack of a unified cross-species framework for comparing diverse underground organs and prioritizing candidate modules. Underground organs are central to plant persistence, vegetative propagation, storage, stress survival, and post-disturbance regrowth, but available data are often scattered across species-specific or organ-specific studies. By integrating a 51-species atlas, an 11-species high-confidence analytical backbone, an independent BUSCO-based phylogenetic context, researcher-facing workflows, benchmark recovery, and a biological discovery case, UGO-Omics provides both a reusable resource and an evolution-informed discovery framework.

A major conceptual contribution of UGO-Omics is the regeneration–resilience toolkit model. Diverse underground organs should not be treated as a single homologous structure: rhizomes, tubers, storage roots, corm-like stems, and root/hypocotyl storage systems can arise from different developmental contexts. However, these structures share functional demands for persistence, regrowth, developmental switching, and tissue remodeling. UGO-Omics suggests that these shared demands may be met through recurrent recruitment of conserved functional modules. This shifts the comparative question from whether underground organs are strictly homologous to whether they repeatedly deploy similar module-level programs [REF_DEEP_HOMOLOGY_01; REF_CONVERGENCE_01; REF_REGULATORY_REDEPLOYMENT_01].

The recurrent modules identified here are biologically coherent. Meristem/regrowth modules are consistent with the need to maintain or reactivate growth potential; stress-resilience modules align with survival under unfavorable conditions; hormone-related modules provide a plausible route for developmental-state transitions; developmental transcription-factor modules offer regulatory control points; and cell-wall remodeling modules support tissue expansion and structural remodeling. The integration of these modules into a regeneration–resilience toolkit provides a candidate mechanism for comparing underground-organ systems across divergent species.

The known-category recovery benchmark provides an important credibility check. The current module layer recovered all current-scope benchmark categories and nine of ten benchmark items overall, while identifying storage metabolism as a clear future expansion target. This result supports the biological plausibility of the module-prioritization framework. At the same time, the benchmark remains category-level and should not be interpreted as experimental validation of individual genes. Functional testing will be required to determine the roles of specific candidates and to assess whether the same modules are deployed through similar or distinct regulatory mechanisms in different lineages.

UGO-Omics also has practical value as a research platform. The Sequence-to-UGO and Gene-list-to-UGO workflows allow users to connect their own sequences or candidate gene lists to UGO orthogroups and module context. Resource Finder and Organ Kits support species- and organ-centered exploration. These workflows make the platform useful for researchers working on non-model systems, crop storage organs, perennial regrowth, or underground-organ evolution.

Several limitations should guide interpretation and future development. First, module recurrence is inferred from available omics and orthogroup resources and should be treated as hypothesis-generating. Second, the BUSCO phylogeny provides evolutionary context for the 11-species backbone but does not reconstruct the definitive origin of underground organs. Third, underground-organ categories are used as species-associated annotations rather than as formal evidence of organ-level recurrence. Fourth, public data quality and completeness vary across species, which can influence module detection. Finally, storage metabolism, QTL/GWAS evidence, single-cell/spatial datasets, and experimental validation should be expanded in future versions.

Despite these limitations, UGO-Omics provides a foundation for comparative underground-organ biology. It converts fragmented datasets into a structured platform, links user inputs to cross-species candidate context, and proposes a testable regeneration–resilience toolkit model. This framework should facilitate future studies of perenniality, vegetative propagation, storage-organ evolution, stress survival, and post-disturbance regeneration across plant lineages.

# Methods

## Construction of the UGO-Omics species atlas and analytical backbone

UGO-Omics was organized as a tiered framework for underground-organ biology. A broad 51-species atlas was used to capture species and organ diversity across rhizomes, tubers, storage roots, corm-like stems, root/hypocotyl storage systems, and related underground organs. An 11-species high-confidence analytical backbone was selected for deeper comparative analyses, including orthogroup-based candidate transfer, candidate-module distribution, phylogenetic interpretation, and user-facing discovery workflows. This tiered structure was designed to separate atlas breadth from analytical depth.

## Orthogroup-based candidate transfer and module organization

UGO-Omics connects species-level resources through orthogroup-based mapping [REF_ORTHOFINDER_01; REF_COMPARATIVE_GENOMICS_01]. Candidate genes and modules were organized into interpretable categories associated with meristem/regrowth, stress resilience, hormone-related regulation, developmental transcriptional regulation, and cell-wall remodeling. These modules were used as the primary framework for cross-species candidate comparison and hypothesis generation.

## BUSCO-based phylogenetic context

A BUSCO-based species tree was reconstructed for the 11-species analytical backbone using protein sequences and the embryophyta_odb10 lineage dataset [REF_BUSCO_01; REF_MAFFT_01; REF_TRIMAL_01; REF_IQTREE_01; REF_MODELFINDER_01; REF_UFBOOT_01]. Because strict single-copy recovery across all 11 species was limited by duplicated BUSCO recovery in several proteomes, the main matrix used BUSCO loci recovered as single copy in at least 9 of the 11 species. Missing species for individual loci were coded as gaps. The main matrix contained 531 BUSCO loci and 279,498 amino-acid sites. A stricter 10-of-11 BUSCO matrix was retained as a sensitivity analysis. The resulting tree was used as a phylogenetic context for interpreting module recurrence, not as a definitive reconstruction of underground-organ origins.

## Module phylogenetic distribution

Candidate modules were mapped onto the 11-species BUSCO phylogenetic context and summarized as species-level module occurrence. Underground-organ categories were treated as species-associated annotations. Module recurrence was interpreted at the candidate-module level rather than as evidence for strict organ-level homology.

## Evolutionary mechanism layer

Each prioritized module was assigned to a mechanistic component of the regeneration–resilience toolkit: regeneration capacity, stress survival, developmental-state switching, regulatory network control, or structural remodeling. A module recurrence index summarized species breadth, monocot/eudicot dispersion, and diversity of species-associated underground-organ contexts. These scores were used to support a hypothesis-generating model of recurrent modular reactivation.

## Known-category recovery benchmark

A known-category benchmark panel was constructed to evaluate whether UGO-Omics recovered expected biological categories related to underground-organ development and persistence. Benchmark categories included meristem/bud regrowth, hormone-mediated developmental-state switching, stress survival, transcriptional network control, structural remodeling, storage metabolism, and organ identity or patterning. Recovery was assessed at the category/module level and was not interpreted as functional validation of individual genes.

## High-impact biological discovery case

The high-impact discovery case integrated module recurrence, phylogenetic dispersion, benchmark recovery, and species-level support. Modules with the strongest combined evidence were classified as core discovery modules. This analysis was used to prioritize a candidate regeneration–resilience core toolkit for future functional and evolutionary testing.

## Web interface and user-facing workflows

UGO-Omics includes researcher-facing workflows designed for common entry points: protein sequence queries, candidate gene lists, species or resource searches, and underground-organ category questions. Sequence-to-UGO, Gene-list-to-UGO, Resource Finder, Organ Kits, Demo Results, and Use Cases were implemented to make the platform usable as a discovery resource rather than as a static data viewer [REF_DIAMOND_01].


# Data and resource availability

The UGO-Omics web interface, figure source tables, JSON metadata files, manuscript support files, example inputs, example outputs, and researcher-facing toolkits are provided through the public repository and final release package [REF_UGO_REPOSITORY_01]. Large sequence databases and external raw data should be distributed separately when needed to avoid repository size limitations [REF_DATA_SOURCES_01]. A permanent Zenodo archive and DOI should be generated immediately before submission, after the final manuscript and repository version are locked.


# Limitations

UGO-Omics is a hypothesis-generating discovery platform. The current version prioritizes candidate modules and evolutionary hypotheses but does not experimentally validate individual gene function. The BUSCO tree provides phylogenetic context for the 11-species analytical backbone but does not reconstruct definitive underground-organ origins. Underground-organ categories are treated as species-associated annotations rather than as formal evidence of organ-level recurrence. Public data quality and completeness vary among species, which can influence module detection. Future versions should expand storage-metabolism modules, strengthen organ-level evidence curation, incorporate QTL/GWAS and single-cell or spatial data, and experimentally test high-priority candidate modules.


# Figure captions

## Figure 1. UGO-Omics platform architecture and underground-organ atlas


UGO-Omics platform architecture and underground-organ atlas. (A) Biological scope of UGO-Omics, covering diverse underground organs that contribute to persistence, regeneration, vegetative propagation, storage, and developmental-state transitions. (B) Tiered data architecture linking a broad 51-species underground-organ atlas, an 11-species high-confidence analytical backbone, an independent BUSCO phylogenetic context, and a regeneration–resilience toolkit model. (C) Researcher-facing discovery tools, including Sequence-to-UGO, Gene-list-to-UGO, Resource Finder, Organ Kits, Demo Results, and Use Cases. (D) UGO-Omics discovery logic, from omics resources and orthogroup mapping to module scoring, benchmark recovery, and biological discovery cases. The platform is designed for candidate prioritization and hypothesis generation.

## Figure 2. Integrated evolutionary framework of UGO-Omics


Integrated evolutionary framework of UGO-Omics. (A) Tiered design linking a broad 51-species underground-organ atlas to an 11-species high-confidence analytical backbone and an evolution-informed discovery layer. (B) BUSCO-based phylogenetic context for the 11-species backbone, reconstructed from the main 9-of-11 BUSCO matrix containing 531 loci and 279,498 amino-acid sites. (C) Species-level distribution of five conserved UGO candidate modules across the BUSCO backbone. Filled circles indicate species-level candidate-module support. Underground-organ categories are shown as species-associated annotations. The figure provides phylogenetic context for candidate module recurrence and is not intended as a definitive reconstruction of underground-organ origins.

## Figure 3. Researcher-facing UGO discovery workflows


Researcher-facing UGO discovery workflows. (A) UGO-Omics supports multiple user entry points, including protein sequence queries, candidate gene lists, species or dataset searches, and underground-organ questions. (B) Sequence-to-UGO and Gene-list-to-UGO convert common molecular inputs into UGO orthogroup, candidate module, and recurrence-context outputs. (C) Resource Finder and Organ Kits allow users to start from species resources or underground-organ categories, including rhizomes, tubers, storage roots, and related systems. (D) These workflows make UGO-Omics a reusable discovery platform by linking user inputs to cross-species mapping, candidate module interpretation, and testable hypotheses.

## Figure 4. Regeneration–resilience toolkit model


Regeneration–resilience toolkit model for underground-organ diversification. (A) Underground organs such as rhizomes, tubers, storage roots, corm-like stems, and root/hypocotyl storage structures can arise from distinct developmental contexts and should not be treated as a single homologous organ. (B) UGO-Omics identifies candidate modules associated with meristem/regrowth, stress survival, hormone-related developmental switching, regulatory control, and cell-wall remodeling. (C) We propose a recurrent modular reactivation model in which morphologically distinct underground organs repeatedly recruit conserved functional modules through module-level convergence and regulatory redeployment. This model is hypothesis-generating and does not imply definitive reconstruction of underground-organ origins or functional validation of individual genes.

## Figure 5. Known-category recovery and high-impact biological discovery case


Known-category recovery and high-impact biological discovery case. (A) Recovery of benchmark categories representing biological processes expected to contribute to underground-organ development, persistence, regeneration, and structural remodeling. (B) Integrated discovery scores for prioritized UGO candidate modules based on module recurrence, phylogenetic dispersion, benchmark support, and species breadth. (C) Species-level support for the recurrent regeneration–resilience core toolkit across the 11-species backbone. (D) Synthesis of benchmark recovery and phylogenetic recurrence identifies a high-priority regeneration–resilience core toolkit, with cell-wall remodeling as a supporting structural component. This analysis supports candidate prioritization and future testing, rather than functional validation of individual genes.

# Supplementary table list

Table S1. Tiered 51-species atlas and 11-species backbone selection logic. Source file: UGO_v2_3_0_species_design_table_v1.tsv. Linked main figure: Figure 1; Figure 2.

Table S2. Species-level candidate module distribution used in Figure 2. Source file: Figure2_v2_module_species_distribution.tsv. Linked main figure: Figure 2.

Table S3. Main 9-of-11 BUSCO phylogenetic tree used in Figure 2. Source file: Figure2_v2_main_9of11_BUSCO_species_tree.nwk. Linked main figure: Figure 2.

Table S4. Summary of researcher-facing UGO workflows. Source file: Figure3_usability_workflow_summary.tsv. Linked main figure: Figure 3.

Table S5. Regeneration–resilience toolkit module index used in Figure 4. Source file: Figure4_toolkit_module_index.tsv. Linked main figure: Figure 4.

Table S6. Module-level discovery evidence used in Figure 4. Source file: Figure4_discovery_case_module_evidence.tsv. Linked main figure: Figure 4.

Table S7. Known-category benchmark panel used in Figure 5. Source file: Figure5_known_category_benchmark_panel.tsv. Linked main figure: Figure 5.

Table S8. Overall benchmark recovery metrics used in Figure 5. Source file: Figure5_benchmark_overall_recovery_metrics.tsv. Linked main figure: Figure 5.

Table S9. Integrated discovery case module evidence used in Figure 5. Source file: Figure5_high_impact_discovery_case_module_evidence.tsv. Linked main figure: Figure 5.

Table S10. Species-level support for the regeneration–resilience core toolkit. Source file: Figure5_discovery_case_species_support.tsv. Linked main figure: Figure 5.




# Citation status note

Bracketed citation markers such as [REF_BUSCO_01] are structured placeholders. They should be replaced with journal-formatted references after final verification of bibliographic details, DOI information, dataset accessions, and Zenodo deposition.


# Reference placeholder list

REF_RHIZOME_REVIEW_01. Chen, H. and Coughlan, J.M. The genetic and developmental enigma of rhizomes: crucial traits with limited understanding. Theoretical and Applied Genetics. Final volume/pages/DOI to be inserted. Action: Insert final DOI and exact bibliographic details.

REF_DEEP_HOMOLOGY_01. Shubin, N., Tabin, C., and Carroll, S. Deep homology and the origins of evolutionary novelty. Nature. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_ORTHOFINDER_01. Emms, D.M. and Kelly, S. OrthoFinder: phylogenetic orthology inference for comparative genomics. Genome Biology. Exact details to be verified. Action: Verify year, volume, article number, DOI.

REF_BUSCO_01. Manni, M. et al. BUSCO update: novel and streamlined workflows along with broader and deeper phylogenetic coverage. Molecular Biology and Evolution. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_IQTREE_01. Minh, B.Q. et al. IQ-TREE 2: new models and efficient methods for phylogenetic inference in the genomic era. Molecular Biology and Evolution. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_MODELFINDER_01. Kalyaanamoorthy, S. et al. ModelFinder: fast model selection for accurate phylogenetic estimates. Nature Methods. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_UFBOOT_01. Hoang, D.T. et al. UFBoot2: improving the ultrafast bootstrap approximation. Molecular Biology and Evolution. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_MAFFT_01. Katoh, K. and Standley, D.M. MAFFT multiple sequence alignment software version 7: improvements in performance and usability. Molecular Biology and Evolution. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_TRIMAL_01. Capella-Gutierrez, S., Silla-Martinez, J.M., and Gabaldon, T. trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses. Bioinformatics. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_DIAMOND_01. Buchfink, B., Reuter, K., and Drost, H.G. Sensitive protein alignments at tree-of-life scale using DIAMOND. Nature Methods. Exact details to be verified. Action: Verify year, volume, pages, DOI.

REF_UGO_REPOSITORY_01. UGO-Omics GitHub repository and Zenodo archive. DOI to be inserted after final Zenodo deposition. Action: Insert repository URL and Zenodo DOI before submission.


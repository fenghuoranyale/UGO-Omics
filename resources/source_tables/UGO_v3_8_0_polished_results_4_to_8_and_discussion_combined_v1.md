# UGO-Omics manuscript polished Results 4–8 and Discussion v3.8.0

## Conserved candidate modules recur across phylogenetically divergent underground-organ systems

We next asked whether the UGO backbone contained recurrent candidate-module signals across phylogenetically divergent species. Candidate modules were mapped onto the BUSCO phylogenetic context and summarized as species-level module occurrence across the 11-species backbone (Figure 2C). This analysis focused on module-level recurrence rather than on direct organ-level homology, because the underground organs represented in UGO-Omics arise from diverse developmental contexts.

Five prioritized modules were retained for the main evolutionary framework: meristem/regrowth, stress resilience, hormone-related regulation, developmental transcriptional regulation, and cell-wall remodeling. Four of these modules—meristem/regrowth, stress resilience, hormone-related regulation, and developmental transcriptional regulation—were detected across all 11 backbone species and spanned both monocot and eudicot representatives. The cell-wall remodeling module showed a more restricted distribution but was also detected across both major clades.

These patterns suggest that underground-organ systems may share recurrent module-level features despite differences in organ morphology and developmental origin. The broad recurrence of regeneration-, stress-, hormone-, and regulatory-associated modules provides a candidate molecular basis for comparing underground organs across species. In contrast, the more restricted distribution of the cell-wall remodeling module suggests that structural remodeling may represent a supporting or context-dependent component rather than a universal core module.


## UGO-Omics supports a regeneration–resilience toolkit model

To interpret the recurrent module signals, we developed a regeneration–resilience toolkit model for underground-organ diversification (Figure 4). This model begins from the observation that underground organs are not necessarily equivalent structures. Rhizomes, tubers, storage roots, corm-like stems, and root/hypocotyl storage structures can arise from different organ contexts. Therefore, repeated underground-organ evolution should not be assumed to reflect repeated evolution of the same organ.

Instead, UGO-Omics supports a module-level model in which distinct underground organs may repeatedly recruit conserved functional programs. In this framework, meristem/regrowth modules contribute to growth reactivation and regenerative potential; stress-resilience modules support persistence under unfavorable conditions; hormone-related modules mediate developmental-state switching; developmental transcription-factor modules provide regulatory control; and cell-wall remodeling modules contribute to tissue expansion and structural reorganization.

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


# Polished Discussion

UGO-Omics addresses a long-standing gap in underground-organ biology: the lack of a unified cross-species framework for comparing diverse underground organs and prioritizing candidate modules. Underground organs are central to plant persistence, vegetative propagation, storage, stress survival, and post-disturbance regrowth, but available data are often scattered across species-specific or organ-specific studies. By integrating a 51-species atlas, an 11-species high-confidence analytical backbone, an independent BUSCO-based phylogenetic context, researcher-facing workflows, benchmark recovery, and a biological discovery case, UGO-Omics provides both a reusable resource and an evolution-informed discovery framework.

A major conceptual contribution of UGO-Omics is the regeneration–resilience toolkit model. Diverse underground organs should not be treated as a single homologous structure: rhizomes, tubers, storage roots, corm-like stems, and root/hypocotyl storage systems can arise from different developmental contexts. However, these structures share functional demands for persistence, regrowth, developmental switching, and tissue remodeling. UGO-Omics suggests that these shared demands may be met through recurrent recruitment of conserved functional modules. This shifts the comparative question from whether underground organs are strictly homologous to whether they repeatedly deploy similar module-level programs.

The recurrent modules identified here are biologically coherent. Meristem/regrowth modules are consistent with the need to maintain or reactivate growth potential; stress-resilience modules align with survival under unfavorable conditions; hormone-related modules provide a plausible route for developmental-state transitions; developmental transcription-factor modules offer regulatory control points; and cell-wall remodeling modules support tissue expansion and structural remodeling. The integration of these modules into a regeneration–resilience toolkit provides a candidate mechanism for comparing underground-organ systems across divergent species.

The known-category recovery benchmark provides an important credibility check. The current module layer recovered all current-scope benchmark categories and nine of ten benchmark items overall, while identifying storage metabolism as a clear future expansion target. This result supports the biological plausibility of the module-prioritization framework. At the same time, the benchmark remains category-level and should not be interpreted as experimental validation of individual genes. Functional testing will be required to determine the roles of specific candidates and to assess whether the same modules are deployed through similar or distinct regulatory mechanisms in different lineages.

UGO-Omics also has practical value as a research platform. The Sequence-to-UGO and Gene-list-to-UGO workflows allow users to connect their own sequences or candidate gene lists to UGO orthogroups and module context. Resource Finder and Organ Kits support species- and organ-centered exploration. These workflows make the platform useful for researchers working on non-model systems, crop storage organs, perennial regrowth, or underground-organ evolution.

Several limitations should guide interpretation and future development. First, module recurrence is inferred from available omics and orthogroup resources and should be treated as hypothesis-generating. Second, the BUSCO phylogeny provides evolutionary context for the 11-species backbone but does not reconstruct the definitive origin of underground organs. Third, underground-organ categories are used as species-associated annotations rather than as formal evidence of organ-level recurrence. Fourth, public data quality and completeness vary across species, which can influence module detection. Finally, storage metabolism, QTL/GWAS evidence, single-cell/spatial datasets, and experimental validation should be expanded in future versions.

Despite these limitations, UGO-Omics provides a foundation for comparative underground-organ biology. It converts fragmented datasets into a structured platform, links user inputs to cross-species candidate context, and proposes a testable regeneration–resilience toolkit model. This framework should facilitate future studies of perenniality, vegetative propagation, storage-organ evolution, stress survival, and post-disturbance regeneration across plant lineages.


mmMOI
=====

Summary
-------
mmMOI is an end-to-end multi-omics framework that combines single-omics
representation learning with multi-scale attention-based fusion for final
classification.

Model Type
----------
Graph and attention-based multi-omics integration model.

Execution in EMAI-COPD
----------------------
- Executed through dedicated omics workflows (not the unified tabular runner)
- Typically run in staged pipelines matching the model's two-phase design
- Results are logged under run-specific directories in results/

Input Requirements
------------------
- Structured multi-omics tabular matrices
- Pre-imputed and normalized inputs
- Label-ready splits for supervised evaluation

Interpretability
----------------
mmMOI has internal attention mechanisms but no native feature-importance export
workflow in the codebase. Additional attribution methods are generally required
for biomarker ranking.

Strengths
---------
- Captures both per-omics and cross-omics interactions
- Strong fusion design for heterogeneous omics views
- Suitable for end-to-end multi-omics classification benchmarks

Limitations
-----------
- Two-stage execution adds operational complexity
- Graph and attention quality depends on input preprocessing quality
- Limited built-in biomarker extraction support

Recommended Use in Tier 1
-------------------------
Use mmMOI when modeling cross-omics interactions is central and the team can
support a multi-step training workflow.

Citation
--------
- Li, Y., Wang, Y., Liang, T., Li, Y., and Du, W. (2025). A multi-omics
	integration framework using multi-label guided learning and multi-scale
	fusion. Briefings in Bioinformatics, 26(5), bbaf493.

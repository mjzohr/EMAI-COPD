MGDMCL
======

Summary
-------
MGDMCL is a supervised multi-omics graph framework that combines dynamic sample
graph learning and multi-granularity contrastive learning for biomedical
classification.

Model Type
----------
Graph neural network with masked graph reconstruction and contrastive learning.

Execution in EMAI-COPD
----------------------
- Executed through dedicated omics workflows (not the unified tabular runner)
- Typically launched from omics-specific scripts and tracked under results/
- Best used with curated train/validation/test splits in model-formatted folders

Input Requirements
------------------
- Structured multi-omics tabular inputs (for example: mRNA, miRNA, methylation)
- Complete matrices after preprocessing
- Class labels for supervised training and contrastive pair construction

Interpretability
----------------
MGDMCL includes internal gating scores, but the repository does not expose a
ready-to-use feature-importance export pipeline. Practical biomarker extraction
usually requires additional attribution tooling.

Strengths
---------
- Learns adaptive sample similarity structure
- Strong representation learning with contrastive objectives
- Competitive for multi-class and binary biomedical classification

Limitations
-----------
- Requires pre-imputation and clean complete inputs
- Higher training complexity and compute cost than simpler baselines
- Limited out-of-the-box interpretability export

Recommended Use in Tier 1
-------------------------
Use MGDMCL when classification performance is the priority and a heavier training
pipeline is acceptable.

Citation
--------
- Chen, W., and Qiu, H. (2025). MGDMCL: A multi-omics integration framework
	based on masked graph dynamic learning and multi-granularity feature
	contrastive learning for biomedical classification. Computer Methods and
	Programs in Biomedicine, 271, 109024.

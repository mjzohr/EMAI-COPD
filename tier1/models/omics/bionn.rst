BioNeuralNet
============

Summary
-------
BioNeuralNet is a modular graph-learning framework for multi-omics analysis. In
Tier 1, it is used to learn patient-level representations and support supervised
or unsupervised downstream tasks from structured omics inputs.

Model Type
----------
Graph neural network framework (for example: GCN, GAT, GraphSAGE, GIN) for
multi-omics representation learning and prediction.

Execution in EMAI-COPD
----------------------
- Executed through dedicated omics workflows (not the unified tabular runner)
- Typically orchestrated from project-level omics scripts (for example run_all.sh)
- Outputs are logged to run-specific folders under results/

Input Requirements
------------------
- Structured omics matrices (tabular format)
- Optional clinical covariates for downstream prediction
- Preprocessing before training: filtering, normalization, and imputation

Interpretability
----------------
BioNeuralNet supports strong network-level analysis (modules/hubs), but does not
provide an out-of-the-box ranked feature-importance export path comparable to the
MOGONET biomarker workflow.

Strengths
---------
- Flexible architecture and pipeline components
- Supports both predictive modeling and graph-centric biological analysis
- Useful for representation learning and clustering

Limitations
-----------
- Performance is sensitive to graph construction choices
- Requires careful preprocessing and feature selection at scale
- Native per-feature attribution workflow is limited

Recommended Use in Tier 1
-------------------------
Use BioNeuralNet when representation quality and network-level biological
structure are primary goals, especially before multimodal fusion in later tiers.

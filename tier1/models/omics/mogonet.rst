MOGONET
=======

Summary
-------
MOGONET is a multi-omics classification framework that trains omics-specific GCN
branches and fuses their predictions through a VCDN integration module.

Model Type
----------
Supervised graph convolutional architecture with late-fusion label-space
integration (VCDN).

Execution in EMAI-COPD
----------------------
- Executed through dedicated omics workflows (not the unified tabular runner)
- Commonly orchestrated with project omics scripts and fold-based outputs
- Supports both classification runs and feature-importance analysis

Input Requirements
------------------
- Structured multi-omics tabular inputs (for example: mRNA, miRNA, methylation)
- Pre-imputed and filtered features
- Per-fold formatted directories for training and evaluation

Interpretability
----------------
MOGONET has the strongest built-in biomarker workflow among Tier 1 omics models.
Feature-importance analysis is typically run after model training.

Example feature analysis command:

.. code-block:: bash

   uv run python -m models.omics.MOGONET.copd_feat_importance \
     --data_folder data/copdgene/data_processed/omics/formatted_data/mogonet_cv5/fold_01 \
     --model_folder results/mogonet_cv/run_20260303_163135/fold_01/models \
     --out_dir results/mogonet_cv/run_20260303_163135/fold_01/featimp \
     --max_features 2000 \
     --topn 50

Strengths
---------
- Clear omics-specific branch design
- Native biomarker-oriented analysis workflow
- Strong baseline for multi-omics patient classification

Limitations
-----------
- VCDN complexity grows quickly with modality/class count
- Relies heavily on sample-graph quality
- Requires careful preprocessing and fold management

Recommended Use in Tier 1
-------------------------
Use MOGONET when both classification performance and practical feature analysis
are required in the same benchmark pipeline.

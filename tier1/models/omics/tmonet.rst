TMO-Net
=======

Summary
-------
TMO-Net is a pre-trained multi-omics model designed for oncology tasks, with
cross-modal fusion to support representation learning and missing-modality
handling.

Model Type
----------
Pre-trained multi-modal VAE and cross-fusion architecture for multi-task
prediction.

Execution in EMAI-COPD
----------------------
- Executed through dedicated omics workflows (not the unified tabular runner)
- Typically run as a specialized omics pipeline with model-specific inputs
- Outputs are tracked in run-specific directories under results/

Input Requirements
------------------
- Structured multi-omics tabular inputs
- Model-aligned preprocessing and splits
- Prefer GPU-enabled execution for practical runtimes

Interpretability
----------------
Although the paper discusses explainability, the repository does not provide a
native feature-importance export workflow. Additional attribution tooling is
required for ranked biomarker outputs.

Strengths
---------
- Designed for transfer and pretraining-style workflows
- Supports missing-modality scenarios better than strict complete-input models
- Useful for advanced oncology-focused representation tasks

Limitations
-----------
- Heavier training and operational complexity
- Pretraining-domain mismatch can affect transfer quality
- Limited out-of-the-box interpretability exports

Recommended Use in Tier 1
-------------------------
Use TMO-Net when pre-trained multi-omics representations and missing-modality
robustness are key project priorities.

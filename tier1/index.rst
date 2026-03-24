Tier 1: Unimodal
================

Summary
-------

Tier 1 provides unimodal baselines for COPD across complementary modalities:

- Multi-omics (for example: transcriptomics, proteomics, metabolomics)
- Clinical tabular features
- CT-derived structured features
- Wearable-derived structured features
- SDOH covariates

The goal is to produce robust subject-level and omics-level representations for
downstream biomedical tasks such as severity prediction, early AECOPD detection,
subtyping, and pathway-focused analysis.

Scope
-----

Tier 1 is intended to:

- Establish strong unimodal baselines per modality
- Enable reproducible local/server experiments with shared data formatting and runners
- Create a consistent baseline foundation for later multimodal tiers

Representation Levels
---------------------

- Subject-level: all modalities can be represented as per-subject feature matrices
- Omics-level: multi-omics models can learn modality-specific representations for
  downstream tasks

Execution Notes
---------------

Unified tabular benchmark runs are launched with:

.. code-block:: bash

   ./run_benchmark.sh <DATASET_VARIANT>

Example:

.. code-block:: bash

   ./run_benchmark.sh clinical_p2

Common variants include ``clinical_p2``, ``ct_clinical_p2``, and
``concat_omics_p2`` (dataset registry-managed).

Common overrides:

.. code-block:: bash

   KFOLDS=10 SEED=123 TARGET_COL=target ./run_benchmark.sh clinical_p2

Omics-specific models (for example MOGONET, MGDMCL, mmMOI, TMO-Net) are usually
executed through dedicated omics scripts (often via ``run_all.sh``) because they
use custom input formats.

Environment Notes
-----------------

- Linux/WSL is recommended
- Python 3.12+ is preferred
- GPU is optional for tabular baselines and recommended for omics models

Navigation
----------

.. toctree::
   :maxdepth: 2
   :caption: Explore the Project

   datasets/index
   models/index



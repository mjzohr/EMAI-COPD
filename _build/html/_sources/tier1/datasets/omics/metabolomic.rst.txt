Metabolomic Dataset (COPDGene P2)
=================================

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Metabolomic measurements capturing small-molecule profiles in COPDGene participants.

Dataset Sources
~~~~~~~~~~~~~~~
Cohort: COPDGene Phase 2

Uses
-----

Direct Use
~~~~~~~~~~
- Disease prediction
- Metabolic pathway analysis
- Multimodal integration

Dataset Structure
-----------------
- Samples: 5,980
- Features: 1,571 metabolites

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Batch correction
- Filtering metabolites with >20% missing values
- kNN imputation (k=10)
- Log2 transformation

Bias, Risks, and Limitations
----------------------------
- Imputation may introduce artifacts
- Missingness not completely random
- Sensitive to preprocessing choices

Recommendations
---------------
- Evaluate robustness to imputation
- Cross-check with proteomics and transcriptomics

Citation
--------
COPDGene Study
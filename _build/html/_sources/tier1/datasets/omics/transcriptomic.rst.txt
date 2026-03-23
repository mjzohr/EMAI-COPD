Transcriptomic Dataset (COPDGene P2)
====================================

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Gene expression profiles derived from RNA-seq data in COPDGene participants.

Dataset Sources
~~~~~~~~~~~~~~~
Cohort: COPDGene Phase 2

Uses
-----

Direct Use
~~~~~~~~~~
- Gene-level modeling
- Disease classification
- Feature selection and pathway analysis

Dataset Structure
-----------------
- Samples: 3,985
- Features: 4,511 genes

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- log2 CPM normalization
- Upper-quartile normalization
- Gene-length correction
- Batch correction
- Low-count filtering
- Low-variance filtering

Bias, Risks, and Limitations
---------------------------
- High dimensionality vs sample size
- Sensitive to normalization pipeline
- Potential batch artifacts

Recommendations
---------------
- Apply dimensionality reduction where needed
- Validate across folds carefully

Citation
--------
COPDGene Study
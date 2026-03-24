Proteomics Data
===============

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Proteomic measurements derived from COPDGene Phase 2 participants. This modality captures protein abundance levels and is used for biomarker discovery and disease prediction.

Curated by
~~~~~~~~~~
COPDGene Consortium

Dataset Sources
~~~~~~~~~~~~~~~
Cohort: COPDGene Phase 2

Uses
-----

Direct Use
~~~~~~~~~~
- COPD classification and severity prediction
- Biomarker discovery
- Integration with other omics modalities

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Raw signal-level proteomics analysis
- Temporal modeling (single snapshot per subject)

Dataset Structure
-----------------
- Samples: 5,670
- Features: 4,979 proteins
- Format: tabular matrix (samples × features)

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Batch correction applied
- Log2 transformation applied

Source Data Producers
~~~~~~~~~~~~~~~~~~~~~
Clinical cohort participants and laboratory proteomics pipelines.

Personal and Sensitive Information
---------------------------------
- De-identified clinical cohort data
- No direct identifiers included

Bias, Risks, and Limitations
---------------------------
- Batch effects may persist despite correction
- Missingness patterns may introduce bias
- Cohort-specific distribution (COPD-focused)

Recommendations
---------------
- Validate results across modalities
- Consider normalization across cohorts if extended

Citation
--------
COPDGene Study
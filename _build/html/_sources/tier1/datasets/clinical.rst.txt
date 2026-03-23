Clinical Dataset (COPDGene P2)
==============================

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Structured clinical and demographic features collected from COPDGene participants.

Dataset Structure
-----------------
- Samples: 4,935
- Features: 296

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Removal of GOLD-related features (to prevent leakage)
- Removal of uninformative variables
- Missing value handling (domain-specific)

Uses
-----

Direct Use
~~~~~~~~~~
- Baseline tabular prediction
- Integration with omics data

Bias, Risks, and Limitations
---------------------------
- Feature leakage risk if not filtered
- Missingness patterns vary by feature

Recommendations
---------------
- Careful feature selection required
- Avoid including label-derived features
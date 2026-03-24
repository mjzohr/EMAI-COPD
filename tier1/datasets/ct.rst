CT Data
=======

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Quantitative CT-derived features computed using Thirona platform.
Tier 1 currently treats CT as engineered/derived structured features for the
tabular pipeline rather than raw-image modeling.

Dataset Structure
-----------------
- Samples: 4,258
- Features: 85

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Platform-specific quantitative feature extraction (Thirona)

Uses
-----

Direct Use
~~~~~~~~~~
- Imaging-based COPD severity modeling
- Multimodal fusion with clinical and omics data

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Raw image modeling (this dataset contains derived features only)

Bias, Risks, and Limitations
---------------------------
- Dependent on extraction pipeline
- Limited feature dimensionality compared to omics

Recommendations
---------------
- Combine with other modalities for improved performance
- If a dedicated CT unimodal raw-image model is added later, document it as a
	separate Tier 1 CT track

Current Access Notes
--------------------
- Full raw CT imaging access may not always be available
- Existing pipelines can still be adopted via derived-feature/public-dataset
	compatible workflows
Wearable Data
=============

Dataset Details
---------------

Dataset Description
~~~~~~~~~~~~~~~~~~~
Wearable-derived features from devices such as Fitbit and Apple Watch.
Current Tier 1 wearable data reflects a small cohort with prior COPD
exacerbation history and combines sensor signals with daily symptom context.

Dataset Structure
-----------------
- Samples: 37
- Features: 7

Dataset Creation
----------------

Data Collection and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Temporal aggregation (daily-level features)
- Missing value handling
- Device streams (Fitbit/Apple Watch) and daily survey signals (EXACT) can be
	fused into structured features for unimodal baselines

Uses
-----

Direct Use
~~~~~~~~~~
- Behavioral and activity modeling
- Early-stage multimodal integration

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Large-scale modeling (limited sample size)

Bias, Risks, and Limitations
---------------------------
- Very small sample size
- High missingness
- Device-dependent variability

Recommendations
---------------
- Use in exploratory or Tier 2+ settings
- Combine with other modalities
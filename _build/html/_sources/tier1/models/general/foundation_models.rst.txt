Foundation Tabular Models (TabPFNv2.5)
=====================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
TabPFNv2.5 represents a foundation model approach for tabular data, leveraging in-context learning to perform prediction without traditional training.

Model Type
~~~~~~~~~~
Pretrained transformer-based foundation model for tabular data.

Uses
-----

Direct Use
~~~~~~~~~~
- Fast inference without training
- Few-shot learning for tabular tasks
- Strong baseline for small datasets

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Very large datasets requiring scalable training
- Tasks requiring full fine-tuning control

Bias, Risks, and Limitations
---------------------------
- Limited interpretability
- Performance tied to pretraining distribution
- Less flexible than trainable models

Training Details
----------------
- Pretrained on synthetic and real tabular tasks
- Uses in-context learning instead of gradient updates

Evaluation
----------
- Metrics: AUROC, accuracy, F1
- Strong performance on small-to-medium datasets

Technical Specifications
------------------------
- Transformer-based architecture
- In-context prediction paradigm

Citation
--------
Hollmann et al. (2023+). TabPFN.
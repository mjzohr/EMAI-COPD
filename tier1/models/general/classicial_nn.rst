Classical Neural Baselines (MLP, ResNet)
=======================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category includes classical neural network baselines adapted for tabular data:

- Multi-Layer Perceptron (MLP)
- Residual Networks (ResNet) adapted for tabular inputs

These models serve as foundational deep learning baselines for structured data and are commonly used for comparison against more specialized tabular architectures.

Developed by
~~~~~~~~~~~~
- MLP: Foundational neural network architecture
- ResNet: He et al. (2015), adapted for tabular learning

Model Type
~~~~~~~~~~
Supervised deep learning models for tabular classification/regression.

Uses
-----

Direct Use
~~~~~~~~~~
- Baseline deep learning models for tabular prediction
- Benchmark comparison against tree-based and transformer-based models

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Raw multimodal inputs (image/audio/text without preprocessing)
- Highly sparse or categorical-heavy datasets without encoding

Bias, Risks, and Limitations
---------------------------
- Weak inductive bias for tabular data
- Sensitive to feature scaling and preprocessing
- Often underperform tree-based models on small datasets

Training Details
----------------
- Requires normalized inputs
- Requires explicit handling of categorical features (encoding)
- Hyperparameter tuning is critical (depth, width, regularization)

Evaluation
----------
- Metrics: AUROC, macro-F1, accuracy
- Serves primarily as a lower-bound baseline

Technical Specifications
------------------------
- Fully connected layers
- Optional residual connections (ResNet)
- Objective: cross-entropy (classification)

Citation
--------
He et al. (2015). Deep Residual Learning for Image Recognition.
Modern Deep Tabular Architectures (RealMLP, Trompt, ExcelFormer)
================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category includes recent deep learning architectures for tabular data, many implemented in PyTorch Frame:

- RealMLP (2024)
- Trompt (2023)
- ExcelFormer (2024)

These models aim to close the performance gap between deep learning and tree-based methods through improved architecture design and training strategies.

Model Type
~~~~~~~~~~
Advanced neural architectures for tabular representation learning.

Uses
-----

Direct Use
~~~~~~~~~~
- Strong deep learning baselines for tabular data
- Benchmarking against tree ensembles and transformers
- Exploring feature interaction learning beyond classical methods

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Extremely small datasets
- Low-resource environments requiring fast training

Bias, Risks, and Limitations
---------------------------
- Still may not consistently outperform tree-based models
- Increased complexity compared to MLP
- Less mature ecosystem compared to XGBoost/LightGBM

Training Details
----------------
- Often require careful tuning
- Benefit from modern optimization techniques
- Designed to improve stability and generalization

Evaluation
----------
- Metrics: AUROC, macro-F1
- Compared against both classical and transformer baselines

Technical Specifications
------------------------

- RealMLP: optimized MLP architecture with improved training dynamics
- Trompt: attention-style interactions with prompt-inspired structure
- ExcelFormer: transformer variant specialized for tabular reasoning

Software
~~~~~~~~
Implemented via:
- PyTorch
- PyTorch Frame (https://github.com/pyg-team/pytorch-frame)

Citation
--------
Refer to individual model repositories and papers for details.
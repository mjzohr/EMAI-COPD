Attention-Based Tabular Models (TabTransformer, TabNet, FT-Transformer)
=======================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category includes early deep learning models specifically designed for tabular data using attention mechanisms and structured inductive biases:

- TabTransformer (2020)
- TabNet (2021)
- FT-Transformer (2021)

These models introduced mechanisms to better capture feature interactions and improve representation learning in tabular settings.

Model Type
~~~~~~~~~~
Transformer-based or attention-based tabular models.

Uses
-----

Direct Use
~~~~~~~~~~
- Modeling complex feature interactions in structured data
- Replacing tree-based models when deep representation learning is desired

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Extremely small datasets (may overfit)
- Tasks where tree ensembles dominate with minimal tuning

Bias, Risks, and Limitations
---------------------------
- Higher computational cost than tree-based models
- Sensitive to hyperparameters
- May not consistently outperform gradient boosting

Training Details
----------------
- Requires tokenization of features (especially FT-Transformer)
- TabTransformer focuses on categorical embeddings
- TabNet uses sequential attention for feature selection

Evaluation
----------
- Metrics: AUROC, macro-F1
- Compared against tree-based baselines

Technical Specifications
------------------------
- TabTransformer: self-attention over categorical embeddings
- TabNet: sparse sequential attention masks
- FT-Transformer: treats each feature as a token

Citation
--------
Huang et al. (2020). TabTransformer.

Arik & Pfister (2021). TabNet.

Gorishniy et al. (2021). FT-Transformer.
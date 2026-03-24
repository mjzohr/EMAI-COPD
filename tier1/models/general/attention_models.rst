Attention Models
================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category includes early deep learning models specifically designed for tabular data using attention mechanisms and structured inductive biases:

* **TabTransformer (2020)**
* **TabNet (2021)**
* **FT-Transformer (2021)**

These models introduced mechanisms to better capture feature interactions and improve representation learning in tabular settings, bridging the gap between deep learning and traditional tree-based methods.

Model Type
~~~~~~~~~~
Transformer-based or attention-based tabular architectures.

Usage
-----

Direct Use
~~~~~~~~~~
* Modeling complex, non-linear feature interactions in structured datasets.
* Replacing or augmenting tree-based ensembles (like XGBoost or LightGBM) when deep representation learning is desired.
* Integrating tabular data streams into larger, multi-modal deep learning pipelines.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Extremely small datasets (highly prone to overfitting without sufficient data).
* Tasks where traditional tree ensembles dominate with minimal tuning and computational resources are strictly constrained.

Supported Modalities
--------------------
* **Structured Tabular Data:** The primary modality for all three models.
* **Categorical Features:** Naturally supported via learned embeddings. TabTransformer specifically focuses on creating robust contextual embeddings for categorical variables.
* **Numerical/Continuous Features:** Supported either directly (TabNet) or via numerical embedding/tokenization strategies (FT-Transformer).

Interpretability
----------------
* **TabNet:** Designed with an inherently interpretable architecture. It uses sparse, sequential attention masks at each decision step, providing both **local interpretability** (which features were important for a specific prediction) and **global interpretability** (overall feature importance across the dataset).
* **TabTransformer & FT-Transformer:** Offer a degree of interpretability through the analysis of **attention weights**, allowing practitioners to see which feature tokens attend to one another, though this is generally less explicit than TabNet's masking approach.

Missing Value Handling
----------------------
* **Categorical Features:** Missing values can easily be treated as a distinct, dedicated ``<MISSING>`` category/token, allowing the models to learn explicit embeddings for the absence of data.
* **Numerical Features:** Generally require standard preprocessing and imputation (e.g., mean, median, or iterative imputation) prior to tokenization and training, as the base architectures do not natively impute continuous values on the fly.

Bias, Risks, and Limitations
----------------------------
* **Computational Cost:** Significantly higher training and inference latency compared to highly optimized tree-based models.
* **Hyperparameter Sensitivity:** Performance is heavily dependent on learning rates, embedding sizes, and attention configurations.
* **Performance Inconsistency:** May not consistently outperform gradient boosting machines (GBMs) across all tabular benchmarks, especially on uncleaned data.

Training Details
----------------
* **Feature Tokenization:** Requires careful preprocessing to convert features into tokens (a core focus of FT-Transformer).
* **Embeddings:** TabTransformer heavily relies on self-attention over categorical embeddings while passing numerical features directly through layer normalization.
* **Attention Mechanisms:** TabNet utilizes sequential attention for dynamic feature selection, whereas FT-Transformer applies standard Multi-Head Self-Attention across all feature tokens simultaneously.

Evaluation
----------
* **Metrics:** Standard classification and regression metrics (AUROC, Accuracy, Macro-F1, RMSE).
* **Baselines:** Typically evaluated against robust tree-based baselines (Random Forest, XGBoost, CatBoost).

Technical Specifications
------------------------
* **TabTransformer:** Self-attention applied specifically to categorical embeddings.
* **TabNet:** Sparse sequential attention masks using attentive transformers and feature transformers.
* **FT-Transformer:** Treats every single feature (both categorical and numerical) as an individual token for a standard Transformer encoder.

Citation
--------
* Huang et al. (2020). *TabTransformer: Tabular Data Modeling Using Contextual Embeddings.*
* Arik & Pfister (2021). *TabNet: Attentive Interpretable Tabular Learning.*
* Gorishniy et al. (2021). *Revisiting Deep Learning Models for Tabular Data.* (FT-Transformer)

More in Future...
-----------------
* *(Placeholder)* Advanced tokenization strategies for skewed continuous variables.
* *(Placeholder)* Self-supervised pre-training setups for tabular foundation models.
* *(Placeholder)* Integration examples with modern MLOps pipelines.
Foundation Models
=================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category represents a paradigm shift in tabular machine learning: foundation models that leverage **in-context learning** to perform predictions without traditional gradient descent on the downstream task. TabPFN (Prior-Data Fitted Network) v2.5 is the latest generation, scaling the context window to handle significantly larger datasets than its predecessors. It effectively learns to approximate Bayesian inference across a massive variety of tabular structures.

Model Type
~~~~~~~~~~
Pre-trained Transformer-based foundation model for tabular classification and regression.

Usage
-----

Direct Use
~~~~~~~~~~
* Ultra-fast, zero-shot/few-shot inference without training loops or hyperparameter tuning.
* Establishing state-of-the-art baselines on small-to-medium tabular datasets (up to 50,000 samples and 2,000 features).
* Scenarios requiring high data efficiency, where traditional tree-based models overfit due to low sample counts.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Massive datasets exceeding the 50,000 sample / 2,000 feature limit (requires complex chunking, ensembling, or downsampling).
* Tasks strictly requiring CPU-only environments for inference (TabPFN is highly optimized for, and heavily reliant on, GPUs).
* Unstructured data modalities (raw text, images) without prior embedding extraction.

Supported Modalities
--------------------
* **Structured Tabular Data:** The primary modality.
* **Categorical & Numerical Features:** Handled natively without requiring manual one-hot encoding or strict feature scaling prior to the forward pass. The model internally tokenizes and processes mixed data types on the fly.

Interpretability
----------------
* **Limited Native Interpretability:** TabPFN operates as a black-box Transformer, processing the entire dataset as a single context window. It lacks the natural, human-readable decision paths found in tree-based models.
* **Post-Hoc Bottlenecks:** While standard explainability tools (e.g., SHAP, SAGE) can be applied, they require hundreds of permutations and forward passes. Because TabPFN evaluates the entire dataset context per pass, deriving feature importance is significantly more computationally expensive than with Random Forests or GBDTs.

Missing Value Handling
----------------------
* **Native Support:** TabPFN inherently handles missing values (``NaN`` or ``Null``) directly out of the box. You do **not** need to apply a separate pre-imputation pipeline.
* **Mechanism:** The model was heavily exposed to diverse missing data patterns (MCAR, MAR, MNAR) during its synthetic pre-training phase. This allows it to internally contextualize and dynamically impute or route around missing features during the inference forward pass.

Bias, Risks, and Limitations
----------------------------
* **Context Window Limits:** There are hard computational limits on dataset size due to the memory and compute complexity of standard attention mechanisms computing relationships across tens of thousands of rows and columns.
* **Production Deployment Hurdles:** The raw Transformer is a heavy model. While v2.5 introduces a distillation engine to export behavior to smaller MLPs/Trees, deploying the native model directly into strict low-latency (e.g., microsecond) CPU-bound environments is challenging.
* **Distribution Shift:** Its zero-shot performance relies heavily on the inductive biases learned during synthetic pre-training.

Training Details
----------------
* **Pre-training:** Trained offline on over 130 million synthetic tabular datasets generated via highly parametric Structural Causal Models (SCMs). (Note: "Real-TabPFN" checkpoints are further fine-tuned on real-world OpenML data).
* **Downstream "Training":** None. It uses In-Context Learning. The training set (features and labels) is simply passed alongside the test set (features only) as context in a single forward pass.

Evaluation
----------
* **Metrics:** AUROC, Accuracy, F1 (Classification); RMSE, R2 (Regression).
* **Baselines:** Matches or outperforms heavily tuned AutoML ensembles (like AutoGluon) and GBDTs (XGBoost, CatBoost) on small-to-medium datasets, achieving results in seconds rather than hours.

Technical Specifications
------------------------
* **Architecture:** Transformer encoder specifically adapted for tabular data.
* **Mechanism:** Treats the entire dataset (or large batches) as a sequence of tokens. It relies on attention mechanisms to learn intra-row feature relationships and inter-row similarities simultaneously, effectively unifying representation learning and prediction.

Citation
--------
* Hollmann et al. (2025). *Accurate predictions on small data with a tabular foundation model.* Nature. 
* Prior Labs (2025). *TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models.* (Technical Report).

More in Future...
-----------------
* *(Placeholder)* Integration strategies with Retrieval-Augmented Generation (RAG) for extreme-scale tabular data beyond 100k rows.
* *(Placeholder)* Native handling of high-cardinality, raw text fields via multimodal tokenization.
* *(Placeholder)* Advances in zero-shot conformal prediction for calibrated uncertainty and confidence bounds natively from the model.
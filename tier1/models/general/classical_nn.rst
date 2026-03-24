========================================
Classical Neural Baselines (MLP, ResNet)
========================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category includes classical neural network architectures that have been adapted to serve as foundational deep learning baselines for tabular data:

* **Multi-Layer Perceptron (MLP):** The standard, fully connected feedforward neural network.
* **Residual Networks (ResNet):** Originally designed for computer vision (He et al., 2015), the ResNet architecture is frequently adapted for tabular learning by replacing convolutional layers with fully connected layers inside the residual blocks.

These models serve as essential deep learning baselines for structured data and are universally used for comparison against both tree-based algorithms and more specialized tabular architectures.

Model Type
~~~~~~~~~~
Supervised deep learning models for tabular classification and regression.

Usage
-----

Direct Use
~~~~~~~~~~
* Establishing standard deep learning lower-bound baselines for tabular prediction tasks.
* Benchmark comparisons against Gradient Boosted Decision Trees (GBDTs) and newer Transformer-based tabular models.
* Integrating structured data processing into larger, end-to-end differentiable multimodal pipelines.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Raw, un-preprocessed multimodal inputs (image/audio/text).
* Highly sparse or categorical-heavy datasets without strict, prior encoding schemes.
* Scenarios with highly limited data, where tree ensembles are vastly more efficient and less prone to overfitting.

Supported Modalities
--------------------
* **Structured Tabular Data:** The sole intended modality.
* **Categorical Features:** Must be explicitly transformed before input. Common strategies include One-Hot Encoding (for low-cardinality), Target Encoding, or passing them through learned Embedding layers prior to the main network.
* **Numerical/Continuous Features:** Supported natively but **strictly require scaling** (e.g., Standardization or MinMax scaling). Neural networks are highly sensitive to unscaled variance across continuous features.

Interpretability
----------------
* **Black-Box Nature:** Unlike decision trees or attention-based models, MLPs and ResNets lack inherent, human-readable mechanisms for feature selection or routing.
* **Post-Hoc Analysis:** Deriving feature importance requires external, post-hoc explainability tools such as **SHAP** (SHapley Additive exPlanations), **LIME**, or **Integrated Gradients**.

Missing Value Handling
----------------------
* **No Native Support:** Classical dense neural networks cannot dynamically handle `NaN` or `Null` inputs. 
* **Pre-Imputation Required:** A rigorous imputation pipeline (e.g., mean, median, mode, k-NN, or iterative imputation) must be applied to numerical features before training and inference.
* **Categorical Handling:** Missing categorical values can be encoded as a distinct, known category (e.g., ``"Missing"``) prior to encoding or embedding.

Bias, Risks, and Limitations
----------------------------
* **Weak Inductive Bias:** Unlike trees that naturally partition the feature space, standard dense layers lack a strong inductive bias for tabular data, often requiring significantly more data to learn optimal decision boundaries.
* **Preprocessing Sensitivity:** Performance is exceptionally fragile and highly dependent on feature scaling, encoding strategies, and the handling of outliers.
* **Performance Gap:** Often underperform well-tuned tree-based models (like XGBoost or CatBoost) on standard, heterogeneous tabular datasets, especially those of small-to-medium size.

Training Details
----------------
* **Optimization:** Trained using standard gradient descent optimizers (Adam, AdamW, SGD) with cross-entropy (classification) or MSE/Huber loss (regression).
* **Hyperparameter Tuning:** Critical for competitive performance. Key parameters include network depth, layer width, dropout rates, weight decay, and learning rate schedules.
* **Regularization:** Highly reliant on Dropout and Batch Normalization to prevent overfitting and stabilize training.

Evaluation
----------
* **Metrics:** Standard classification and regression metrics (AUROC, Accuracy, Macro-F1, RMSE).
* **Role in Benchmarks:** Typically serves as the control group in deep tabular learning research to prove the efficacy of novel architectures.

Technical Specifications
------------------------
* **MLP:** A simple stack of Fully Connected (Dense) layers interspersed with non-linear activation functions (typically ReLU or GELU) and Dropout.
* **ResNet (Tabular):** Composed of sequential residual blocks. Each block typically contains Batch Normalization, Fully Connected layers, activations, and a skip connection (identity mapping) that adds the block's input to its output, allowing the successful training of significantly deeper networks.

Citation
--------
* Goodfellow et al. (2016). *Deep Learning.* MIT Press. (Foundational MLP reference).
* He et al. (2015). *Deep Residual Learning for Image Recognition.* (Original ResNet architecture).
* Gorishniy et al. (2021). *Revisiting Deep Learning Models for Tabular Data.* (Standardized implementation and benchmarking of MLP/ResNet for tabular data).

More in Future...
-----------------
* *(Placeholder)* Advanced regularization techniques specific to tabular MLPs (e.g., modern dropout variants or weight initialization schemes).
* *(Placeholder)* Best-practice automated hyperparameter optimization (HPO) search spaces for robust MLP baselines.
* *(Placeholder)* Strategies for enhancing baseline performance using synthetic data generation (e.g., SMOTE, CTGAN).
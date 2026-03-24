=================
Tree-Based Models
=================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This model card covers a family of tree-based ensemble methods used as strong tabular baselines in Tier 1 of EMAI-COPD. 
The included models are:

* **Random Forest (RF)**
* **Extreme Gradient Boosting (XGBoost)**
* **Light Gradient Boosting Machine (LightGBM)**
* **CatBoost**

These models operate on structured tabular data and are particularly effective for clinical, omics, and mixed-feature datasets, serving as the gold standard for many tabular prediction tasks.

Developed by
~~~~~~~~~~~~
* **Random Forest:** Leo Breiman (scikit-learn implementation)
* **XGBoost:** Tianqi Chen et al. (DMLC)
* **LightGBM:** Microsoft Research
* **CatBoost:** Yandex Research

Funded by
~~~~~~~~~
Various academic and industry institutions (e.g., Microsoft, Yandex, open-source contributors).

Model Type
~~~~~~~~~~
Supervised machine learning models for classification and regression using decision tree ensembles (Bagging and Boosting).

Language(s)
~~~~~~~~~~~
Not applicable (tabular / structured data models).

License
~~~~~~~
* **Random Forest (scikit-learn):** BSD License
* **XGBoost:** Apache 2.0
* **LightGBM:** MIT License
* **CatBoost:** Apache 2.0

Model Sources
~~~~~~~~~~~~~
* **XGBoost Repository:** https://github.com/dmlc/xgboost
* **LightGBM Repository:** https://github.com/microsoft/LightGBM
* **CatBoost Repository:** https://github.com/catboost/catboost
* **Scikit-learn (RF):** https://scikit-learn.org

Usage
-----

Direct Use
~~~~~~~~~~
* Baseline classification and regression for COPD prediction tasks.
* Tabular modeling for clinical, demographic, and omics-derived features.
* Feature importance analysis, biomarker discovery, and interpretability studies.

Downstream Use
~~~~~~~~~~~~~~
* Benchmark comparisons against deep learning and multimodal foundational models.
* Feature selection and importance ranking prior to deep learning pipelines.
* Input to ensemble systems, stacked models, or meta-classifiers.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Raw image, audio, or sequence modeling without extensive prior feature extraction.
* Extremely high-dimensional sparse data (e.g., raw text tokens) without proper preprocessing or dimensionality reduction.
* End-to-end multimodal learning without strict structured representation.

Supported Modalities
--------------------
* **Structured Tabular Data:** The primary modality.
* **Clinical & Demographic Data:** Naturally handles combinations of continuous (age, BMI) and categorical (sex, smoking status) variables.
* **Omics Data:** Effectively processes tabular representations of genomics, transcriptomics, or metabolomics, provided dimensionality is managed.

Interpretability
----------------
* **Inherent Global Interpretability:** Tree-based models naturally yield robust global feature importance metrics (e.g., Gini impurity decrease, Split counts, Information Gain), allowing researchers to easily rank clinical biomarkers.
* **Local Interpretability:** Highly compatible with post-hoc explainers like **TreeSHAP** (SHapley Additive exPlanations), which provides exact, rapid, and mathematically consistent explanations for individual patient predictions.

Missing Value Handling
----------------------
* **XGBoost & LightGBM:** Native, highly efficient support for missing values. During training, the models automatically learn the best "default direction" (left or right child node) for missing values to minimize loss.
* **CatBoost:** Native support for missing values. It can process them by treating `NaN` as either the minimum or maximum value in the feature space, depending on the chosen strategy.
* **Random Forest (scikit-learn):** **No native support.** Requires explicit pre-imputation (e.g., median, mean, mode, or k-NN imputation) of the EMAI-COPD dataset before training.

Bias, Risks, and Limitations
----------------------------
* **Imbalance Sensitivity:** Can be sensitive to clinical data imbalance, often favoring the majority class unless mitigated (e.g., via `scale_pos_weight` or SMOTE).
* **Overfitting Risks:** Gradient boosting methods (XGB, LGBM, CatBoost) can easily overfit noisy clinical data if tree depth, learning rate, and regularization are not properly constrained.
* **Correlated Features:** Feature importance metrics can be misleading when inputs are highly correlated (e.g., multiple closely related lung function metrics), as the models may arbitrarily split importance among them.
* **Extrapolation:** Trees cannot extrapolate beyond the numerical range of the training data (a known limitation for regression tasks).

Recommendations
---------------
Users should:

* Apply proper cross-validation and evaluation metrics (e.g., AUROC, macro-F1) tailored to the clinical outcome.
* Monitor class imbalance and apply target weighting or resampling if needed.
* Use feature importance cautiously, especially in correlated feature spaces; consider relying on SHAP for more robust analysis.
* Compare across multiple tree-based methods for robustness, as different boosting implementations handle categorical and missing data differently.

How to Get Started with the Model
---------------------------------

Example (XGBoost):

.. code-block:: python

    import xgboost as xgb
    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        missing=np.nan # Automatically handle missing clinical data
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

Example (Random Forest):

.. code-block:: python

    from sklearn.ensemble import RandomForestClassifier
    # Note: X_train must be pre-imputed; RF cannot handle NaNs
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)

Training Details
----------------

Training Data
~~~~~~~~~~~~~
* Tabular datasets from the EMAI-COPD cohort, including:
  * Clinical features (spirometry, vital signs)
  * Demographics
  * Omics-derived features (processed and scaled)
* Pre-requisites vary by model (e.g., imputation for RF, specific encoding for categoricals if not using CatBoost/LightGBM native features).

Training Procedure
~~~~~~~~~~~~~~~~~~

Preprocessing
^^^^^^^^^^^^^
* **Missing value imputation:** Required for RF (median / domain-specific); optional but recommended to test against native handling for Boosting algorithms.
* **Categorical encoding:**
  * One-hot or ordinal encoding (RF, XGBoost).
  * Native handling (CatBoost, LightGBM) is highly recommended to preserve data structure.
* **Feature filtering:** Removing zero-variance omics features.

Training Hyperparameters
~~~~~~~~~~~~~~~~~~~~~~~~

Training Regime
^^^^^^^^^^^^^^^
* Supervised classification or regression.
* Strict Train/Validation/Test split or k-fold Cross-Validation grouped by patient ID to prevent data leakage.

Typical Hyperparameters:
* ``n_estimators``: 100–1000
* ``max_depth``: 3–10 (Shallower often better for tabular clinical data to prevent overfitting).
* ``learning_rate`` (boosting): 0.01–0.3
* ``subsample`` / ``colsample_bytree``: 0.7-1.0 (Crucial for generalization).

Evaluation
----------

Testing Data
~~~~~~~~~~~~
Held-out clinical test set or cross-validation folds drawn from the identical distribution as the training data, ensuring no patient overlap between folds.

Factors
~~~~~~~
* Class imbalance (e.g., severe vs. mild COPD).
* Feature distribution shifts across different collection sites or cohorts.
* Missing data patterns (MCAR, MAR, MNAR) in clinical records.

Metrics
~~~~~~~
* AUROC
* Macro-F1 / Weighted-F1
* Accuracy
* Precision-Recall AUC (Crucial for highly imbalanced cohorts).

Results
~~~~~~~
Tree-based models typically provide strong, often state-of-the-art baseline performance for tabular COPD prediction tasks. They serve as the primary reference point to justify the added complexity of Tier 2/3 deep learning and multimodal models.

Summary
-------

Model Examination
~~~~~~~~~~~~~~~~~
* Exceptionally strong performance on structured tabular data.
* Robust to feature scaling and monotonic transformations.
* Highly effective even with limited clinical cohort sizes.
* Readily interpretable via global feature importance and local SHAP values.

Environmental Impact
--------------------

Hardware Type
~~~~~~~~~~~~~
CPU (primary and highly efficient), optional GPU acceleration for large-scale XGBoost/LightGBM/CatBoost runs.

Hours Used
~~~~~~~~~~
Low to moderate, depending heavily on dataset size and the extensiveness of the hyperparameter search grid.

Cloud Provider
~~~~~~~~~~~~~~
Agnostic / Optional (AWS, GCP, Azure, or local clinical clusters).

Carbon Emitted
~~~~~~~~~~~~~~
Relatively low compared to training foundational deep learning or multimodal models.

Technical Specifications
------------------------

Model Architecture and Objective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Random Forest:** Bagging ensemble of independent decision trees to reduce variance.
* **XGBoost / LightGBM / CatBoost:** Gradient boosting frameworks that utilize sequential tree learning, where each new tree corrects the residual errors of the previous ensemble.

Objective Functions:
* **Classification:** Logistic loss, Cross-entropy.
* **Regression:** Mean Squared Error (MSE), Mean Absolute Error (MAE), Huber loss.

Compute Infrastructure
~~~~~~~~~~~~~~~~~~~~~~
* Single-node training is generally sufficient for clinical datasets of this scale.
* Heavy parallelization is supported at the node level (especially optimized in LightGBM and XGBoost).

Hardware
~~~~~~~~
* Multi-core CPU is highly recommended.
* GPU acceleration (CUDA) is available and drastically speeds up histogram building for Boosting algorithms on large datasets.

Software
~~~~~~~~
* Python 3.x
* ``scikit-learn``
* ``xgboost``
* ``lightgbm``
* ``catboost``

Citation
--------
* Breiman, L. (2001). *Random Forests.* Machine Learning.
* Chen, T., & Guestrin, C. (2016). *XGBoost: A Scalable Tree Boosting System.* KDD.
* Ke, G. et al. (2017). *LightGBM: A Highly Efficient Gradient Boosting Decision Tree.* NeurIPS.
* Dorogush, A. V. et al. (2018). *CatBoost: unbiased boosting with categorical features.* NeurIPS.

More in Future...
-----------------
* *(Placeholder)* Integration of **Survival Trees** (e.g., XGBoost Survival Embeddings) for longitudinal COPD exacerbation risk modeling over time.
* *(Placeholder)* Federated learning pipelines for multi-institutional COPD data sharing using decentralized tree building.
* *(Placeholder)* Advanced SHAP clustering techniques to identify distinct clinical COPD sub-phenotypes based on model decision paths.
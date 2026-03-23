Tree-Based Models
=================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This model card covers a family of tree-based ensemble methods used as strong tabular baselines in Tier 1 of EMAI-COPD. 
The included models are:

- Random Forest (RF)
- Extreme Gradient Boosting (XGBoost)
- Light Gradient Boosting Machine (LightGBM)
- CatBoost

These models operate on structured tabular data and are particularly effective for clinical, omics, and mixed-feature datasets.

Developed by
~~~~~~~~~~~~
- Random Forest: Leo Breiman
- XGBoost: Tianqi Chen et al.
- LightGBM: Microsoft Research
- CatBoost: Yandex Research

Funded by
~~~~~~~~~
Various academic and industry institutions (e.g., Microsoft, Yandex, open-source contributors).

Model Type
~~~~~~~~~~
Supervised learning models for classification and regression using decision tree ensembles.

Language(s)
~~~~~~~~~~~
Not applicable (tabular / structured data models).

License
~~~~~~~
- Random Forest (scikit-learn): BSD License
- XGBoost: Apache 2.0
- LightGBM: MIT License
- CatBoost: Apache 2.0

Model Sources
~~~~~~~~~~~~~
- XGBoost Repository: https://github.com/dmlc/xgboost
- LightGBM Repository: https://github.com/microsoft/LightGBM
- CatBoost Repository: https://github.com/catboost/catboost
- Scikit-learn (RF): https://scikit-learn.org

Uses
-----

Direct Use
~~~~~~~~~~
- Baseline classification for COPD prediction tasks
- Tabular modeling for clinical, demographic, and omics-derived features
- Feature importance analysis and interpretability studies

Downstream Use
~~~~~~~~~~~~~~
- Benchmark comparison against deep learning and multimodal models
- Feature selection and importance ranking
- Input to ensemble systems or stacked models

Out-of-Scope Use
~~~~~~~~~~~~~~~~
- Raw image, audio, or sequence modeling without feature extraction
- Extremely high-dimensional sparse data without preprocessing
- End-to-end multimodal learning without structured representation

Bias, Risks, and Limitations
---------------------------

- Sensitive to data imbalance (may favor majority class)
- Can overfit if not properly regularized (especially boosting methods)
- Feature importance can be misleading under correlated inputs
- Performance depends heavily on preprocessing and feature engineering
- May encode biases present in clinical or demographic data

Recommendations
---------------

Users should:

- Apply proper cross-validation and evaluation metrics (e.g., AUROC, macro-F1)
- Monitor class imbalance and apply weighting or resampling if needed
- Use feature importance cautiously, especially in correlated feature spaces
- Compare across multiple tree-based methods for robustness

How to Get Started with the Model
--------------------------------

Example (XGBoost):

.. code-block:: python

    import xgboost as xgb
    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

Example (Random Forest):

.. code-block:: python

    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None
    )
    model.fit(X_train, y_train)

Training Details
----------------

Training Data
~~~~~~~~~~~~~
- Tabular datasets including:
  - Clinical features
  - Demographics
  - Omics-derived features (processed)
- Typically requires:
  - Missing value handling
  - Encoding of categorical variables
  - Feature scaling (optional depending on model)

Training Procedure
~~~~~~~~~~~~~~~~~~

Preprocessing
^^^^^^^^^^^^^
- Missing value imputation (median / domain-specific)
- Categorical encoding:
  - One-hot encoding (RF, XGB)
  - Native handling (CatBoost, LightGBM)
- Feature filtering and normalization (optional)

Training Hyperparameters
~~~~~~~~~~~~~~~~~~~~~~~~

Training Regime
^^^^^^^^^^^^^^^
- Supervised classification
- Train/validation/test split or cross-validation

Typical Hyperparameters:
- n_estimators: 100–1000
- max_depth: 3–10
- learning_rate (boosting): 0.01–0.3
- subsample / colsample (boosting)

Evaluation
----------

Testing Data
~~~~~~~~~~~~
Held-out test set or cross-validation folds from the same distribution as training data.

Factors
~~~~~~~
- Class imbalance
- Feature distribution shifts
- Missing data patterns
- Dataset size and dimensionality

Metrics
~~~~~~~
- AUROC
- Macro-F1
- Weighted-F1
- Accuracy

Results
~~~~~~~
Tree-based models typically provide strong baseline performance for tabular COPD prediction tasks and serve as a reference point for evaluating more complex models.

Summary
-------

Model Examination
~~~~~~~~~~~~~~~~~
- Strong performance on structured data
- Robust to feature scaling
- Effective with limited data
- Interpretable via feature importance and SHAP values

Environmental Impact
--------------------

Hardware Type
~~~~~~~~~~~~~
CPU (primary), optional GPU for XGBoost/LightGBM

Hours Used
~~~~~~~~~~
Low to moderate depending on dataset size

Cloud Provider
~~~~~~~~~~~~~~
Optional (AWS, GCP, Azure)

Carbon Emitted
~~~~~~~~~~~~~~
Relatively low compared to deep learning models

Technical Specifications
------------------------

Model Architecture and Objective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Random Forest: Bagging ensemble of decision trees
- XGBoost / LightGBM / CatBoost:
  - Gradient boosting framework
  - Sequential tree learning minimizing loss function

Objective:
- Classification (logistic loss, cross-entropy)
- Regression (MSE, MAE)

Compute Infrastructure
~~~~~~~~~~~~~~~~~~~~~~
- Single-node training sufficient for most datasets
- Parallelization supported (especially LightGBM)

Hardware
~~~~~~~~
- CPU (multi-core recommended)
- Optional GPU acceleration for boosting methods

Software
~~~~~~~~
- Python
- scikit-learn
- xgboost
- lightgbm
- catboost

Citation
--------

Breiman, L. (2001). Random Forests.

Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System.

Ke, G. et al. (2017). LightGBM: A Highly Efficient Gradient Boosting Decision Tree.

Dorogush, A. V. et al. (2018). CatBoost: unbiased boosting with categorical features.
====================================================================================================
Multi-Omics Integration Models: MOGONET (Multi-Omics Graph Convolutional Networks)
====================================================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
MOGONET is a pioneering end-to-end deep learning framework designed for multi-omics integration and biomedical classification. It effectively addresses the heterogeneity of multi-omics data by decoupling the representation learning into two distinct stages:

1. **Omics-Specific Learning:** Utilizes independent Graph Convolutional Networks (GCNs) for each omics data type to learn patient representations based on omics features and corresponding sample similarity networks.
2. **Multi-Omics Integration:** Introduces a novel View Correlation Discovery Network (VCDN) that explores the cross-omics correlations at the label space level. It computes a cross-omics discovery tensor from the initial predictions of the omics-specific GCNs to make the final unified prediction.

Model Type
~~~~~~~~~~
Supervised Graph Convolutional Network (GCN) with late-fusion View Correlation Discovery Network (VCDN) for tabular multi-omics classification.

Usage
-----

Direct Use
~~~~~~~~~~
* Patient classification tasks, such as cancer subtyping (e.g., BRCA, KIPAN), tumor grading (LGG), and Alzheimer's disease diagnosis (ROSMAP).
* **Ready-to-use biomarker discovery** for identifying the most discriminative genomic, transcriptomic, or epigenetic features driving clinical outcomes.
* Analyzing cross-omics interactions at the class-probability level.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Extremely small cohorts where k-Nearest Neighbor (k-NN) graphs cannot construct a meaningful patient-to-patient similarity network.
* Tasks requiring pixel-level or sequence-level inputs without prior feature extraction into structured, tabular formats.

Supported Modalities
--------------------
* **Structured Tabular Multi-Omics Data:** Evaluated natively on combinations of:
  * mRNA expression
  * miRNA expression
  * DNA methylation
* **Scalability:** The architecture allows for the addition or removal of omics modalities by simply adjusting the number of parallel GCN branches and expanding the dimensionality of the VCDN tensor.

Interpretability & Biomarker Discovery
--------------------------------------
* **Outstanding Native Support:** Unlike many other deep learning multi-omics models, MOGONET features a fully implemented, ready-to-use pipeline for feature-importance analysis.
* **Implementation Details:** * **Dedicated Scripts:** Found in ``feat_importance.py`` and wrapped in ``main_biomarker.py``.
  * **Methodology (Leave-One-Feature-Out):** The model employs an ablation strategy. It systematically zeroes out specific features, re-runs the inference pipeline, and measures the drop in the F1-score or Accuracy to calculate an exact importance score for every input feature.
* **Biomarker Workflow:** Users can directly execute ``main_biomarker.py``, which runs ``cal_feat_imp()`` followed by ``summarize_imp_feat()``, to immediately export a ranked list of the most critical biological markers (e.g., specific genes or CpG sites).

Missing Value Handling
----------------------
* **Pre-imputation Required:** MOGONET relies on the construction of sample similarity graphs (e.g., using cosine similarity) and standard GCN layers, which cannot inherently process ``NaN`` or ``Null`` values.
* **Standard Pre-processing:** The data must be cleaned, pre-imputed (e.g., k-NN or median imputation), and filtered to remove noise and redundant zero-variance features prior to generating the input matrices and adjacency graphs.

Bias, Risks, and Limitations
----------------------------
* **VCDN Scaling Complexity:** The size of the cross-omics discovery tensor in the VCDN module scales exponentially with the number of modalities ($k$) and the number of classes ($C$), creating a tensor of size $C^k$. This makes MOGONET computationally expensive for tasks with highly highly multiplexed omics layers combined with a massive number of target classes.
* **Graph Quality Dependency:** The performance of the omics-specific GCNs is strictly bound by the quality of the initial sample similarity networks generated during pre-processing.

Training Details
----------------
The repository provides clean, modular scripts for execution, separating classification tasks from biomarker discovery.

**1. Classification Training & Testing:**
Executes the joint training of the omics-specific GCNs and the VCDN.

.. code-block:: bash

    # Examples for classification tasks are located in main_mogonet.py
    python main_mogonet.py

**2. Biomarker Identification:**
Executes the ablation-based feature importance pipeline on a trained model.

.. code-block:: bash

    # Wrapper script for feature importance extraction
    python main_biomarker.py

**Key Files:**
* ``models.py``: Contains the architectures for both the GCNs and the VCDN.
* ``train_test.py``: Contains the training loops and evaluation metrics.
* ``utils.py``: Handles data loading, pre-processing, and graph construction.

Evaluation
----------
* **Metrics:** Accuracy (ACC), F1 score (macro and weighted), and Area Under the Curve (AUC).
* **Baselines:** Demonstrated superior performance across benchmark datasets (ROSMAP, BRCA, LGG, KIPAN) when compared against classic machine learning algorithms (SVM, Random Forest), single-omics GCNs, and early-fusion deep learning models.

Technical Specifications
------------------------
* **Omics-Specific GCNs:** Each modality is processed by a GCN that takes a feature matrix and a pre-computed k-NN adjacency matrix as inputs. It outputs an initial class probability vector for each sample.
* **VCDN (View Correlation Discovery Network):** * Takes the initial class probability vectors from all GCN branches.
  * Computes their outer product to form a higher-order tensor, effectively capturing the cross-omics interactions at the label space level.
  * Flattens the tensor and processes it through a fully connected (Dense) layer to produce the final classification output.
* **End-to-End Optimization:** The GCNs and VCDN are trained jointly using a weighted cross-entropy loss function to handle class imbalances natively.

Citation
--------
* Wang, T., Shao, W., Huang, Z., Tang, H., Zhang, J., Ding, Z., & Huang, K. (2021). *MOGONET integrates multi-omics data using graph convolutional networks allowing patient classification and biomarker identification*. Nature communications, 12(1), 3445.

More in Future...
-----------------
* *(Placeholder)* Optimizations for the VCDN tensor calculation to support high-cardinality classification tasks (e.g., >20 cancer subtypes) without memory bottlenecks.
* *(Placeholder)* Adapting the Leave-One-Feature-Out methodology to calculate combined, multi-feature pathway importance scores.
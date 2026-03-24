=====================================================================================================
Multi-Omics Integration Models: mmMOI (Multi-label Guided Learning and Multi-scale Fusion)
=====================================================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
mmMOI is an end-to-end deep learning framework designed explicitly for the integration of high-dimensional multi-omics data[cite: 12]. It addresses the limitations of manual feature selection and restricted applicability in existing methods by directly processing raw omics data[cite: 11, 13]. The framework operates in two distinct phases: 

1. **Single-omics Representation Learning (SoRL):** Utilizes a dimensionality reduction Autoencoder (AE) combined with a multi-view Graph Neural Network (GNN) guided by multi-label learning (using both true labels and pseudo-labels from consensus graph clustering)[cite: 67, 69, 138, 178].
2. **Multi-omics Data Fusion (MoDF):** Employs a multi-scale attention fusion network comprising a Global Attention Fusion Network (GAFN) to weight different omics channels, and a Local Attention Fusion Network (LAFN) using multi-head self-attention to capture patient-specific cross-omics interactions[cite: 67, 224, 250].

Model Type
~~~~~~~~~~
Supervised Graph Neural Network (GNN) and Attention-based fusion framework for tabular multi-omics classification[cite: 20, 317].

Usage
-----

Direct Use
~~~~~~~~~~
* Accurate classification of complex cancer subtypes[cite: 27, 74].
* Integration of diverse biological data layers without relying on prior manual feature preselection[cite: 13].
* End-to-end patient survival risk assessment and prognostic analysis[cite: 413, 414].

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Extremely small cohorts where GNNs cannot construct meaningful patient-to-patient similarity graphs.
* Raw unstructured data (e.g., whole-slide histology images) without prior extraction into tabular features.

Supported Modalities
--------------------
* **Structured Multi-Omics Data:** Validated across combinations of three primary omics layers[cite: 324]:
  * mRNA expression [cite: 324]
  * miRNA expression [cite: 324]
  * DNA methylation [cite: 324]
* **Flexibility:** The architecture is designed to adaptively learn representations across different datasets, improving generalizability across various sequencing technologies[cite: 14, 17].

Interpretability & Biomarker Discovery
--------------------------------------
* **Architectural Mechanism:** mmMOI utilizes global and local attention layers in its MoDF module (``mmMOI/MoDF/models.py``) which internally weigh the importance of different omics channels and interactions[cite: 225, 250].
* **Implementation Limitation:** **Lacks out-of-the-box feature attribution.** Unlike models such as MOGONET (which includes a dedicated Leave-One-Feature-Out pipeline), mmMOI's current codebase does not include the necessary scripts to translate internal attention weights back into a ranked list of original input features (e.g., specific genes or CpG sites).
* **Required Workarounds:** To extract feature importance rankings for biomarkers, practitioners must manually integrate attribution methods such as:
  * **Permutation Importance:** Randomly shuffling input features per omics layer to observe the drop in F1-score.
  * **Integrated Gradients (e.g., via Captum):** For gradient-based attribution mapped back to the input space.
  * **Gradient $\times$ Input:** To measure the feature's contribution relative to the final classification output.

Missing Value Handling
----------------------
* **Pre-imputation Expected:** As mmMOI directly inputs omics matrices into a dimensionality reduction Autoencoder ($X \in \mathbb{R}^{n \times d}$) and computes pairwise similarity graphs[cite: 138, 140], it requires complete datasets. Standard omics pre-imputation pipelines (e.g., k-NN or median imputation) must be applied prior to generating the input matrices.

Bias, Risks, and Limitations
----------------------------
* **Two-Stage Execution:** Requires training the Single-omics Representation Learning (SoRL) module to convergence before routing the embeddings to the Multi-omics Data Fusion (MoDF) module, increasing workflow complexity.
* **Biomarker Export:** The lack of a native feature-importance export pipeline limits immediate clinical interpretability without additional coding effort.
* **Graph Dependency:** Performance relies heavily on the quality of the initial similarity graphs constructed from the AE embeddings[cite: 154].

Training Details
----------------
The repository structure separates the training pipeline strictly into two phases:

**1. Single-omics Data Representation (SoRL):**
Optimizes feature reconstruction and initial classification using multi-label guided graph fusion[cite: 81, 290].

.. code-block:: bash

    cd SoRL
    python main.py --dataset GBM --cuda_device 0

**2. Multi-omics Data Fusion (MoDF):**
Takes the learned single-omics representations and trains the multi-scale attention networks to predict the final labels[cite: 213, 215].

.. code-block:: bash

    cd MoDF
    python main.py --dataset GBM --cuda_device 0 --mode True

Evaluation
----------
* **Metrics:** Evaluated extensively using Accuracy, F1-macro, Precision, and Recall[cite: 337].
* **Baselines:** Demonstrated statistically significant superiority over classical ML (Random Forest, SVM, XGBoost) and state-of-the-art deep learning methods (MOGONET, CustOmics, AttentionMOI, MCRGCN, GREMI) across GBM, BRCA, OV, and KIPAN datasets[cite: 328, 329, 339, 341].

Technical Specifications
------------------------
* **SoRL Module:** Utilizes an Autoencoder to reduce dimension $d$ to $c$, creating latent representation $Z$[cite: 144]. A parameter-shared GNN then encodes $Z$ alongside view-specific adjacency matrices and a consensus graph $S$[cite: 189, 191, 193].
* **MoDF Module:** * **Global Attention Fusion Network (GAFN):** Squeeze-and-excitation style channel attention to learn the contribution of each omics modality, applying a residual connection[cite: 224, 225, 242].
  * **Local Attention Fusion Network (LAFN):** Multi-head self-attention applied across the scaled omics embeddings for each individual patient to capture shared and complementary local information[cite: 250, 269].

Citation
--------
* Li, Y., Wang, Y., Liang, T., Li, Y., & Du, W. (2025). *A multi-omics integration framework using multi-label guided learning and multi-scale fusion*. Briefings in Bioinformatics, 26(5), bbaf493. [cite: 2, 4, 5]

More in Future...
-----------------
* *(Placeholder)* Development of a wrapper script implementing Permutation Importance for native mmMOI biomarker extraction.
* *(Placeholder)* Adapting the LAFN multi-head attention module to natively output attention scores mapped to the original feature space.
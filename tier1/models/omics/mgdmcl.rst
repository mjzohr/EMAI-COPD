=============================================================================================================
Multi-Omics Integration Models: MGDMCL (Masked Graph Dynamic & Multi-Granularity Contrastive Learning)
=============================================================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
MGDMCL is an advanced graph-based deep learning framework designed for integrative multi-omics data analysis[cite: 2538]. It addresses two major limitations of prior Graph Convolutional Network (GCN) methods: the reliance on fixed, static sample similarity graphs (SSGs) and the insufficient exploration of interrelations between different omics features[cite: 2537]. The framework operates through a multi-step pipeline:

1. **Omics-specific Masked Graph Dynamic Learning (MGDL):** Dynamically learns and adjusts a highly reliable Sample Similarity Graph (SSG) for each omics type using feature selection and masked graph reconstruction[cite: 2539].
2. **Layer-specific Feature Aggregation:** Concatenates multi-layer GCN features and applies Multi-Granularity Feature Contrastive Learning (MGFCL)[cite: 2540].
3. **Layer-specific Confidence Learning:** Utilizes True Class Probability (TCP) to regulate the classification confidence of the consensus representations[cite: 2541].

Model Type
~~~~~~~~~~
Supervised Graph Neural Network (GNN) with Masked Autoencoding and Contrastive Learning for biomedical classification[cite: 2533, 2538].

Usage
-----

Direct Use
~~~~~~~~~~
* Biomedical classification tasks, including cancer subtyping (e.g., BRCA, KIPAN), tumor grading (LGG), and survival prediction (LUSC)[cite: 2861, 2863, 2865, 2866].
* Disease diagnosis distinguishing affected patients from normal controls (e.g., Alzheimer's disease via ROSMAP)[cite: 2862].
* Extracting highly refined, adaptive patient-similarity networks based on multi-omics profiles[cite: 2674].

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* **Incomplete Datasets:** The current model cannot inherently handle missing modal data or extract meaningful features from samples with missing labels[cite: 3369].
* **Unstructured Modalities:** Lacks the capability to incorporate non-tabular data modalities, such as whole-slide medical imaging or raw clinical text[cite: 3374].
* **High-Order Relationships:** Cannot capture complex, multi-way relationships between samples, as its standard graph edges are restricted to pairwise binary relationships[cite: 3366].

Supported Modalities
--------------------
* **Structured Tabular Multi-Omics Data:** Evaluated on combinations of:
  * mRNA expression [cite: 2681]
  * miRNA expression [cite: 2681]
  * DNA methylation [cite: 2681]

Interpretability & Biomarker Discovery
--------------------------------------
* **Internal Mechanism:** The architecture contains a ``GateSelect`` module designed to learn dynamic informativeness scores for features, producing per-feature gating scores (``att_score``) located in ``MGDMCL/model/common_layer.py``[cite: 2682].
* **Implementation Limitation:** **Lacks out-of-the-box feature importance export.** The current training and evaluation pathways do not expose or export these ``att_score`` values as a ranked "feature importance" list for biomarker discovery.
* **Required Workarounds:** To utilize MGDMCL for biomarker ranking, users must manually integrate an attribution method into the pipeline:
  * **Permutation Importance:** Randomly shuffling features and observing the drop in classification performance.
  * **Integrated Gradients (e.g., via Captum):** For gradient-based feature attribution.
  * **Gradient $\times$ Input:** To measure feature contribution relative to the model's output.
  * *(Note: These methods must be aggregated per-feature across all samples and folds to ensure statistical significance).*

Missing Value Handling
----------------------
* **Pre-imputation Strictly Required:** MGDMCL explicitly assumes the availability of complete multi-omics data matrices[cite: 3368, 3369]. The model does not feature an internal mechanism for imputing missing values (like `NaN` or `Null`). A robust imputation pipeline (e.g., k-NN, mean, or median) must be run prior to constructing the input matrices.

Bias, Risks, and Limitations
----------------------------
* **Label Dependency:** The Coarse-grained Contrastive Learning (CgCL) module heavily relies on true label information to define positive and negative sample pairs[cite: 2808]. It will struggle in highly unsupervised or sparsely labeled cohorts.
* **Computational Complexity:** The dynamic, iterative updating of the Sample Similarity Graph (SSG) alongside multi-layer contrastive learning results in a higher computational and memory burden compared to static GCN baselines[cite: 2946].
* **Biomarker Export Barrier:** The lack of a readily available biomarker export script limits its immediate utility for clinical researchers seeking to identify actionable genomic targets.

Training Details
----------------
The training process jointly optimizes several specialized loss functions[cite: 2844]:

* **Adaptive Feature Selection:** Applies $l_1$-norm regularization to the gating network scores to filter informative features[cite: 2689, 2690].
* **Masked Graph Reconstruction (MGRC):** Randomly masks feature representations of samples (sharing the same label) and trains a GCN decoder to reconstruct them using unmasked neighbors[cite: 2768, 2769, 2743]. This iterative reconstruction dynamically refines the SSG structure[cite: 2748].
* **Multi-Granularity Contrastive Learning (MGFCL):**
  * *Fine-grained (FgCL):* Aligns the feature representations of different omics for the *same sample* to maximize mutual information[cite: 2806, 2810].
  * *Coarse-grained (CgCL):* Attracts samples with the *same label* (positive pairs) and repels samples with *different labels* (negative pairs) to address positive-negative sample imbalance[cite: 2808, 2809, 2818].

Evaluation
----------
* **Metrics:** Evaluated using AUROC, Accuracy (ACC), F1 score (binary), and macro/weighted-F1 for multi-class tasks[cite: 2882, 2883].
* **Baselines:** Demonstrated statistically significant improvements over 12 representative baselines, including MOGONET, MOGLAM, MoGCN, and MCRGCN across all five benchmark datasets[cite: 2868, 2894, 2895].

Technical Specifications
------------------------
* **Graph Encoder/Decoder:** Utilizes standard Graph Convolutional Networks (GCN)[cite: 2732, 2743].
* **Contrastive Optimization:** Employs a scaled cosine error loss for fine-grained alignment and a temperature-scaled exponential dot product for coarse-grained contrastive pairs[cite: 2814, 2822].
* **Confidence Learning Module:** Approximates True Class Probability (TCP) using an auxiliary confidence neural network trained via $l_2$ loss to dynamically weight layer-specific consensus features[cite: 2828, 2829].

Citation
--------
* Chen, W., & Qiu, H. (2025). *MGDMCL: A multi-omics integration framework based on masked graph dynamic learning and multi-granularity feature contrastive learning for biomedical classification*. Computer Methods and Programs in Biomedicine, 271, 109024[cite: 2523, 2524].

More in Future...
-----------------
* *(Placeholder)* Development of a hypergraph structure to capture complex, high-order, multi-way relationships between samples beyond simple pairwise edges[cite: 3366, 3367].
* *(Placeholder)* Integration of uncertainty-induced modules to natively handle incomplete multi-omics data and missing labels[cite: 3370].
* *(Placeholder)* Implementation of an automated script to extract and rank ``att_score`` values from the ``GateSelect`` module for immediate biomarker discovery.
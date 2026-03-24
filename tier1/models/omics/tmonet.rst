==================================================================================================
Multi-Omics Integration Models: TMO-Net (Tumor Multi-Omics Pre-trained Network)
==================================================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
TMO-Net is a pre-trained tumor multi-omics deep learning model designed to learn robust representations across diverse pan-cancer datasets. It addresses the challenge of heterogeneous data integration by utilizing a specialized "Cross Fusion Module" alongside self-modal and cross-modal Variational Autoencoders (VAEs). This architecture facilitates cross-omics interactions, enables joint representation learning, and uniquely infers incomplete (missing) omics data to empower downstream oncology tasks through transfer learning.

Model Type
~~~~~~~~~~
Pre-trained Multi-modal Variational Autoencoder (VAE) and Cross-Fusion deep learning framework for multi-task oncology prediction.

Usage
-----

Direct Use
~~~~~~~~~~
* Pan-cancer subtype classification and patient survival prediction.
* Downstream oncology tasks, such as drug response prediction, utilizing transfer learning (fine-tuning) from the pre-trained foundation.
* Representation learning for tumor samples using incomplete or partially missing multi-omics datasets.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Non-oncology disease modeling, where the pre-trained pan-cancer latent space (derived from TCGA) may not transfer effectively.
* Raw unstructured clinical data (e.g., raw medical text, whole-slide histology images) without prior extraction into structured omics or clinical features.

Supported Modalities
--------------------
* **Structured Multi-Omics Data:** The model is pre-trained on and natively supports four primary omics layers:
  * mRNA expression
  * DNA methylation
  * Copy Number Variation (CNV)
  * Gene mutation

Interpretability & Biomarker Discovery
--------------------------------------
* **Paper Claims vs. Codebase Reality:** While the original publication highlights biological interpretation via global gene attributions using Integrated Gradients to characterize pathway enrichments, **the provided codebase lacks these utilities.**
* **Implementation Limitation:** There are **no out-of-the-box feature-importance or biomarker ranking utilities** found in the repository. It lacks an attribution or export pipeline entirely.
* **Required Workarounds:** To extract feature importance rankings for actionable biomarker discovery, practitioners must manually integrate an attribution method into the PyTorch pipeline. Recommended approaches include:
  * **Integrated Gradients (e.g., via Captum):** For gradient-based attribution mapped back to the input space (as utilized in the original paper).
  * **Permutation Importance:** Randomly shuffling input features per omics layer to observe the performance impact on the fine-tuned model.
  * **Gradient $\times$ Input:** To measure the feature's contribution relative to the model's output.
  * *(Note: These methods must be aggregated per-feature across all samples and cross-validation folds to ensure statistical significance).*

Missing Value Handling
----------------------
* **Native Missing Modality Inference:** Unlike many multi-omics models that require strict pre-imputation or force the dropping of samples with missing modalities, TMO-Net natively accommodates incomplete multi-omics datasets.
* **Mechanism:** The "Cross Fusion Module" is explicitly devised to align latent embeddings from different modalities. It performs cross-modal learning to computationally infer missing modalities from the available data prior to fusing them into a complete multi-omics embedding.

Bias, Risks, and Limitations
----------------------------
* **Biomarker Export Barrier:** The complete absence of feature-importance export scripts in the open-source repository creates a high barrier to entry for clinical researchers needing immediate, interpretable biomarker lists.
* **Pre-training Dependency:** The model's success heavily relies on the distributions present in the pan-cancer pre-training dataset. It may exhibit bias or reduced performance when applied to rare cancers or demographic cohorts severely underrepresented in the pre-training corpus.
* **Computational Overhead:** The dual-phase pipeline (pre-training VAEs followed by multi-task fine-tuning) requires more computational resources and complex hyperparameter tuning compared to direct, single-task ensemble methods.

Training Details
----------------
Implemented in PyTorch, the repository structure provides a unified script for both pre-training and downstream fine-tuning.

**1. Data Preparation:**
Processed multi-omics profiles (available via Zenodo) must be downloaded and placed in the target directory before initialization.

**2. Execution Pipeline:**
The file ``train/train_tcga_pancancer_multitask.py`` contains the training functions for pre-training, pan-cancer classification, and pan-cancer survival prediction using default hyperparameters.

.. code-block:: python

    # Example execution flows are embedded within the main training script
    # to handle both pre-training and fine-tuning phases:
    python train/train_tcga_pancancer_multitask.py

Evaluation
----------
* **Tasks:** Evaluated extensively on pan-cancer representation learning (measured via t-SNE clustering and Silhouette scores), classification accuracy, and survival prediction (C-index).
* **Baselines:** Demonstrated enhanced multi-omics sample representation compared to standard single-omics inputs and competing baseline integration methods, particularly excelling in scenarios with missing patient modalities.

Technical Specifications
------------------------
* **Architecture (``model/TMO_Net_model.py``):**
  * **Self-Modal VAEs:** Compress individual omics layers into modality-specific latent spaces.
  * **Cross-Modal VAEs & Cross Fusion Module:** Align latent embeddings across modalities and infer representations for missing data to create a fused, unified multi-omics embedding vector.
* **Loss Functions (``util/loss_function.py``):** Implements custom multi-task loss functions balancing reconstruction loss (for the VAEs) and predictive loss (e.g., Cross-Entropy for classification, Cox Partial Likelihood for survival).

Citation
--------
* Wang, F.-A., Zhuang, Z., Gao, F., He, R., et al. (2024). *TMO-Net: an explainable pretrained multi-omics model for multi-task learning in oncology*. Genome Biology, 25(1).

More in Future...
-----------------
* *(Placeholder)* Implementation of a native Captum wrapper to automatically export Integrated Gradients scores for rapid pan-cancer biomarker discovery.
* *(Placeholder)* Extending the Cross Fusion Module to support spatial transcriptomics and single-cell RNA-seq (scRNA-seq) modalities.
* *(Placeholder)* Benchmarking TMO-Net's missing modality inference against state-of-the-art statistical imputation algorithms (e.g., missForest, GAIN).
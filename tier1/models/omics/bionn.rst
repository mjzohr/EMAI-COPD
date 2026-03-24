================================================================================================
Multi-Omics Integration Models: BioNeuralNet (Graph Neural Network based Multi-Omics Tool)
================================================================================================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
BioNeuralNet is a highly flexible, modular Python framework tailored for end-to-end network-based multi-omics data analysis. Unlike rigid, task-specific models, it provides a comprehensive suite of tools to convert complex molecular interactions into versatile low-dimensional embeddings using various Graph Neural Networks (GNNs). The framework supports the entire analytical pipeline: from raw data ingestion and imputation to multi-strategy network construction, representation learning, and downstream predictive tasks.

Model Type
~~~~~~~~~~
Modular supervised and unsupervised Graph Neural Network (GNN) framework for multi-omics representation learning, clustering, and phenotype prediction.

Usage
-----

Direct Use
~~~~~~~~~~
* End-to-end disease and phenotype prediction using the built-in DPMON (Disease Prediction using Multi-Omics Networks) module.
* Unsupervised subject representation, stratification, and clustering using GNN-derived latent spaces.
* Biological module discovery via subgraph and community detection algorithms (e.g., Louvain, PageRank).
* Extensive network topology analysis and multi-omics visualization.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Analyzing raw, unstructured data formats (e.g., raw sequence reads, whole-slide images) directly.
* Workflows requiring fine-grained, node-level gradient attribution scores natively (noted as an active area of research for this framework).

Supported Modalities
--------------------
* **Structured Tabular Multi-Omics Data:** Extensively tested on combinations of:
  * mRNA expression
  * miRNA expression
  * DNA methylation
* **Clinical/Phenotype Data:** Can directly integrate clinical covariates (e.g., tumor stage, age) into the downstream DPMON predictive modeling phase.

Interpretability & Biomarker Discovery
--------------------------------------
* **Network-Level Interpretability:** BioNeuralNet emphasizes system-level biological interpretability rather than simple tabular feature ranking. It identifies "hub omics" (features with high degree centrality) and biologically meaningful subgraphs/modules of interacting genes and proteins.
* **Implementation Limitation:** The documentation explicitly states that while it excels at network-level interpretability, *fine-grained node-level explanations (e.g., exact predictive importance weights per feature per sample) remain an active research area*. It lacks an automated ablation or gradient-based feature importance export script like MOGONET.
* **Required Workarounds:** Biomarker discovery is primarily achieved by extracting the network's top hub features (using `bioneuralnet.utils.graph_analysis`) or employing traditional feature selection (ANOVA, Random Forest) provided in the pre-processing utility suite prior to graph construction. 

Missing Value Handling
----------------------
* **Native Imputation Utilities:** Unlike many GNN frameworks that fail on incomplete matrices, BioNeuralNet includes built-in functions to handle missing omics data. Users can apply utilities such as ``impute_omics`` and ``impute_omics_knn`` directly from the package to resolve incomplete multi-omics matrices before network construction.

Bias, Risks, and Limitations
----------------------------
* **Topology Sensitivity:** The model's downstream predictive performance is highly sensitive to the initial network construction strategy. Users must carefully benchmark different network types (e.g., Correlation vs. Cosine Similarity vs. Gaussian k-NN) to find the optimal biological representation.
* **Feature Selection Dependency:** Because massive omics networks can cause memory bottlenecks, aggressive feature selection (e.g., top 6,000 features via variance or ANOVA F-test) is often required, potentially discarding subtle biological signals.
* **External Tool Dependencies:** Advanced phenotype-driven network construction (using SmCCNet) requires a working R environment bridged to Python.

Training Details
----------------
Implemented via PyTorch and PyTorch Geometric, the repository provides a highly customizable pipeline. 

**1. Installation:**

.. code-block:: bash

    pip install bioneuralnet torch torch_geometric

**2. Example Workflow (Network Construction & Prediction):**

.. code-block:: python

    import pandas as pd
    from bioneuralnet.utils import gen_similarity_graph
    from bioneuralnet.downstream_task import DPMON

    # 1. Network Construction (Cosine k-NN)
    similarity_10 = gen_similarity_graph(omics_data, k=10, metric="cosine")

    # 2. Disease Prediction using DPMON
    dpmon = DPMON(
        adjacency_matrix=similarity_10,
        omics_list=[omics_genes, omics_proteins],
        phenotype_data=phenotype,
        clinical_data=clinical,
        model="GCN",       # Supports GCN, GAT, GraphSAGE, GIN
        repeat_num=5,
        tune=True,         # Built-in Ray Tune hyperparameter optimization
        gpu=True
    )
    predictions, avg_accuracy = dpmon.run()

Evaluation
----------
* **Metrics:** Accuracy, F1-weighted, and F1-macro.
* **Baselines:** In the TCGA-BRCA case study, BioNeuralNet's end-to-end pipeline achieved a state-of-the-art accuracy of ~0.951, significantly outperforming Random Forest (0.789), MOGONET (0.829), and SUPREME (0.840).

Technical Specifications
------------------------
* **GNN Architectures Supported:** Graph Convolutional Networks (GCN), Graph Attention Networks (GAT), GraphSAGE (for inductive learning), and Graph Isomorphism Networks (GIN).
* **Network Construction Methods:**
  * Similarity: k-NN (Cosine/Euclidean), RBF, mutual information.
  * Correlation: Pearson, Spearman (with optional soft-thresholding).
  * Phenotype-aware: SmCCNet integration.
  * Gaussian k-NN.
* **Output:** Results and predictions are strictly formatted as Pandas DataFrames for seamless interoperability with standard Python data science ecosystems.

Citation
--------
* Ramos, V., Hussein, S., Abdel-Hafiz, M., Sarkar, A., Liu, W., Kechris, K. J., Bowler, R. P., Lange, L., & Banaei-Kashani, F. (2025). *BioNeuralNet: A Graph Neural Network based Multi-Omics Network Data Analysis Tool*. arXiv preprint arXiv:2507.20440.

More in Future...
-----------------
* *(Placeholder)* Development of native node-level explainability modules for precise patient-specific biomarker attribution.
* *(Placeholder)* Extended support for heterogeneous graph architectures (e.g., explicitly separating mRNA nodes from DNA methylation nodes with distinct edge types).
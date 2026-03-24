Modern Deep Models
==================

Model Details
-------------

Model Description
~~~~~~~~~~~~~~~~~
This category encompasses recent, highly competitive deep learning architectures designed specifically to close the persistent performance gap between neural networks and Gradient-Boosted Decision Trees (GBDTs) on tabular data:

* **RealMLP (2024):** A highly optimized Multilayer Perceptron (MLP) enhanced with modern architectural tricks, superior preprocessing (e.g., periodic activations), and robust, meta-learned default parameters.
* **Trompt (2023):** "Tabular Prompt", a novel architecture inspired by prompt learning in language models. It separates the learning of intrinsic table information from varied sample information using iterative "Trompt Cells".
* **ExcelFormer (2023/2024):** A Transformer variant equipped with a semi-permeable attention module to regulate feature interactions and specialized tabular data augmentation techniques, aiming to surpass heavily tuned GBDTs.

Model Type
~~~~~~~~~~
Advanced supervised neural architectures for tabular representation learning, classification, and regression.

Usage
-----

Direct Use
~~~~~~~~~~
* Establishing state-of-the-art deep learning baselines for tabular data on medium-to-large datasets.
* Benchmarking against heavily tuned tree ensembles (XGBoost, CatBoost) and earlier transformers (FT-Transformer).
* Exploring complex, non-linear feature interaction learning in scenarios where traditional GBDTs plateau.

Out-of-Scope Use
~~~~~~~~~~~~~~~~
* Extremely small datasets where these highly parameterized models are prone to severe overfitting.
* Low-resource environments or strict CPU-bound pipelines requiring ultra-fast training and inference times.

Supported Modalities
--------------------
* **Structured Tabular Data:** The primary and exclusive modality.
* **Categorical & Numerical Features:** Handled via distinct embedding strategies prior to the main network. RealMLP utilizes techniques like Piecewise Linear Representation (PLR) embeddings, while ExcelFormer often converts categorical variables via target statistics before applying numerical sorting.

Interpretability
----------------
* **Trompt:** Offers a degree of structural interpretability. The prompt vectors generated at each Trompt Cell can theoretically be analyzed to understand sample-specific feature importance across different layers.
* **RealMLP & ExcelFormer:** Generally operate as black boxes. While ExcelFormer's attention weights can be inspected, both models typically require post-hoc explainability tools (like SHAP or LIME) for rigorous, user-friendly feature attribution.

Missing Value Handling
----------------------
* **Pre-imputation Required:** Unlike foundation models (TabPFN), these architectures typically require a rigorous preprocessing pipeline to handle ``NaN`` or ``Null`` values before embedding. 
* **Mechanism:** Missing numericals must be imputed (e.g., via mean or iterative imputation), and missing categoricals must be explicitly encoded as a distinct ``<MISSING>`` category to allow the network to learn embeddings for data absence.

Bias, Risks, and Limitations
----------------------------
* **Compute Requirements:** Training ExcelFormer or Trompt requires GPU acceleration and significantly more memory than GBDTs, which often train efficiently on CPUs.
* **Ecosystem Maturity:** While implementations exist, the deployment ecosystem and community support are less mature than the ubiquitous scikit-learn or XGBoost pipelines.
* **Performance Consistency:** Despite advancements, they may still not consistently outperform extremely well-tuned GBDTs across *all* heterogeneous datasets, particularly uncleaned or highly skewed data.

Training Details
----------------
* **Optimization & Initialization:** These models benefit heavily from modern optimization. ExcelFormer, for instance, uses an interaction-attenuation initialization strategy (starting with minimal parameter values to gradually learn interactions).
* **Data Augmentation:** ExcelFormer introduces specialized tabular Mixup variants (Hid-Mix, Feat-Mix) to mitigate the conflicts between standard computer vision Mixup and tabular data irregularity.
* **Hyperparameter Tuning:** While Trompt and ExcelFormer often require careful tuning, **RealMLP** explicitly addresses the HPO burden by providing strong meta-learned default parameters that rival extensively tuned models.

Evaluation
----------
* **Metrics:** AUROC, Accuracy, Macro-F1 (Classification); RMSE, R2 (Regression).
* **Baselines:** Evaluated against both heavily tuned GBDTs (XGBoost, CatBoost, LightGBM) and earlier deep tabular models (FT-Transformer, ResNet).

Technical Specifications
------------------------
* **RealMLP:** Standard MLP backbone improved with modern regularization, bias initialization, and numeric embeddings.
* **Trompt:** Multi-layer architecture utilizing Trompt Cells that iteratively refine feature representations using learnable prompt embeddings.
* **ExcelFormer:** Alternates between feature interaction modules (semi-permeable attention to break rotational invariance) and feature embedding updates.

Software
~~~~~~~~
Implemented via:

* **PyTorch**
* **PyTorch Frame:** (https://github.com/pyg-team/pytorch-frame) (Native implementations for Trompt and ExcelFormer).
* **PyTabKit:** (https://github.com/dholzmueller/pytabkit) (Official interface for RealMLP).

Citation
--------
* Holzmüller et al. (2024). *Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data.* (RealMLP)
* Chen et al. (2023). *Trompt: Towards a Better Deep Neural Network for Tabular Data.* (ICML)
* Chen et al. (2023/2024). *ExcelFormer: A Neural Network Surpassing GBDTs on Tabular Data.*

More in Future...
-----------------
* *(Placeholder)* Best practices for distilling heavy Trompt/ExcelFormer models into lightweight deployable artifacts.
* *(Placeholder)* Expanding automated hyperparameter optimization (HPO) profiles for semi-permeable attention modules.
* *(Placeholder)* Comparative scaling laws of tabular transformers vs. tabular MLPs on datasets exceeding 10 million rows.
Dataset Catalog
===============

Summary
-------

Tier 1 data is organized around unimodal inputs consumed directly by baseline
pipelines.

Modalities at a glance:

- Clinical research data: structured covariates
- CT: engineered/derived imaging summaries
- SDOH: socioeconomic and contextual covariates
- Wearables: derived features from Fitbit/Apple streams
- Omics: bulk omics views for dedicated multi-omics workflows

Execution Notes
---------------

- Tabular-ready variants are managed through the dataset registry
- Omics variants can require model-specific formatting

Expected data preparation pattern:

.. code-block:: text

    COPDGene/
       raw/
       processed/
          ml_ready/
             train_val_test/
             train_unsupervised/
       formatted/
          model_specific/

Navigation
----------

.. toctree::
   :maxdepth: 2

   omics/index
   clinical
   ct
   sdoh
   wearable
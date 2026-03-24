General Models
==============

Summary
-------

This section organizes Tier 1 baseline models for structured prediction.
The models are grouped by methodological family, from classical neural baselines
to attention-based architectures, modern deep tabular models, and foundation models.

Execution Notes
---------------

These models are typically executed through the unified tabular benchmark runner
with registry-defined dataset variants and shared defaults (for example k-fold,
seed, and validation split).

Navigation
----------

.. toctree::
   :maxdepth: 1

   classical_nn
   attention_models
   modern_dl
   tree_based
   foundation_models
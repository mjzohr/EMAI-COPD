Omics Integration Models
========================

Summary
-------

This section covers dedicated multi-omics architectures (for example MOGONET,
MGDMCL, mmMOI, and TMO-Net) that use custom omics-formatted inputs.

Execution Notes
---------------

In practice, these runs are often orchestrated separately from the unified
tabular benchmark runner (for example via ``run_all.sh``), and outputs are logged
under ``results/`` per run/fold.

Navigation
----------

.. toctree::
   :maxdepth: 1

   bionn
   mgdmcl
   mmmoi
   mogonet
   tmonet
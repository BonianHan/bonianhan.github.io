---
title: "INST-Align: Implicit Neural Alignment for Spatial Transcriptomics via Canonical Expression Fields"
collection: publications
permalink: /publication/25-miccai
date: 2026-02-26
excerpt: "Overview of the INST-Align pipeline for joint spatial alignment and expression integration of spatial transcriptomics data.<br/><img src='/images/miccai.png'>"
venue: 'MICCAI 2026 (Submitted)'
paperurl: '/files/miccai.pdf'
citation: ""
---

Spatial transcriptomics (ST) measures mRNA expression while preserving spatial organization, but multi-slice analysis faces two coupled difficulties: large non-rigid deformations across slices and inter-slice batch effects when alignment and integration are treated independently. We present INST-Align, an unsupervised pairwise framework that couples a coordinate-based deformation network with a shared Canonical Expression Field, an implicit neural representation mapping spatial coordinates to expression embeddings, for joint alignment and reconstruction. A two-phase training strategy first establishes a stable canonical embedding space and then jointly optimizes deformation and spatial-feature matching, enabling mutually constrained alignment and representation learning. Across nine datasets, INST-Align achieves state-of-the-art mean OT Accuracy (0.702), NN Accuracy (0.719), and Chamfer distance, with Chamfer reductions of up to 94.9% on large-deformation sections relative to the strongest baseline.

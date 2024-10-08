---
layout: post
title: End-to-end learning geometries for graphs, dynamical systems, and regression
date: 2024-01-01
powerpoint: 2024.e2e-geometries.pptx
pdf: 2024.e2e-geometries.pdf
abstract: >-
    Every machine learning setting has an underlying geometry where
    the data is represented and the predictions are performed in.
    While defaulting the geometry to a Euclidean or known manifold is
    capable of building powerful models, /learning/ a non-trivial geometry
    from data is useful for improving the overall performance and estimating
    unobserved structures.
    This talk focuses on learning geometries for:
    1) *graph embeddings*, where the geometry of the embedding
    (e.g., Euclidean, spherical, or hyperbolic) heavily influences the
    accuracy and distortion of the embedding depending on the graph's structure;
    2) *dynamical systems*, where the geometry of the state space can uncover
    unobserved properties of the underlying systems, e.g.,
    geographic information such as obstacles or terrains; and
    3) *regression*, where the geometry of the prediction space
    influences where the model should be accurate or inaccurate
    for some downstream task.

    We will focus on *latent* geometries in these settings that are
    not directly observable from the data, i.e., the geometry cannot
    be estimated as a submanifold of the Euclidean space the data
    is observed in.
    Instead in these settings the geometry can be shaped via a downstream
    signal that propagates through differentiable operations such as
    the geodesic distance, and log/exp maps on Riemannian manifolds.
    The talk covers the foundational tools here on making operations
    differentiable (in general via the envelope and implicit function theorems,
    but potentially simpler when closed-form operations are available),
    and demonstrates where the end-to-end learned geometry is effective.
---

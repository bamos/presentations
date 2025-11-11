---
layout: post
title: Transport and flows between distributions over distributions
date: 2024-11-05
powerpoint: 2024.transport-between-distributions-over-distributions.pptx
pdf: 2024.transport-between-distributions-over-distributions.pdf
abstract: >-
  Generative models based on transport, flows, and diffusion are
  widely deployed and usually connect a single source distribution to
  a single target distribution in Euclidean space. This talk covers
  the generalization when there are multiple source or target
  distributions, i.e., when the distributions are themselves over
  distributions. Transporting between many distributions arises in
  many applications, such as 1) text-to-image generation (each text
  prompt results in samples from a distribution over images), 2) image
  editing (between many pairs of images), 3) scheduling and
  supply-demand allocations (between many initial conditions) 4) point
  cloud generation (each point cloud is an empirical distribution),
  and 5) cellular transport (many pairs of untreated to treated
  populations). In this space, the talk will cover
  [Meta Optimal Transport](https://arxiv.org/abs/2206.05262) and
  [Meta Flow Matching](https://arxiv.org/abs/2408.14608) when the
  pairings or couplings between the distributions are known and
  otherwise [Wasserstein Flow Matching](https://arxiv.org/abs/2411.00698)
  over the Wasserstein manifold (using Riemannian Flow Matching) when there
  is no coupling information.
---

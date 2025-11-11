---
layout: post
title: Amortized optimization for OT and LLMs
date: 2024-07-01
powerpoint: 2024.amortized-optimization-for-OT-and-LLMs.pdf
pdf: 2024.amortized-optimization-for-OT-and-LLMs.pdf
abstract: >-
  Amortized optimization methods provide fast solvers by predicting
  approximate solutions to optimization problems. This talk covers two
  recent advancements using amortization to significantly speed up the
  solvers of non-trivial optimization problems arising in the fields of
  optimal transport (OT) and large language model (LLM)
  attacks. Computational optimal transport problems may involve solving
  three nested optimization problems, each of which amortization can
  help with: 1) the solution map from the measures to the primal/dual OT
  solution ([Meta OT](https://arxiv.org/abs/2206.05262)), 2) the
  computation of the c-transform or Fenchel conjugate
  ([amortized conjugates](https://arxiv.org/abs/2210.12153)), and
  3) the computation of geodesics and Lagrangian (minimum-action)
  paths/costs ([Lagrangian OT](https://openreview.net/pdf?id=myb0FKB8C9)).
  Adding amortization to
  the standard solvers in these OT settings significantly improves the
  runtime and deployment time of the methods. These faster amortized
  solutions to the Fenchel conjugate and geodesic/Lagrangian paths are
  of potential more general interest in other settings bottlenecked by
  numerical solutions to them. Beyond these optimal transport
  applications, we will also discuss the prompt optimization problems
  arising in adversarial attacks on LLMs
  ([AdvPrompter](https://arxiv.org/abs/2404.16873)).
  Here, amortization enables us to
  attain state-of-the-art results on the standard AdvBench dataset, that
  also transfer to closed-source black-box LLM APIs. The fast amortized
  predictions then enable us to generate a synthetic dataset of
  adversarial examples which an LLM can be fine-tuned on to make it more
  robust against jailbreaking attacks while maintaining performance.
---

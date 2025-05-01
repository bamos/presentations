---
layout: post
title: On amortized optimization for RL, Bayesian optimization, and biology
date: 2025-05-01
powerpoint: 2025.amortization-rl-bio.pptx
pdf: 2025.amortization-rl-bio.ppdf
abstract: >-
  [Amortized optimization](https://arxiv.org/abs/2202.00665) is the use of learning to augment and
  accelerate optimization solvers by leveraging the knowledge and
  predictability of past solutions and similarity between problem
  instances. It is widely-deployed across fields such as reinforcement
  learning, variational inference, and meta-learning and improves upon
  classical solvers by many orders of magnitude. The first part of this
  talk will briefly overview the basic foundations of amortization,
  focusing on policy learning in RL and control as the main
  application. At a general level, classical optimization solvers are
  akin to Kahneman's system-2 style of slow thinking by solving each
  problem from scratch every time, and the foundations here will show
  how to think of amortization as a system-1 style of fast thinking
  learned and distilled by past experiences. With these foundations in
  hand, we will turn to how amortization can improve solvers for
  acquisition functions in Bayesian optimization settings, e.g., as in
  the paper Learning to [Learn without Gradient Descent by Gradient
  Descent](https://arxiv.org/abs/1611.03824).
  Then, we will conclude with a discussion on what amortization
  would bring to the AI and computational biology space when
  repeatedly-solved optimization problems arise, such as in
  [Meta Optimal Transport](https://arxiv.org/abs/2206.05262) and
  [Meta Flow Matching](https://arxiv.org/abs/2408.14608)
  Flow Matching and Meta Flow Matching for modeling cellular dynamics
  with flows conditional on patient and drug treatment information.
---

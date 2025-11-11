---
layout: post
title: "On meta prompt optimization and coding agents"
date: 2025-12-07
powerpoint: 2025.advprompter-algotune.pptx
pdf: 2025.advprompter-algotune.pdf
abstract: >-
  Language models (LMs) encode vast amounts of human knowledge in a
  queryable form and are now widely deployed across domains that
  previously could not directly benefit from language.
  Yet major challenges remain: how to effectively extract information
  (e.g., where and how to prompt the model), and how to ensure alignment with
  human values and preferences (e.g., personalization, safety, undesirable behaviors).
  A path forward to solving these is to quantify the
  objective, perform (test-time) optimization over the
  prompt space to improve that objective, and ultimately
  integrate the improvement back into the base model.
  This talk explores this in two domains:


  1) Prompt optimization and adversarial attacks---in
  [AdvPrompter](https://arxiv.org/abs/2404.16873) (ICML 2025) we
  learn a *meta-prompting* model that rapidly predicts the optimal
  adversarial suffix for jailbreaking an LM, and in
  [AdvPrefix](https://arxiv.org/abs/2412.10321) (NeurIPS 2025),
  we show variants on the jailbreaking optimization
  problem objective can result in significantly improved performance, and

  2) Numerical code synthesis with agents---in
  [AlgoTune](https://arxiv.org/abs/2507.15887) (NeurIPS D&B 2025),
  we propose a benchmark suite of 154 numerical coding tasks
  along with a baseline code agent to solve it.
  The coding agent iteratively optimizes the code (and prompts)
  for the task's runtime as the objective.


  We'll draw connections between these two seemingly separate settings
  and show how meta-learning and agentic test-time computations squeeze
  the most out of the base model, advancing both capabilities and alignment.
---

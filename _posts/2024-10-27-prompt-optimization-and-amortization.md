---
layout: post
title: On LLM prompt optimization and amortization
date: 2024-10-27
powerpoint: 2024.prompt-optimization-and-amortization.pptx
pdf: 2024.prompt-optimization-and-amortization.pptx
abstract: >-
  Prompting LLMs is a challenging art where different ways of expressing
  the same idea can lead to drastically different responses. Not
  prompting in the right way gives suboptimal performance and has led to
  the budding space of prompt engineering and optimization techniques. A
  standard example here is that appending the string "let's think step
  by step" to the prompt may significantly improve the quality on
  few-shot classification tasks. In this session, we'll first cover how
  prompt optimization can be expressed as a combinatorial optimization
  problem (over the token sequence space) and overview the standard
  methods here. (A warning for this audience (Dagstuhl seminar on
  ML and combinatorial optimization): standard combinatorial
  solvers or approaches are often not used, and instead approaches are
  specialized to LLMs.) Beyond this, prompt optimization problems are
  often not solved a single time in isolation, but are repeatedly solved
  for every new task or piece of information we want to extract from the
  language model. So, we'll conclude with an overview of learned
  optimization, or amortization, to share the information between the
  repeatedly-solved optimization problems.
---

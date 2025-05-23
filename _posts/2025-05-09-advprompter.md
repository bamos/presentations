---
layout: post
title: "AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs"
date: 2025-05-09
powerpoint: 2025.advprompter.pptx
pdf: 2025.advprompter.pdf
abstract: >-
  While recently Large Language Models (LLMs) have achieved remarkable
  successes, they are vulnerable to certain jailbreaking attacks that
  lead to generation of inappropriate or harmful content. Manual
  red-teaming requires finding adversarial prompts that cause such
  jailbreaking, e.g. by appending a suffix to a given instruction, which
  is inefficient and time-consuming. On the other hand, automatic
  adversarial prompt generation often leads to semantically meaningless
  attacks that can easily be detected by perplexity-based filters, may
  require gradient information from the TargetLLM, or do not scale well
  due to time-consuming discrete optimization processes over the token
  space. In this paper, we present a novel method that uses another LLM,
  called the AdvPrompter, to generate human-readable adversarial prompts
  in seconds, ∼800x faster than existing optimization-based
  approaches. We train the AdvPrompter using a novel algorithm that does
  not require access to the gradients of the TargetLLM. This process
  alternates between two steps: (1) generating high-quality target
  adversarial suffixes by optimizing the AdvPrompter predictions, and
  (2) low-rank fine-tuning of the AdvPrompter with the generated
  adversarial suffixes. The trained AdvPrompter generates suffixes that
  veil the input instruction without changing its meaning, such that the
  TargetLLM is lured to give a harmful response. Experimental results on
  popular open source TargetLLMs show state-of-the-art results on the
  AdvBench dataset, that also transfer to closed-source black-box LLM
  APIs. Further, we demonstrate that by fine-tuning on a synthetic
  dataset generated by AdvPrompter, LLMs can be made more robust against
  jailbreaking attacks while maintaining performance, i.e. high MMLU scores.
---

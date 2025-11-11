---
layout: post
title: Amortized optimization and AI
date: 2024-07-01
powerpoint: 2024.amortized-optimization-and-AI.pptx
pdf: 2024.amortized-optimization-and-AI.pdf
abstract: >-
    AI and optimization systems are widely deployed in today's computing
    landscape. AI systems have a remarkable capacity to make abstractions
    and predictions about the world while optimization systems drive
    decision-making, control, and robotic systems that reason and interact
    with the world. These technologies are already intertwined and
    overlapping, and optimization-based reasoning systems will continue
    playing a crucial role in AI systems as they continue advancing
    towards general intelligence. Connecting to Kahneman's modes on
    thought, explicitly forming and solving an optimization problem is
    akin to "System 2" (i.e., slow thinking), while rapidly predicting a
    solution to the problem can be seen as "System 1" (i.e., fast
    thinking). AI systems can interact with optimization solvers via a
    "System 2" approach by using optimization as a tool, where humans can
    also inject domain knowledge or safety constraints and guardrails, or
    via "System 1" by learning to rapidly predict
    (or [amortize](https://arxiv.org/abs/2202.00665)) solutions
    to the optimization problems.

    This talk focuses on the amortization process of distilling the
    solutions to optimization problems into a fast, predictive model. We
    highlight a few recent developments in:
    1) amortizing transportation between measures
    ([Meta Optimal Transport](https://arxiv.org/abs/2206.05262)
    and [Meta Flow Matching](https://openreview.net/forum?id=f9GsKvLdzs)).
    These methods have applications in
    computational biology for predicting how a population of cells will be
    transported given an initial population and treatment.
    2) amortizing [convex conjugates](https://arxiv.org/abs/2210.12153)
    and [Lagrangian paths](https://arxiv.org/abs/2406.00288),
    including geodesic computations. These significantly improve neural optimal
    transport methods repeatedly solving these subproblems, and are of
    broader interest anywhere repeatedly conjugating or solving path
    planning problems.
    3) [amortizing language model prompt optimization and adversarial attacks](https://arxiv.org/abs/2404.16873).
    This setting involves repeatedly searching over the prompt
    space for every new prompt to jailbreak a target model, and
    amortization involves learning a language model that generates
    prompt-conditional suffixes that solve this optimization
    problem. Amortizing these problems attains state-of-the-art results
    and human-interpretable prompt modifications on the standard AdvBench
    settings that also transfer to closed-source black-box LLM APIs.
---

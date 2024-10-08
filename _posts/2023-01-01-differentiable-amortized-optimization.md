---
layout: post
title: Learning with differentiable and amortized optimization
date: 2023-01-01
powerpoint: 2023.differentiable-amortized-optimization.pptx
pdf: 2023.differentiable-amortized-optimization.pdf
abstract: >-
    Optimization has been a transformative modeling and decision-making paradigm over the past century that computationally encodes non-trivial reasoning operations.  Developments in optimization foundations alongside domain experts have resulted in breakthroughs for 1) controlling robotic, autonomous, mechanical, and multi-agent systems, 2) making operational decisions based on future predictions, 3) efficiently transporting or matching resources, information, and measures, 4) allocating budgets and portfolios, 5) designing materials, molecules, and other structures, 6) solving inverse problems to infer underlying hidden costs, incentives, geometries, terrains, and other structures, and 7) learning and meta-learning the parameters of predictive and statistical models. These settings often analytically specify the relevant models of the world along with an explicit objective to optimize for. Once these are specified, computational optimization solvers are able to search over the space of possible solutions or configurations and return the best one.

    The magic of optimization stops when 1) the relevant models of the world are too difficult or impossible to specify, leading to inaccurate or incomplete representations of the true setting, and 2) solving the optimization problem is computationally challenging and takes too long to return a solution on today's hardware. Machine learning methods help overcome both of these by providing fast predictive models and powerful latent abstractions of the world. In this talk, I will cover two ways of tightly integrating optimization and machine learning methods:]

    1. *Differentiable optimization* characterizes how the solution to an optimization problem changes as the inputs change. In machine learning settings, differentiable optimization provides an implicit layer that integrates optimization-based domain knowledge into the model and enables unknown parts of the optimization problem to be learned. I will cover the foundations of learning these layers with implicit differentiation and highlight applications in robotics and control settings.

    2. *Amortized optimization* rapidly predicts approximate solutions to optimization problems and is useful when repeatedly solving optimization problems. Traditional optimization methods typically solve every new problem instance from scratch, ignoring shared structures and information when solving a new instance. In contrast, a solver augmented with amortized optimization learns the shared structure present in the solution mappings and better-searches the domain. I will cover the foundations of amortized optimization and highlight new applications in control and optimal transport.
---

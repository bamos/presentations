This repository contains the slides behind [my](http://bamos.github.io) major
presentations with a [CC-BY](http://creativecommons.org/licenses/by/4.0/) license.

![](https://user-images.githubusercontent.com/707462/174943502-3e50162b-09a0-4e34-b7c2-c203d8729fce.gif)

# [2023] Learning with differentiable and amortized optimization
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.differentiable-amortized-optimization.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.differentiable-amortized-optimization.pdf)

Optimization has been a transformative modeling and decision-making paradigm over the past century that computationally encodes non-trivial reasoning operations.  Developments in optimization foundations alongside domain experts have resulted in breakthroughs for 1) controlling robotic, autonomous, mechanical, and multi-agent systems, 2) making operational decisions based on future predictions, 3) efficiently transporting or matching resources, information, and measures, 4) allocating budgets and portfolios, 5) designing materials, molecules, and other structures, 6) solving inverse problems to infer underlying hidden costs, incentives, geometries, terrains, and other structures, and 7) learning and meta-learning the parameters of predictive and statistical models. These settings often analytically specify the relevant models of the world along with an explicit objective to optimize for. Once these are specified, computational optimization solvers are able to search over the space of possible solutions or configurations and return the best one.

The magic of optimization stops when 1) the relevant models of the world are too difficult or impossible to specify, leading to inaccurate or incomplete representations of the true setting, and 2) solving the optimization problem is computationally challenging and takes too long to return a solution on today's hardware. Machine learning methods help overcome both of these by providing fast predictive models and powerful latent abstractions of the world. In this talk, I will cover two ways of tightly integrating optimization and machine learning methods:]

1. *Differentiable optimization* characterizes how the solution to an optimization problem changes as the inputs change. In machine learning settings, differentiable optimization provides an implicit layer that integrates optimization-based domain knowledge into the model and enables unknown parts of the optimization problem to be learned. I will cover the foundations of learning these layers with implicit differentiation and highlight applications in robotics and control settings.

2. *Amortized optimization* rapidly predicts approximate solutions to optimization problems and is useful when repeatedly solving optimization problems. Traditional optimization methods typically solve every new problem instance from scratch, ignoring shared structures and information when solving a new instance. In contrast, a solver augmented with amortized optimization learns the shared structure present in the solution mappings and better-searches the domain. I will cover the foundations of amortized optimization and highlight new applications in control and optimal transport.

# [2023] Continuous optimal transport
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.continuous-optimal-transport.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.continuous-optimal-transport.pdf)

# [2022] Amortized optimization for computing optimal transport maps
[Powerpoint](https://github.com/bamos/presentations/raw/main/2022.amortized-optimal-transport.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2022.amortized-optimal-transport.pdf)

# [2022] Differentiable optimization
[Powerpoint](https://github.com/bamos/presentations/raw/main/2022.differentiable-optimization.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2022.differentiable-optimization.pdf)

# [2022] Differentiable control

[Powerpoint](https://github.com/bamos/presentations/raw/main/2022.differentiable-control.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2022.differentiable-control.pdf)


# [2022] Amortized optimization

[Powerpoint](https://github.com/bamos/presentations/raw/main/2022.amortized-optimization.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2022.amortized-optimization.pdf)

# [2021] On the model-based stochastic value gradient for continuous RL

[Powerpoint](https://github.com/bamos/presentations/raw/main/2021.svg.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2021.svg.pdf)

# [2021] Riemannian Convex Potential Maps

[Keynote](https://github.com/bamos/presentations/raw/main/2021.rcpm.key) | [PDF](https://github.com/bamos/presentations/raw/main/2021.rcpm.pdf)

# [2020] Differentiable cross-entropy method

[Powerpoint](https://github.com/bamos/presentations/raw/main/2020.dcem.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2018.dcem.pdf)

# [2019] Ph.D. Thesis: Differentiable optimization-based modeling for machine learning

[Powerpoint](https://github.com/bamos/presentations/raw/main/2019.thesis.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2019.thesis.pdf)

# [2018] PyTorch libraries for linear algebra, optimization, and control

[Powerpoint](https://github.com/bamos/presentations/raw/main/2018.pytorchcon.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2018.pytorchcon.pdf)

# [2018] OptNet, end-to-end task-based learning, and control

[Powerpoint](https://github.com/bamos/presentations/raw/main/2018.optnet.ismp.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2017.optnet.ismp.pdf)

# [2018] Differentiable MPC

[Powerpoint](https://github.com/bamos/presentations/raw/main/2018.differentiable-mpc.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2018.differentiable-mpc.pdf)] | [Poster Powerpoint](https://github.com/bamos/presentations/raw/main/2018.differentiable-mpc-poster.pptx) | [Poster PDF](https://github.com/bamos/presentations/raw/main/2018.differentiable-mpc-poster.pdf)

# [2017] OptNet

[Powerpoint](https://github.com/bamos/presentations/raw/main/2017.optnet.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2017.optnet.pdf)

# [2017] ICNN

[Powerpoint](https://github.com/bamos/presentations/raw/main/2017.icnn.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2017.icnn.pdf)

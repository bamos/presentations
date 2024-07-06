This repository contains the slides behind [my](http://bamos.github.io) major
presentations with a [CC-BY](http://creativecommons.org/licenses/by/4.0/) license.

![](https://user-images.githubusercontent.com/707462/174943502-3e50162b-09a0-4e34-b7c2-c203d8729fce.gif)

# [2024] [Lagrangian OT](https://arxiv.org/abs/2406.00288) Poster
[Powerpoint](https://github.com/bamos/presentations/raw/main/2024.lagrangian-ot-poster.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2024.lagrangian-ot-poster.pdf)

We investigate the optimal transport problem between probability
measures when the underlying cost function is understood to satisfy a
least action principle, also known as a Lagrangian cost. These
generalizations are useful when connecting observations from a
physical system where the transport dynamics are influenced by the
geometry of the system, such as obstacles (e.g., incorporating barrier
functions in the Lagrangian), and allows practitioners to incorporate
a priori knowledge of the underlying system such as non-Euclidean
geometries (e.g., paths must be circular). Our contributions are of
computational interest, where we demonstrate the ability to
efficiently compute geodesics and amortize spline-based paths, which
has not been done before, even in low dimensional problems. Unlike
prior work, we also output the resulting Lagrangian optimal transport
map without requiring an ODE solver. We demonstrate the effectiveness
of our formulation on low-dimensional examples taken from prior work.

# [2024] End-to-end learning geometries for graphs, dynamical systems, and regression
[Powerpoint](https://github.com/bamos/presentations/raw/main/2024.e2e-geometries.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2024.e2e-geometries.pdf)


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

# [2023] Amortized optimization for optimal transport
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.amortized-optimal-transport.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.amortized-optimal-transport.pdf)

Optimal transport has thriving applications in machine learning, computer vision, natural language processing, the physical sciences, and economics. These applications have largely been enabled by computational breakthroughs that have lead to tractable solutions to challenging optimization problems, especially in discrete spaces through the use of convex optimization methods. Beyond these well-understood classes problems, many difficult optimization problems and sub-problems in optimal transport remain open. This talk focuses on the use of learning methods to predict, or amortize, the solutions to these optimization problems. This amortization process incurs an initial computational cost of training a model to approximately predict the solutions, but afterwards, the model can produce predictions faster than solving the optimization problems from scratch to the same level of error. Furthermore, even inaccurate predictions are tolerable because they are easily detectable, e.g., via the optimality conditions, and can be fine-tuned by warm-starting an existing method with the prediction. The talk covers how to amortize the computation at three levels: 1) the optimal transport map or potential, 2) the c-transform or convex conjugate, and 3) costs defined by a Lagrangian.

# [2023] [TaskMet](https://arxiv.org/abs/2312.05250) Poster
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.taskmet-neurips-poster.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.taskmet-neurips-poster.pdf)

Deep learning models are often deployed in downstream tasks that the training procedure may not be aware of. For example, models solely trained to achieve accurate predictions may struggle to perform well on downstream tasks because seemingly small prediction errors may incur drastic task errors. The standard end-to-end learning approach is to make the task loss differentiable or to introduce a differentiable surrogate that the model can be trained on. In these settings, the task loss needs to be carefully balanced with the prediction loss because they may have conflicting objectives. We propose take the task loss signal one level deeper than the parameters of the model and use it to learn the parameters of the loss function the model is trained on, which can be done by learning a metric in the prediction space. This approach does not alter the optimal prediction model itself, but rather changes the model learning to emphasize the information important for the downstream task. This enables us to achieve the best of both worlds: a prediction model trained in the original prediction space while also being valuable for the desired downstream task. We validate our approach through experiments conducted in two main settings: 1) decision-focused model learning scenarios involving portfolio optimization and budget allocation, and 2) reinforcement learning in noisy environments with distracting states. 

# [2023] On optimal control and machine learning
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.control-learning.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.control-learning.pdf)

This talk tours the optimal control and machine learning methodologies behind recent breakthroughs in the field. These are crucial components for building agents capable of computationally modeling and interacting with our world via planning and reasoning, e.g. for robotics, aircrafts, autonomous vehicles, games, economics, finance, and language, as well as agricultural, biomedical,chemical, industrial, and mechanical systems. We will start with 1) a lightweight introduction to optimal control, and then cover 2) machine learning for optimal control --- this includes reinforcement learning and overviews how the powerful abstractive and predictive capabilities of machine learning can drastically improve every part of a control system; and 3) optimal control for machine learning --- surprisingly in this opposite direction, some machine learning problems are able to be formulated as control problems and solved with optimal control methods, e.g. parts of diffusion models, optimal transport,and optimizing the parameters of models such as large language models with reinforcement learning.

# [2023] Learning with differentiable and amortized optimization
[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.differentiable-amortized-optimization.pptx) |
[PDF](https://github.com/bamos/presentations/raw/main/2023.differentiable-amortized-optimization.pdf)

Optimization has been a transformative modeling and decision-making paradigm over the past century that computationally encodes non-trivial reasoning operations.  Developments in optimization foundations alongside domain experts have resulted in breakthroughs for 1) controlling robotic, autonomous, mechanical, and multi-agent systems, 2) making operational decisions based on future predictions, 3) efficiently transporting or matching resources, information, and measures, 4) allocating budgets and portfolios, 5) designing materials, molecules, and other structures, 6) solving inverse problems to infer underlying hidden costs, incentives, geometries, terrains, and other structures, and 7) learning and meta-learning the parameters of predictive and statistical models. These settings often analytically specify the relevant models of the world along with an explicit objective to optimize for. Once these are specified, computational optimization solvers are able to search over the space of possible solutions or configurations and return the best one.

The magic of optimization stops when 1) the relevant models of the world are too difficult or impossible to specify, leading to inaccurate or incomplete representations of the true setting, and 2) solving the optimization problem is computationally challenging and takes too long to return a solution on today's hardware. Machine learning methods help overcome both of these by providing fast predictive models and powerful latent abstractions of the world. In this talk, I will cover two ways of tightly integrating optimization and machine learning methods:]

1. *Differentiable optimization* characterizes how the solution to an optimization problem changes as the inputs change. In machine learning settings, differentiable optimization provides an implicit layer that integrates optimization-based domain knowledge into the model and enables unknown parts of the optimization problem to be learned. I will cover the foundations of learning these layers with implicit differentiation and highlight applications in robotics and control settings.

2. *Amortized optimization* rapidly predicts approximate solutions to optimization problems and is useful when repeatedly solving optimization problems. Traditional optimization methods typically solve every new problem instance from scratch, ignoring shared structures and information when solving a new instance. In contrast, a solver augmented with amortized optimization learns the shared structure present in the solution mappings and better-searches the domain. I will cover the foundations of amortized optimization and highlight new applications in control and optimal transport.

# [2023] Amortized optimization
Optimization is a ubiquitous modeling tool and is often
deployed in settings which repeatedly solve similar
instances of the same problem.
Amortized optimization methods use learning to predict the solutions to
problems in these settings, exploiting the shared structure
between similar problem instances.
These methods have been crucial in variational inference
and reinforcement learning and are capable of solving
optimization problems many orders of magnitudes times faster
than traditional optimization methods that do not use amortization.
This talk presents an introduction to the amortized optimization
foundations behind these advancements and overviews
their applications in variational inference, sparse coding,
gradient-based meta-learning, control, reinforcement learning,
convex optimization, optimal transport, and deep equilibrium networks.

[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.amortized-optimization.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2023.amortized-optimization.pdf) | [paper](https://arxiv.org/abs/2202.00665)


# [2023] On amortizing convex conjugates for optimal transport

This paper focuses on computing the convex conjugate operation that
arises when solving Euclidean Wasserstein-2 optimal transport
problems. This conjugation, which is also referred to as the
Legendre-Fenchel conjugate or c-transform,is considered difficult to
compute and in practice,Wasserstein-2 methods are limited by not being
able to exactly conjugate the dual potentials in continuous space. To
overcome this, the computation of the conjugate can be approximated
with amortized optimization, which learns a model to predict the
conjugate. I show that combining amortized approximations to the
conjugate with a solver for fine-tuning significantly improves the
quality of transport maps learned for the Wasserstein-2 benchmark by
Korotin et al. (2021a) and is able to model many 2-dimensional
couplings and flows considered in the literature.

[Powerpoint](https://github.com/bamos/presentations/raw/main/2023.w2ot.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2023.w2ot.pdf) | [paper](https://arxiv.org/abs/2210.12153)

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

[Powerpoint](https://github.com/bamos/presentations/raw/main/2021.svg.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2021.svg.pdf) | [paper](https://arxiv.org/abs/2008.12775)

# [2021] Riemannian Convex Potential Maps

[Keynote](https://github.com/bamos/presentations/raw/main/2021.rcpm.key) | [PDF](https://github.com/bamos/presentations/raw/main/2021.rcpm.pdf) | [paper](https://arxiv.org/abs/2106.10272)

# [2020] Differentiable cross-entropy method

[Powerpoint](https://github.com/bamos/presentations/raw/main/2020.dcem.pptx) | [PDF](https://github.com/bamos/presentations/raw/main/2018.dcem.pdf) | [paper](https://arxiv.org/abs/1909.12830)

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

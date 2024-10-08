---
layout: post
title: TaskMet Poster
date: 2023-01-01
powerpoint: 2023.taskmet-neurips-poster.pptx
pdf: 2023.taskmet-neurips-poster.pdf
paper: https://arxiv.org/abs/2312.05250
abstract: >-
    Deep learning models are often deployed in downstream tasks that the
    training procedure may not be aware of. For example, models solely trained
    to achieve accurate predictions may struggle to perform well on downstream
    tasks because seemingly small prediction errors may incur drastic task
    errors. The standard end-to-end learning approach is to make the task loss
    differentiable or to introduce a differentiable surrogate that the model
    can be trained on. In these settings, the task loss needs to be carefully
    balanced with the prediction loss because they may have conflicting
    objectives. We propose take the task loss signal one level deeper than the
    parameters of the model and use it to learn the parameters of the loss
    function the model is trained on, which can be done by learning a metric in
    the prediction space. This approach does not alter the optimal prediction
    model itself, but rather changes the model learning to emphasize the
    information important for the downstream task. This enables us to achieve
    the best of both worlds: a prediction model trained in the original
    prediction space while also being valuable for the desired downstream task.
    We validate our approach through experiments conducted in two main
    settings: 1) decision-focused model learning scenarios involving portfolio
    optimization and budget allocation, and 2) reinforcement learning in noisy
    environments with distracting states.
---

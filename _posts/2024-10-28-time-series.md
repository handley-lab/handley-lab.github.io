---
layout: post
title:  "Scaling laws for large time-series models: More data, more parameters"
date:   2024-10-28
categories: seminars
---

![tmpkhval60o](https://github.com/user-attachments/assets/be89285e-2def-4c13-be31-ba14a23ccb7f)


James Alvey recently gave a seminar at the Kavli Institute for Cosmology, as part of the Astro Data Science Discussion Group seminar series. His talk was titled "Scaling laws for large time-series models: More data, more parameters", and was based on work recently presented at the NeurIPS Time Series in the Age of Large Models workshop [2405.13867](https://arxiv.org/abs/2405.13867).

## Scaling Laws for LLMs

The remarkable success of large language models (LLMs) such as ChatGPT is well-known. However, training these models is extremely computationally expensive, to the point that only a handful of organisations worldwide have the resources to do so. 

The question of how best to allocate resources when training LLMs was explored in depth by OpenAI in the process of developing GPT-3 and GPT-4. By training a large number of smaller models with varying numbers of parameters, sizes of training datasets, and training times, they were able to demonstrate that the performance of LLMs follows a predictable power-law scaling with all three of these quantities [2001.08361](https://arxiv.org/abs/2001.08361). This has two important consequences: firstly, it allows for the reliable extrapolation of performance to larger models, and secondly, it allows for the optimal allocation of resources to achieve a given performance goal.

Perhaps the most important conclusion from this work was that, given a fixed computational budget, the best performance is almost always achieved by training the largest model possible, even if there are not enough resources to train it to convergence. This is because larger models are more sample-efficient; they are able to learn more effectively from a given amount of data.

## Time Series and Transformers

Time series data share many similarities with language, in that they are both sequential and causal. Transformer architectures, originally developed for natural language processing, have also been shown to be highly effective for time series forecasting.

The question naturally arises: do the same scaling laws that have been observed for LLMs also hold for time series models?

## A Baseline Study

To answer this question, Alvey and collaborators assembled a dataset of approximately 8 billion data points from a variety of domains, including climate data, energy usage, traffic flow, financial markets, and audio signals. They then trained a series of decoder-only transformer models of varying sizes on this dataset, using a Student's-$t$ distribution head to enable probabilistic forecasting.

Their results show that, to a good approximation, the same power-law scaling laws do indeed hold for time series models. In particular, they observe power-law scaling of the test loss (measured using mean squared error, continuous ranked probability score, and log-likelihood) with model size, dataset size, and compute. They also find that, as with LLMs, the architecture of the model has relatively little impact on performance, provided it is not too extreme.

## Conclusions and Future Directions

This work establishes a baseline for the scaling of large time-series models, and suggests that it may be possible to achieve significant performance gains by training even larger models on even larger datasets.

Several open questions remain, including:

* What are the optimal computational requirements for training large time-series models?
* How can we best curate datasets for training these models?
* How does the forecast horizon affect the scaling laws?
* What are the failure modes of large time-series models?

Answering these questions will be crucial for developing a deeper understanding of the capabilities and limitations of large time-series models, and for unlocking their full potential for scientific discovery and real-world applications. 


*This post was written using [Gemini](https://deepmind.google/technologies/gemini/) with this [prompt](/prompts/2024-10-28-time-series.md)*

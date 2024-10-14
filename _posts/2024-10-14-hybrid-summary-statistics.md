---
layout: post
title:  "Hybrid Summary Statistics: Telling Neural Networks Where to Look"
date:   2024-10-14
categories: seminars
---

![DALLE3 prompt: A swirling galaxy of data points, converging towards a glowing neural network.  Traditional summary statistics form a structured grid, while new, complementary information emerges as streaks of light.](https://github.com/user-attachments/assets/4ac93078-40be-48f0-a06a-81cc406e0cd8)

Lukas Mäkinen from Imperial College London recently gave a talk at the Cambridge Data Science Discussion Group about his work on hybrid summary statistics for cosmological inference.  This blog post summarises the main points of his talk and the related papers [2407.18909](https://arxiv.org/pdf/2407.18909) and [2410.07548](https://arxiv.org/pdf/2410.07548).

### The Challenge of Cosmological Inference

In cosmology, we try to understand the properties of the Universe, such as its matter content and how it has expanded over time. This is done by comparing observations of the Universe, such as the distribution of galaxies, with theoretical predictions from cosmological models. This process is known as cosmological inference.

One of the main challenges of cosmological inference is that the data we observe is extremely high-dimensional. For example, a typical galaxy survey might image millions or even billions of galaxies.  To make this problem tractable, we need to find ways to compress the data without losing valuable information about the cosmological parameters we want to measure.

### Traditional and Neural Summary Statistics

Traditionally, cosmologists have relied on summary statistics, such as the two-point correlation function or the power spectrum, to compress data for cosmological inference. These statistics capture information about the distribution of matter in the Universe on different scales. They have proven to be very useful for constraining cosmological models, but they do not capture all of the information present in the data.

In recent years, neural networks have emerged as a powerful tool for learning informative data representations.  In cosmology, neural networks have been used to construct new summary statistics that outperform traditional statistics in some cases. These neural compression schemes are trained to preserve as much information as possible about the cosmological parameters of interest.

### The Power of Hybrid Summary Statistics

The main idea behind Mäkinen's work is to combine the strengths of both traditional and neural summary statistics. Instead of training a neural network to compress the data from scratch, he proposes training it to extract the information that is *not* already captured by a set of pre-defined traditional summaries. In other words, the network is told to look for information in the data that is complementary to the information contained in the traditional summaries.

This approach has several advantages. First, it guarantees that the new neural summary statistics will be at least as informative as the traditional summaries. Second, it can significantly reduce the number of simulations required to train the network, which is important for computationally expensive cosmological models. Finally, it can provide insights into the physical features in the data that are most informative about the cosmological parameters.

### Applications to Weak Lensing and the 21cm Signal

In his talk, Mäkinen presented the results of applying hybrid summary statistics to weak gravitational lensing maps. His hybrid approach yielded significantly tighter constraints on the cosmological parameters compared to using either traditional statistics or neural statistics alone. This highlights the potential of hybrid summary statistics to extract more information from cosmological data and improve our understanding of the Universe.

### Future Directions

Hybrid summary statistics are a promising new approach for cosmological inference. There are many exciting avenues for future research in this area, such as:

* **Extending the method to other cosmological observables:** The hybrid approach can be applied to a wide range of cosmological datasets, such as galaxy clustering, galaxy clusters, and the Lyman-alpha forest.
* **Developing more sophisticated network architectures:**  More complex network architectures could potentially extract even more information from the data.
* **Understanding the physical meaning of the learned summaries:** One of the key questions is to understand what physical features in the data the neural networks are learning to identify. This could provide new insights into the physical processes that govern the Universe.

Overall, hybrid summary statistics represent a powerful new tool for unlocking the secrets of the cosmos. By combining the strengths of traditional and neural approaches, we can extract more information from cosmological data and improve our understanding of the Universe we live in. 


*This post was written using [Gemini](https://deepmind.google/technologies/gemini/) with this [prompt](/prompts/2024-10-14-hybrid-summary-statistics.md)*

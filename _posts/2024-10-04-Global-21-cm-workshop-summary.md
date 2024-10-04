---
layout: post
title:  "The 7th Global 21cm Workshop: Technical summary "
date:   2024-10-04
categories: conferences technical
---

## The 7th Global 21cm Workshop: Technical summary

_Generated with [Gemini 1.5 pro](https://deepmind.google/technologies/gemini/) from a prompt based on on [Will Handley's](/people/will-handley) notes and a [Tactiq](https://tactiq.io/) transcript. Some talks missing [particularly day 2] due to absence of Will Handley and internet malfunction. 271298 tokens in total_

The [7th Global 21cm Workshop](https://sites.google.com/view/global-21-cm-workshop), held at the Raman Research Institute in Bengaluru, India, from September 30th to October 4th, 2024, served as a vital platform for researchers exploring the detection and analysis of the cosmological 21cm signal, a faint radio emission from neutral hydrogen that holds clues to the early universe. The workshop featured a diverse range of presentations, discussions, and poster sessions, covering topics from theoretical modeling and experimental updates to calibration techniques and data analysis methods. 

The workshop commenced with an emphasis on the implications of the EDGES detection, a signal claimed to originate from the Cosmic Dawn. Andrei Mesinger presented a compelling argument, suggesting that the EDGES signal might not be cosmological, as its unique shape is better explained by foregrounds and systematics. He introduced the 21cmEMU emulator, a tool that incorporates observational constraints from various sources, including the Epoch of Reionization history and UV luminosity functions, to refine theoretical models. This theme of reconciling theoretical models with diverse observational data sets echoed throughout the workshop.

The first day also saw presentations on star-formation efficiency in the early universe, Lyman-alpha heating and cooling, and novel polynomial fitting algorithms for detecting the global 21cm signal. Lively discussions centered around the need for better feedback between experimentalists and modelers, the standardization of simulators, and the challenge of defining a consistent parameterization for complex astrophysical processes.

Day 2 focused on experimental updates, with Emilie Storer providing an update on PRIZM, a project designed to measure the radio sky from Marion Island.  Despite challenges like precipitation and strong winds, PRIZM has gathered valuable data, showcasing the island's remarkably clean RFI environment.  Yash Agrawal discussed direction-dependent effects in SARAS, highlighting the need to carefully account for systematics introduced by antenna parameters and environmental factors. Presentations on space-based experiments like STARFIRE and PRATUSH explored the potential of Earth orbit and lunar orbits for detecting the 21cm signal. The day concluded with discussions on the various receiver calibration schemes employed by different experiments and the effectiveness of beam modeling.

Day 3 delved deeper into the complexities of analyzing and interpreting the 21cm signal. Nivedita Mahesh provided a comprehensive update on EDGES, outlining hardware upgrades, data processing advancements, and the discovery of a puzzling 63 MHz signal likely linked to Starlink satellites. Rigel Cappallo elaborated on this signal and discussed plans for a northern site deployment at Adak Island to mitigate RFI contamination. Steven Murray presented an open-source pipeline for analyzing EDGES data, emphasizing the importance of transparency and reproducibility in the field.  The afternoon session featured presentations on GINAN, a new experiment designed to measure the global 21cm signal from the SKA site in Australia, and MIST, which is gathering data from the Canadian High Arctic.  Discussions revolved around the challenges of soil modeling, the importance of measuring antenna impedance in situ, and the potential of balloon-based experiments.

The final day of the workshop began with Leon Koopmans’ insightful overview of lunar-based 21cm cosmology experiments, highlighting both the opportunities presented by the radio-quiet lunar far side and the challenges of RFI from Earth-based sources. David Rapetti discussed the dawn of radio astronomy from the moon, presenting results from the ROLSES and LuSEE-Night experiments, both of which have gathered data from the lunar surface.  Presentations on LCRT and SEAMS explored the potential of ambitious lunar-based telescopes and space missions dedicated to ultra-low frequency radio observations. The workshop concluded with discussions on the interplay between ground-based and space-based experiments, the need for further technological advancements, and the importance of international collaboration in pushing the frontiers of 21cm cosmology.

In summary, the 7th Global 21cm Workshop showcased significant progress in both experimental and theoretical aspects of 21cm cosmology. The emphasis on open data and code sharing, the development of sophisticated calibration techniques, and the exploration of new observational platforms like the moon promise to accelerate our understanding of the universe’s first billion years. The workshop successfully fostered collaboration and critical discussion, laying the groundwork for future breakthroughs in this exciting field. 

## Detailed Summary

### Day 1: Theoretical Implications and Experimental Challenges

**Welcome and Introduction:**

The workshop began with a welcome address highlighting the Raman Research Institute's legacy of sustained research programs, particularly in the field of 21cm cosmology. The organizers emphasized the importance of the workshop in fostering collaboration and advancing our understanding of the early universe.

**What does the EDGES detection really mean for physical models of the cosmic 21cm signal? (Andrei Mesinger):**

Andrei Mesinger's presentation focused on the implications of the EDGES detection, a signal purportedly originating from the Cosmic Dawn. He argued that the EDGES signal might not be cosmological, as its unusual shape is better explained by foregrounds and systematics. He also introduced the 21cmEMU emulator, a tool incorporating observational constraints from various sources, including the Epoch of Reionization history and UV luminosity functions, to refine theoretical models. 

Mesinger highlighted the need for a holistic approach to data analysis, urging researchers to consider not just the best-fit residual but also the raw data and complementary observations. He emphasized that relying solely on simplified parameterizations could lead to biased conclusions, advocating for a more comprehensive approach that incorporates diverse observational data sets.

**Constraining star-formation efficiency in the early Universe using JWST and the cosmic 21-cm signal (Jitin Dhanda):**

Jitin Dhanda's presentation delved into the implications of recent JWST observations, which have revealed a surprising abundance of galaxies at high redshifts. He discussed the challenges of modeling this unexpected galaxy population and its impact on star-formation efficiency in the early universe. Dhanda explored the potential synergies between JWST observations and 21cm cosmology, emphasizing the need to combine these data sets to constrain theoretical models and understand the evolution of the early universe.

**Revisiting Lyman-α Heating and Cooling during the Cosmic Dawn (Janakee Raste):**

Janakee Raste focused on the role of Lyman-alpha photons in heating and cooling the intergalactic medium during the Cosmic Dawn. She presented a detailed analysis of Lyman-alpha radiative transfer, highlighting the importance of considering both continuum photons and injected photons. Raste challenged the common assumption of quasi-static equilibrium, advocating for a more nuanced approach that accounts for the time-dependent evolution of Lyman-alpha photons and their impact on the 21cm signal.

**Detecting Cosmic 21cm global signal using an improved polynomial fitting algorithm (Tianyang Liu - Remote):**

Tianyang Liu presented a novel polynomial fitting algorithm, the Vari-Zeroth-Order Polynomial (VZOP), for detecting the global 21cm signal. This method addresses the challenges of chromaticity correction without relying on sky map simulations. Liu demonstrated the robustness of VZOP, showing its ability to accurately recover the 21cm signal even in the presence of significant beam errors. He also discussed the application of VZOP to the DSL project, a Chinese lunar mission aiming to detect the 21cm signal from the far side of the moon.

**PolySwyft: a sequential simulation-based nested sampler (Will Handley):**

Will Handley introduced PolySwyft, a novel method that combines simulation-based inference (SBI) with nested sampling. This approach addresses the limitations of traditional likelihood-based inference, particularly when dealing with complex astrophysical models. PolySwyft leverages the power of neural ratio estimation and nested sampling to efficiently explore high-dimensional parameter spaces and provide robust posterior estimates. Handley demonstrated the effectiveness of PolySwyft in a cosmological context, showcasing its ability to jointly constrain six parameters and handle hundreds of data points.

**Lightning Talks and Discussion 1:**

The day concluded with lightning talks on foreground removal techniques and particle production during inflation, followed by a discussion on the interplay between experimentalists and modelers. Participants debated the need for standardized simulators, consistent parameterizations, and effective ways for experiments to provide feedback to modelers. The discussion highlighted the importance of defining a common "latent space" for comparing different simulations and fostering a more collaborative approach to 21cm cosmology.

### Day 2: Experimental Progress: Ground-based and Space-based

**Probing Radio Intensity at high-Z from Marion (PRIZM) - An Update (Emilie Storer):**

Emilie Storer provided an update on PRIZM, a project designed to measure the radio sky from Marion Island. Storer discussed the island's unique advantages, including its remarkably clean RFI environment, but also highlighted the challenges of operating in this remote and harsh environment. She presented preliminary results from the 2021 data set, demonstrating progress in RFI flagging, calibration techniques, and foreground fitting. Storer's presentation showcased the valuable contributions of PRIZM in providing independent constraints on the global 21cm signal.

**Direction-dependent effects in SARAS and its latest deployment (Yash Agrawal):**

Yash Agrawal discussed direction-dependent effects in SARAS, emphasizing the need to carefully consider systematics introduced by antenna parameters, raft characteristics, and environmental factors. He presented simulations showcasing the impact of varying conductivity, raft tilt, and raft height on the SARAS beam pattern. Agrawal also highlighted the importance of in situ S11 measurements for accurate calibration and discussed recent deployments of SARAS in both land-based and water-based configurations. He concluded by outlining future work, including the development of SARAS 4, an antenna designed for the 100-200 MHz frequency range.

**Detecting the redshifted Global 21-cm signal in Earth orbit (Yogen Pranesh):**

Yogen Pranesh presented STARFIRE2, a simulation tool for predicting terrestrial radio frequency interference (RFI) in various Earth orbits. He discussed the application of STARFIRE2 to PRATUSH, a proposed space-based experiment aiming to detect the global 21cm signal from Earth orbit and eventually lunar orbit. Pranesh showcased the tool's ability to generate RFI cubes for different altitudes and frequencies, demonstrating its utility in optimizing orbits to maximize RFI-clean observation time. He concluded by outlining future work, including the development of a comprehensive FM transmitter database and further refinement of orbit optimization techniques.

**In-situ measurement of antenna return loss for 21-cm cosmology experiments (Adarsh Kumar Dash):**

Adarsh Kumar Dash focused on the importance of in situ S11 measurements for 21cm cosmology experiments, highlighting the limitations of lab measurements due to the influence of environmental factors on antenna characteristics. He discussed the challenges of achieving high-precision S11 measurements in the field, particularly for space-based experiments like PRATUSH, which face constraints on power and weight. Dash presented a new approach for in situ S11 measurements utilizing a directional coupler and three-term error correction, showcasing its potential for improving calibration accuracy and reducing systematics. 

**RHINO: Observing the 21cm global signal with a large horn antenna (Hugh Garsden):**

Hugh Garsden introduced RHINO, a project utilizing a large horn antenna to observe the global 21cm signal. Garsden discussed the advantages of horn antennas, including high sidelobe suppression, good beam shape control, and inherent shielding from the environment. He presented two horn designs, a pyramidal horn and a conical corrugated horn, highlighting their respective beam characteristics and trade-offs. Garsden showcased a prototype under construction at Jodrell Bank and discussed plans for receiver development and continuous wave calibration, a simple and effective method for calibrating the horn antenna.

**Lightning Talks and Discussion 2:**

The day concluded with lightning talks on noise wave calibration and statistical filtering for denoising 21cm data, followed by a discussion on the various RX calibration schemes employed by different experiments. Participants debated the effectiveness of redundancy, antenna simulators, and lab-based versus field-based calibration techniques. The discussion highlighted the need for comprehensive validation methods to ensure calibration accuracy and build confidence in the final results.

### Day 3: Data Analysis and Interpretation: Towards Robust Results

**Another yearly round-up of EDGES (Nivedita Mahesh):**

Nivedita Mahesh provided a comprehensive update on EDGES, outlining hardware upgrades, data processing advancements, and new insights from recent observations. She discussed the status of both EDGES2 and EDGES3, highlighting the advantages of the new EDGES3 system, which features a larger ground plane, in situ calibration, and a less chromatic beam. Mahesh presented results from a recent site trip, demonstrating the effectiveness of theodolite measurements for accurately characterizing ground plane undulations and refining beam models. She concluded by discussing progress in developing an open-source Python package for processing EDGES data, enabling greater transparency and reproducibility.

**The Calibration Accuracy of the EDGES-3 21-cm System and Recent Results (Rigel Cappallo):**

Rigel Cappallo delved deeper into the calibration accuracy of the EDGES-3 system, discussing the environmental considerations and challenges involved in achieving high-precision measurements. He presented an analysis of a puzzling 63 MHz signal observed in both EDGES2 and EDGES3 data, concluding that it is likely linked to Starlink satellites. Cappallo discussed the implications of this RFI contamination for future ground-based observations and outlined plans for a northern site deployment at Adak Island to mitigate these effects. He concluded by presenting the latest results from EDGES3, showing consistency with the previously reported absorption profile.

**Progress on EDGES-3 data analysis (Akshatha Vydula):**

Akshatha Vydula focused on the progress in analyzing EDGES-3 data using the new open-source pipeline, edges-collab. She discussed the advantages of in situ calibration, outlining the updated calibration design and validation efforts against the legacy C pipeline. Vydula presented an analysis of residual structures in long cable calibration sources, highlighting ongoing investigations into potential sources of these residuals. She concluded by showcasing preliminary 10-day spectra from EDGES-3 and outlining the next steps in the analysis, including beam chromaticity correction, loss corrections, and simulated sky tests.

**Improved and Open-Source analysis of EDGES-2018 (Steven Murray - Remote):**

Steven Murray presented an improved and open-source analysis pipeline for the 2018 EDGES data. He emphasized the importance of transparency and reproducibility, outlining the limitations of the original C code and the need for a more modular and well-documented pipeline. Murray described the components of the new pipeline, including edges-cal, edges-analysis, pygsdata, and edges-estimate, highlighting their respective functionalities and potential for broader community use. He concluded by announcing plans to release the full raw data and analysis pipelines, enabling full reproduction of the 2018 results and further scrutiny by the community.

**Marginal Bayesian Statistics and Post Processing of Bayesian Constraints from 21-cm Experiments (Harry Bevins):**

Harry Bevins delved into the application of marginal Bayesian statistics and post-processing techniques for analyzing 21cm data. He introduced normalizing flows, a generative density estimation tool, and discussed their utility in accessing marginal probabilities, calculating marginal likelihood functions, and quantifying information gain. Bevins presented three applications of these tools: marginal statistics for comparing the constraining power of different experiments, joint analysis for efficiently combining constraints from multiple experiments, and mutual information for assessing the dependence between different parameter subsets. He concluded by highlighting the potential of these techniques for extracting robust and meaningful insights from 21cm data.

**Lightning Talks and Discussion 3:**

The day concluded with lightning talks on the impact of large optical depth on the 21cm bispectrum and the effect of different reionization scenarios on the 21cm bispectrum. A discussion followed, focusing on the calibration schemes employed by various experiments. Participants debated the effectiveness of different techniques, including Dicke switching, absolute calibration, continuous wave calibration, and correlator calibration. The discussion highlighted the importance of validation against sky models, the use of redundant calibrators, and the need for precise measurements of system parameters to ensure accurate calibration and robust results.

### Day 4: Lunar-Based Cosmology and Future Directions

**Lunar-Based 21-cm Cosmology Experiments: Opportunities and Challenges (Leon Koopmans):**

Leon Koopmans provided a comprehensive overview of lunar-based 21cm cosmology experiments, highlighting the unique advantages of the radio-quiet lunar far side for probing the Dark Ages and the challenges of mitigating RFI from Earth-based sources. He discussed the scientific potential of lunar-based observations, spanning fundamental physics, dark matter, dark energy, and the early stages of galaxy formation. Koopmans presented an overview of current and proposed lunar-based experiments, including Pratush, DSL, LuSEE-night, FarView, ROLSES, LCRT, DEX, and SEAMS, discussing their respective science goals, technologies, and challenges. He concluded by emphasizing the importance of technological advancements, international collaboration, and a strategic approach to realizing the full potential of lunar-based 21cm cosmology.

**The Dawn of Radio Astronomy from the Moon: Current Results and Near-Term Prospects (David Rapetti - Remote):**

David Rapetti discussed the dawn of radio astronomy from the moon, presenting results from the ROLSES and LuSEE-Night experiments, both of which have gathered data from the lunar surface. He outlined the challenges faced by these missions, including hardware malfunctions, limited power, and communication constraints. Rapetti presented preliminary data analysis from ROLSES, showcasing the detection of potential techno-signatures from Earth and highlighting the instrument's capability for studying the lunar radio environment. He also discussed LuSEE-Night, a pathfinder for dark ages science from the lunar far side, and its potential for constraining the global 21cm signal. Rapetti concluded by discussing upcoming lunar missions and the importance of developing robust data analysis pipelines and emulators for interpreting lunar-based observations.

**Modeling Science Return from the Lunar Crater Radio Telescope (LCRT) Mission Concept (Saptarshi Bandyopadhyay):**

Saptarshi Bandyopadhyay presented the Lunar Crater Radio Telescope (LCRT) mission concept, an ambitious project aiming to build a 350-meter diameter radio telescope within a lunar crater. He discussed the science goals of LCRT, focusing on observing the universe in the poorly explored 6-64 meter wavelength band. Bandyopadhyay outlined the technological challenges involved in realizing this ambitious concept, including crater selection, structural design, thermal strain compensation, and rim-to-floor transportation. He presented a deployment strategy involving harpooned anchors and an origami-folded reflector, highlighting the need for technological demonstrations to prove the feasibility of these concepts. Bandyopadhyay concluded by discussing the science return from LCRT, showcasing simulations demonstrating the telescope's potential for detecting the global 21cm signal from the Dark Ages.

**SEAMS: A space mission dedicated to ultra-low frequency radio observations (Abhirup Datta):**

Abhirup Datta presented SEAMS, a proposed space mission dedicated to ultra-low frequency radio observations. He discussed the scientific motivation for observing the universe below 30 MHz, highlighting the ionosphere's opacity at these frequencies and the potential for studying a wide range of phenomena, including solar radio bursts, planetary auroral emissions, and the redshifted 21cm signal from the Cosmic Dark Ages. Datta outlined the three phases of SEAMS, starting with RFI characterization in low Earth orbit, followed by interferometric observations using multiple CubeSats, and culminating in a payload deployed on the lunar far side or at the Moon-Earth L2 point. He concluded by discussing the technological challenges and opportunities presented by SEAMS, emphasizing its potential for advancing our understanding of the low-frequency radio universe.

**Design of a Wideband Monopole Antenna for the Detection of EoR signal (Vishakha Pandharpure):**

Vishakha Pandharpure discussed the design of a wideband monopole antenna for detecting the Epoch of Reionization (EoR) signal, focusing on the development of SARAS 4, a new antenna for the SARAS experiment. She outlined the challenges of designing antennas for this frequency range, highlighting the need for smooth reflection coefficients, low chromaticity, and robustness to environmental factors. Pandharpure presented two antenna configurations, one with a thin reflector and another with a thick reflector, detailing the optimization process using FEKO simulations and the figures of merit employed for evaluating antenna performance. She concluded by showcasing the simulated antenna performance on different terrains, including water, heterogeneous land, homogeneous land, and snow, demonstrating the antenna's suitability for various deployment scenarios.

**Could the Moon's rough behaviour close the 21-cm EoR window? : The Dark-ages EXplorer (DEX) Study (Sonia Ghosh):**

Sonia Ghosh explored the impact of lunar topography on the 21cm EoR window, focusing on the Dark-ages EXplorer (DEX) project. She discussed the science case for DEX, emphasizing the complementary nature of power spectrum measurements to sky-averaged signal observations. Ghosh presented the DEX array design, featuring 1,024 co-located dual polarization dipoles distributed on a regular grid on the lunar far side. She highlighted the challenges of deploying a perfectly spaced array given the rugged lunar terrain and presented simulation results demonstrating the impact of positional deviations on the 21cm power spectrum. Ghosh concluded by discussing the importance of identifying suitable landing sites with low roughness and developing strategies for mitigating the effects of lunar topography on array performance.

**Lightning Talks and Discussion 4:**

The workshop concluded with lightning talks on various topics, including probing the cosmic dawn 21cm signal with NenuFAR, updates from the HERA interferometer, and ANN-based global 21cm signal extraction. A final discussion followed, focusing on the interplay between ground-based and lunar-based experiments. Participants debated the challenges of characterizing the lunar environment, the potential of different antenna designs for lunar observations, and the importance of international collaboration for realizing ambitious lunar-based projects. The discussion highlighted the growing momentum in lunar-based 21cm cosmology and the exciting prospects for future discoveries in this field. 

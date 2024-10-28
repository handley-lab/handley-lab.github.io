{% raw %}
James Alvey gave a Seminar at the Kavli Institute for Cosmology, University of Cambridge.
Could you write a blog post for my jekyll website using the below information, with the header

```markdown
---
layout: post
title:  "INSERT title""
date:   2024-10-28
categories: seminars
---
```

Here are the meeting details:

```mail

________________________________
From: Kaisey Mandel <km723@cam.ac.uk>
Sent: 25 October 2024 15:17
To: ucam-astro-datascience@lists.cam.ac.uk <ucam-astro-datascience@lists.cam.ac.uk>
Subject: Re: Astro Data Sci on Mon, 28 Oct, 4pm Ryle: James Alvey on large time-series models

Just to correct a copy-paste error in the previous message...

The next Astro Data Science Discussion Group of this term convene on Monday, 28 October at 4-5pm in the Kavli Ryle Room. Our speaker will be James Alvey (KICC) on "Scaling laws for large time-series models: More data, more parameters" (abstract provided below).

You can join the Astro Data Science Discussion Group mailing list here<https://lists.cam.ac.uk/sympa/info/ucam-astro-datascience>, view the schedule here<https://talks.cam.ac.uk/show/index/186019>, and, if you are on the IoA Slack space, join the channel #astro-data-sci.

Cheers,
Kaisey Mandel & Organisers

Speaker: James Alvey (KICC)
Monday, 28 October, 4pm, Kavli Ryle Room

Title: Scaling laws for large time-series models: More data, more parameters
Abstract:
Scaling laws for large language models (LLMs) offer valuable insights into how increasing model size and training data leads to predictable performance improvements. Time series forecasting, which shares a sequential structure similar to language, is well-suited to large-scale transformer architectures. In this talk, I will demonstrate that foundational decoder-only time series transformer models exhibit scaling behaviour analogous to LLMs. I will begin with a general introduction to scaling laws and how they can inform efficient, optimised model training. I will then focus on their specific application to time series data, highlighting the emergence of power law behaviour. Finally, I will discuss the broader implications of these findings, and potential scientific applications.

Related papers:

https://arxiv.org/abs/2001.08361

https://arxiv.org/abs/2405.13867
```

Here is the latex of the papers his talk is based on


```bibtex
% main.bbl
\begin{thebibliography}{10}

\bibitem{kording2004bayesian}
K.~P. K{\"o}rding and D.~M. Wolpert, ``Bayesian integration in sensorimotor
  learning,'' {\em Nature}, vol.~427, no.~6971, pp.~244--247, 2004.

\bibitem{doya2007bayesian}
K.~Doya, {\em Bayesian brain: Probabilistic approaches to neural coding}.
\newblock MIT press, 2007.

\bibitem{doya2008modulators}
K.~Doya, ``Modulators of decision making,'' {\em Nature neuroscience}, vol.~11,
  no.~4, pp.~410--416, 2008.

\bibitem{funamizu2016neural}
A.~Funamizu, B.~Kuhn, and K.~Doya, ``Neural substrate of dynamic bayesian
  inference in the cerebral cortex,'' {\em Nature neuroscience}, vol.~19,
  no.~12, pp.~1682--1689, 2016.

\bibitem{lindig2022bayes}
C.~Lindig-Le{\'o}n, N.~Kaur, and D.~A. Braun, ``From bayes-optimal to heuristic
  decision-making in a two-alternative forced choice task with an
  information-theoretic bounded rationality model,'' {\em Frontiers in
  Neuroscience}, vol.~16, p.~906198, 2022.

\bibitem{west2013bayesian}
M.~West and J.~Harrison, {\em Bayesian Forecasting and Dynamic Models}.
\newblock Springer Series in Statistics, Springer New York, 2013.

\bibitem{hyndman2018forecasting}
R.~J. Hyndman and G.~Athanasopoulos, {\em Forecasting: principles and
  practice}.
\newblock OTexts, 2018.

\bibitem{torres2021deep}
J.~F. Torres, D.~Hadjout, A.~Sebaa, F.~Mart{\'\i}nez-{\'A}lvarez, and
  A.~Troncoso, ``Deep learning for time series forecasting: a survey,'' {\em
  Big Data}, vol.~9, no.~1, pp.~3--21, 2021.

\bibitem{devlin2018bert}
J.~Devlin, M.-W. Chang, K.~Lee, and K.~Toutanova, ``Bert: Pre-training of deep
  bidirectional transformers for language understanding,'' {\em arXiv preprint
  arXiv:1810.04805}, 2018.

\bibitem{brown2020language}
T.~Brown, B.~Mann, N.~Ryder, M.~Subbiah, J.~D. Kaplan, P.~Dhariwal,
  A.~Neelakantan, P.~Shyam, G.~Sastry, A.~Askell, {\em et~al.}, ``Language
  models are few-shot learners,'' {\em Advances in neural information
  processing systems}, vol.~33, pp.~1877--1901, 2020.

\bibitem{touvron2023llama}
H.~Touvron, L.~Martin, K.~Stone, P.~Albert, A.~Almahairi, Y.~Babaei,
  N.~Bashlykov, S.~Batra, P.~Bhargava, S.~Bhosale, {\em et~al.}, ``Llama 2:
  Open foundation and fine-tuned chat models,'' {\em arXiv preprint
  arXiv:2307.09288}, 2023.

\bibitem{chung2024scaling}
H.~W. Chung, L.~Hou, S.~Longpre, B.~Zoph, Y.~Tay, W.~Fedus, Y.~Li, X.~Wang,
  M.~Dehghani, S.~Brahma, {\em et~al.}, ``Scaling instruction-finetuned
  language models,'' {\em Journal of Machine Learning Research}, vol.~25,
  no.~70, pp.~1--53, 2024.

\bibitem{dosovitskiy2020image}
A.~Dosovitskiy, L.~Beyer, A.~Kolesnikov, D.~Weissenborn, X.~Zhai,
  T.~Unterthiner, M.~Dehghani, M.~Minderer, G.~Heigold, S.~Gelly, {\em et~al.},
  ``An image is worth 16x16 words: Transformers for image recognition at
  scale,'' {\em arXiv preprint arXiv:2010.11929}, 2020.

\bibitem{radford2021learning}
A.~Radford, J.~W. Kim, C.~Hallacy, A.~Ramesh, G.~Goh, S.~Agarwal, G.~Sastry,
  A.~Askell, P.~Mishkin, J.~Clark, {\em et~al.}, ``Learning transferable visual
  models from natural language supervision,'' in {\em International conference
  on machine learning}, pp.~8748--8763, PMLR, 2021.

\bibitem{ramesh2021zero}
A.~Ramesh, M.~Pavlov, G.~Goh, S.~Gray, C.~Voss, A.~Radford, M.~Chen, and
  I.~Sutskever, ``Zero-shot text-to-image generation,'' in {\em International
  conference on machine learning}, pp.~8821--8831, Pmlr, 2021.

\bibitem{yan2021videogpt}
W.~Yan, Y.~Zhang, P.~Abbeel, and A.~Srinivas, ``Videogpt: Video generation
  using vq-vae and transformers,'' {\em arXiv preprint arXiv:2104.10157}, 2021.

\bibitem{arnab2021vivit}
A.~Arnab, M.~Dehghani, G.~Heigold, C.~Sun, M.~Lu{\v{c}}i{\'c}, and C.~Schmid,
  ``Vivit: A video vision transformer,'' in {\em Proceedings of the IEEE/CVF
  international conference on computer vision}, pp.~6836--6846, 2021.

\bibitem{he2022masked}
K.~He, X.~Chen, S.~Xie, Y.~Li, P.~Doll{\'a}r, and R.~Girshick, ``Masked
  autoencoders are scalable vision learners,'' in {\em Proceedings of the
  IEEE/CVF conference on computer vision and pattern recognition},
  pp.~16000--16009, 2022.

\bibitem{li2023blip}
J.~Li, D.~Li, S.~Savarese, and S.~Hoi, ``Blip-2: Bootstrapping language-image
  pre-training with frozen image encoders and large language models,'' in {\em
  International conference on machine learning}, pp.~19730--19742, PMLR, 2023.

\bibitem{2023arXiv231010688D}
A.~{Das}, W.~{Kong}, R.~{Sen}, and Y.~{Zhou}, ``{A decoder-only foundation
  model for time-series forecasting},'' {\em arXiv e-prints},
  p.~arXiv:2310.10688, Oct. 2023.

\bibitem{2024arXiv240203885G}
M.~{Goswami}, K.~{Szafer}, A.~{Choudhry}, Y.~{Cai}, S.~{Li}, and
  A.~{Dubrawski}, ``{MOMENT: A Family of Open Time-series Foundation Models},''
  {\em arXiv e-prints}, p.~arXiv:2402.03885, Feb. 2024.

\bibitem{2023arXiv231008278R}
K.~{Rasul}, A.~{Ashok}, A.~R. {Williams}, A.~{Khorasani}, G.~{Adamopoulos},
  R.~{Bhagwatkar}, M.~{Bilo{\v{s}}}, H.~{Ghonia}, N.~V. {Hassen},
  A.~{Schneider}, S.~{Garg}, A.~{Drouin}, N.~{Chapados}, Y.~{Nevmyvaka}, and
  I.~{Rish}, ``{Lag-Llama: Towards Foundation Models for Time Series
  Forecasting},'' {\em arXiv e-prints}, p.~arXiv:2310.08278, Oct. 2023.

\bibitem{2023arXiv231003589G}
A.~{Garza} and M.~{Mergenthaler-Canseco}, ``{TimeGPT-1},'' {\em arXiv
  e-prints}, p.~arXiv:2310.03589, Oct. 2023.

\bibitem{2022arXiv221114730N}
Y.~{Nie}, N.~H. {Nguyen}, P.~{Sinthong}, and J.~{Kalagnanam}, ``{A Time Series
  is Worth 64 Words: Long-term Forecasting with Transformers},'' {\em arXiv
  e-prints}, p.~arXiv:2211.14730, Nov. 2022.

\bibitem{2024arXiv240202592W}
G.~{Woo}, C.~{Liu}, A.~{Kumar}, C.~{Xiong}, S.~{Savarese}, and D.~{Sahoo},
  ``{Unified Training of Universal Time Series Forecasting Transformers},''
  {\em arXiv e-prints}, p.~arXiv:2402.02592, Feb. 2024.

\bibitem{2023arXiv231005063W}
G.~{Woo}, C.~{Liu}, A.~{Kumar}, and D.~{Sahoo}, ``{Pushing the Limits of
  Pre-training for Time Series Forecasting in the CloudOps Domain},'' {\em
  arXiv e-prints}, p.~arXiv:2310.05063, Oct. 2023.

\bibitem{2023arXiv230512095X}
W.~{Xue}, T.~{Zhou}, Q.~{Wen}, J.~{Gao}, B.~{Ding}, and R.~{Jin}, ``{CARD:
  Channel Aligned Robust Blend Transformer for Time Series Forecasting},'' {\em
  arXiv e-prints}, p.~arXiv:2305.12095, May 2023.

\bibitem{2024arXiv240210198I}
R.~{Ilbert}, A.~{Odonnat}, V.~{Feofanov}, A.~{Virmaux}, G.~{Paolo},
  T.~{Palpanas}, and I.~{Redko}, ``{Unlocking the Potential of Transformers in
  Time Series Forecasting with Sharpness-Aware Minimization and Channel-Wise
  Attention},'' {\em arXiv e-prints}, p.~arXiv:2402.10198, Feb. 2024.

\bibitem{salinas2020deepar}
D.~Salinas, V.~Flunkert, J.~Gasthaus, and T.~Januschowski, ``Deepar:
  Probabilistic forecasting with autoregressive recurrent networks,'' {\em
  International journal of forecasting}, vol.~36, no.~3, pp.~1181--1191, 2020.

\bibitem{oreshkin2019n}
B.~N. Oreshkin, D.~Carpov, N.~Chapados, and Y.~Bengio, ``N-beats: Neural basis
  expansion analysis for interpretable time series forecasting,'' {\em arXiv
  preprint arXiv:1905.10437}, 2019.

\bibitem{oreshkin2021meta}
B.~N. Oreshkin, D.~Carpov, N.~Chapados, and Y.~Bengio, ``Meta-learning
  framework with applications to zero-shot time-series forecasting,'' in {\em
  Proceedings of the AAAI Conference on Artificial Intelligence}, vol.~35,
  pp.~9242--9250, 2021.

\bibitem{gruver2024large}
N.~Gruver, M.~Finzi, S.~Qiu, and A.~G. Wilson, ``Large language models are
  zero-shot time series forecasters,'' {\em Advances in Neural Information
  Processing Systems}, vol.~36, 2024.

\bibitem{ma2023survey}
Q.~Ma, Z.~Liu, Z.~Zheng, Z.~Huang, S.~Zhu, Z.~Yu, and J.~T. Kwok, ``A survey on
  time-series pre-trained models,'' {\em arXiv preprint arXiv:2305.10716},
  2023.

\bibitem{2024arXiv240307815F}
A.~{Fatir Ansari}, L.~{Stella}, C.~{Turkmen}, X.~{Zhang}, P.~{Mercado},
  H.~{Shen}, O.~{Shchur}, S.~{Sundar Rangapuram}, S.~{Pineda Arango},
  S.~{Kapoor}, J.~{Zschiegner}, D.~C. {Maddix}, H.~{Wang}, M.~W. {Mahoney},
  K.~{Torkkola}, A.~G. {Wilson}, M.~{Bohlke-Schneider}, and Y.~{Wang},
  ``{Chronos: Learning the Language of Time Series},'' {\em arXiv e-prints},
  p.~arXiv:2403.07815, Mar. 2024.

\bibitem{originalscaling}
J.~{Kaplan}, S.~{McCandlish}, T.~{Henighan}, T.~B. {Brown}, B.~{Chess},
  R.~{Child}, S.~{Gray}, A.~{Radford}, J.~{Wu}, and D.~{Amodei}, ``{Scaling
  Laws for Neural Language Models},'' {\em arXiv e-prints},
  p.~arXiv:2001.08361, Jan. 2020.

\bibitem{tan2019efficientnet}
M.~Tan and Q.~Le, ``Efficientnet: Rethinking model scaling for convolutional
  neural networks,'' in {\em International conference on machine learning},
  pp.~6105--6114, PMLR, 2019.

\bibitem{tan2021efficientnetv2}
M.~Tan and Q.~Le, ``Efficientnetv2: Smaller models and faster training,'' in
  {\em International conference on machine learning}, pp.~10096--10106, PMLR,
  2021.

\bibitem{raghu2021vision}
M.~Raghu, T.~Unterthiner, S.~Kornblith, C.~Zhang, and A.~Dosovitskiy, ``Do
  vision transformers see like convolutional neural networks?,'' {\em Advances
  in neural information processing systems}, vol.~34, pp.~12116--12128, 2021.

\bibitem{riquelme2021scaling}
C.~Riquelme, J.~Puigcerver, B.~Mustafa, M.~Neumann, R.~Jenatton,
  A.~Susano~Pinto, D.~Keysers, and N.~Houlsby, ``Scaling vision with sparse
  mixture of experts,'' {\em Advances in Neural Information Processing
  Systems}, vol.~34, pp.~8583--8595, 2021.

\bibitem{henighan2020scaling}
T.~Henighan, J.~Kaplan, M.~Katz, M.~Chen, C.~Hesse, J.~Jackson, H.~Jun, T.~B.
  Brown, P.~Dhariwal, S.~Gray, {\em et~al.}, ``Scaling laws for autoregressive
  generative modeling,'' {\em arXiv preprint arXiv:2010.14701}, 2020.

\bibitem{hersbach2000decomposition}
H.~Hersbach, ``Decomposition of the continuous ranked probability score for
  ensemble prediction systems,'' {\em Weather and Forecasting}, vol.~15, no.~5,
  pp.~559--570, 2000.

\bibitem{godahewa2021monash}
R.~Godahewa, C.~Bergmeir, G.~I. Webb, R.~J. Hyndman, and P.~Montero-Manso,
  ``Monash time series forecasting archive,'' in {\em Neural Information
  Processing Systems Track on Datasets and Benchmarks}, 2021.

\bibitem{emami2023buildingsbench}
P.~Emami, A.~Sahu, and P.~Graf, ``Buildingsbench: A large-scale dataset of 900k
  buildings and benchmark for short-term load forecasting,'' {\em Advances in
  Neural Information Processing Systems}, 2023.

\bibitem{liu2023largest}
X.~Liu, Y.~Xia, Y.~Liang, J.~Hu, Y.~Wang, L.~Bai, C.~Huang, Z.~Liu, B.~Hooi,
  and R.~Zimmermann, ``Largest: A benchmark dataset for large-scale traffic
  forecasting,'' in {\em Advances in Neural Information Processing Systems},
  2023.

\bibitem{2018arXiv180403209W}
P.~{Warden}, ``{Speech Commands: A Dataset for Limited-Vocabulary Speech
  Recognition},'' {\em arXiv e-prints}, p.~arXiv:1804.03209, Apr. 2018.

\bibitem{https://doi.org/10.1111/2041-210X.13103}
D.~Stowell, M.~D. Wood, H.~Pamuła, Y.~Stylianou, and H.~Glotin, ``Automatic
  acoustic detection of birds through deep learning: The first bird audio
  detection challenge,'' {\em Methods in Ecology and Evolution}, vol.~10,
  no.~3, pp.~368--380, 2019.

\bibitem{vaswani2017attention}
A.~Vaswani, N.~Shazeer, N.~Parmar, J.~Uszkoreit, L.~Jones, A.~N. Gomez,
  {\L}.~Kaiser, and I.~Polosukhin, ``Attention is all you need,'' {\em Advances
  in neural information processing systems}, vol.~30, 2017.

\bibitem{BJERREGARD2021100058}
M.~B. Bjerregård, J.~K. Møller, and H.~Madsen, ``An introduction to
  multivariate probabilistic forecast evaluation,'' {\em Energy and AI},
  vol.~4, p.~100058, 2021.

\bibitem{2018arXiv181206162M}
S.~{McCandlish}, J.~{Kaplan}, D.~{Amodei}, and {OpenAI Dota Team}, ``{An
  Empirical Model of Large-Batch Training},'' {\em arXiv e-prints},
  p.~arXiv:1812.06162, Dec. 2018.

\bibitem{2024arXiv240305530G}
{Gemini Team}, ``{Gemini 1.5: Unlocking multimodal understanding across
  millions of tokens of context},'' {\em arXiv e-prints}, p.~arXiv:2403.05530,
  Mar. 2024.

\bibitem{graphcast}
R.~{Lam}, A.~{Sanchez-Gonzalez}, M.~{Willson}, P.~{Wirnsberger},
  M.~{Fortunato}, F.~{Alet}, S.~{Ravuri}, T.~{Ewalds}, Z.~{Eaton-Rosen},
  W.~{Hu}, A.~{Merose}, S.~{Hoyer}, G.~{Holland}, O.~{Vinyals}, J.~{Stott},
  A.~{Pritzel}, S.~{Mohamed}, and P.~{Battaglia}, ``{Learning skillful
  medium-range global weather forecasting},'' {\em Science}, vol.~382,
  pp.~1416--1421, Dec. 2023.

\bibitem{fourcastnet}
J.~{Pathak}, S.~{Subramanian}, P.~{Harrington}, S.~{Raja}, A.~{Chattopadhyay},
  M.~{Mardani}, T.~{Kurth}, D.~{Hall}, Z.~{Li}, K.~{Azizzadenesheli},
  P.~{Hassanzadeh}, K.~{Kashinath}, and A.~{Anandkumar}, ``{FourCastNet: A
  Global Data-driven High-resolution Weather Model using Adaptive Fourier
  Neural Operators},'' {\em arXiv e-prints}, p.~arXiv:2202.11214, Feb. 2022.

\bibitem{osti_1854582}
E.~J.~H. Wilson, A.~Parker, A.~Fontanini, E.~Present, J.~L. Reyna, R.~Adhikari,
  C.~Bianchi, C.~CaraDonna, M.~Dahlhausen, J.~Kim, A.~LeBar, L.~Liu,
  M.~Praprost, L.~Zhang, P.~DeWitt, N.~Merket, A.~Speake, T.~Hong, H.~Li, N.~M.
  Frick, Z.~Wang, A.~Blair, H.~Horsey, D.~Roberts, K.~Trenbath, O.~Adekanye,
  E.~Bonnema, R.~El~Kontar, J.~Gonzalez, S.~Horowitz, D.~Jones, R.~T.
  Muehleisen, S.~Platthotam, M.~Reynolds, J.~Robertson, K.~Sayers, and Q.~Li,
  ``End-use load profiles for the u.s. building stock: Methodology and results
  of model calibration, validation, and uncertainty quantification,'' {\em
  Technical Report}, 3 2022.

\end{thebibliography}

```
```latex
% main.tex
\documentclass{article}

% if you need to pass options to natbib, use, e.g.:
%     \PassOptionsToPackage{numbers, compress}{natbib}
% before loading neurips_2022
\PassOptionsToPackage{numbers, sort&compress}{natbib}

% ready for submission
% \usepackage[preprint]{neurips_2024}

%\usepackage{style/neurips_2022}


% to compile a preprint version, e.g., for submission to arXiv, add add the
% [preprint] option:
%     \usepackage[preprint]{neurips_2022}


% to compile a camera-ready version, add the [final] option, e.g.:
% \usepackage[final]{neurips_2023}
% \usepackage{neurips_2024}
\usepackage[preprint]{neurips_2024}


% to avoid loading the natbib package, add option nonatbib:
%    \usepackage[nonatbib]{neurips_2022}

% Optional math commands from https://github.com/goodfeli/dlbook_notation.
\input{math_commands.tex}

\usepackage[utf8]{inputenc} % allow utf-8 input
\usepackage[T1]{fontenc}    % use 8-bit T1 fonts
\usepackage{url}            % simple URL typesetting
\usepackage{booktabs}       % professional-quality tables
\usepackage{amsfonts}       % blackboard math symbols
\usepackage{nicefrac}       % compact symbols for 1/2, etc.
\usepackage{microtype}      % microtypography
\usepackage[dvipsnames]{xcolor}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{tabularx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{booktabs}
\usepackage{wrapfig}
\usepackage{float}
% \usepackage[pagebackref,breaklinks,colorlinks]{hyperref}
\usepackage{tikz}
\usetikzlibrary{backgrounds}
\usetikzlibrary{arrows,shapes}
\usetikzlibrary{tikzmark}
\usetikzlibrary{calc}
\usepackage{graphicx}
\usepackage{xspace}
\usepackage{tcolorbox}
\usepackage{multirow}

\definecolor{dullblue}{RGB}{16, 47, 104}
\definecolor{darkgreen}{rgb}{0.075,0.302,0.047}
% \definecolor{dullred}{rgb}{0.706,0.208,0.192}
\definecolor{dullred}{RGB}{176, 36, 35}

\RequirePackage[colorlinks=true
,urlcolor=dullblue
,anchorcolor=blue
,citecolor=dullred
,filecolor=blue
,linkcolor=darkgreen
,menucolor=blue
,pagecolor=blue
,linktocpage=true
,pdfproducer=medialab
]{hyperref}

\newcommand{\te}[1]{{\color{dullred}[TE: #1]}}
\newcommand{\ja}[1]{{\color{magenta}[JA: #1]}}
\newcommand{\jaa}[1]{{\color{blue}[JAA: #1]}}

% comment out when done
\usepackage{xargs}       

\usepackage{tikz}
\usepackage{subcaption}

\usepackage{color, colortbl}
\usepackage{makecell}




\title{Scaling-laws for Large Time-series Models}

\author{%
  Thomas D. P. Edwards \\
  Johns Hopkins University \\
  \texttt{tedwar42@jhu.edu} \\
  \And
  James Alvey \\
  % Address \\
  University of Amsterdam \\
  \texttt{j.b.g.alvey@uva.nl} \\
  \AND
  Justin Alsing\\
  Calda AI \\
  Oskar Klein Centre \\
  \texttt{justin@calda.ai} \\
  \And
  Nam H. Nguyen \\
  Capital One \\
  \texttt{nam.nguyen@capitalone.com} \\
  \And
  Benjamin D. Wandelt \\
  Institut d’Astrophysique de Paris\\
  CCA, Flatiron Institute \\
  \texttt{bwandelt@iap.fr} \\
}


\begin{document}


\maketitle


\begin{abstract}
 Scaling laws for large language models (LLMs) have provided useful guidance on how to train ever larger models for predictable performance gains. Time series forecasting shares a similar sequential structure to language, and is amenable to large-scale transformer architectures. Here we show that foundational decoder-only time series transformer models exhibit analogous scaling-behavior to LLMs, while architectural details (aspect ratio and number of heads) have a minimal effect over broad ranges. We assemble a large corpus of heterogenous time series data on which to train, and establish, for the first time, power-law scaling relations with respect to parameter count, dataset size, and training compute, spanning five orders of magnitude. 
\end{abstract}

\section{Introduction}
\label{sec:intro}

Time-series forecasting is fundamental to decision-making and scientific inference across all domains involving time-ordered observations. In fact, making probabilistic forecasts given past data (whether explicitly or implicitly) arguably underpins every human decision \cite{kording2004bayesian, doya2007bayesian, doya2008modulators, funamizu2016neural, lindig2022bayes}. In industrial and scientific settings, time-series forecasting has traditionally involved supervised training of either statistical models (e.g., ARIMA, GARCH, state-space models, and others; see \citep{west2013bayesian,hyndman2018forecasting} for reviews), bespoke dynamical models based on domain-specific knowledge, or more recently deep-learning based approaches trained for a specific forecasting task (see \citep{torres2021deep} for a review). While these approaches have formed the bedrock of time-series analysis up until now, key challenges and limitations remain: statistical models often fail to describe and capture the latent processes underlying the data, hampering their predictive utility; developing specialized problem-specific models requires considerable investment in human time and resources; and supervised deep-learning approaches trained on a single dataset are typically only useful in the data-rich regime, and generalize poorly to other problems.

The emergence of large language (LLMs; \citep{devlin2018bert,brown2020language,touvron2023llama,chung2024scaling}) and computer vision models \cite{dosovitskiy2020image, radford2021learning, ramesh2021zero, yan2021videogpt, arnab2021vivit, he2022masked, li2023blip} with zero-shot prediction capabilities has sparked a growing interest in developing foundation models for time-series — general purpose models for forecasting, pre-trained on a large and diverse corpus of time-series data, with the aim of achieving state-of-the-art zero-shot forecasting performance across many domain areas~\cite{2023arXiv231010688D, 2024arXiv240203885G,2023arXiv231008278R, 2023arXiv231003589G, 2022arXiv221114730N, 2024arXiv240202592W, 2023arXiv231005063W, 2023arXiv230512095X, 2024arXiv240210198I, salinas2020deepar, oreshkin2019n, oreshkin2021meta, gruver2024large, ma2023survey, 2024arXiv240307815F}. Large time-series models (LTMs) are already achieving zero-shot prediction capability that is similar to (and in some cases better than) baseline statistical or domain-specific models in many areas \cite{2023arXiv231010688D, 2024arXiv240203885G,2023arXiv231008278R, 2023arXiv231003589G, 2022arXiv221114730N, 2024arXiv240202592W, 2023arXiv231005063W, 2023arXiv230512095X, 2024arXiv240210198I, 2024arXiv240307815F}.

Underpinning the resource investment and subsequent success of LLMs and large-scale computer vision models was the demonstration of neural scaling laws \citep{originalscaling, tan2019efficientnet, tan2021efficientnetv2, raghu2021vision, riquelme2021scaling, he2022masked, henighan2020scaling}. The observed power-law scaling of test loss with model sizes, compute resources, and training set sizes, has provided a basis for predicting the expected gains from different efforts, aiding the community in allocating resources appropriately to achieve breakthroughs in performance. The establishment of similarly favourable neural scaling laws for LTMs would serve as both a motivation and guide in the pursuit of foundation models for time-series forecasting.
%

\textbf{Contributions:} In this work, we establish for the first time neural scaling laws for large time-series models (LTMs), demonstrating that LTMs enjoy similar power-law scaling laws to language and computer vision. We train decoder-only transformer models (with architectures tailored to time-series forecasting; \S\ref{subsec:model}) on a large, diverse, and well-balanced dataset comprising around 8 billion data points across 30,211,687 individual time-series, drawn from $38$ qualitatively distinct data sources from varied areas (see \S \ref{sec:data}). We demonstrate power-law like scaling behavior of model performance with model size, compute, and dataset size (Fig. \ref{fig:scaling}). For each scaling case-study, we show similar scaling behavior in three key measures of the model performance: the mean-square error (MSE) characterizing the accuracy of point (posterior mean) forecasts; the Continuous Ranked Probability Score (CRPS \cite{hersbach2000decomposition}) characterizing the fidelity of the probabilistic predictions (ie., coverage of the forecast posterior density); and the log-likelihood loss characterizing the Kullback-Leibler (KL) divergence between the model and data generative distributions.

\textbf{Summary of Results:} In Fig.~\ref{fig:scaling} we show the scaling of model performance (MSE, CRPS and log-likelihood) with model size (top row), compute (middle row), and dataset size (bottom row). We observe power-law scaling in the log-likelihood across the full range of parameters tested, whereas the MSE and CRPS show broken power-law behavior. Parameters of the fitted power-law functions can be found in Tab.~\ref{tab:fits}. In Fig.~\ref{fig:model_shape_scaling} we show that the model performance is only weakly sensitive to architecture details (aspect ratio, and the number of heads).

\textbf{Compute Requirements:} To produce the results in this paper requires $\mathcal{O}(50 - 70)$ individual production runs. Apart from the 100M parameter run, these were all carried out on single A100 NVIDIA GPU instances, each taking between 1 and 3 days to complete. As such, overall, the work presented here required $\mathcal{O}(150)$ GPU-days of compute. To host the full dataset, we also required a CPU RAM allocation of approximately 250 GB.

\begin{figure}[t!]
    \centering
\includegraphics[width=\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{parameters_vs_loss_studentT.pdf}
\includegraphics[width=\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{compute_scaling_plot.pdf}
\includegraphics[width=\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{data_vs_loss_studentT.pdf}
    \caption{\textbf{Test Loss Scaling Laws:} Here we show three metrics for the minimum in-sequence test loss as a function of the number of parameters, compute, and dataset size. We demonstrate that, like language, the performance of large time-series models scales approximately as a power law with all three quantities. Note that we use the log-likelihood as the actual loss function for training. To ensure it remains positive for the power-law scaling we add a small constant.}
    \label{fig:scaling}
\end{figure}


\section{Data}
\label{sec:data}
The development of a foundation model for time-series forecasting is predicated on the availability of a sufficiently large, diverse, and well-balanced dataset to train on. We constructed a corpus of time-series data comprising around $8$ billion data points drawn from $38$ varied data sources (see Tab.~\ref{tab:dataset_stats}). For the purpose of this study, our focus was to ensure our dataset is: large enough so that for our largest models ($\sim 100$M parameters) we are still operating in the approximately infinite data limit (as discussed in the original LLM scaling-law paper \cite{originalscaling}); as diverse as possible given the practical limitations on publicly available data; and balanced, such that no individual dataset comprises more than roughly $15\%$ of the total number of data points. Our resulting dataset is competitive with the state-of-the-art in terms of both diversity and size\footnote{Note that where other state-of-the-art time-series datasets from recent studies are larger, this discrepency is largely accounted for by either the use of synthetic data in those studies (which we do not include in this work), and/or the reduction in our total data point numbers due to re-balancing of our data to ensure it is not dominated by a single data source.}, while covering a wide variety of sampling frequencies, record lengths, dynamic ranges, and underlying latent process phenomenology. In this study we focus exclusively on univariate time-series forecasting, and leave the study of scaling-laws for multivariate LTMs to future work.

The data sources used to construct our dataset are summarized as follows (see also Tabs. \ref{tab:dataset_stats}, \ref{tab:monash}--\ref{tab:audio}):

\textbf{Monash:} The Monash repository~\cite{godahewa2021monash} is an open-source collection of data from many sources. We exclude datasets that are too short (shorter than our context length of $256$; see \S~\ref{subsec:model}), and removed individual time-series that we found to destabilise training (due to e.g., a combination of heavy-tailed behavior and a large fraction of missing data). The included Monash data is summarized in Tab.~\ref{tab:monash}.

\textbf{Climate:} We include climate data from two sources: the National Oceanic and Atmospheric Administration (NOAA), and the fifth generation European Centre for Medium-Range Weather Forecasts atmospheric reanalysis of the global climate (ERA5). From these we select a variety of different observables and sampling frequencies, summarized in Tabs.~\ref{tab:NOAA}--\ref{tab:ERA5}.

\textbf{Energy:} Here we use a subset of the data from the \texttt{BuildingsBench} dataset \cite{emami2023buildingsbench}. The data is sampled at a fixed 15-minute cadence and represents energy demand across US commercial and real estate buildings.

\textbf{Traffic:} We use the LargeST~\cite{liu2023largest} traffic dataset from 2017-2021 which represents traffic flow in California and is made up (once processed) of a total of 8520 series.

\textbf{Finance:} We source daily returns and trading volume data for $5038$ stocks lists across various exchanges from \texttt{yahoo finance} (see Tab.~\ref{tab:finance}). For trading volume, we model the logarithm of the data (due to the large dynamic range).

\textbf{Audio:} We include a diverse set of audio data from the \textit{command}, \textit{bird}, and \textit{Arabic speech} datasets~\cite{2018arXiv180403209W, https://doi.org/10.1111/2041-210X.13103}; see Tab.~\ref{tab:audio}.

Each dataset is made up of a large number of individual time series of varying lengths. We use 95\% of the set of time series for training and the remaining 5\% for testing. Since the majority of the series are significantly longer than our context window, during training and testing we visit each series with probability $p_i = t_i/T$, where $t_i$ is the number of data points in that series and $T$ is the total number of data points in the training set. Additionally, each time we visit a series we choose a random starting index. This strategy ensures that the model sees each section of the data once (on average) in a given epoch. We normalize each time-series in the training set to have zero mean and unit standard deviation.\footnote{In rare instances where input time-series are constant (and hence have zero standard deviation), we set them to a constant value of zero.}

\begin{table}[t!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{Dataset summary}. M indicates million and B indicates billion.}
\label{tab:dataset_stats}
\begin{tabularx}{\textwidth}{l*{7}{>{\centering\arraybackslash}X}}
\toprule
& \textbf{Monash} & \textbf{Climate} & \textbf{Energy} & \textbf{Traffic} & \textbf{Finance} & \textbf{Audio} & \textbf{Total} \\ \midrule
\textbf{Datasets} & 23 & 15 & 2 & 5 & 2 & 3 & 38 \\
\textbf{\# of data points} & 503M & 1.56B & 2.5B & 1.5B  & 42.6M & 1.98B & 8.13B \\
\textbf{\% of data} & 6.18\% & 19.19\% & 30.75\% & 18.45\% & 0.52\% & 24.35\% 
& 100\% \\ \bottomrule
\end{tabularx}
\end{table}

\section{Methods}
\label{sec:training}
%
\subsection{Model and Training Details}
\label{subsec:model}

\textbf{Decoder-only Transformer:} We use decoder-only transformer models with self-attention as the primary architecture throughout, with a learned positional-encoding and flexible distribution head to make it more amenable to probabilistic time-series forecasting (as discussed below). We use a context length of $256$ data points, and ReLU activation functions throughout.

\textbf{Learned Positional Encoding and Embedding:} Following the performance gains shown in Ref.~\cite{2023arXiv231005063W}, we use a learnable encoding rather than the sinusoidal positional encoding used in the original transformer model \cite{vaswani2017attention}. Both the learned positional encoding and embedding are simple linear layers going from one input to $d_\mathrm{m}$ outputs (see below). The positional encoding is treated in the usual fashion by just adding elementwise to the embedded float.

\textbf{Distribution Head:} The distribution head defines the distribution family modelled by the transformer, and is a critical architecture choice in enabling probabilistic forecasts with accurate coverage, as well as stable training and convergence. We use a Student's-$t$ distribution head, where the mean, $\mu$, variance, $\sigma^2$, and degree of freedom, $\nu$, are separate outputs of the model.\footnote{We apply softplus activations to the distribution head outputs corresponding the variance and degrees-of-freedom, to ensure positive definiteness.} The Student's-$t$ distribution head allows us to model heavy-tailed data and processes, and in experiments we found that the Student's-$t$ head enabled significantly more stable training than a Gaussian head (or simple posterior mean forecasting with an MSE loss). We note that in reality, many time-series data and underlying processes exhibit skewness, and a distribution head family that can describe asymmetric distributions would be well-motivated (e.g., Generalized gaussians, SinhArcSinh distributions, or more expressive normalizing flow or diffusion-based heads). We leave the exploration of more expressive distribution heads to future work.
%


We use a separate multi-layer perceptron (MLP) with four hidden layers of dimension $d_\mathrm{m}$ for each output of the distribution head, i.e., the mean, variance and degrees-of-freedom of the Student's-$t$ distribution. In experiments we found that including separate MLPs for each distribution parameter (rather than a single MLP with three outputs), significantly stabilizes training. We use a negative log-likelihood loss throughout. 

\textbf{Parameter Counting:} With this setup, the model architecture is defined by the following parameters: the number of output dimensions $\theta_{\mathrm{out}}$, the input/output size of the linear layers in the self-attention $d_\mathrm{m}$, the number of heads\footnote{
    Note that adding heads does not add to the parameter count. Instead the sequence is split and passed though different heads and recombined at the end. We therefore require that $d_\mathrm{m} \, \mathrm{mod} \, N_{\mathrm{heads}} = 0$
} $N_{\mathrm{heads}}$, the hidden layer size of the linear layers directly after the self-attention $d_{\mathrm{ff}}$, and the number of decoder layers $N_\mathrm{l}$. Throughout this work we fix $d_\mathrm{m} = d_{\mathrm{ff}}$ and treat all trainable parameters (including weights and biases of all layers) equally in the parameter counting. As shown in Fig.~\ref{fig:scaling}, we explore models with $\sim 10^3$ to $\sim 10^8$ trainable parameters.


\textbf{Training Details:} We use the \texttt{AdamW} optimizer with a batch size of 512, a cosine learning rate scheduler with a linear warm up of 3000 training steps, and train for a total of $10^5$ steps. When training on the entire dataset ($\sim8$B data points), this equates to roughly two epochs. To reduce computational costs we compute the test loss every $\mathcal{O}(200)$ steps and average over a random 10\% of the test data each time. 

\subsection{Learning Rate and Architecture Dependence}
\label{subsec:LR}

\begin{figure}[t!]
    \centering
\includegraphics[width=0.7\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{maxLR.pdf}
    \caption{\textbf{Importance of Learning Rate:} Here we show the minimum CRPS measured on the test data as a function of the maximum learning rate reached at the end of the linear warm up schedule. Crosses indicate that the model diverged before training was complete. There is a clear optimum max learning rate which decreases as a function of model size/number of parameters.}
    \label{fig:LR_scaling}
\end{figure}

In order to extract reliable scaling laws, we first need to determine the sensitivity of LTM performance as a function of both architecture choices (e.g., aspect ratio and number of heads), and learning rate scheduling.

\textbf{Learning Rate Scheduling:} In training we use a linear warm up followed by sinusoidal decay for the learning rate scheduling. In Fig.~\ref{fig:LR_scaling} we show the effect of changing the maximum learning rate reached at the end of the warm up. The performance of the model (CRPS) clearly depends on the maximum learning rate, and that dependence is itself a function of parameter count. The dependence on maxmimum learning rate is strong enough that it is possible to get better performance with a smaller model, if the maximum learning rate is too small (or too large) for the larger model. Moreover, for a fixed model size we see a clear optimum learning rate above which models diverge (shown as crosses on       Fig.~\ref{fig:LR_scaling}). To ensure that we used an optimal maximum learning rate as a function of model size, we fit a power law with a constant offset to the best models (at each parameter size) shown in Fig. 2. In the few cases for the largest models where our power law fit overestimates the optimal maximum learning rate (leading to divergence), we slowly reduce the learning rate until we achieve convergence.

\textbf{Aspect Ratio and Number of Heads:} Figure~\ref{fig:model_shape_scaling} shows how the minimum CRPS varies as a function of aspect ratio $d_m/N_\mathrm{l}$ (left panel) and the number of attention heads, $N_{\mathrm{heads}}$ (right panel).  Overall, we find that neither of these choices have a large effect on performance; we note that this is similar to the weak architecture sensitivity observed for LLMs \cite{originalscaling}. This is most clearly seen in the right panel of Fig.~\ref{fig:model_shape_scaling} where we are able to keep the number of parameters constant whilst varying the number of attention heads. For both model sizes tested, there is no significant change in the minimum CRPS achieved as more heads are added. For the main parameter, compute, and data scaling runs (the main results of this paper), we fix the number of heads to four.

Performance as a function of aspect ratio shows a slightly more complex behavior. In particular, we find smaller aspect ratios tend to perform better. However, this dependence is only weak up until aspect ratios of $>128$, after which the model performance decreases substantially. Based on these observations, we keep the aspect ratio $<70$ for all scaling runs.

\section{Scaling and Optimality}
\label{sec:results}

We now discuss the scaling results as a function of parameter count $N_p$, dataset size $\mathcal{D}$, and compute $\mathcal{C}$. For each scaling-relation, we fit a power law with the form:
\begin{equation}
    L(A) = \left(\frac{A}{A_0}\right)^{-B_0}\,,
\end{equation}
where $L$ is the objective function (i.e., MSE, CRPS, or log-likelihood) and $A$ is the quantity being scaled (i.e., parameter count $N_p$, dataset size $\mathcal{D}$, or compute $\mathcal{C}$. The fitted values of the normalization $A_0$ and index $B_0$ for each scaling-law are given in Tab.~\ref{tab:fits}. Where broken power-law like scaling is observed, we report the power law fit after the break only, since this is the relevant quantity to motivate extrapolation to larger models / datasets / compute resources. 
\begin{figure}[t!]
    \centering
\includegraphics[width=\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{n_heads_AR_combined.pdf}
    \caption{\textbf{Importance of Transformer Architecture:} We show the minimum CRPS on the test set as a function of architecture choices and number of parameters. \textit{Left:} Performance on the test data has a weak dependence on aspect ratio below $<100$ but degrades significantly $>128$. We therefore keep aspect ratios $<70$ for all scaling runs. \textit{Right:} Here we see that the number of attention heads has no noticeable affect on the performance for both model sizes tested. We fix the number of heads to four for the scaling runs.} 
    \label{fig:model_shape_scaling}
\end{figure}

\subsection{Parameter Scaling}
\label{sec:par_scale}

First we look at parameter scaling which is shown in the top panels of Fig.~\ref{fig:scaling}. In particular, we plot the in-sequence test loss computed for the MSE, CRPS, and log-likelihood (which is used as the loss function during training). For each model size we only plot the minimum test loss. We can see that all loss functions follow approximately power-law behavior over nearly five orders of magnitude in model size. This trend is particularly well observed in the log-likelihood. Note that we added a constant factor of two to the log-likelihood, to keep it positive.\footnote{
    We note here that a constant additive factor can change the slope of the fitted power-law. To remain as agnostic as possible we choose to add the smallest integer required to make all values of the loss positive (i.e., two).
}

Interestingly, we do see a slight break in the power-law behavior in both the MSE and CRPS test losses, although this is mainly due to the behavior of models at very low parameter count. We plan to investigate the details of this break in future work. To ensure that power-law scaling isn't biased by this break, we only fit to models with $>10^5$ parameters. This difference between the MSE and log-likelihood is not surprising as the MSE only tests the performance of the model to predict the mean whereas the log-likelihood captures the distribution. On the other hand, the difference in the scaling behavior seen across the CRPS score is slightly more surprising. A possible explanation for this discrepancy is that the log-likelihood is known to be more sensitive to variations in the tails of the forecast (Student's-$t$) distribution~\cite{BJERREGARD2021100058}.
Regardless of these details, this observed scaling over many orders of magnitude is remarkable and demonstrates that LTMs are likely to reach state-of-the-art performance given enough data and model size.


\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{Power-law fits.}}
\label{tab:fits}
\begin{tabularx}{0.9\textwidth}{l|*{2}{>{\centering\arraybackslash}X}|*{2}{>{\centering\arraybackslash}X}|*{2}{>{\centering\arraybackslash}X}}
\toprule
& \multicolumn{2}{c|}{MSE} & \multicolumn{2}{c|}{CRPS} & \multicolumn{2}{c}{Log-Likelihood} \\
& $\log_{10}(A_0)$ & $B_0$ & $\log_{10}(A_0)$ & $B_0$ & $\log_{10}(A_0)$ & $B_0$ \\ \midrule
Number of Parameters, $N_p$ & -19.47 & 0.042 & -22.64 & 0.036 & 4.33 & 0.151 \\
Training Compute, $\mathcal{C}$ & -38.88 & 0.031 &  -43.03 & 0.028 & -6.65 & 0.101 \\
Dataset Size, $\mathcal{D}$ & -8.91 & 0.062 & -30.42 & 0.027 & 7.00 & 0.188 \\ \bottomrule
\end{tabularx}
\end{table}


\subsection{Data Scaling}
\label{sec:data_scale}

Scaling the dataset in a coherent manner requires some care. In particular, we find that to achieve reliable scaling behavior as the dataset size grows requires one to keep the diversity approximately fixed i.e., the proportion of each dataset's contribution to the total must remain the same (see Tab.~\ref{tab:dataset_stats}). For data that is significantly longer than our context length, we simply use a random fraction, $f_d$, of each time series. For data that would become shorter than our context length once cut, we instead randomly drop the entire series with probability equal to $1-f_d$. To compute the test loss, however, we average over the full test set as in the parameter scaling runs. This is to allow direct comparison between data scaling runs with different values of $f_d$, and reduce the noise in the test loss computation for small dataset sizes. 

Results are shown in the bottom panel of Fig.~\ref{fig:scaling} where we train a $\sim 20$M parameter model using the optimum max learning rate found during the parameter scaling exploration as well as early stopping. We again find power-law scaling across approximately four orders of magnitude. Interestingly, all three loss functions scale as a power law over the full range tested, although there is a mild indication of saturation for the largest dataset sizes.\footnote{
    Ideally we would use a larger model to ensure we are operating in the approximately infinite parameter limit, but we were limited by computational resources.
} Results of the power-law fits are shown in the bottom row of Tab.~\ref{tab:fits}.

\subsection{Compute Scaling}
\label{sec:compute_scale}

Finally, we turn to compute scaling where we again follow a similar method to Ref.~\cite{originalscaling}. In particular, the compute at any given stage in the training process is given by $\mathcal{C} = 6BN_\mathrm{p}L_\mathrm{seq}$ where $B$ is the batch size, $N_\mathrm{p}$ is the number of parameters in the model, and $L_\mathrm{seq}$ is the context length. Test losses as a function of compute are shown in Fig.~\ref{fig:scaling} (middle panel) and the scaling law is obtained by taking the minimum value at any given value of compute. Although we see a significant amount of noise in the loss functions during training, there is a clear overall trend towards lower test losses for higher compute which is accurately tracked by a power law.

Similarly to the parameter scaling we see a slight break at low values of compute for both the MSE and CRPS test losses. We therefore again choose to only fit to data above $10^{-7}$ PF-days. Finally, we note that the steepness of the log-likelihood test losses at large compute values indicates that the models are not yet fully converged. The effect is more dramatic at larger model sizes, indicating that further tuning of the models and learning rate scheduling can still improve performance. We empirically observe that the test loss tends to plateau in the middle of training and then decrease again as the scheduler reaches low values of the learning rate (towards the end of the sinusoidal decay). Further work is needed to test whether an alternative scheduler can improve overall performance and thus further improve model scaling.

\section{Discussion and Limitations}
\label{sec:discussion}

Throughout this paper we have focused on evaluating models by their in-sequence test loss, and have not discussed explicitly how this translates into a model's ability to forecast into the future. Again taking inspiration from LLMs, we have implicitly assumed that a model which produces good in-sequence predictions should naturally be able to forecast into the future. This is theoretically and empirically well-motivated; as the modelled posterior predictive distribution for the next value becomes increasingly well-calibrated, any accumulating errors from auto-regressively rolling out those predictions into the future should also decrease (leading to more accurate prediction further into the future). In App.~\ref{app:forecast}, we show some clear examples of how forecast roll-out becomes increasingly coherent with increasing model size (and corresponding decreases in test loss)~\cite{2024arXiv240202592W, 2024arXiv240307815F}. We leave the study of scaling-laws based on rolled out forecasting ability (on different time horizons) to future work.

We have detailed the specific scaling laws for a decoder-only transformer with self-attention. However, it would be interesting to explore how modifications to this architecture might improve model scaling. In particular, much of the recent progress in using LTMs~\cite{2023arXiv231010688D, 2024arXiv240203885G,2023arXiv231008278R, 2023arXiv231003589G, 2022arXiv221114730N, 2024arXiv240202592W, 2023arXiv231005063W, 2023arXiv230512095X, 2024arXiv240210198I, 2024arXiv240307815F} has involved various changes to transformer architectures to make them more suited to time-series data. We advocate for comparative scaling law studies as new architectures are introduced, to allow the community to evaluate which model architectures will eventually reach state-of-the-art zero-shot prediction capabilities.

When experimenting with data scaling, we found it was neccessary to scale the training data in such a way as to (approximately) preserve the data diversity in the scaled training set (i.e., keep relative contributions of each data source constant). Approaches to data scaling that did not preserve data diversity failed to reveal clear scaling behaviour; we attributed this to the resulting variation in data diversity dominating over any scaling behaviour. Given the importance of training data diversity in establishing data scaling laws, and in training state-of-the-art pre-trained foundation models in general, developing a robust framework for measuring data diversity would be of great utility to the field. Taking inspiration from Ref.~\cite{2018arXiv181206162M}, one avenue could be looking at the impact of new data sources on gradients during training; data which produce gradients with a high cosine similarity compared to the current training set would be likely to increase data diversity. We leave exploration of measures of data diversity to future work.


An additional scaling law that we have not explored in this work (due to computational limitations) is performance as a function of increasing context length. Multiple studies (e.g., \cite{2024arXiv240307815F, 2024arXiv240305530G}), both for LLMs and LTMs, have shown that increasing the context length window significantly improves both in-sequence prediction as well as forecasting. This should be particularly apparent for time series data as increasing context length gives the LTMs access to lower frequency modes of variability, which might otherwise be missed. We will explore context-length scaling in future work.

In this work we have focused exclusively on univariate time-series data. However, a general purpose foundation model for time-series forecasting should be able to cope with the more general setting of multivariate time-series prediction, while accounting for multiple exogeneous covariates. Establishing scaling-laws for multivariate time-series forecasting would be an important extension to this work. This will demand the assembly of a large and diverse training set of multivariate data, each with their own (varying number of) exogeneous factors.

Finally, the literature on transformers for time series forecasting has, to date, mostly focused on trying to achieve state-of-the-art performance on a small set of benchmark experiments. Our results indicate that large scale pre-training leads to scalable performance improvements that, given enough time and compute, can result in state-of-the-art performance across the majority of benchmarks.

\textbf{Impact Statement and Ethics:} The main goal of this paper is to advance the fields of machine learning and foundational time series forecasting. Time series forecasting has numerous applications across both commercial sectors and other critical areas such as healthcare, climate science, finance, and energy management. By improving forecasting techniques, our work can contribute to more accurate predictions and better decision-making in these diverse fields. Due the exploratory nature of this work, it is highly unlikely that there are direct negative societal impacts of the current study. In addition, there are no specific ethical implications of our work that are relevant for further discussion here. Indeed, we confirm that everything in this paper complies with the NeurIPS Code of Ethics.


\textbf{Acknowledgments:} TE thanks Jared Kaplan for providing initial motivation that these scaling laws would appear. TE is supported by the Horizon Postdoctoral Fellowship. We thank Hiranya Peiris for providing access to GPU compute resources. JA has been supported by funding from the
European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programmes (grant agreement no. 101018897 CosmicExplorer). This work partly was carried out at the Advanced Research Computing at Hopkins (ARCH) core facility  (rockfish.jhu.edu), which is supported by the National Science Foundation (NSF) grant number OAC 1920103. Some of this work was also carried out on the Snellius Compute Cluster at SURFsara.



\bibliographystyle{ieeetr}
\bibliography{main.bib}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\appendix

\newpage
\section{Dataset Details}
\label{app:data}

In this section we detail the various sources that form the basis of our dataset and the choices made during its construction. Throughout data acquisition we had two critical features that the dataset needed to satisfy to facilitate the study of the main paper. Firstly, we needed a large enough dataset to train models up to $\mathcal{O}(100)\mathrm{M}$ parameters. This is particularly important as the original work~\cite{originalscaling} demonstrated scaling laws over many orders of magnitude. Although we were limited here by computational resources, it was important to explore the parameter range $10^3 - 10^8$ (the current range used in other transformer based time series models). Secondly, the dataset needed to be sufficiently balanced across sources and features such that the scaling laws observed here can be considered a feature of foundation models and not associated with a particular dataset.

Taking inspiration from large language models~\cite{originalscaling}, we therefore aimed to gather around $\mathcal{O}(10^{10})$ data points from a variety of domains. We note, however, that treating a single floating point number on a similar footing to a language token is not necessarily a good comparison. In particular, language tokens can contain significantly more semantic meaning than a floating point number can. It's therefore likely that we will need more data points overall, although more work is required to make this comparison more precise.
Before detailing our particular sources, we would like to emphasize that there is an enormous corpus of time series data publicly available but is not currently formatted for easy downloading and processing. Ref.~\cite{2024arXiv240202592W} is the first paper to open-source a fairly large dataset but significant work is still required to expand its size and diversity.\footnote{
    Note that by the time this data became open-source we had already fixed our dataset.
} For example, large-scale, state-of-the-art language models are likely trained on well over a trillion tokens. 

We now discuss each dataset presented in Tab.~\ref{tab:dataset_stats}. Overall, we assembled approximately 8B data points from six domains, each with a its own source of variation.

All data used throughout this work has been labelled/licensed as free to use for non-commercial purposes with the appropriate citations. We have included the appropriate citations where necessary below.

\subsection{Monash}

The Monash dataset has been the default repository of open-source time series data used by the academic community for some time~\cite{godahewa2021monash}. It contains data from a huge variety of sources and contains a wide variety of characteristics. For this work we exclude series that are either too short or are particularly noisy.\footnote{
    We found through experimentation that removing very noisy datasets significantly improved training stability.
}
We are then left with a total of 23 different sources which add up to a total of $\sim 500\mathrm{M}$ data points; details are given in Tab.~\ref{tab:monash}.

\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{Monash Data:} For each dataset we list the sampling frequency, the total number of series, and the total number of data points.}
\label{tab:monash}
\begin{tabularx}{\textwidth}{l|*{3}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Dataset} & \textbf{Frequency} & \textbf{Number of Series} & \textbf{Number of Data Points} \\ \midrule
London Smart Meters & Half Hourly & 5,560 & 166.5M \\
Wind Farms & Every Minute & 339 & 172.1M \\
Wind Power & 4 Seconds Intervals& 1 & 7.4M \\
Solar Power & 4 Second Intervals & 1 & 7.4M \\
Oikolab Weather & Hourly & 8 & 0.8M \\
Elecdemand & Half Hourly & 1 & 17.5k \\
Kaggle Web Traffic & Daily & 145,063  & 116.5M \\
Tourism Quarterly & Quarterly & 427 & 42.5k \\
Tourism Monthly & Monthly & 366 & 109.3k \\
CIF 2016 & Monthly & 72 & 7.1k \\
Traffic Weekly & Weekly & 862 & 89.6k \\
Traffic Hourly & Hourly & 862 & 15.1M \\
Australian Electricity & Half Hourly & 5 & 1.2M \\
Sunspot & Daily & 1 & 73.9k \\
Hospital & Monthly & 767 & 64.4k \\
NN5 Daily & Daily & 111 & 87.8k \\
NN5 Weekly & Weekly & 111 & 12.5k \\
M4 Hourly & Hourly & 414 & 373.4k \\
Fred MD & Monthly & 107 & 77.9k \\
Solar Weekly & Weekly & 137 & 7.1k \\
Solar 10 Minutes & 10 Minute Intervals & 137 & 7.2M \\
Electricity Weekly & Weekly & 321 & 50.1k \\
Electricity Hourly & Hourly & 321 & 8.4M \\
\bottomrule

\end{tabularx}
\end{table}


\subsection{Climate}

Our climate dataset, made up of around 1.5B data points, has two primary sources: the National Oceanic and Atmospheric Administration (NOAA) and the fifth generation European Centre for Medium-Range Weather Forecasts atmospheric reanalysis of the global climate (ERA5). Each source provides approximately 750M data points split across a variety of observables and time frames.

We note here that since the global climate is a correlated system, forecasting a single variable into the future whilst ignoring the evolution of the rest of the system is intrinsically difficult (maybe impossible in some cases). Nevertheless, each time series can provide important information from which the foundation model can learn correlations. Moreover, some seasonal trends are very stable and predictable from a single time series. Future work should carefully consider how to include climate data in a way that allows the model to exploit correlations inherent in the data~\cite{graphcast, fourcastnet}.


\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{NOAA Data:} For each dataset we list the sampling frequency, the total number of series, the length of each series, and the total number of data points.}
\label{tab:NOAA}
\begin{tabularx}{\textwidth}{l|*{4}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Dataset} & \textbf{Frequency} & \textbf{Number of Series} & \textbf{Length} & \textbf{Number of Data Points} \\ \midrule
SST Mean & Daily & 582241 & 365 & 212.5M  \\
SST Anomalies & Daily & 581249 & 365 & 212.1M  \\
SST Long Term Average & Daily & 218211 & 365 & 79.6M  \\
SST Monthly Average & Monthly & 72730 & 509 & 37M  \\
SST Weekly Average & Monthly & 72689 & 2214 & 161M  \\ \midrule

Ice Mean & Daily & 63971 & 365 & 23M  \\
Ice Long Term Average & Daily & 12451 & 365 & 4.5M  \\
Ice Monthly Average & Daily & 5363 & 509 & 2.7M  \\ \midrule

Radiation Long Term Average & Daily & 6622 & 365 & 2.4M  \\ \bottomrule

\end{tabularx}
\end{table}

\vskip 6pt

\textbf{NOAA:} We primarily gather data from NOAA high-resolution blended analysis of daily sea surface temperature (SST) which includes both temperature measurements and ice level measurements on a $0.25^{\circ}$ grid worldwide.\footnote{
    The original data can be found here \url{https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/}.
} Weather at different points of the grid are intrinsically correlated, especially on such small grid sizes. We therefore downsample the data by a factor of three by randomly choosing grid points without replacement (we do this independently for each dataset). 

To ensure we have data that covers a wide range of time scales and variability we pick a variety of observables shown in Tab.~\ref{tab:NOAA}. For the daily data we pick 8 years of data, each separated by 5 years (spread out to maximize data diversity i.e., minimize year to year correlations) but skip leap years for easier data processing (so all arrays are 365 elements long). The final year selection is 1985, 1990, 1995, 2001, 2005, 2010, 2015, and 2021. This size of this dataset could easily be supplemented simply by adding more of the 40 years of available data.

For additional diversity we use the same method to extract outgoing long wave radiation time series from \url{https://downloads.psl.noaa.gov/Datasets/uninterp_OLR/}. This is the shown in the final row of Tab.~\ref{tab:NOAA}.


\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{ERA5 Data:} Similar to above. The different number of series for each dataset is due to the randomness in the subsampling.}
\label{tab:ERA5}
\begin{tabularx}{\textwidth}{l|*{4}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Dataset} & \textbf{Frequency} & \textbf{Number of Series} & \textbf{Length} & \textbf{Number of Data Points} \\ \midrule
Sea Level Pressure & 4 Hour Intervals & 63094 & 2190 & 138M \\
2m Temp. & 4 Hour Intervals & 63190 & 2190 & 138M \\
2m Dewpoint Temp. & 4 Hour Intervals & 63123 & 2190 & 138M \\
Surface Pressure & 4 Hour Intervals & 63263 & 2190 & 139M \\
10m V Wind Comp. & 4 Hour Intervals & 63263 & 2190 & 139M \\ 
10m U Wind Comp. & 4 Hour Intervals & 63220 & 2190 & 138M \\ \bottomrule

\end{tabularx}
\end{table}
%
\textbf{ERA5:} We take a similar approach to above when processing/gathering ERA5 data. Here though, we focus on higher frequencies by using a single year of data (2001) sampled every four hours. We additionally use different data variables (the six most popular variables) to ensure that the data features are likely different to those present in the NOAA data. ERA5 data is also originally on a $0.25^{\circ}$ global grid which we randomly down sample by a factor of four. Details are given in Tab.~\ref{tab:ERA5}.

\subsection{Energy}

For the energy dataset, we use the benchmark dataset prepared in the \texttt{BuildingsBench} data release~\cite{emami2023buildingsbench}. In particular, we choose to sample 2.5B data points from the full dataset (which totals over 15B individual data points). These 2.5B data points, which overall constitute approximately 30\% of our full dataset, are all taken from the Buildings-900K database. These time series represent a large-scale sample of simulated US building energy demand and are designed to be broadly representative of US commercial and residential building stock. As described in~\cite{emami2023buildingsbench}, the dataset is originally sourced from the NREL EULP database~\cite{osti_1854582}, which provides 15- minute resolution, appliance-level consumption for 550K residential and 350K commercial buildings spread across all climate regions in the U.S. For more finer-grained details, see App.~B.3 in Ref.~\cite{emami2023buildingsbench}.

\subsection{Traffic}

We consider the public LargeST~\cite{liu2023largest} dataset which is a collection of 8600 time series recorded from traffic sensors in the California area. The data spans over 5 years, from 2017 to 2021, and is sampled at 15 minute resolution. To reduce the data size, we down-sample the data to hourly resolution and remove series that contains over $50\%$ missing entries. This gives us a total of 8520 series all with length 175296, which translates to 1.46B data points.     


\subsection{Finance}

We include daily stock returns and volume data, treated as separate one-dimensional time-series respectively, for $5038$ stocks listed across the Nasdaq, NYSE, and AMEX stock exchanges. Daily stock returns and volume tickers are obtained for $7230$ stocks from \texttt{yahoo finance}, from the beginning of each listing up to 1st January 2024. We discard any stocks that have fewer than $512$ ticks (recorded trading days), and any series containing \texttt{NaN} or \texttt{inf}. This results in time-series for $5038$ stocks, with both returns and volume data, and a total of $42.6$M data points (Tab. \ref{tab:finance}).
%
\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{Finance Data:} Daily stock returns and volume data for $5038$ stocks listed across the Nasdaq, NYSE and AMEX exchanges, obtained from \texttt{yahoo finance}.}
\label{tab:finance}
\begin{tabularx}{\textwidth}{l|*{3}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Dataset} & \textbf{Frequency} & \textbf{Number of Series} & \textbf{Number of Data Points} \\ \midrule
Stock Returns & Daily & 5038 & 26.3M  \\
Stock Volume & Daily & 5038 & 26.3M  \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Audio}

Audio data is intrinsically a one dimensional time series rich with structure and features; it is therefore perfectly suited for our study.  We have three primary sources of audio data, all from the DagsHub Open-Source Audio Datasets repository (\url{https://github.com/DagsHub/audio-datasets}). Again, the total volume of data here is extremely large and can be used to supplement future datasets for larger models. Here we use three particular sources each from a different domain to enhance its diversity. As presented in Tab~\ref{tab:dataset_stats}, these three sources add up to approximately 2B data points and $\sim 25\%$ of our overall dataset. A summary of the three sources can be found in Tab.~\ref{tab:audio}

\begin{table}[h!]
\renewcommand{\arraystretch}{1.2}
\centering
\caption{\textbf{Audio Data:} Similar to above.}
\label{tab:audio}
\begin{tabularx}{\textwidth}{l|*{4}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Dataset} & \textbf{Frequency} & \textbf{Number of Series} & \textbf{Length} & \textbf{Number of Data Points} \\ \midrule
Commands & 16 $\mathrm{kHz}$ & 47650 & 16,000 & 762.4M  \\

Arabic Speech & 24 $\mathrm{kHz}$ & 1813 & Varied & 329.9M  \\

Bird Audio & 22 $\mathrm{kHz}$  & 4000 & Varied & 888.3M  \\ \bottomrule

\end{tabularx}
\end{table}


\textbf{Commands:} The speech command dataset~\cite{2018arXiv180403209W} is made up of a series of short audio files with different voices saying a collection of common English words (e.g., ``happy'' and ``five''). From all the data provided \url{https://github.com/DagsHub/audio-datasets/blob/main/Speech_Commands_Dataset/README.md} we take a random half of the data and exclude any clips that are not 16k long (again for easy saving). We are then left with 47650 series, making a total of $\sim 750\mathrm{M}$ data points.

\vskip 3pt

\textbf{Arabic Speech:} This dataset contains 1813 time series of high quality (studio recorded) spoken Arabic utterances sampled at $48\mathrm{kHz}$ -- \url{https://github.com/DagsHub/audio-datasets/tree/main/Arabic-Speech-Corpus}. To reduce the data size without dramatically affecting its quality, we down sample the data by a factor of two (human speech is typically below $24\mathrm{kHz}$). This gives us a total of $\sim 300\mathrm{M}$ data points.

\vskip 3pt

\textbf{Birds:} Finally, we use the bird detection dataset from \url{https://github.com/DagsHub/audio-datasets/blob/main/Bird-Audio-Detection-challenge/README.md}~\cite{https://doi.org/10.1111/2041-210X.13103}. This dataset contains a combination of bird and other sounds designed to train machine learning algorithms to detect bird noises. Here we ignore the labels and use the entire dataset in training. Again, to reduce data volumes we down sample by a factor of two, and only use a randomly chosen half of the data. This leaves us with 4000 time series sampled at 22 $\mathrm{kHz}$ for a total of $\sim 900\mathrm{M}$ data points.

\begin{figure}[t!]
    \centering
\includegraphics[width=\linewidth,trim={0.1cm 0.1cm 0.1cm 0.1cm},clip]{forecasts.pdf}
    \caption{\textbf{In-sequence test loss to forecasting:} Here we show the connection between improved in-sequence test loss and forecasting performance as a function of model size. In particular, we show the true data in black with $1\sigma$ ranges for both in-sequence and forecasting predictions. It is clear that as in-sequence test loss decreases, forecasting also becomes substantially more predictive.}
    \label{fig:forecast}
\end{figure}

\section{In-Sequence Predictions to Forecasting}
\label{app:forecast}


Here we simply show an example of how in-sequence test loss correlates with forecasting prediction from roll-out. In particular, in Fig.~\ref{fig:forecast} we show forecasts for three different datasets as a function of model size. Here we use the best weights (i.e., the model that achieved the lowest test loss during training) for each model size and show both in-sequence and forecasting along with the true data. For both the in-seqeunce and forecasting predictions we show the $1\sigma$ range of predictions. Although not perfect, it's clear that as one scales up model size (and therefore in-sequence test loss decreases), forecasting performance also improves substantially. Although we only show three examples here, we observe a similar trend in the forecasting power of our models for a variety of datasets. We leave a more detailed exploration to future work.


\end{document}

```
```latex
% math_commands.tex
%%%%% NEW MATH DEFINITIONS %%%%%

\usepackage{amsmath,amsfonts,bm}

% Mark sections of captions for referring to divisions of figures
\newcommand{\figleft}{{\em (Left)}}
\newcommand{\figcenter}{{\em (Center)}}
\newcommand{\figright}{{\em (Right)}}
\newcommand{\figtop}{{\em (Top)}}
\newcommand{\figbottom}{{\em (Bottom)}}
\newcommand{\captiona}{{\em (a)}}
\newcommand{\captionb}{{\em (b)}}
\newcommand{\captionc}{{\em (c)}}
\newcommand{\captiond}{{\em (d)}}

% Highlight a newly defined term
\newcommand{\newterm}[1]{{\bf #1}}


% Figure reference, lower-case.
\def\figref#1{figure~\ref{#1}}
% Figure reference, capital. For start of sentence
\def\Figref#1{Figure~\ref{#1}}
\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
% Section reference, lower-case.
\def\secref#1{section~\ref{#1}}
% Section reference, capital.
\def\Secref#1{Section~\ref{#1}}
% Reference to two sections.
\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
% Reference to three sections.
\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
% Reference to an equation, lower-case.
\def\eqref#1{equation~\ref{#1}}
% Reference to an equation, upper case
\def\Eqref#1{Equation~\ref{#1}}
% A raw reference to an equation---avoid using if possible
\def\plaineqref#1{\ref{#1}}
% Reference to a chapter, lower-case.
\def\chapref#1{chapter~\ref{#1}}
% Reference to an equation, upper case.
\def\Chapref#1{Chapter~\ref{#1}}
% Reference to a range of chapters
\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
% Reference to an algorithm, lower-case.
\def\algref#1{algorithm~\ref{#1}}
% Reference to an algorithm, upper case.
\def\Algref#1{Algorithm~\ref{#1}}
\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
% Reference to a part, lower case
\def\partref#1{part~\ref{#1}}
% Reference to a part, upper case
\def\Partref#1{Part~\ref{#1}}
\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}

\def\ceil#1{\lceil #1 \rceil}
\def\floor#1{\lfloor #1 \rfloor}
\def\1{\bm{1}}
\newcommand{\train}{\mathcal{D}}
\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}

\def\eps{{\epsilon}}


% Random variables
\def\reta{{\textnormal{$\eta$}}}
\def\ra{{\textnormal{a}}}
\def\rb{{\textnormal{b}}}
\def\rc{{\textnormal{c}}}
\def\rd{{\textnormal{d}}}
\def\re{{\textnormal{e}}}
\def\rf{{\textnormal{f}}}
\def\rg{{\textnormal{g}}}
\def\rh{{\textnormal{h}}}
\def\ri{{\textnormal{i}}}
\def\rj{{\textnormal{j}}}
\def\rk{{\textnormal{k}}}
\def\rl{{\textnormal{l}}}
% rm is already a command, just don't name any random variables m
\def\rn{{\textnormal{n}}}
\def\ro{{\textnormal{o}}}
\def\rp{{\textnormal{p}}}
\def\rq{{\textnormal{q}}}
\def\rr{{\textnormal{r}}}
\def\rs{{\textnormal{s}}}
\def\rt{{\textnormal{t}}}
\def\ru{{\textnormal{u}}}
\def\rv{{\textnormal{v}}}
\def\rw{{\textnormal{w}}}
\def\rx{{\textnormal{x}}}
\def\ry{{\textnormal{y}}}
\def\rz{{\textnormal{z}}}

% Random vectors
\def\rvepsilon{{\mathbf{\epsilon}}}
\def\rvtheta{{\mathbf{\theta}}}
\def\rva{{\mathbf{a}}}
\def\rvb{{\mathbf{b}}}
\def\rvc{{\mathbf{c}}}
\def\rvd{{\mathbf{d}}}
\def\rve{{\mathbf{e}}}
\def\rvf{{\mathbf{f}}}
\def\rvg{{\mathbf{g}}}
\def\rvh{{\mathbf{h}}}
\def\rvu{{\mathbf{i}}}
\def\rvj{{\mathbf{j}}}
\def\rvk{{\mathbf{k}}}
\def\rvl{{\mathbf{l}}}
\def\rvm{{\mathbf{m}}}
\def\rvn{{\mathbf{n}}}
\def\rvo{{\mathbf{o}}}
\def\rvp{{\mathbf{p}}}
\def\rvq{{\mathbf{q}}}
\def\rvr{{\mathbf{r}}}
\def\rvs{{\mathbf{s}}}
\def\rvt{{\mathbf{t}}}
\def\rvu{{\mathbf{u}}}
\def\rvv{{\mathbf{v}}}
\def\rvw{{\mathbf{w}}}
\def\rvx{{\mathbf{x}}}
\def\rvy{{\mathbf{y}}}
\def\rvz{{\mathbf{z}}}

% Elements of random vectors
\def\erva{{\textnormal{a}}}
\def\ervb{{\textnormal{b}}}
\def\ervc{{\textnormal{c}}}
\def\ervd{{\textnormal{d}}}
\def\erve{{\textnormal{e}}}
\def\ervf{{\textnormal{f}}}
\def\ervg{{\textnormal{g}}}
\def\ervh{{\textnormal{h}}}
\def\ervi{{\textnormal{i}}}
\def\ervj{{\textnormal{j}}}
\def\ervk{{\textnormal{k}}}
\def\ervl{{\textnormal{l}}}
\def\ervm{{\textnormal{m}}}
\def\ervn{{\textnormal{n}}}
\def\ervo{{\textnormal{o}}}
\def\ervp{{\textnormal{p}}}
\def\ervq{{\textnormal{q}}}
\def\ervr{{\textnormal{r}}}
\def\ervs{{\textnormal{s}}}
\def\ervt{{\textnormal{t}}}
\def\ervu{{\textnormal{u}}}
\def\ervv{{\textnormal{v}}}
\def\ervw{{\textnormal{w}}}
\def\ervx{{\textnormal{x}}}
\def\ervy{{\textnormal{y}}}
\def\ervz{{\textnormal{z}}}

% Random matrices
\def\rmA{{\mathbf{A}}}
\def\rmB{{\mathbf{B}}}
\def\rmC{{\mathbf{C}}}
\def\rmD{{\mathbf{D}}}
\def\rmE{{\mathbf{E}}}
\def\rmF{{\mathbf{F}}}
\def\rmG{{\mathbf{G}}}
\def\rmH{{\mathbf{H}}}
\def\rmI{{\mathbf{I}}}
\def\rmJ{{\mathbf{J}}}
\def\rmK{{\mathbf{K}}}
\def\rmL{{\mathbf{L}}}
\def\rmM{{\mathbf{M}}}
\def\rmN{{\mathbf{N}}}
\def\rmO{{\mathbf{O}}}
\def\rmP{{\mathbf{P}}}
\def\rmQ{{\mathbf{Q}}}
\def\rmR{{\mathbf{R}}}
\def\rmS{{\mathbf{S}}}
\def\rmT{{\mathbf{T}}}
\def\rmU{{\mathbf{U}}}
\def\rmV{{\mathbf{V}}}
\def\rmW{{\mathbf{W}}}
\def\rmX{{\mathbf{X}}}
\def\rmY{{\mathbf{Y}}}
\def\rmZ{{\mathbf{Z}}}

% Elements of random matrices
\def\ermA{{\textnormal{A}}}
\def\ermB{{\textnormal{B}}}
\def\ermC{{\textnormal{C}}}
\def\ermD{{\textnormal{D}}}
\def\ermE{{\textnormal{E}}}
\def\ermF{{\textnormal{F}}}
\def\ermG{{\textnormal{G}}}
\def\ermH{{\textnormal{H}}}
\def\ermI{{\textnormal{I}}}
\def\ermJ{{\textnormal{J}}}
\def\ermK{{\textnormal{K}}}
\def\ermL{{\textnormal{L}}}
\def\ermM{{\textnormal{M}}}
\def\ermN{{\textnormal{N}}}
\def\ermO{{\textnormal{O}}}
\def\ermP{{\textnormal{P}}}
\def\ermQ{{\textnormal{Q}}}
\def\ermR{{\textnormal{R}}}
\def\ermS{{\textnormal{S}}}
\def\ermT{{\textnormal{T}}}
\def\ermU{{\textnormal{U}}}
\def\ermV{{\textnormal{V}}}
\def\ermW{{\textnormal{W}}}
\def\ermX{{\textnormal{X}}}
\def\ermY{{\textnormal{Y}}}
\def\ermZ{{\textnormal{Z}}}

% Vectors
\def\vzero{{\bm{0}}}
\def\vone{{\bm{1}}}
\def\vmu{{\bm{\mu}}}
\def\vtheta{{\bm{\theta}}}
\def\va{{\bm{a}}}
\def\vb{{\bm{b}}}
\def\vc{{\bm{c}}}
\def\vd{{\bm{d}}}
\def\ve{{\bm{e}}}
\def\vf{{\bm{f}}}
\def\vg{{\bm{g}}}
\def\vh{{\bm{h}}}
\def\vi{{\bm{i}}}
\def\vj{{\bm{j}}}
\def\vk{{\bm{k}}}
\def\vl{{\bm{l}}}
\def\vm{{\bm{m}}}
\def\vn{{\bm{n}}}
\def\vo{{\bm{o}}}
\def\vp{{\bm{p}}}
\def\vq{{\bm{q}}}
\def\vr{{\bm{r}}}
\def\vs{{\bm{s}}}
\def\vt{{\bm{t}}}
\def\vu{{\bm{u}}}
\def\vv{{\bm{v}}}
\def\vw{{\bm{w}}}
\def\vx{{\bm{x}}}
\def\vy{{\bm{y}}}
\def\vz{{\bm{z}}}

% Elements of vectors
\def\evalpha{{\alpha}}
\def\evbeta{{\beta}}
\def\evepsilon{{\epsilon}}
\def\evlambda{{\lambda}}
\def\evomega{{\omega}}
\def\evmu{{\mu}}
\def\evpsi{{\psi}}
\def\evsigma{{\sigma}}
\def\evtheta{{\theta}}
\def\eva{{a}}
\def\evb{{b}}
\def\evc{{c}}
\def\evd{{d}}
\def\eve{{e}}
\def\evf{{f}}
\def\evg{{g}}
\def\evh{{h}}
\def\evi{{i}}
\def\evj{{j}}
\def\evk{{k}}
\def\evl{{l}}
\def\evm{{m}}
\def\evn{{n}}
\def\evo{{o}}
\def\evp{{p}}
\def\evq{{q}}
\def\evr{{r}}
\def\evs{{s}}
\def\evt{{t}}
\def\evu{{u}}
\def\evv{{v}}
\def\evw{{w}}
\def\evx{{x}}
\def\evy{{y}}
\def\evz{{z}}

% Matrix
\def\mA{{\bm{A}}}
\def\mB{{\bm{B}}}
\def\mC{{\bm{C}}}
\def\mD{{\bm{D}}}
\def\mE{{\bm{E}}}
\def\mF{{\bm{F}}}
\def\mG{{\bm{G}}}
\def\mH{{\bm{H}}}
\def\mI{{\bm{I}}}
\def\mJ{{\bm{J}}}
\def\mK{{\bm{K}}}
\def\mL{{\bm{L}}}
\def\mM{{\bm{M}}}
\def\mN{{\bm{N}}}
\def\mO{{\bm{O}}}
\def\mP{{\bm{P}}}
\def\mQ{{\bm{Q}}}
\def\mR{{\bm{R}}}
\def\mS{{\bm{S}}}
\def\mT{{\bm{T}}}
\def\mU{{\bm{U}}}
\def\mV{{\bm{V}}}
\def\mW{{\bm{W}}}
\def\mX{{\bm{X}}}
\def\mY{{\bm{Y}}}
\def\mZ{{\bm{Z}}}
\def\mBeta{{\bm{\beta}}}
\def\mPhi{{\bm{\Phi}}}
\def\mLambda{{\bm{\Lambda}}}
\def\mSigma{{\bm{\Sigma}}}

% Tensor
\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
\def\tA{{\tens{A}}}
\def\tB{{\tens{B}}}
\def\tC{{\tens{C}}}
\def\tD{{\tens{D}}}
\def\tE{{\tens{E}}}
\def\tF{{\tens{F}}}
\def\tG{{\tens{G}}}
\def\tH{{\tens{H}}}
\def\tI{{\tens{I}}}
\def\tJ{{\tens{J}}}
\def\tK{{\tens{K}}}
\def\tL{{\tens{L}}}
\def\tM{{\tens{M}}}
\def\tN{{\tens{N}}}
\def\tO{{\tens{O}}}
\def\tP{{\tens{P}}}
\def\tQ{{\tens{Q}}}
\def\tR{{\tens{R}}}
\def\tS{{\tens{S}}}
\def\tT{{\tens{T}}}
\def\tU{{\tens{U}}}
\def\tV{{\tens{V}}}
\def\tW{{\tens{W}}}
\def\tX{{\tens{X}}}
\def\tY{{\tens{Y}}}
\def\tZ{{\tens{Z}}}


% Graph
\def\gA{{\mathcal{A}}}
\def\gB{{\mathcal{B}}}
\def\gC{{\mathcal{C}}}
\def\gD{{\mathcal{D}}}
\def\gE{{\mathcal{E}}}
\def\gF{{\mathcal{F}}}
\def\gG{{\mathcal{G}}}
\def\gH{{\mathcal{H}}}
\def\gI{{\mathcal{I}}}
\def\gJ{{\mathcal{J}}}
\def\gK{{\mathcal{K}}}
\def\gL{{\mathcal{L}}}
\def\gM{{\mathcal{M}}}
\def\gN{{\mathcal{N}}}
\def\gO{{\mathcal{O}}}
\def\gP{{\mathcal{P}}}
\def\gQ{{\mathcal{Q}}}
\def\gR{{\mathcal{R}}}
\def\gS{{\mathcal{S}}}
\def\gT{{\mathcal{T}}}
\def\gU{{\mathcal{U}}}
\def\gV{{\mathcal{V}}}
\def\gW{{\mathcal{W}}}
\def\gX{{\mathcal{X}}}
\def\gY{{\mathcal{Y}}}
\def\gZ{{\mathcal{Z}}}

% Sets
\def\sA{{\mathbb{A}}}
\def\sB{{\mathbb{B}}}
\def\sC{{\mathbb{C}}}
\def\sD{{\mathbb{D}}}
% Don't use a set called E, because this would be the same as our symbol
% for expectation.
\def\sF{{\mathbb{F}}}
\def\sG{{\mathbb{G}}}
\def\sH{{\mathbb{H}}}
\def\sI{{\mathbb{I}}}
\def\sJ{{\mathbb{J}}}
\def\sK{{\mathbb{K}}}
\def\sL{{\mathbb{L}}}
\def\sM{{\mathbb{M}}}
\def\sN{{\mathbb{N}}}
\def\sO{{\mathbb{O}}}
\def\sP{{\mathbb{P}}}
\def\sQ{{\mathbb{Q}}}
\def\sR{{\mathbb{R}}}
\def\sS{{\mathbb{S}}}
\def\sT{{\mathbb{T}}}
\def\sU{{\mathbb{U}}}
\def\sV{{\mathbb{V}}}
\def\sW{{\mathbb{W}}}
\def\sX{{\mathbb{X}}}
\def\sY{{\mathbb{Y}}}
\def\sZ{{\mathbb{Z}}}

% Entries of a matrix
\def\emLambda{{\Lambda}}
\def\emA{{A}}
\def\emB{{B}}
\def\emC{{C}}
\def\emD{{D}}
\def\emE{{E}}
\def\emF{{F}}
\def\emG{{G}}
\def\emH{{H}}
\def\emI{{I}}
\def\emJ{{J}}
\def\emK{{K}}
\def\emL{{L}}
\def\emM{{M}}
\def\emN{{N}}
\def\emO{{O}}
\def\emP{{P}}
\def\emQ{{Q}}
\def\emR{{R}}
\def\emS{{S}}
\def\emT{{T}}
\def\emU{{U}}
\def\emV{{V}}
\def\emW{{W}}
\def\emX{{X}}
\def\emY{{Y}}
\def\emZ{{Z}}
\def\emSigma{{\Sigma}}

% entries of a tensor
% Same font as tensor, without \bm wrapper
\newcommand{\etens}[1]{\mathsfit{#1}}
\def\etLambda{{\etens{\Lambda}}}
\def\etA{{\etens{A}}}
\def\etB{{\etens{B}}}
\def\etC{{\etens{C}}}
\def\etD{{\etens{D}}}
\def\etE{{\etens{E}}}
\def\etF{{\etens{F}}}
\def\etG{{\etens{G}}}
\def\etH{{\etens{H}}}
\def\etI{{\etens{I}}}
\def\etJ{{\etens{J}}}
\def\etK{{\etens{K}}}
\def\etL{{\etens{L}}}
\def\etM{{\etens{M}}}
\def\etN{{\etens{N}}}
\def\etO{{\etens{O}}}
\def\etP{{\etens{P}}}
\def\etQ{{\etens{Q}}}
\def\etR{{\etens{R}}}
\def\etS{{\etens{S}}}
\def\etT{{\etens{T}}}
\def\etU{{\etens{U}}}
\def\etV{{\etens{V}}}
\def\etW{{\etens{W}}}
\def\etX{{\etens{X}}}
\def\etY{{\etens{Y}}}
\def\etZ{{\etens{Z}}}

% The true underlying data generating distribution
\newcommand{\pdata}{p_{\rm{data}}}
% The empirical distribution defined by the training set
\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
% The model distribution
\newcommand{\pmodel}{p_{\rm{model}}}
\newcommand{\Pmodel}{P_{\rm{model}}}
\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
% Stochastic autoencoder distributions
\newcommand{\pencode}{p_{\rm{encoder}}}
\newcommand{\pdecode}{p_{\rm{decoder}}}
\newcommand{\precons}{p_{\rm{reconstruct}}}

\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution

\newcommand{\E}{\mathbb{E}}
\newcommand{\Ls}{\mathcal{L}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\emp}{\tilde{p}}
\newcommand{\lr}{\alpha}
\newcommand{\reg}{\lambda}
\newcommand{\rect}{\mathrm{rectifier}}
\newcommand{\softmax}{\mathrm{softmax}}
\newcommand{\sigmoid}{\sigma}
\newcommand{\softplus}{\zeta}
\newcommand{\KL}{D_{\mathrm{KL}}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\standarderror}{\mathrm{SE}}
\newcommand{\Cov}{\mathrm{Cov}}
% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
% But then they seem to use $L^2$ for vectors throughout the site, and so does
% wikipedia.
\newcommand{\normlzero}{L^0}
\newcommand{\normlone}{L^1}
\newcommand{\normltwo}{L^2}
\newcommand{\normlp}{L^p}
\newcommand{\normmax}{L^\infty}

\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.

\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}

\DeclareMathOperator{\sign}{sign}
\DeclareMathOperator{\Tr}{Tr}
\let\ab\allowbreak

```



Here are the notes I took during the talk
```markdown

# Scaling laws for large time-series models: More data, more parameters

- Astro Data Science Discussion Group 
- https://talks.cam.ac.uk/talk/index/222820

## Abstract

Scaling laws for large language models (LLMs) offer valuable insights into how increasing model size and training data leads to predictable performance improvements. Time series forecasting, which shares a sequential structure similar to language, is well-suited to large-scale transformer architectures. In this talk, I will demonstrate that foundational decoder-only time series transformer models exhibit scaling behaviour analogous to LLMs. I will begin with a general introduction to scaling laws and how they can inform efficient, optimised model training. I will then focus on their specific application to time series data, highlighting the emergence of power law behaviour. Finally, I will discuss the broader implications of these findings, and potential scientific applications.

## Notes

- James Alvey
- [2405.13867](https://arxiv.org/pdf/2405.13867)
- Not gravitational waves, SBI, or much astrophysics!
- project over the summer with Alsing, EDwards, Nguyen & Wandelt
- about scaling laws applied to time series data.
- Why are scaling laws helpful?
  - look at GPT-4 technical report:
    - training really large models is super expensive
    - ($100m)
    - even then, it's difficult to do
  - openAI found a cheap way to do this
  - to train GPT-4, the trained a lot of smaller models, with 100x less compute, prototyped there, and skipped everything in between
  - the scaling law allowed them to do this
  - all other large models now use this
  - GPT-2, GTP-3, GPT-4
- What can we vary?
  - model size
  - dataset size (# of tokens)
    - token = single word 
  - how long we train (compute)
  - (model architecture)
- have to get out of a mindset of 'epoch 100' -- in these cases, often don't see all the data more than once
- low loss, low is better
  - step back -- GPT is trained by saying 'tell me what the next word is'
  - we want long sentences and paragraphs
  - there is a gap between predicting the next word and predicting 300 words from now
  - not obvious that those two are linked, but empirically things to work pretty well
  - there is always going to be an argument that 'if I'm predicitng the next word, am I really reasoning'?
- scaling law is the envelope of how well you can do
  - there will be some optimal choice, and that's the point that you put on your graph 
- 'where does it become like it's thinking'? 
  - there's a lot of emergence that happens in the gap 
  - empirical fact that lets you jump
- there becomes a limit where so long as you have enough data, it's no longer the limit 
- concrete example:
  - [2001.08361](https://arxiv.org/pdf/2001.08361)
  - kaplan: co-founder of anthropic
    - so he probably knows what he's doing
    - these experiments set the foundation for LLM success
  - experimental setup:
    - autoregressively train decoder-only transformers on large corpus of text data (WebText2) with 1024-length context window optimised on the cross-entropy loss
  - make a prediction for the next work, compute the cross entropy with the ground truth
  - vary number of parameters (with limits that are basically, 'infinite data', 'infinite compute', 'infinite batch size')
  - results from Figure 1
    - loss is power law in compute, power law in amount of data, power law in number of parameters
    - implications: performances is predictable, and optimal resource allocation is possible
  - this has to stop at some point 
    - we know that language doesn't have zero entropy
      - there are lots of different endings to a given sentence
      - but this tells you that we're not there yet
  - also useful for allocating resources
    - "you're only going to get to do this once, maybe twice"
    - the best thing to do is to take the biggest model you could possibly fit on, and don't bother training it to convergence, just train it for as long as you can
  - larger models require fewer samples to reach the same performance
    - so you should train the larger model if the goal is performance 
  - it's useful to know where these limits are 
  - the optimal model size grows smoothly with the loss target and compute budget
  - if I vary the amount of data that I show the model, this performs predictably
  - They found out that architecture doesn't matte, provieded you're not being ridiculous
  - So what did they learn:
    - As compute budget increases, spend it on larger models, don't worry about convergence
      - model size wins over everything else
      - "big models may be more important than big data"
        - data is typically not the limitation, train a bigger model (providing you have enough data)
      - "We expect that large language moels will perform bett and be more sample efficient than current models"
- How do transformers work?
  - understanding context
    - 'He had to make sure his friend's clothes'
      - were clean
    - 'He had to make sure his friend's trousers'
      - were ironed
    - 'Gromit had to make sure Wallace's trousers' 
      - didn't run away
    - build a probability distribution of 'what comes next' 
    - GPT-4 know's who wallace and gromit is, even though it's just a set of matrices 
  - steps: 
    - embedding 
      - (nvocab, dembed) matrix
    - positional embedding
      - (ncontext, dembed) matrix 
      - every element adds a fixed vector to the meaning 
    - attention mechanism
    - distributional head
      - de-embedding back to token space 
  - context sharing:
    - how do I know that wallace and gromit are paired, and how do I know that this should inform the rest of the sentence
  - how do we 'learn' that:
    - gromit and wallace are connected
    - the trousers belong to wallace
  - an attention 'head'
    - a single head of attention consists of keys Q, queries Q, and values V
    - [3Blue1Brown: attention in transformers, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc)
      - watch this 
    - matrix multiplications compute keys and queries and values
    - and asks 'how aligned are these'
      - these things are trained autoregressively, can't learn behind, only ahead, this is more an artifact of how these things are trained than what is actually the case 
      - gives you a manageable number of training examples
      - mirrors the way that humans speak
    - assign a score to pairs of keys and queries 
  - alignment = dot product
    - strong analogy with differential geometry 
  - these are mixed and repeated many times by a standard feedforward network, this process is then repeated. most important pairs ultimately guide where 
  - multiheaded attention does this in parallel,
  - if you want to read about the proper mechanism:
    - attention is all you need: [1706.03762](https://arxiv.org/pdf/1706.03762)
    - In reality: multi-head attention, multiple times i.e. "ask lots of different questions, lots of times", and some normalisation details I skipped over 
- Q: hyperparameter sweep?
  - this only works because these are relatively insensitive to architecture
- Time series
  - read the kaplan paper
  - then applied this to time series:
    - these are also causal
    - they are amenable to transformer architectures
    - we care a lot about forecasting
  - what do we want?
    - relatively unexplored, so want to set a baseline
      - people have been extremely focussed on language 
      - so we wanted to set a baseline
      - some papers after neurips
    - simple question: do the same scaling laws hold?
    - if so, then worth thinking about the details
    - Accepted for the 'Neurips Time series in the age of large models' workshop (not real neurips)
  - needed data
    - buildings bench 
      - 15bn tokens for building stock demand data
    - downloaded as much data as we could find
      - sea ice level
      - wind solar usage
      - california traffic data
    - as varied as we could make it
    - until we got to 10bn tokens, so we could be in the same order as the Kaplan paper
      - wanted to set a baseline on purely free data
    - some astronomy data, but not much very clean data
    - hard to get to clean data with ~O(2bn tokens)
    - would be subdominant in the sample, and wouldn't move things around too much
    - I have lots of questions about astronomy data in the conclusions
    - Q: what do you mean by clean data in this context?
      - not too many missing values, regularly spaced (no need for inpainting)
      - not too many outliers
      - Could be solved by continuous embeddings, rather than using simple indexes
    - looked at ZTF data, but decided not to include it because the number we got to was << 1bn, and adding a dataset that is not a dominant part is not well recieved
    - they want a relatively smoothly distributed argument
    - would be interested in what a calibrated astronomy dataset looks like in this context
    - Q: tokenisation?
      - how do you ensure you have a good tokenisation?
        - dominant part of the project
  - differences for time series:
    - no tokenisation needed
    - only normalisation
    - essentially the same architecture except for distributional heads (and no tokenisation)
    - trained from scratch because distribution heads changed
    - some people have tried fine-tuning existing LLMs
  - Results:
    - a broadly similar story:
    - power laws, although some wrinkles (running out of GPU time) 
    - Scaling laws for student-T log-likelihood
  - had to have a go
    - kaplan paper never shows the model doing anything
    - at the end, these show weekly sea temperature data and traffic data similarly well predicted
  - the important distinction is that this performance is very predictable
    - If I were bold, I would say big time series models are more than big time series data
- Outlook + Discussion:
  - applications in astro?
    - domain-specific scaling laws
    - early detection
    - event forecasting
  - conculsions
    - time series aren't so different from language
    - they exhibit the same scaling behaviour with dataset size, model size and compute
  - open questions
    - design choices
    - optimal computational requirements (same language or not?)
    - dataset curation
    - how does the forecast scale?
    - what are the failure modes e.g. the GPT-style hallucinations
- Q: coming back to hiranya's point, where does our neural network sit on this compute axis? 
  - human brain is a very large model
```
Please include relevent references with their numbers throughout the text. Format these in markdown as [XXXX.YYYYY](https://arxiv.org/abs/XXXX.YYYYY), with the correct numbers filled in as inferred from the latex of the paper.

Please use a tone written by a scientific expert, so no hyperbole or spin. The aim is to communicate the science clearly and accurately, but in a way that is accessible to a general audience.


{% endraw %}

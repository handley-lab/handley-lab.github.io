{% raw %}
PhD student Wei-Ning Deng from the Handley research group gave a talk on her latest paper at the Cambridge-LMU meeting. Could you write a blog post for my jekyll website using the below information, with the header

```markdown
---
layout: post
title:  "INSERT title""
date:   2024-10-04
categories: conferences
---
```

Here are the meeting details:

```mail
Dear Cambridge cosmo community,

as part of the Cambridge-LMU strategic partnership we are going to hold a
joint workshop of Munich and Cambridge cosmologists on January 07 and 08,
which also partly merges with the "The rise of field theory" workshop taking
place earlier in this week. Our goal is to bring together experts in theory,
simulation and observation of the large-scale structure of the Universe to
deepen the ties between the Cambridge and Munich cosmology communities.
Together we will summarise current achievements in order to stimulate an
active discussion about the future of the field. You find a draft schedule and
a participant sign up form below.

Participant sign up form:
https://docs.google.com/forms/d/1RE6J5WVJGZVhm-VF8U4stW9W2M7xzFdXXu66FlR_a9U/edit

Draft Schedule:
https://docs.google.com/document/d/1gqWXqgCk1ka7vCel5DIczFxbIYmJHhOQ6nFCsiMrilU/edit

If you would like to participate, could you please fill out the sign up form
as soon as possible (but latest by 07 Dec)? We are also looking for
contributions from Cambridge researchers, so if you are interested in
presenting your work, please consider any of the following options.

* Students: please indicate in the sign up form, if you are interested in
giving a short-talk about your work.

* Public Cam resources: if you want to promote public software, simulations or
observational data, that you have been working on, then please indicate that
in the corresponding field in the sign up form as well.

* postdocs: If you would like to give a (15+5)min presentation about your
work, please send and e-mail with your suggested talk title directly to me.
Please also note that there will be further workshops like this in the future,
i.e. should one of your suggestions not make it into the final program, then
priority will be given to these in future instalments.
```

Here is the arxiv link:

https://arxiv.org/abs/2407.18225

Here is the latex of the paper her talk is based on:

```latex
% main.tex
% ****** Start of file apssamp.tex ******
%
%   This file is part of the APS files in the REVTeX 4.2 distribution.
%   Version 4.2a of REVTeX, December 2014
%
%   Copyright (c) 2014 The American Physical Society.
%
%   See the REVTeX 4 README file for restrictions and more information.
%
% TeX'ing this file requires that you have AMS-LaTeX 2.0 installed
% as well as the rest of the prerequisites for REVTeX 4.2
%
% See the REVTeX 4 README file
% It also requires running BibTeX. The commands are as follows:
%
%  1)  latex apssamp.tex
%  2)  bibtex apssamp
%  3)  latex apssamp.tex
%  4)  latex apssamp.tex
%
\documentclass[%
 reprint,
%superscriptaddress,
%groupedaddress,
%unsortedaddress,
%runinaddress,
%frontmatterverbose, 
%preprint,
%preprintnumbers,
%nofootinbib,
%nobibnotes,
%bibnotes,
 amsmath,amssymb,
 prl,
%pra,
%prb,
%rmp,
%prstab,
%prstper,
%floatfix,
]{revtex4-2}
\usepackage{graphicx}% Include figure files
\usepackage{dcolumn}% Align table columns on decimal point
\usepackage{bm}% bold math
\usepackage{amsmath}
\usepackage[hidelinks]{hyperref}% add hypertext capabilities
\usepackage{cleveref}
\usepackage{natbib}
\usepackage{aas_macros}
\bibliographystyle{unsrtnat}
%\usepackage[mathlines]{lineno}% Enable numbering of text and display math
%\linenumbers\relax % Commence numbering lines

%\usepackage[showframe,%Uncomment any one of the following lines to test 
%%scale=0.7, marginratio={1:1, 2:3}, ignoreall,% default settings
%%text={7in,10in},centering,
%%margin=1.5in,
%%total={6.5in,8.75in}, top=1.2in, left=0.9in, includefoot,
%%height=10in,a5paper,hmargin={3cm,0.8in},
%]{geometry}

\begin{document}

\preprint{APS/123-QED}

\title{Predicting spatial curvature \(\Omega_K\) in globally $CPT$-symmetric universes}% Force line breaks with \\
%\thanks{}%

\author{Wei-Ning Deng}
\email{wnd22@cam.ac.uk}
% \affiliation{Astrophysics Group, Cavendish Laboratory, J.J. Thomson Avenue, Cambridge, CB3 0HE, UK}
% \affiliation{Kavli Institute for Cosmology, Madingley Road, Cambridge, CB3 0HA, UK} 
% \affiliation{Queens College, Silver Street, Cambridge, CB3 9ET, UK}
 

\author{Will Handley}%
\email{wh260@cam.ac.uk}
\affiliation{Astrophysics Group, Cavendish Laboratory, J.J. Thomson Avenue, Cambridge, CB3 0HE, UK}
\affiliation{Kavli Institute for Cosmology, Madingley Road, Cambridge, CB3 0HA, UK} 
% \affiliation{
%  Gonville \& Caius College, Trinity Street, Cambridge, CB2 1TA, UK
%  }

%\collaboration{}%\noaffiliation

\date{\today}% It is always \today, today,
             %  but any date may be explicitly specified

\begin{abstract}
    Boyle and Turok's $CPT$-symmetric universe model posits that the universe was symmetric at the Big Bang, addressing numerous problems in both cosmology and the Standard Model of particle physics. We extend this model by incorporating the symmetric conditions at the end of the Universe, which impose constraints on the allowed perturbation modes. These constrained modes conflict with the integer wave vectors required by the global spatial geometry in a closed universe. To resolve this conflict, only specific values of curvature are permissible, and in particular the curvature density is constrained to be $\Omega_K \in \{-0.014, -0.009, -0.003, \ldots\}$, consistent with \textit{Planck} observations.
\end{abstract}

\maketitle

\section{Introduction}
The concordance $\Lambda$CDM model and the Standard Model successfully explain a range of observed and theoretical phenomena in cosmology~\cite{2020A&A...641A...6P} and particle physics~\cite{1995iqft.book.....P}. However, several issues remain unresolved: For cosmology, there are the horizon~\cite{1972grun.book.....D} and flatness~\cite{1983Natur.305..673C} problems, as well as the composition and nature of dark matter and energy. For the standard model of particle physics, there is the cosmological constant problem~\cite{1989RvMP...61....1W}, Weyl anomaly~\cite{1994CQGra..11.1387D} and the strong $CP$ problem~\cite{1976PhRvL..37....8T}. Attempts to address these challenges often involve introducing new degrees of freedom, such as an era of inflation~\cite{1981PhRvD..23..347G}, a wide variety of dark matter particles~\cite{2019Univ....5..213P}, axions~\cite{1977PhRvL..38.1440P}, or modifying General Relativity~\cite{2012PhR...513....1C}. Despite these efforts, no single model can resolve all these issues simultaneously, and such modifications compromise the apparent simplicity of our universe as suggested by recent observations~\cite{2020A&A...641A...6P, 2024ApJ...966..157F}.

To address these challenges, \citet{2018PhRvL.121y1301B, 2022AnPhy.43868767B} propose a novel cosmological model known as the $CPT$-symmetric Universe. Rather than introducing new degrees of freedom, they posit that the universe is $CPT$-symmetric at the Big Bang singularity. Given this initial condition, the aforementioned issues could be solved without adding extra complexity~\cite{2021arXiv211006258B,2022arXiv220810396B,2024PhLB..84938442B,2023arXiv230200344T}. For example, the $CPT$-symmetric universe exhibits a periodic global structure, which allows for the calculation of its gravitational entropy~\cite{1977PhRvD..15.2752G}. As noted by \citet{2024PhLB..84938443T}, maximizing this entropy resolves the flatness, homogeneity, and isotropy problems without requiring inflation.

In this letter, we further investigate the impact of this periodic global structure on cosmological perturbations. Previous work by \citet{2022PhRvD.105h3514L} has explored this concept within the context of flat universes. Their findings suggest that the periodic conditions impose constraints on perturbations within the universe, which have observable effects on the Cosmic Microwave Background (CMB) power spectrum~\cite{2022PhRvD.105h3515B,2022PhRvD.105l3508P}.

Building on this work, we extend the analysis of \citet{2022PhRvD.105h3514L} to include curved universes. Our findings indicate that the constraints imposed by the future conformal boundary conflict with the spatial boundary conditions in a closed universe. To reconcile this conflict, only specific values of curvature are permissible, which are consistent with the observations from \texttt{Planck 2018}~\cite{2020A&A...641A...6P}, adding to the recent conversation in the literature surrounding closed universes~\cite{2020NatAs...4..196D, 2021PhRvD.103d1301H, 2022MNRAS.517.3087G, 2020MNRAS.496L..91E}.


\section{Background and perturbations} 
We build on the derivation presented in \citet{2022PhRvD.105h3514L} and extend it to a curved universe. The perturbed FLRW metric can be written as:
\begin{equation}
    ds^2 = a^2 \left[-(1 + 2\Phi)d\eta^2 + (1 - 2\Phi)\left(\frac{1}{1-\kappa r^2}dr^2+r^2d\Omega^2\right) \right],
\end{equation}
where \(\Phi\) is the perturbation in the Newtonian gauge, and $\kappa$ controls the spatial curvature of the universe.

We analyse the evolution of the background in conformal time \(\eta\) instead of physical time to render explicit the periodic behaviour of the universe. Following Lasenby~\cite{2022PhRvD.105h3514L}, only three components are considered: dark energy $\lambda$, radiation $r$, and spatial curvature $\kappa$, omitting matter. The zero-order Friedmann equations are: 
\begin{equation}\label{eq:friedmann_eq}
    \dot{a}^2 = \tfrac{1}{3}\lambda a^4 - \kappa a^2  + \tfrac{1}{3} r, \qquad 
    \ddot{a} = \tfrac{2}{3}\lambda a^3 - \kappa a,
\end{equation}
where \(\hbar = c = 8\pi G = 1\) and dots denote \(d/d\eta\).

The solution to \cref{eq:friedmann_eq} can be expressed as a Jacobi elliptic function~\cite{2021arXiv210906204B}, which exhibits periodic global structure in conformal time. The universe begins at the Big Bang \(a = 0\), evolves to the end of the universe at \(a=\infty\) at a finite conformal time \(\eta_{\infty}\) termed the future conformal boundary (FCB), and then returns from the future boundary back to a future Big Bang, starting the cycle over again. However, this cyclic behaviour does not by default hold for perturbations. To maintain the behaviour, the perturbations should be symmetric not just at the Bang, but also at the FCB. The symmetry constrains the allowed modes of perturbations (see \cref{fig:a_perturbations-eta}).
\begin{figure*}[!ht]\centering
     \includegraphics{a_perturbations-eta.pdf}
     \caption{Evolution of the scale factor \(a\), its reciprocal \(s\equiv 1/a\), and the first five allowed perturbations which are (anti)-symmetric about the future conformal boundary. The perturbations have been normalised to have constant oscillatory amplitude across cosmic time for clarity.}
     \label{fig:a_perturbations-eta}
\end{figure*}

To analyse the perturbations, we write the first-order Einstein equation as:
\begin{equation}\label{eq:perturbation_eq}
    \ddot{\Phi} + 4aH\dot{\Phi} + \tfrac{1}{3}(k^2 + 4a^2\lambda-12\kappa)\Phi = 0.
\end{equation}
where \(k\) is the comoving wave vector of the perturbation. Switching the independent variable from conformal time $\eta$ to scale factor $a$, one finds
\begin{equation}\label{eq:perturbation_a}
    (\lambda a^2 - 3\kappa + \frac{r}{a^2} )\Phi'' + (6\lambda a - \frac{15\kappa}{a} + \frac{4r}{a^3})\Phi' + (4\lambda+\frac{k^2-12\kappa}{a^2})\Phi = 0,
\end{equation}
where a prime denotes \(d/da\).

One degree of freedom between \(r\) and \(\lambda\) can be removed from \cref{eq:friedmann_eq,eq:perturbation_a} by fixing the scaling of \(a\). Following~\cite{2022PhRvD.105h3514L}, \(r = \lambda\) is chosen, equivalent to demanding \(a=1\) when the energy density of matter radiation and dark energy are equal, after which \cref{eq:perturbation_a} becomes
\begin{equation}\label{eq:Phi_ODE}
    a(a^4 - 2a^2 \tilde\kappa + 1) \Phi'' + (6a^4- 10a^2 \tilde\kappa + 4 ) \Phi' + a(4a^2 + \tilde{k}^2-8\tilde\kappa) \Phi = 0, \nonumber
\end{equation}
\vspace{-2.5em}
\[ \text{where} \qquad
    \tilde{k} \equiv k/\sqrt{\lambda}, \qquad \tilde \kappa \equiv \frac{3}{2\lambda}\kappa\]
are the dimensionless wave vector and curvature respectively. This equation reduces to eq.~(23) in~\citet{2022PhRvD.105h3514L} when \( \tilde\kappa = 0 \).
Note that if we replace \(\Phi(a)\) with \(\varphi(a) \equiv a^2 \Phi(a)\), the equation remains invariant under the transformation \({a\leftrightarrow1/a}\). This symmetry is important in the next section when considering perturbations passing through the FCB as \(a\rightarrow \infty\).

This equation can be solved analytically, yielding two solutions. The solution can be expressed in terms of Heun functions:
\begin{equation}
\begin{aligned}\label{eq:Heun}
    \Phi(a) &= \text{HeunG} \left( -1+2\tilde\kappa \tilde a_+^2,\frac{\tilde k^2-8\tilde\kappa}{-4 \tilde a_-^2},\frac{1}{2},2, \frac{5}{2},\frac{1}{2},a^2\tilde a_+^2\right)\\
    &\tilde a_{\pm}=\sqrt{\tilde\kappa\pm\sqrt{\tilde\kappa^2-1}}
\end{aligned}
\end{equation}
where \(\tilde a_{\pm}\) are the extremum values of the scale factor, corresponding to \(\dot{a}=0\) in \cref{eq:friedmann_eq}. Since the perturbation is frozen at the beginning and starts to oscillate after entering the horizon \(k = aH\), a specific linear combination of these solutions is selected to ensure that \(\Phi(a =0) = 1\) and \(\Phi'(a = 0) = 0\).


\section{Constraints from the future conformal boundary}\label{sec:constrain_FCB}
Next, we investigate the behaviour of perturbations near the FCB.  For universes with curvature \( \tilde{\kappa} \equiv \frac{3}{2\lambda}\kappa > 1 \), the scale factor \(a\) reaches a maximum before they collapse in a ``big crunch'', which are not physically relevant, since we observe an accelerating Universe today. This implies that the Universe cannot possess excessive curvature, establishing an upper limit of \(\tilde{\kappa} < 1\). In this case, the scale factor \(a\) approaches infinity at the FCB.
Consequently, we should consider the reciprocal scale factor \( s \equiv 1/a \). Because of the symmetry in \cref{eq:Phi_ODE}, the solution can be expressed as \(\Phi(s)= s^4 \Phi(a(s)) \). As a result, the solution would continue oscillating through the FCB until the future Big Bang. \citet{2022PhRvD.105h3514L} found that most perturbations diverge before reaching the future Big Bang. Only those solutions that are finite and symmetric or antisymmetric at the FCB remain non-singular (see \cref{fig:a_perturbations-eta}). This symmetry requirement means that only a discrete spectrum of wavevectors are allowed.

To calculate the discrete spectrum of wave vectors, we re-write the perturbation solution into an integral form \cref{eq:integration_sol}, where the sine component captures the solution's oscillatory nature:
\begin{equation}\label{eq:integration_sol}
\begin{aligned}
    \Phi(a) &= \frac{3\sqrt{a^4 + (\tilde{k}^2 -2\tilde\kappa)a^2 + 1}}{a^3\tilde{k}\sqrt{(\tilde{k}^2 -2\tilde\kappa)^2 - 4}} \sin\theta(\tilde k,\tilde\kappa,a),\\
    \theta = \int_0^a &\frac{\tilde{k} a'^2 \sqrt{(\tilde{k}^2 -2\tilde\kappa)^2 - 4}}{\sqrt{1 + a'^4 - 2\tilde\kappa a'^2} \left( a'^4 + (\tilde{k}^2 -2\tilde\kappa)a'^2 + 1 \right)} da',
\end{aligned}
\end{equation}
The integration in \(\theta(a)\) can be expressed as an incomplete elliptic integral of the third kind \(\Pi\):
\begin{equation}\label{eq:psi_elliptic}
\begin{aligned}
    \theta(a) = \tilde{k} \tilde a_- \times \Bigg[ &\Pi\left( \frac{a}{\tilde a_-}, -\frac{1}{2}\tilde a_-^2 \tilde K_{-}^2, \tilde a_-^2 \right) \\
    - &\Pi\left( \frac{a}{\tilde a_-}, -\frac{1}{2}\tilde a_-^2 \tilde K_{+}^2, \tilde a_-^2 \right) \Bigg],\\
\end{aligned}
\end{equation}
\vspace{-1.5em}
\begin{equation*}
\begin{aligned}
    &\Pi(z,\nu,k)=\int_0^z \frac{1}{(1-\nu t^2)\sqrt{1-t^2}\sqrt{1-k^2t^2}} dt,\\
    &\tilde K_{\pm}=\sqrt{(\tilde{k}^2 -2\tilde\kappa) \pm \sqrt{(\tilde{k}^2 -2\tilde\kappa)^2 - 4}}.
\end{aligned}
\end{equation*}
For the flat case (\(\tilde\kappa=0\)), the solution \cref{eq:integration_sol,eq:psi_elliptic} reduces to eq.~(26-28) in~\citet{2022PhRvD.105h3514L}.

If we require the solution to be (anti)symmetric at the FCB, the cycles of oscillation should be complete at the boundary. This implies that the angle \(\theta\) in the sine function should equal \( n\frac{\pi}{2} \) at \( a \rightarrow \infty \). 
\begin{equation}\label{eq:theta}
    \theta(\tilde{k}, \tilde\kappa, a \rightarrow \infty) \overset{!}{=} \frac{n\pi}{2}.
\end{equation}
The corresponding \(\tilde{k}\) are the allowed values of discrete wave vectors. The function \(\theta(\tilde k,a\rightarrow\infty)\) with different \(\tilde\kappa\) is illustrated in \cref{fig:theta_diffK}. While increasing the curvature value \(\tilde\kappa\), \(\theta\) becomes steeper, and the corresponding discrete wave vectors \(\tilde{k}\) have smaller spacing. 

\begin{figure}
     \includegraphics{theta_discretek.pdf}
     \caption{Phase of perturbations \(\theta(\tilde{k},a\rightarrow \infty)\) with different curvature \(\tilde\kappa\). Larger \(\tilde\kappa\) results in a steeper curve. The value of \(\theta\) should be \(\frac{\pi}{2}n, n\in\mathbb{N}\), where the corresponding \(\tilde k\) are the allowed wave vectors forming a discrete spectrum.}
     \label{fig:theta_diffK}
\end{figure}



\section{Implications for spatial curvature \(\Omega_K\)} 
These observations have significant implications for closed universes, where the compactness of spacial slices necessitates integer wave vectors (Sec.~2.4 in~\cite{2017CCoPh..22..852T}). This requirement is generally in conflict with the discrete spectrum of wave vectors arising from FCB considerations, prompting the question of whether this conflict can be resolved by matching the two discrete sets.

In \cref{fig:theta_diffK} \(\theta(\tilde{k})\) approaches a straight line for high-\(k\) modes due to perturbations oscillating as \(\sim \cos(\tilde{k}\eta/\sqrt{3})\).
This implies that the allowed wave vectors are equally spaced for high-\(k\) modes. By adjusting \(\tilde{\kappa}\), we can align the allowed wavevectors to be integers. Note that the unit of \(\tilde{k}\) differs from that of the integer wave vectors \(k_{\text{int}}\). The transformation between them can be expressed as: \(\tilde{k}\equiv  \sqrt{\frac{2\tilde{\kappa}}{3}} \sqrt{k_{\text{int}}(k_{\text{int}}+2) }  \approx \sqrt{\frac{2\tilde{\kappa}}{3}} k_{\text{int}}\) in high-\(k\) modes. Consequently, the actual gradient is given by:
\begin{equation}
\frac{d\theta}{dk_{\text{int}}}(\tilde{\kappa},\tilde{k}\gg 1,a\rightarrow \infty) \approx \sqrt{\frac{2\tilde{\kappa}}{3}}\frac{\eta_{\infty}(\tilde{\kappa})}{\sqrt{3}} \overset{!}{=} N^{\pm 1}\frac{\pi}{2},
\end{equation}
where to match the integer wave vectors, the gradient should be \(N\frac{\pi}{2}\) or \(\frac{1}{N}\frac{\pi}{2}\) (where \(N\in\mathbb{N}\)), corresponding to either sparser discrete \(\theta\) or sparser \(k_{\text{int}}\) (see \cref{fig:theta_kint}). Since the gradient depends on \(\tilde{\kappa}\), this constrains the allowed curvature values. Some allowed \(\tilde{\kappa}\) values are shown in \cref{fig:Slope_kc}. The gradient increases with \(\tilde{\kappa}\) and approaches infinity as \(\tilde{\kappa}\) approaches unity, the maximum allowed curvature value. Beyond this value, the universe would collapse, resulting in a crunch.

\begin{figure}
     \includegraphics{theta-kint_loglog.pdf}
     \caption{Phase of perturbations $\theta$, in log-log plot. In the high-\(k\) mode, the gradient of \(\theta\) approximates a straight line, indicating that the discrete wave vectors are equally spaced. In a closed universe, these wave vectors must be integers, constraining the gradient to be \(N\frac{\pi}{2}\) or \(\frac{1}{N}\frac{\pi}{2}\) (where \(N\in\mathbb{N}\))..
     }
     \label{fig:theta_kint}
\end{figure} 

\begin{figure}
     \includegraphics{slope_kappa.pdf}
     \caption{The gradient of the phase of perturbations \(\theta\), as a function of \(\tilde\kappa\). The gradient constraint determines the preferred curvature values.}
     \label{fig:Slope_kc}
\end{figure} 

The predicted values of \(\tilde{\kappa}\) are then transformed to the current curvature density \(\Omega_K=-2\tilde{\kappa}\sqrt{\Omega_\Lambda\Omega_r}\) and compared with the \texttt{Planck 2018} data (\cref{fig:Planck_kappa}). The \(\tilde{\kappa}\), for unit gradient, corresponds to \(\Omega_K\sim -0.009\). The maximum curvature, \(\tilde{\kappa}=1\), corresponds to \(\Omega_K\sim -0.014\). Although this is closer to flat than the observational value of \(-0.044^{+0.018}_{-0.015}\)~\cite{2021PhRvD.103d1301H,2020NatAs...4..196D,2020A&A...641A...6P}, incorporating matter into our model would likely yield more precise predictions. Despite its simplicity, our model recovers curvature values consistent with observational data. 

\begin{figure}
     \includegraphics{Planck_kappa.pdf}
     \caption{Comparison of predicted curvature values with \texttt{Planck 2018} data (\texttt{base\_omegak\_plikHM\_TTTEEE\_lowl\_lowE} from~\cite{2020A&A...641A...6P}). Predicted curvature values from \cref{fig:Slope_kc} are shown.}
     \label{fig:Planck_kappa}
\end{figure}

\section{Conclusion} 
In this letter, we extended the work of \citet{2022PhRvD.105h3514L} and \citet{2021arXiv210906204B} by solving the first-order perturbation equation to derive analytic solutions. These solutions remain physical if they exhibit symmetry or antisymmetry at the FCB. This temporal boundary condition imposes a discrete spectrum on the wave vectors, which conflicts with the integer wave vectors derived from the spatial compactness of closed universes. Since both sets of discrete \(k\) values exhibit equal spacing in the high \(k\) regime, we can reconcile them by constraining the spatial curvature to specific values.. 

To refine the predictions of this allowed curvature spectrum further, we plan to solve the perturbations numerically in a more detailed universe model that includes matter and radiation anisotropy. The resulting solutions will be used to generate the CMB power spectra, which will then be compared with observational data, following the methodologies of~\cite{2022PhRvD.105h3515B} and~\cite{2022PhRvD.105l3508P}.

\begin{acknowledgments}
\section{acknowledgments}
We extend our gratitude to Latham Boyle for his helpful feedback on the calculations and logic presented in this paper. WND was supported by a Cambridge Trusts Taiwanese Scholarship. WJH was supported by a Royal Society University Research Fellowship. 

\end{acknowledgments}
\vfill
\pagebreak

% \appendix

% \section{Perturbation solution in Heun function form}

% \begin{equation}
% \begin{aligned}
%     &\Phi(a) = 
%     \left(1 + 2(1 - 2 \tilde\kappa^2) a^4 + a^8\right)^{1/8} \left(\frac{i a^2}{\alpha} - 1\right)^{-\gamma} (i \alpha a^2 + 1)^{\gamma} \\
%     &\times \exp\left(-\frac{1}{4}\tanh^{-1}\left(\frac{2a^2\tilde\kappa}{1+a^4}\right)+\frac{i +\tilde\kappa}{2\sqrt{\tilde\kappa^2-1}} \tanh^{-1} \left(\frac{-a^2+\tilde\kappa}{\sqrt{\tilde\kappa^2-1}}\right) \right)\\
%     &\times \text{HeunG}\left(-\frac{1}{\alpha^2}, -\frac{i \tilde{k}^2-i8\tilde\kappa - 5 \alpha}{4 \alpha}, 1, \frac{5}{2}, \frac{5}{2}, \frac{1}{2}, \frac{i a^2}{\alpha}\right),
% \end{aligned}
% \end{equation}


% where \(\alpha\) and \(\gamma\) are given by:
% \begin{equation*}
%     \alpha = i \tilde\kappa + \sqrt{1 - \tilde\kappa^2}, \quad \gamma = \frac{\alpha(\alpha - 1)}{2 \alpha^2 + 2}.
% \end{equation*}

\let\oldbibitem\bibitem
\renewcommand{\bibitem}{%
    \renewcommand{\doi}[1]{doi: ##1}% Override \doi
    \let\bibitem\oldbibitem% Restore \bibitem
    \oldbibitem% Call old \bibitem
}

\bibliography{Reference}% Produces the bibliography via BibTeX.

\end{document}
%
% ****** End of file ******

```

Here is the bibtex from that paper:
```bibtex
% Reference.bib
@ARTICLE{2018PhRvL.121y1301B,
       author = {{Boyle}, Latham and {Finn}, Kieran and {Turok}, Neil},
        title = "{C P T -Symmetric Universe}",
      journal = {\prl},
     keywords = {High Energy Physics - Phenomenology, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Theory},
         year = 2018,
        month = dec,
       volume = {121},
       number = {25},
          eid = {251301},
        pages = {251301},
          doi = {10.1103/PhysRevLett.121.251301},
archivePrefix = {arXiv},
       eprint = {1803.08928},
 primaryClass = {hep-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2018PhRvL.121y1301B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}


@ARTICLE{2022AnPhy.43868767B,
       author = {{Boyle}, Latham and {Finn}, Kieran and {Turok}, Neil},
        title = "{The Big Bang, CPT, and neutrino dark matter}",
      journal = {Annals of Physics},
     keywords = {Dark matter, CPT Symmetry, Early Universe Cosmology, Neutrino},
         year = 2022,
        month = mar,
       volume = {438},
          eid = {168767},
        pages = {168767},
          doi = {10.1016/j.aop.2022.168767},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022AnPhy.43868767B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2022PhRvD.105h3514L,
       author = {{Lasenby}, A.~N. and {Handley}, W.~J. and {Bartlett}, D.~J. and {Negreanu}, C.~S.},
        title = "{Perturbations and the future conformal boundary}",
      journal = {\prd},
     keywords = {General Relativity and Quantum Cosmology, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2022,
        month = apr,
       volume = {105},
       number = {8},
          eid = {083514},
        pages = {083514},
          doi = {10.1103/PhysRevD.105.083514},
archivePrefix = {arXiv},
       eprint = {2104.02521},
 primaryClass = {gr-qc},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022PhRvD.105h3514L},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2020A&A...641A...6P,
       author = {{Planck Collaboration}},
        title = "{Planck 2018 results. VI. Cosmological parameters}",
      journal = {\aap},
     keywords = {cosmic background radiation, cosmological parameters, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2020,
        month = sep,
       volume = {641},
          eid = {A6},
        pages = {A6},
          doi = {10.1051/0004-6361/201833910},
archivePrefix = {arXiv},
       eprint = {1807.06209},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2020A&A...641A...6P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@BOOK{1995iqft.book.....P,
       author = {{Peskin}, Michael E. and {Schroeder}, Daniel V.},
        title = "{An Introduction to Quantum Field Theory}",
         year = 1995,
       adsurl = {https://ui.adsabs.harvard.edu/abs/1995iqft.book.....P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@BOOK{1972grun.book.....D,
       author = {{Dicke}, R.~H.},
        title = "{Gravitation and the universe.}",
         year = 1972,
       adsurl = {https://ui.adsabs.harvard.edu/abs/1972grun.book.....D},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{1983Natur.305..673C,
       author = {{Carrigan}, R.~A., Jr. and {Trower}, W.~P.},
        title = "{Magnetic monopoles}",
      journal = {\nat},
     keywords = {Magnetic Monopoles, Particle Theory, Quantum Theory, Unified Field Theory, Astrophysics, Dirac Equation, Elementary Particle Interactions, Gauge Theory, Ionization Chambers, Squid (Detectors), Nuclear and High-Energy Physics},
         year = 1983,
        month = oct,
       volume = {305},
       number = {5936},
        pages = {673-678},
          doi = {10.1038/305673a0},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1983Natur.305..673C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{1989RvMP...61....1W,
       author = {{Weinberg}, Steven},
        title = "{The cosmological constant problem}",
      journal = {Reviews of Modern Physics},
         year = 1989,
        month = jan,
       volume = {61},
       number = {1},
        pages = {1-23},
          doi = {10.1103/RevModPhys.61.1},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1989RvMP...61....1W},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{1994CQGra..11.1387D,
       author = {{Duff}, M.~J.},
        title = "{REVIEW ARTICLE: Twenty years of the Weyl anomaly}",
      journal = {Classical and Quantum Gravity},
     keywords = {General Relativity and Quantum Cosmology, High Energy Physics - Theory},
         year = 1994,
        month = jun,
       volume = {11},
       number = {6},
        pages = {1387-1403},
          doi = {10.1088/0264-9381/11/6/004},
archivePrefix = {arXiv},
       eprint = {hep-th/9308075},
 primaryClass = {gr-qc},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1994CQGra..11.1387D},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}


@ARTICLE{1976PhRvL..37....8T,
       author = {{'t Hooft}, G.},
        title = "{Symmetry Breaking through Bell-Jackiw Anomalies}",
      journal = {\prl},
         year = 1976,
        month = jul,
       volume = {37},
       number = {1},
        pages = {8-11},
          doi = {10.1103/PhysRevLett.37.8},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1976PhRvL..37....8T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{1981PhRvD..23..347G,
       author = {{Guth}, Alan H.},
        title = "{Inflationary universe: A possible solution to the horizon and flatness problems}",
      journal = {\prd},
         year = 1981,
        month = jan,
       volume = {23},
       number = {2},
        pages = {347-356},
          doi = {10.1103/PhysRevD.23.347},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1981PhRvD..23..347G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2019Univ....5..213P,
       author = {{Profumo}, Stefano and {Giani}, Leonardo and {Piattella}, Oliver F.},
        title = "{An Introduction to Particle Dark Matter}",
      journal = {Universe},
     keywords = {dark matter theory, dark matter searches, dark matter candidates, High Energy Physics - Phenomenology, Astrophysics - Astrophysics of Galaxies, High Energy Physics - Theory},
         year = 2019,
        month = oct,
       volume = {5},
       number = {10},
          eid = {213},
        pages = {213},
          doi = {10.3390/universe5100213},
archivePrefix = {arXiv},
       eprint = {1910.05610},
 primaryClass = {hep-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019Univ....5..213P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
@ARTICLE{1977PhRvL..38.1440P,
       author = {{Peccei}, R.~D. and {Quinn}, Helen R.},
        title = "{CP conservation in the presence of pseudoparticles}",
      journal = {\prl},
         year = 1977,
        month = jun,
       volume = {38},
       number = {25},
        pages = {1440-1443},
          doi = {10.1103/PhysRevLett.38.1440},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1977PhRvL..38.1440P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2012PhR...513....1C,
       author = {{Clifton}, Timothy and {Ferreira}, Pedro G. and {Padilla}, Antonio and {Skordis}, Constantinos},
        title = "{Modified gravity and cosmology}",
      journal = {\physrep},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Theory},
         year = 2012,
        month = mar,
       volume = {513},
       number = {1},
        pages = {1-189},
          doi = {10.1016/j.physrep.2012.01.001},
archivePrefix = {arXiv},
       eprint = {1106.2476},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2012PhR...513....1C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2024ApJ...966..157F,
       author = {ACT Collaboration},
        title = "{The Atacama Cosmology Telescope: Cosmology from Cross-correlations of unWISE Galaxies and ACT DR6 CMB Lensing}",
      journal = {\apj},
     keywords = {Observational cosmology, Sigma8, Cosmological parameters from large-scale structure, Cosmic microwave background radiation, Weak gravitational lensing, Large-scale structure of the universe, Cosmology, Cosmological parameters, 1146, 1455, 340, 322, 1797, 902, 343, 339, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2024,
        month = may,
       volume = {966},
       number = {2},
          eid = {157},
        pages = {157},
          doi = {10.3847/1538-4357/ad31a5},
archivePrefix = {arXiv},
       eprint = {2309.05659},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024ApJ...966..157F},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2021arXiv211006258B,
       author = {{Boyle}, Latham and {Turok}, Neil},
        title = "{Cancelling the vacuum energy and Weyl anomaly in the standard model with dimension-zero scalar fields}",
      journal = {arXiv e-prints},
     keywords = {High Energy Physics - Theory, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Phenomenology},
         year = 2021,
        month = oct,
          eid = {arXiv:2110.06258},
        pages = {arXiv:2110.06258},
          doi = {10.48550/arXiv.2110.06258},
archivePrefix = {arXiv},
       eprint = {2110.06258},
 primaryClass = {hep-th},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv211006258B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2022arXiv220810396B,
       author = {{Boyle}, Latham and {Teuscher}, Martin and {Turok}, Neil},
        title = "{The Big Bang as a Mirror: a Solution of the Strong CP Problem}",
      journal = {arXiv e-prints},
     keywords = {High Energy Physics - Phenomenology, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Theory},
         year = 2022,
        month = aug,
          eid = {arXiv:2208.10396},
        pages = {arXiv:2208.10396},
          doi = {10.48550/arXiv.2208.10396},
archivePrefix = {arXiv},
       eprint = {2208.10396},
 primaryClass = {hep-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv220810396B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2024PhLB..84938442B,
       author = {{Boyle}, Latham and {Turok}, Neil},
        title = "{Thermodynamic solution of the homogeneity, isotropy and flatness puzzles (and a clue to the cosmological constant)}",
      journal = {Physics Letters B},
     keywords = {General Relativity and Quantum Cosmology, Astrophysics - Cosmology and Nongalactic Astrophysics, High Energy Physics - Phenomenology, High Energy Physics - Theory},
         year = 2024,
        month = feb,
       volume = {849},
          eid = {138442},
        pages = {138442},
          doi = {10.1016/j.physletb.2024.138442},
archivePrefix = {arXiv},
       eprint = {2210.01142},
 primaryClass = {gr-qc},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024PhLB..84938442B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2023arXiv230200344T,
       author = {{Turok}, Neil and {Boyle}, Latham},
        title = "{A Minimal Explanation of the Primordial Cosmological Perturbations}",
      journal = {arXiv e-prints},
     keywords = {High Energy Physics - Phenomenology, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Theory},
         year = 2023,
        month = feb,
          eid = {arXiv:2302.00344},
        pages = {arXiv:2302.00344},
          doi = {10.48550/arXiv.2302.00344},
archivePrefix = {arXiv},
       eprint = {2302.00344},
 primaryClass = {hep-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023arXiv230200344T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{1977PhRvD..15.2752G,
       author = {{Gibbons}, G.~W. and {Hawking}, S.~W.},
        title = "{Action integrals and partition functions in quantum gravity}",
      journal = {\prd},
         year = 1977,
        month = may,
       volume = {15},
       number = {10},
        pages = {2752-2756},
          doi = {10.1103/PhysRevD.15.2752},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1977PhRvD..15.2752G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2024PhLB..84938443T,
       author = {{Turok}, Neil and {Boyle}, Latham},
        title = "{Gravitational entropy and the flatness, homogeneity and isotropy puzzles}",
      journal = {Physics Letters B},
     keywords = {High Energy Physics - Theory, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Phenomenology},
         year = 2024,
        month = feb,
       volume = {849},
          eid = {138443},
        pages = {138443},
          doi = {10.1016/j.physletb.2024.138443},
archivePrefix = {arXiv},
       eprint = {2201.07279},
 primaryClass = {hep-th},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024PhLB..84938443T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2022PhRvD.105h3515B,
       author = {{Bartlett}, D.~J. and {Handley}, W.~J. and {Lasenby}, A.~N.},
        title = "{Improved cosmological fits with quantized primordial power spectra}",
      journal = {\prd},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology},
         year = 2022,
        month = apr,
       volume = {105},
       number = {8},
          eid = {083515},
        pages = {083515},
          doi = {10.1103/PhysRevD.105.083515},
archivePrefix = {arXiv},
       eprint = {2104.01938},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022PhRvD.105h3515B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2022PhRvD.105l3508P,
       author = {{Prathaban}, Metha and {Handley}, Will},
        title = "{Rescuing palindromic universes with improved recombination modeling}",
      journal = {\prd},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology},
         year = 2022,
        month = jun,
       volume = {105},
       number = {12},
          eid = {123508},
        pages = {123508},
          doi = {10.1103/PhysRevD.105.123508},
archivePrefix = {arXiv},
       eprint = {2111.14588},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022PhRvD.105l3508P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2020NatAs...4..196D,
       author = {{Di Valentino}, Eleonora and {Melchiorri}, Alessandro and {Silk}, Joseph},
        title = "{Planck evidence for a closed Universe and a possible crisis for cosmology}",
      journal = {Nature Astronomy},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Phenomenology, High Energy Physics - Theory},
         year = 2020,
        month = feb,
       volume = {4},
        pages = {196-203},
          doi = {10.1038/s41550-019-0906-9},
archivePrefix = {arXiv},
       eprint = {1911.02087},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2020NatAs...4..196D},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2021PhRvD.103d1301H,
       author = {{Handley}, Will},
        title = "{Curvature tension: Evidence for a closed universe}",
      journal = {\prd},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology},
         year = 2021,
        month = feb,
       volume = {103},
       number = {4},
          eid = {L041301},
        pages = {L041301},
          doi = {10.1103/PhysRevD.103.L041301},
archivePrefix = {arXiv},
       eprint = {1908.09139},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021PhRvD.103d1301H},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2022MNRAS.517.3087G,
       author = {{Glanville}, Aaron and {Howlett}, Cullan and {Davis}, Tamara},
        title = "{Full-shape galaxy power spectra and the curvature tension}",
      journal = {\mnras},
     keywords = {cosmological parameters, early Universe, large-scale structure of Universe, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2022,
        month = dec,
       volume = {517},
       number = {2},
        pages = {3087-3100},
          doi = {10.1093/mnras/stac2891},
archivePrefix = {arXiv},
       eprint = {2205.05892},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.3087G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2020MNRAS.496L..91E,
       author = {{Efstathiou}, George and {Gratton}, Steven},
        title = "{The evidence for a spatially flat Universe}",
      journal = {\mnras},
     keywords = {cosmic background radiation, cosmological parameters, inflation, Astrophysics - Cosmology and Nongalactic Astrophysics, High Energy Physics - Theory},
         year = 2020,
        month = jul,
       volume = {496},
       number = {1},
        pages = {L91-L95},
          doi = {10.1093/mnrasl/slaa093},
archivePrefix = {arXiv},
       eprint = {2002.06892},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2020MNRAS.496L..91E},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2021arXiv210906204B,
       author = {{Boyle}, Latham and {Turok}, Neil},
        title = "{Two-Sheeted Universe, Analyticity and the Arrow of Time}",
      journal = {arXiv e-prints},
     keywords = {High Energy Physics - Theory, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology, High Energy Physics - Phenomenology},
         year = 2021,
        month = sep,
          eid = {arXiv:2109.06204},
        pages = {arXiv:2109.06204},
          doi = {10.48550/arXiv.2109.06204},
archivePrefix = {arXiv},
       eprint = {2109.06204},
 primaryClass = {hep-th},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv210906204B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2017CCoPh..22..852T,
       author = {{Tram}, Thomas},
        title = "{Computation of Hyperspherical Bessel Functions}",
      journal = {Communications in Computational Physics},
         year = 2017,
        month = sep,
       volume = {22},
       number = {3},
        pages = {852-862},
          doi = {10.4208/cicp.OA-2016-0071},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2017CCoPh..22..852T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

```

When writing the blog poste emphasise the facts
- Neil Turok and Latham Boyle originally built their CPT symmetric universe models, which impose conditions at the start of the universe
- Anthony Lasenby built future conformal boundary models which impose symmetry conditions at the end of the universe
- this work combines those two approaches, extending Lasenby to include curvature, and Turok to include a future conformal boundary
- Wei-Ning presented this work in a talk at the CAM LMU meeting, and a summary of who was there

Please include relevent references with their numbers throughout the text. Format these in markdown as [XXXX.YYYYY](https://arxiv.org/abs/XXXX.YYYYY), with the correct numbers filled in as inferred from the latex of the paper.

Please use a tone written by a scientific expert, so no hyperbole or spin. The aim is to communicate the science clearly and accurately, but in a way that is accessible to a general audience.

{% endraw %}

---
id: camb-torsion
title: "Navigating CAMB's BBN Pipeline for Modified $N_\\text{eff}$"
category: "Legacy Code Navigation"
timebox: "one session"
status: "Complete"
summary: "In Poincaré gauge torsion gravity, the torsion parameter ϖ_r implicitly modifies
  the effective number of relativistic species. Feeding the resulting dark energy into CAMB
  without propagating that modification to the BBN helium predictor silently biases the CMB
  damping tail. Claude traced the parameter through three modules to identify the
  inconsistency and implement the fix."
outcome: "A corrected Cobaya theory class that computes the N_eff shift from the torsion
  parameter and passes the consistent Y_He to CAMB, enabling trustworthy CMB power spectrum
  constraints on the torsion model."
evidence: "Systematic LLM-guided code archaeology with reference-output validation."
author: "Sinah Legner, Institute of Astronomy, University of Cambridge"
date: 2026-05-05
---

## Torsion Condensation

[Torsion Condensation (TorC)](/papers/2025/07/12/2507.09228.html) is a one-parameter extension of ΛCDM arising from Poincaré gauge
theory — a formulation of gravity motivated by the gauge field theories of the Standard Model
([Barker et al. 2020](https://arxiv.org/abs/2003.02690)). Unlike general relativity, the
theory incorporates intrinsic torsion degrees of freedom which modifies the
early-Universe expansion history. The key parameter is $\varpi_r$, the value of the torsion
scalar field in the radiation era; when $\varpi_r \to 1$ the model reduces to standard ΛCDM.


#### CAMB implementation through $\rho(a)$ and $P(a)$

In the numerical implementation, the torsion contribution is encoded through the effective dark energy density $\rho(a)$ and pressure $P(a)$, obtained from the TorC
background evolution equations. These are supplied to CAMB through the parametrized
post-Friedmann (PPF) dark-energy framework, allowing the modified expansion history to be
evolved consistently within the Boltzmann solver.

#### Effective Number of Neutrinos

During radiation domination, the torsion scalar field behaves effectively as an additional
radiation-like component with equation of state $w = 1/3$. As a result, $\varpi_r$ can be
interpreted as modifying the effective relativistic energy density, producing an equivalent
shift in $N_{\rm eff}$ ([Barker et al. 2020](https://arxiv.org/abs/2003.02690)). The corresponding effective number of relativistic species is

$$N_{\rm eff}^{\rm TorC}(\varpi_r) = N_{\rm eff,std} + \left(\varpi_r^{-2} - 1\right)\left[\frac{8}{7}\left(\frac{4}{11}\right)^{4/3} + N_{\rm eff,std}\right].$$

When $\varpi_r = 1$ the model reduces to standard $\Lambda$CDM. For $\varpi_r < 1$, the
enhanced early-time expansion rate reduces the sound horizon at recombination and permits a
larger CMB-inferred value of $H_0$.

## The BBN–CMB connection

The primordial helium abundance $Y_{\rm He}$ predicted by BBN depends sensitively on the expansion
rate during nucleosynthesis. A larger effective radiation density causes the Universe to expand
faster, leading to earlier weak-interaction freeze-out, a larger neutron fraction, and therefore
more primordial helium production. This altered helium abundance subsequently affects the CMB
damping tail: a larger $Y_{\rm He}$ reduces the number density of free electrons prior to hydrogen
recombination, increasing photon diffusion damping at small angular scales
([Cooke 2024](https://arxiv.org/abs/2409.06015)). Since $\varpi_r \neq 1$ modifies the
early expansion rate, a consistent analysis must propagate this modification through to $Y_{\rm He}$
— the baseline TorC chain does not do this, making it physically inconsistent.

## Claude's assistance

<div style="display:flex; gap:0.6rem; margin:2rem 0; align-items:stretch;">

<div style="flex:1; border:2px solid #DC267F; border-radius:8px; padding:0.8rem 0.8rem; background:rgba(220,38,127,0.04);">
<h4 style="color:#DC267F; margin-top:0; border-bottom:1px solid #DC267F; padding-bottom:0.4rem;">① Human attempt</h4>

<p><strong>Goal:</strong> Inform CAMB of $\varpi_r$'s effect on the CMB damping tail through BBN.</p>

<p><strong>Approach:</strong> Pass $N_{\rm eff}^{\rm TorC}(\varpi_r)$ directly to CAMB. The BBN predictor would then use the correct $N_{\rm eff}$ and compute a consistent $Y_{\rm He}$.</p>

<p><strong>Result:</strong> $\varpi_r$ is pulled tighter towards 1 relative to the baseline.</p>

<img src="/assets/images/recipes/recipe_before.png" style="width:100%; margin-top:0.8rem; border-radius:4px;">
</div>

<div style="flex:1; border:2px solid #648FFF; border-radius:8px; padding:1.2rem 0.8rem; background:rgba(100,143,255,0.04);">
<h4 style="color:#648FFF; margin-top:0; border-bottom:1px solid #648FFF; padding-bottom:0.4rem;">② AI-assisted diagnosis</h4>

<p><strong>1. Understanding the pipeline.</strong></p>
<ul>
<li>Torsion ODE solver → $\rho(a)$, $P(a)$</li>
<li>CAMB Boltzmann solver → $H(a)$</li>
<li>CAMB BBN predictor → $Y_{\rm He}(\Omega_b h^2,\, \Delta N_{\rm eff})$</li>
</ul>

<p><strong>2. Identifying the double counting.</strong> CAMB uses the same $N_{\rm eff}$ parameter for both $\Omega_r$ and the BBN helium prediction — so modifying it changes both simultaneously. With $\varpi_r$ already entering through Route A, passing a modified $N_{\rm eff}$ adds a second radiation contribution on top:</p>

<div style="margin:0.8rem 0; font-size:0.92em; line-height:1.8;">
  <div style="margin-bottom:0.6rem;">
    <span style="font-weight:600; color:#648FFF;">Route A</span><br>
    $\varpi_r \;\to\; \rho(a),\, P(a) \;\to\; H(a)$
  </div>
  <div style="margin-bottom:0.8rem;">
    <span style="font-weight:600; color:#648FFF;">Route B</span><br>
    $\varpi_r \;\to\; \Delta N_{\rm eff} \;\to\; \Omega_r \;\to\; H(a)$<br>
    $\phantom{\varpi_r \;\to\; \Delta N_{\rm eff} \;\to\;} \hookrightarrow\; Y_{\rm He}$
  </div>
  <div style="text-align:center; border:2px solid #c0392b; border-radius:6px; padding:0.3rem 0.6rem; color:#c0392b; font-weight:600; display:inline-block;">
    $H(a)$ double counts $\varpi_r$'s effect
  </div>
</div>
</div>

<div style="flex:1; border:2px solid #1a7a4a; border-radius:8px; padding:1.2rem 0.8rem; background:rgba(26,122,74,0.04);">
<h4 style="color:#1a7a4a; margin-top:0; border-bottom:1px solid #1a7a4a; padding-bottom:0.4rem;">③ AI-proposed fix</h4>

<p>Keep the expansion history entirely in $\rho(a)$ and $P(a)$. Compute $\Delta N_{\rm eff}(\varpi_r)$ separately and compute $Y_{\rm He}$ through the BBN predictor, and pass this corrected $Y_{\rm He}$ directly to CAMB.</p>

<div style="margin:0.8rem 0; font-size:0.92em; line-height:1.8;">
  <div style="margin-bottom:0.6rem;">
    <span style="font-weight:600; color:#1a7a4a;">Expansion history</span><br>
    $\varpi_r \;\to\; \rho(a),\, P(a) \;\to\; H(a)$
  </div>
  <div style="display:flex; align-items:center; gap:0.6rem; flex-wrap:wrap;">
    <div>
      <span style="font-weight:600; color:#1a7a4a;">BBN correction</span><br>
      $\varpi_r \;\to\; \Delta N_{\rm eff} \;\to\; Y_{\rm He}$
    </div>
    <div style="border:2px solid #1a7a4a; border-radius:6px; padding:0.3rem 0.6rem; color:#1a7a4a; font-weight:600; white-space:nowrap;">
      $H(a)$ modified once
    </div>
  </div>
</div>

<img src="/assets/images/recipes/recipe_after.png" style="width:100%; margin-top:0.8rem; border-radius:4px;">
</div>

</div>

## What was done with Claude

Claude traced $N_{\rm eff}$ through the CAMB source to identify where $\varpi_r$'s effect on the expansion history was already encoded, diagnosed the double-counting introduced by the human fix, and proposed bypassing CAMB's $N_{\rm eff}$ interface to correct $Y_{\rm He}$ directly. The comparison plots on this page were also generated with Claude's assistance, as was the design and writing of this recipe.


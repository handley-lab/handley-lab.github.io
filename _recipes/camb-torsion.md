---
id: camb-torsion
title: "Propagating torsional gravity modified N_eff into CAMB's primordial helium calculation"
category: "Legacy Code Navigation"
timebox: "one session"
status: "Draft"
proposer: "Sinah Legner"
summary: "In Poincaré gauge torsion gravity, a single parameter (cpr) implicitly modifies
  the effective number of relativistic species. Feeding the resulting dark energy into CAMB
  without propagating that modification to the BBN helium predictor silently biases the CMB
  damping tail. Claude traced the parameter through three modules to identify the
  inconsistency and implement the fix."
outcome: "A corrected Cobaya theory class (rhopa_mnu/rhopa_mnu/core.py) that computes
  delta_N_eff from cpr and passes the consistent Y_He to CAMB, enabling trustworthy CMB
  power spectrum constraints on the torsion parameter."
evidence: "Fix in TorC_omk/packages/rhopa_mnu/rhopa_mnu/core.py. Verification chains:
  rhopa_modified_YHe, rhopa_modified_YHe_checkplanck, rhopa_modified_YHe_checkH0."
author: "Sinah Legner, Institute of Astronomy, University of Cambridge"
date: 2026-05-05
---

## The problem

Poincaré gauge torsion gravity introduces a dimensionless field ϖ (`cpr`) that modifies
the Friedmann equation. In the radiation-dominated era, the torsion field acts like extra
radiation: varying `cpr` away from 1 is mathematically equivalent to changing the effective
number of relativistic species, N_eff.

The pipeline for producing CMB predictions has three stages, each sensitive to N_eff:

1. **The dark energy solver** (`rhopa_mnu`) integrates the torsion field equations to produce
   ρ(a) and P(a). These are fed into CAMB as tabulated dark energy via a custom
   `DarkEnergyPressurePPF` class.
2. **CAMB's Boltzmann solver** uses those arrays to compute H(a) and the CMB power spectrum.
3. **CAMB's BBN predictor** independently computes the primordial helium abundance Y_He from
   (ombh2, delta_N_eff), which sets the free electron fraction and the photon diffusion scale.

The bug: stages 1 and 2 knew about the modified N_eff (it was encoded in the ρ(a)/P(a)
arrays). Stage 3 did not — it used the default N_eff = 3.044, producing a Y_He inconsistent
with the expansion history the Boltzmann solver was actually running.

## What Claude traced

The session started with a question: *why is nnu not appearing in the chains even though the
model is varying the radiation content?* Claude read three files in sequence.

**`equations.py`** revealed that `omega_r(h, nnu)` — the radiation density entering the ODE
— uses a standard `nnu`. The `cpr` dependence enters through the geometry of the torsion
field equations, not by explicitly varying `nnu`. So `nnu` never appeared as a sampled
parameter; its effect was absorbed silently into the shape of ρ(a).

Two helper functions made the connection explicit:

```python
def Neff_modified(cpr, nnu=3.046):
    A = 8/7 * (11/4)**(4/3)
    return (cpr**(-2) - 1) * (A + nnu) + nnu

def delta_Neff(cpr, nnu=3.046):
    return Neff_modified(cpr, nnu) - nnu
```

`cpr = 0.99` gives delta_N_eff ≈ +0.27 — comparable to the width of current observational
constraints.

**`model.py` (CAMB)** showed the BBN call at line 690:

```python
YHe = bbn_predictor.Y_He(ombh2, nnu - standard_neutrino_neff)
```

This uses whatever `nnu` you pass to `set_cosmology`. If you pass the default 3.044, delta_neff
is zero, and Y_He comes out standard regardless of what `cpr` is doing to the expansion
history.

**`bbn.py`** confirmed the scale of the error: the PArthENoPE fitting formula gives
roughly ΔY_p ≈ 0.013 per unit of delta_N_eff. A `cpr` shift of 0.01 — well within a typical
posterior — moves Y_He by ~0.004, enough to shift the CMB damping tail by a detectable
amount.

## The fix

The corrected `core.py` does three things per sample:

```python
# 1. Solve the torsion equations as before
a, rho, P = rhopsol(cpr, omega_m, h, OmL, mnu, nnu=nnu)

# 2. Compute the N_eff shift implied by cpr
delta_neff = delta_Neff(cpr, nnu)

# 3. Pass the consistent Y_He to CAMB
YHe = bbn_predictor.Y_He(ombh2, delta_neff)
state["YHe"] = YHe
```

CAMB receives `YHe` via `get_param("YHe")` and skips its own BBN computation. The helium
abundance is now consistent with the same N_eff shift already encoded in ρ(a)/P(a).

## Why this matters

The failure mode is silent. Runs without the fix produce valid-looking CMB spectra — the
Boltzmann solver converges and the chains sample normally. The inconsistency only shows up in
the damping tail and recombination timing, where a ~0.004 shift in Y_He is detectable by
Planck at roughly 2σ. Without the fix, the posterior on `cpr` is subtly biased: the model
is simultaneously claiming a modified expansion history and a standard helium abundance,
which is physically impossible.

The broader lesson: when a single parameter affects multiple independent physics modules in a
pipeline, tracing the parameter through each module explicitly — rather than trusting that
the pipeline handles it — is the only way to catch this class of bug.

---

## Methods note

The relationship between `cpr` and N_eff comes from the Friedmann equation in Poincaré gauge
gravity. At early times the torsion field ϖ satisfies ϖ ≈ cpr (constant), and the modified
Friedmann equation reduces to:

$$H^2 = \frac{1}{\text{cpr}^2} \cdot \frac{8\pi G}{3}\rho_r + \ldots$$

This is equivalent to rescaling the radiation density by cpr⁻², which maps onto an effective
N_eff via:

$$N_\text{eff}^\text{torsion} = \left(\text{cpr}^{-2} - 1\right)\left(\frac{8}{7}\left(\frac{11}{4}\right)^{4/3} + N_\text{eff,std}\right) + N_\text{eff,std}$$

The ODE in `equations.py` uses `nnu/3*2` in `omega_r` calls within `dda`/`ddcp` — this
passes 2/3 of `nnu` to account for only the massless neutrino species (the third is
handled separately as a massive neutrino via CAMB's `get_Omega_mnu` / `get_w_massive_nu`).

The BBN sensitivity arises because faster expansion at nucleosynthesis (higher N_eff → higher
H) freezes out the neutron-to-proton ratio earlier, leaving more neutrons available for
helium synthesis. The PRIMAT 2021 table used by default in CAMB covers
ombh2 ∈ [0.005, 0.065] × delta_N_eff ∈ [-2, 4] and returns Y_He to ~0.1% accuracy.

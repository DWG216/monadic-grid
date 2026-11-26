# PREDICTIONS t169: one η or two? The record's field entanglement on the grid's own grain

Registered 2026-11-26, committed before t169_field_eta.py is written or run.

Question (record §314). The grid defines G = 1/(4η), with η what the record cannot see per unit horizon area. Two counts claim to be η:
- meetings across the horizon, three hidden states each: η_m = (√3/10) ln 3 = 0.190 per cell area (t166 density, §308 states);
- the record's field entanglement, t27: 0.295 R² per degree of freedom on a sphere, so 0.0235 per degree of freedom per lattice area, times N = 118 degrees of freedom: 2.77 per lattice area.
Sufficient reason allows one η. t27 was computed on a regular lattice, which t151 excluded as the grain. Here the field entanglement is computed on the grain itself.

Inputs fixed before code, each from earlier results:
- Grain: Poisson sprinkling at one event per cell (t151; §312: events are writings, one per cell), ρ = 1, in a 4D causal diamond of height T, N = πT⁴/24 elements on average.
- Propagator: the record's links carry it (t158): K_R = (√ρ/(2π√6)) L, L the link matrix; iΔ = i(K_R − K_Rᵀ).
- State: Sorkin–Johnston, W = positive part of iΔ (no choice of frame or slice, consistent with t160).
- Truncation, from the sampling bound (t133: one sample per cell): a field sampled once per cell carries one mode per cell of a Cauchy surface. Keep the n largest positive eigenvalues of iΔ (with their negative partners), n = number of cells on the region's widest Cauchy surface: n_D = (π/6)T³ for the diamond, n_R = n_D/2 for the half. The same rule is applied to the diamond (to build W) and to the region (double truncation, Sorkin–Yazdi 2016).
- Region R: the domain of dependence of the half-ball {t = 0, x < 0, r < T/2}: elements with x < −|t|. Complement R': x > |t|. Entangling surface: the disk x = 0, r < T/2, area A = π(T/2)².
- Entropy: S = Σ μ ln|μ| over the generalized eigenvalues W_R v = μ iΔ_R v within the kept subspace of iΔ_R (Sorkin 2012).
- Sizes N = 1500, 3000, 6000 (mean), two sprinklings each (seeds 1691–1696).

S1 [sanity]: complement symmetry: |S(R) − S(R')| / mean < 0.15 for every sprinkling.
P1 [M]: area law on the grain: fitting S ∝ A^p over the six sprinklings, 0.75 < p < 1.25.
P2 [M, the test]: one η. The per-degree-of-freedom coefficient η_f = S/A (mean over the N = 6000 runs), times 118, lies within a factor 1.5 of η_m = 0.190 (between 0.127 and 0.285). Pass: the field entanglement and the meeting count are the same η on the same grain, and t27's 2.77 was the regular lattice's. Fail: reported with the value; the two counts disagree on the grain and one of them is not the record's entropy (next to be decided from the ground).
Reported, not scored: η_f against t27's lattice 0.0235 per degree of freedom; S/A for each N.

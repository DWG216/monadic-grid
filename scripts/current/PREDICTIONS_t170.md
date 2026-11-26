# PREDICTIONS t170: the field route with the record's own frequency cut

Registered 2026-11-26, committed before t170_field_cut.py is written or run.

Question. t169 found the field's entanglement on the grain near the volume law, because its mode-count cut barely acted at reachable sizes. The record has a sharper cut from the ground: it registers at most π of phase per tick (t133), so a mode turning faster than π per tick (ω > ω_N = π in cell units) writes the same record as its alias and is not a separate degree of freedom of the record. By §316 the record's entropy does not depend on the number of fields: one field (the hands' relative phase) is computed, with no ×118.

Inputs fixed before code:
- Grain, propagator, state and region as in t169: Poisson sprinkling, ρ = 1, 4D diamond of height T (N = πT⁴/24 mean); K_R = L/(2π√6); iΔ = i(K_R − K_Rᵀ); W = positive part of iΔ; region R = {x < −|t|}, complement R' = {x > |t|}; entangling disk area A = π(T/2)².
- Frequency cut: an on-shell mode of frequency ω, held over a time extent τ, gives an eigenvalue of the discrete iΔ of size λ ≈ ρτ/(2ω). The cut ω ≤ π keeps eigenpairs with |λ| ≥ λ_N = τ/(2π). τ is the region's mean time extent, its 4-volume over the 3-volume of its Cauchy surface: τ = N_D/((π/6)T³) for the diamond, τ_R = N_R/((π/12)T³) for each half (element counts over the half-ball volume). The cut is applied to the diamond (to build W) and to each half (double truncation).
- Entropy S = Σ μ ln|μ| over W_R v = μ iΔ_R v in the kept subspace of iΔ_R.
- Sizes N = 1500, 3000, 6000 (mean), two sprinklings each, seeds 1697–1702.

S1 [sanity]: complement symmetry |S(R) − S(R')|/mean < 0.15 for every sprinkling with N ≥ 3000.
P1 [M]: area law: S ∝ A^p over the six sprinklings with 0.75 < p < 1.25.
P2 [M, the test]: one η. η_f = S/A (mean of the N = 6000 runs) lies within a factor 1.5 of the meeting count η_m = (√3/10) ln 3 = 0.190 (between 0.127 and 0.285). Pass: the field route, cut where the record cuts, gives the meeting count; one η. Fail: reported with the value.
Reported, not scored: modes kept in the diamond and in each half against the Nyquist count (π/6)V_s; S/A for each N; 3η_f.

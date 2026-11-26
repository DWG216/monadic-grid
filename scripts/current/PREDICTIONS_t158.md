# PREDICTIONS t158: the covariant kernel is the record's links

Registered 2026-11-26, before t158_links_kernel.py was written or run.

Problem. t156–t157 write the record's noise and decoherence with the Newtonian kernel δ(t − t′)/|x − y|, smeared at R₀ in one rest frame: not covariant.
Proposal [S + I]. On the sprinkled grain (t151) the only frame-free relation between two cells is the causal order, and its irreducible part is the link (p ≺ q with nothing between). Johnston (2008): on a 4D sprinkling of density ρ the massless retarded propagator is (√ρ/(2π√6)) × the link matrix. So the covariant decoherence kernel of the record is its links, time-symmetrised (retarded plus advanced): K_cov(p, q) = (√ρ/(2π√6)) [p, q linked], with the same prefactor as t157 (G/ħ and the record strength a). For static masses, integrating the continuum kernel over time gives 1/|x − y| exactly, so the Newtonian form of t157 is its rest-frame limit.
Expected links between small blobs A, B (spatial volumes V_A, V_B, separation s, lab duration T, link probability exp(−ρπτ⁴/24)): N_L = 2Tρ² ∫∫ I(s) with I(s) = ∫₀^∞ e^{−ρπw²/24} dw / (2√(w + s²)).

S1 [M]: continuum check: the time integral of the symmetric kernel 2δ(t² − r²), regularised as a Gaussian of width 1e-4 in t² − r², gives 1/r within 1e-3 at r = 1, 3, 10.
P1 [M]: N_L × √ρ/(2π√6) divided by ρ²TV_AV_B/(2πs) tends to 1: within 2% at s = 20 grain lengths (ρ = 1), and the fitted power of s over s ∈ [10, 100] is −1.00 ± 0.02.
P2 [M]: covariance: two blobs moving together at rapidity η = 0.5 and 1.0, rest separation 20 perpendicular and parallel to the motion: link count per unit proper time equals the rest value within 3% (Monte Carlo over the blobs, numerical time integral). The frame-fixed Newtonian kernel fails: per unit proper time it gives γ (perpendicular) and γ² (parallel) times the rest value, both more than 10% off at η = 1.
P3 [M + I, expected to exclude]: the link kernel is finite at zero separation: k(0) = I(0)·2√ρ/√6 in units where k(s) → 1/s. Its effective Gaussian smearing length R_link = 1/(√π k(0)) is of order the grain (ρ^(−1/4)); with the grain at 3.33 l_P (t27, §122) that is about 1e-34 m, against Gran Sasso's R₀ > 0.54 Å. Prediction: the links do not set the mass resolution; R₀ must come from the matter side (what the record resolves of a mass), not from the grain.
Consequence fixed in advance: P1 and P2 pass → the record's decoherence and noise are covariant on the sprinkled grain, with the Newtonian form as their rest-frame limit; the Hamiltonian constraint of the full metric is still not built.

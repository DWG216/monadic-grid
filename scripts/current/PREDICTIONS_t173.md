# PREDICTIONS t173: positive energy from the singlet (Witten's spinor argument as the record's law)

Registered 2026-11-26, committed before t173_positive_energy.py is written or run.

Reading [S]. §308/§319: a spinor pair's record splits 1 ⊕ 3; the singlet ½|ψ|² is the meeting term, gravity's source; the triplet writes the gauge field (t171). R3: only the singlet sources curvature, so the energy density gravity sees is non-negative, ρ ≥ 0. Witten (1981): with a spinor ε solving the Dirac equation on a slice and tending to a constant ε₀ at infinity, 4π m |ε₀|² = ∫ (|∇ε|² + ¼ R |ε|²) dV, and R = 16πρ on time-symmetric data, so ρ ≥ 0 gives m ≥ 0. In the record: gravity's mass is non-negative because its source is the square's balanced part.

Setting: time-symmetric, spherically symmetric, conformally flat slices g = ψ⁴ δ (G = c = 1), written with the scaled source ρ̃ = ρψ⁴: (r²ψ')' = −2π r² ρ̃ ψ, ψ → 1, ADM mass m from ψ = 1 + m/(2r) outside the source. The Witten spinor on such a slice is ε = ψ⁻² ε₀ (conformal covariance of the Dirac operator in three dimensions), which gives |∇ε|² dV = 6 ψ'² ψ⁻⁴ d³x and ¼R|ε|² dV = 4π ρ̃ ψ⁻² d³x for |ε₀| = 1.
Sources: 1,000 random profiles ρ̃(r) = Σ of 3 Gaussian shells (centres in [0.5, 4], widths in [0.2, 1], amplitudes in [0, 0.02]), seed 1730, solved on r ∈ [0, 12].

P1 [M]: Witten's identity: ∫ (6ψ'²ψ⁻⁴ + 4πρ̃ψ⁻²) 4πr² dr = 4πm to 1e-6 relative for every profile.
P2 [M]: with the singlet as the only source (ρ̃ ≥ 0): m > 0 for every profile, and both integrands are non-negative everywhere.
P3 [M]: if the source also carried the triplet's sign-indefinite cross term (amplitudes drawn from [−0.02, 0.02] instead), the identity still holds (P1's tolerance) but m < 0 occurs in at least 10% of 1,000 profiles: positivity comes from the singlet, not from the identity.
Consequence fixed now: if P1–P3 pass, the record holds that gravity's mass is non-negative because only the singlet of the square sources it (Witten's argument, read in the record).
Gate: statement about nature; public.

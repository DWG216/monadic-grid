# PREDICTIONS t179: the glueball ratio with the Coulomb term (reanalysis of t177's configurations)

Registered 2026-11-27, committed before t179_cornell.py is written or run. Uses the measurements saved by t177 (t177_SU2.npz, t177_2I.npz); W(R, T) for R, T = 3, 4 at T = 4 and the static potential have not been looked at.

Why. t177's S2 failed because the Creutz ratio χ(3,3) still carries the Coulomb term. The static potential V(R) = ln[W(R,3)/W(R,4)] for R = 1..4, fitted to the Cornell form V(R) = V₀ + σR − e/R, separates them.

P1 [sanity]: SU(2): the fitted e lies within a factor 2 of the string value π/12 ≈ 0.26, and σa² within 30% of the literature 0.071 at β = 2.4.
P2 [M]: SU(2): m(0⁺⁺)/√σ (with t177's mass ln C(1)/C(2)) within 20% of 3.78.
P3 [M]: 2I equals SU(2) in σ within two combined jackknife errors, and in the ratio within two combined errors.
Consequence fixed now: if P2 and P3 pass, the grain's gauge group gives SU(2)'s glueball ratio, with the value near the continuum one; if P2 fails, the value stays unestablished at this lattice size.
Gate: physics; public.

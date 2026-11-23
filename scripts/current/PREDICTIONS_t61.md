# t61 explicit googly construction on PT = PG(3,9) (pre-registered 2026-11-23, before run)
Coordinates Z = (omega0, omega1, pi0, pi1). Dual map D(Z) = (pi0^3, pi1^3, omega0^3, omega1^3) = (lambda, mu) (Sigma(Z) = Z . D(Z)).
ASD graviton: fiber shear Phi_A: omega1 -> omega1 - eps g(omega0, t), g = omega0^2 t, on the pi-fibration (t = pi1/pi0).
SD graviton: the same shear on dual twistor space, Phi_S: mu1 -> mu1 - eps g(mu0, u), u = lambda1/lambda0, on the lambda-fibration.
E1 D is a bijection of the 820 points and D(D(Z)) = Z (involution); D maps each spacetime line L_x to the dual line {(lambda, x^(3) lambda)} of the conjugate point x^(3).
E2 D maps each pi-fiber onto a lambda-fiber (the dual fibration pulled back is the original fibration).
E3 D^-1 Phi_S D is a fiber shear over pi: omega1 -> omega1 - eps' g(omega0^3, t^3)^3 with omega0, pi unchanged (checked on all points).
E4 The googly patching Phi = Phi_A o (D^-1 Phi_S D) is a bijection of PT that fixes pi, shears only omega1: both helicities deform one space over one fibration.
E5 On F9 points the SD shear equals the ASD shear (g(w^3, t^3)^3 = g(w, t), since x^9 = x); as formal polynomials they differ (degrees 2+1 vs 18+9).
E6 Formal sections for the combined patching eps*(omega0^2 t + omega0^18 t^9) exist for random x (matching 50/50, the t59 split).
E7 Over F9 the combined (googly) null relation differs from the ASD-only one for at least 1 of 20 sampled x.

## Run 1 outcome (recorded before t61b): E1, E2, E4, E5, E6 pass; E3 FAIL (my bug: shear term omega0^2 pi1 has degree 3, not 1, so the map is not projective); E7 FAIL (0/20): the formal Frobenius image omega0^18 t^9 has all t-powers >= 2, so it is holomorphic on U0 = pure gauge.

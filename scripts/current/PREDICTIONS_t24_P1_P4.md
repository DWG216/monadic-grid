# t24: tests P1-P4 of the gluing design (§99), pre-registered 2026-11-22 18:15
P1 twistor carrier [M]. f(Z) = 1/((A.Z)^3 (B.Z)^3) (degree -6), g(W) = its dual-space analogue, reference r = (C.Z)^d, s = (D.W)^d.
Record on ambitwistor space I(Z,W) = (f + r)(g + s). Phase projection onto bidegrees with 16 x 16 angles.
 P1a incidence: Z.W = 0 for Z on L_x, W on L*_x (max |Z.W| < 1e-12).
 P1b d = 2: the (-6, d) component divided by s(W) returns f on L_x; its Penrose transform phi_0(x) matches the direct transform (rel. err < 1e-8); likewise (d, -6)/r(Z) returns g and psi_0(x).
 P1c d = 2: the (-6, -6) component equals f g (rel. err < 1e-8): the product of the hands.
 P1d Gabor control d = -6: the same recovery of phi_0 fails (rel. err > 0.1).
P2 linear light-cone cut equation on the sphere [M]. Random shear sigma (spin weight 2, l = 2..8).
 P2a LCCE first order Z1 (ethbar^2 eth^2 Z1 = eth^2 sigmabar + ethbar^2 sigma) is real on a sphere grid (max|Im| / max|Re| < 1e-12).
 P2b one-hand truncation (H-space, ethbar^2 Z = sigma) is complex for generic sigma (max|Im| / max|Re| > 0.1) and real when sigma is pure electric.
 P2c (reported, at fixed u) adding a pure-magnetic shear leaves Z1 unchanged (< 1e-12).
 Scope note: building the linear conformal metric and Weyl from Z1 is not attempted here.
P3 second-order cross term [M]. Complex Sachs equations with independent hands Psi0 (drives sigma) and Psitilde0 (drives sigmatilde); D rho = rho^2 + sigma sigmatilde.
 P3a area deficit / lam^4 -> Psi0 Psitilde0 / 90 for independent complex values (rel. err < 1e-6).
 P3b one hand only (Psitilde0 = 0): deficit at order 4 is 0 (< 1e-12).
 P3c with the P1 fields at a point (Psi0 = psi_0 from the dual-space reading, Psitilde0 = phi_0 from the twistor reading), deficit/lam^4 = psi_0 phi_0 / 90.
P4 Kerr from the Kerr theorem [M].
 P4a the Kerr-Schild congruence (M = 1, a = 0.6) is geodesic and shear-free in flat space (|shear| / |grad l| < 1e-6 by finite differences).
 P4b its twistors Z(x) = (i x pi, pi) at 400 random real points lie on one quadric: smallest / next singular value of the 10-monomial matrix < 1e-10. Negative control (congruence twisted by 0.1 rad about z, x-dependent): ratio > 1e-3.
 P4c closure in one step: Kerr-Schild superposition with the same l and masses M1 = 0.4, M2 = 0.6 is vacuum (relative Ricci < 1e-6); superposing two Kerr-Schild terms with different l (a = 0.6 and a = 0.3) is not (> 1e-3).

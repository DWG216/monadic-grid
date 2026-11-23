# Pre-registered before running e8.py (2026-11-08 ~23:15 ET)
Conceptual point fixed in advance: E8 is not a separate topic. Our frame 2I (120 unit icosians) generates, over Z[phi], the icosian ring,
and the icosian ring IS the E8 lattice (Conway-Sloane, from memory). tau60 is built from icosians (Parzanchevski-Sarnak). So E8 should be
the lattice our frame and our expensive gate both live in, and the "60" of tau60 should be an E8/icosian count.
E1 [identity]: E8 Cartan Perron-Frobenius vector gives the 8 Zamolodchikov masses; m2/m1 = 2cos(pi/5) = phi; top eigenvalue of the E8
   adjacency = 2cos(pi/30) (Coxeter number 30 = edges of the icosahedron, noted, not claimed meaningful).
E2 [known math, not computed]: McKay: the 9 irreps of 2I (dims 1,2,2',3,3',4,4',5,6) are the nodes of affine E8; the twisted 2' of our codes is one node.
E3 [real test]: with norm N(q) = a + b sqrt5 and form Q(q) = a + b, the Z-span of {u, phi u : u in 2I} has rank 8, Gram matrix of 2Q is even,
   positive definite, determinant 1 (so it is E8, the unique such lattice), with exactly 240 vectors of Q = 1.
E4 [real test, the tie]: tau60 unnormalised = pure quaternion (0,1,1,2+phi) is an icosian (in the Conway-Sloane frame, or a signed coordinate
   permutation of it; we report which), with Q = 12. The number of icosians of reduced norm exactly 7+5phi is 120 x (59+1) = 7200, i.e. 60
   classes up to units: the 60 branches of the tau60 tree are the 60 icosian "primes" above 59.
Control: for reduced norm 3 (not prime in Z[phi]? 3 is inert, norm 9) the count is NOT 120 x 60; we predict 120 x (9+1) = 1200.

# Scored after run (2026-11-08)
E1 PASS: top eigenvalue 1.989044 = 2cos(pi/30); masses 1, 1.618, 1.989, 2.405, 2.956, 3.218, 3.891, 4.783; m2/m1 = phi to 1e-6.
E3 PASS: rank 8; Gram of 2Q even, det 1, positive definite -> E8. Q=1 vectors: 120 units + 120 of norm phi^-2 = 240.
E4 PASS: tau60 (0,1,1,2+phi) is an icosian in the Conway-Sloane frame itself (no permutation needed), Q = 12.
   Icosians of reduced norm 7+5phi: exactly 7200 = 120 x 60. Control norm 3: 1200 = 120 x 10, as predicted.
Reading: the 60 tau-gates are the 60 icosian elements of norm 7+5phi up to units: the 59+1 "primes" above 59 in the E8 lattice.
(Tier note: E4's count is the standard class-number-1 Hecke count; it was a real test of our code and frame, not new mathematics.)

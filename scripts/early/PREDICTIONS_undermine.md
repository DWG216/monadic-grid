# Pre-registered before running undermine.py (2026-11-08 ~23:40 ET). Label: math.
Claim under attack: "E8 is the only rung where an open (fluid) medium shows a finite face" (golden layer is special).
Fact used (math): any 2-dim irreducible 3-strand braid window is a quotient of the triangle group (2,3,n), n = order of the ratio of the
two crossing eigenvalues; finite iff n <= 5 (n=3 tetrahedral, 4 octahedral, 5 icosahedral), whatever theory it comes from.
Attack: leave spin-1/2. Scan SU(2)_k, k = 3..60 (k != 4), strands of spin j, all targets Y, for 2-dim windows; keep strands that are
fluid (d_j^2 not an integer); record crossing order n.
U1 [prediction, our honest guess]: fluid strands with OCTAHEDRAL (n=4) and TETRAHEDRAL (n=3) 2-dim windows exist. If so, the claim falls.
U2 [check]: for the first octahedral example, the 4-strand image (built from quantum 6j symbols) contains an infinite-order element,
   so it is a shadow of a fluid theory, exactly like level 8. Validation first: unitarity and braid relations to 1e-9.
If U1 finds none: the claim survives this attack (within SU(2)_k), and we say so.

# Scored after run (2026-11-08)
U1 PASS (the attack succeeds): among fluid strands (d^2 not an integer), 2-dim 3-strand windows: tetrahedral 36, octahedral 56, icosahedral 44
   (k <= 60). First octahedral: SU(2)_6, spin 1, target spin 2, d^2 = 5.8284 = (1+sqrt2)^2 (silver). First tetrahedral: SU(2)_10, spin 1,
   d^2 = 7.4641 = (1+sqrt3)^2.
U2 PASS: SU(2)_6 spin-1, 4 strands (dim 17): unitarity 3e-15, braid relations 4e-15. Target-2 window closes at 24 (octahedral = Clifford
   rotations, projectively); the same 3 strands' target-1 window is already dense (>20,000), and s1 s1 s1 s2 s2 has infinite order.
VERDICT: the claim "E8 is the only rung where a fluid medium shows a finite face" is FALSE. Octahedral (Clifford) and tetrahedral faces of
   fluid theories exist. The golden layer is not special in this respect.
Difference noted, NOT used as a rescue: at level 8 spin-1/2 EVERY 3-strand sector is finite; at SU(2)_6 spin-1 only one sector is.
   Whether "a whole 3-strand window closes" singles out golden is a NEW claim, to be pre-registered and attacked separately.
Observation (not claimed): each face pairs with a metallic number: octahedral (1+sqrt2)^2, tetrahedral (1+sqrt3)^2, icosahedral 2+phi.

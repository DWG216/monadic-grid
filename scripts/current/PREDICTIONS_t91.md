# t91 Hypercharge selection on the grid's cut (roadmap item 1) (pre-registered 2026-11-25, before any t91 code is written or run)

Ground (t66): the cut leaves SU(3)_C x SU(3)_L x SU(3)_R; the 27 = (3,3bar,1) + (3bar,1,3) + (1,3,3bar); SU(2)_L is the T-spin of SU(3)_L (components 1, 2 of its triplet).
Question: which U(1) in the span of T8_L, T3_R, T8_R is hypercharge, and is there a choice to explain?
[S] reading under test: if every U(1) that gives the Standard Model's charges is the same up to relabelling of SU(3)_R's components (a Weyl permutation), the grid makes no choice: hypercharge is forced.

Computation [M]: Y = a T8_L + b T3_R + c T8_R with fundamental weights (1/2, 1/(2 sqrt3)), (-1/2, 1/(2 sqrt3)), (0, -1/sqrt3). Require on the quarks Q (doublet) = 1/6 and the singlet D = -1/3; on the antiquarks the multiset {-2/3, 1/3, 1/3}; then check the lepton bifundamental without further freedom.
S1 Sanity: the standard weights are traceless on each triplet.
G1 [M] The quark bifundamental fixes a = -1/sqrt3 uniquely.
G2 [M] The antiquark multiset has exactly 3 solutions (b, c), one for each choice of which SU(3)_R component is u^c; they are permuted by the Weyl group of SU(3)_R.
G3 [M] For each of the 3 solutions the lepton bifundamental gives exactly the multiset {doublet -1/2, doublet +1/2, doublet -1/2, singlet +1, singlet 0, singlet 0} (L, H_u, H_d, e^c, nu^c, N), with no fitting.
G4 [M] sin^2 theta_W = 3/8 at the cut for each solution (Tr T3_L^2 / Tr Q^2 over the 27).
Verdict: G1-G4 pass -> hypercharge is forced up to relabelling; the "selection" left open in t66 carries no free choice.

## Scoring (2026-11-25)
Run 1 (t91_run1.log). All pass. G1: a = -1/sqrt3 fixed by the quarks (D at -1/3). G2: exactly 3 solutions (b, c) = (-1, -1/sqrt3), (1, -1/sqrt3), (0, 2/sqrt3), one per choice of the u^c component, permuted by SU(3)_R's Weyl group. G3: each gives the lepton multiset (L, H_u, H_d, e^c, nu^c, N) exactly, with consistent SU(2)_L doublets. G4: sin^2 theta_W = 3/8 for each.
Verdict: hypercharge is forced up to relabelling; t66's open "selection" carries no free choice.

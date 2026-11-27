# PREDICTIONS t172: the grid's groups fix Chern–Simons levels (ADE of modular invariants)

Registered 2026-11-26, committed before t172_chern_simons.py is written or run.

Question. The grid builds E6 from the binary tetrahedral group 2T (clock of three) and E8 from the binary icosahedral group 2I (clock of five), by the McKay graph (t60, t66); its flavour group S₄ is the octahedral rotation group, whose double cover 2O gives E7. In SU(2) Chern–Simons theory at level k (Witten 1989), the consistent ways to pair left and right characters (modular invariants) are classified by A, D and E (Cappelli–Itzykson–Zuber 1987). Claim [I]: the grid's groups fix the Chern–Simons levels at which their exceptional invariants occur: k = Σ dim(irreps) − 2, the Coxeter number h minus 2, and the invariant's diagonal is the group's exponent set.

Method, all from the groups built as unit quaternions (no table of ADE data is input):
- Build 2T, 2O, 2I by closure from generators; conjugacy classes by conjugation; character table by Burnside's method (common eigenvectors of the class matrices); McKay graph from tensoring with the defining 2-dimensional representation V (χ_V = 2 Re q).
- Remove the trivial representation's node; h from the largest adjacency eigenvalue, 2cos(π/h); exponents m from the eigenvalues 2cos(πm/h).
- SU(2)_k: S_λμ = √(2/(k+2)) sin(π(λ+1)(μ+1)/(k+2)), T = diag exp(2πi(h_λ − c/24)), h_λ = λ(λ+2)/(4(k+2)). Modular invariants: nonnegative integer M with M_00 = 1, [M, T] = 0 (slots with h_λ − h_μ ∈ Z), [M, S] = 0, found by enumerating the integer points of the commutant with free entries in {0, 1, 2}.

P1 [M]: orders 24, 48, 120; after removing the trivial node the McKay graphs are trees with 6, 7, 8 nodes and one branch node of degree 3, arms of 2, 2, 1 / 3, 2, 1 / 4, 2, 1 edges (E6, E7, E8); Σ dim(irreps) = h = 12, 18, 30; exponents {1, 4, 5, 7, 8, 11}, {1, 5, 7, 9, 11, 13, 17}, {1, 7, 11, 13, 17, 19, 23, 29}.
P2 [M]: for each group, at k = h − 2 (10, 16, 28) there is a modular invariant whose diagonal set {λ + 1 : M_λλ > 0} equals the group's exponents.
P3 [M]: at no other level 1 ≤ k ≤ 30 does any invariant found have that diagonal set.
Reported, not scored: 2cos(π/n), the clock of n's golden step, is the quantum dimension of spin ½ at k = n − 2 (clock of three: k = 1; clock of five: k = 3); this is a definition, not a result.
Consequence fixed now: if P1–P3 pass, the record holds that the grid's three binary groups fix the Chern–Simons levels 10, 16, 28 and their exceptional pairings, from the groups alone.
Gate: a statement about mathematics and nature; public. Applications to topological quantum computing are gated and not part of this test.

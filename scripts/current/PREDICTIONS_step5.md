# Pre-registration (2026-11-22, 05:05): step 5, the pairing measure (record §73)
Game (Karchmer-Wigderson, on a slice): one player holds a yes-graph x, the other a no-graph y of the same slice; they must name an edge in x and not in y. Any monotone formula separating yes from no on the slice splits the yes-by-no table into L rectangles, each labelled by one such edge.
Measure [M, proved in the record]: N = yes/no pairs one swap apart (B of them); N_i = those whose swapped-out edge is i; sigma = max_i top singular value of N_i. Inside a rectangle labelled i only N_i pairs can lie, at most sigma sqrt(|S||T|) of them; Cauchy-Schwarz over the L rectangles gives L >= K(f) = B^2 / (sigma^2 |X||Y|).
SANITY RUN (t14_sanity.py, m = 5; seen): single edge K = 1.000 (exact: its formula has one leaf); parity of 5 edges K = 21.4; triangle 8.36; degree >= 3: 6.25; invariant null 7.9-20.0 (median 13.2).
P1 [control] m = 6: single edge K = 1 on both slices. P2 [control] parity of 5 edges: K > 15 on both slices.
R1 [real] K(triangle) > K(degree >= 4) on the 7-edge slice and K(4-clique) > K(degree = 5) on the 8-edge slice: the pairing orders clique above its easy reference.
R2 [real] clique's K is below the median of the invariant null (100 random graph properties, seed 20261122) in both cases: at this size the pairing, like the spectrum, sees clique as simpler than a typical graph property.
E1 [exploratory] K per variable count (K / 15) and the trivial ceiling: sigma^2 >= B_0^2/(|X_0||Y_0|) type bounds are not computed; we only report values.

## Results (t14_step5.log)
P1 PASS (K = 1.000 on both slices). P2 PASS (23.70 on both).
R1: triangle FAIL (8.87 vs degree >= 4: 14.57); 4-clique PASS (6.88 vs degree = 5: 5.35). The pairing does not order clique above its easy reference consistently.
R2 PASS: null min/median/max 9.93 / 20.45 / 39.01 (triangle slice) and 9.05 / 24.65 / 36.43 (4-clique slice); clique is below every one of the 100 null draws in both cases.

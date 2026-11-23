# Pre-registration (2026-11-22, 04:50): step 4, measure the cut (record §71)
Setting as step 3: graphs on 6 vertices, slices of 7 edges (triangle) and 8 edges (4-clique); 24 isomorphism classes each. Easy references on the same slices: "some vertex has degree >= 4" (7 edges) and "some vertex has degree 5" (8 edges): threshold-type properties, cheap for monotone circuits.
Measures. Boundary B(f) = number of single edge-swaps that change f. Sensitivity s(x) = swaps at x that change f. Witness W1(f) (W0(f)) = fewest edges, stated present or absent, that force f = 1 (f = 0) on the whole slice; searched up to 6 (7 means more than 6).
SANITY RUN (t13_sanity.py, m = 5; seen): boundary computed directly equals the spectral formula (1140 = 1140); triangle W1 = 3, W0 = 4; degree >= 3: W1 = 3, W0 = 5; shuffled-class null W1 = 3 in 9 of 60 draws and 4 in 51, so both outcomes occur.
T1 [identity] B(f) = sum_j (lambda_0 - lambda_j) |f_j|^2 for clique and for 20 random functions: the size of the cut is a function of the spectrum, so it falls with spectral level (§70).
R1 [real] short witness: W1(triangle) = 3 and W1(4-clique) = 6, each at or below the 5th percentile of the null (200 random graph properties: class values shuffled, seed 20261122).
R2 [real] the easy references also have short witnesses at or below the null's 5th percentile (W1 = 4 and 5). If R1 and R2 both pass: witness size marks checkability (the NP side), and does not separate clique from easy properties.
R3 [real] asymmetry: W0 > W1 for clique in both cases (refuting is longer than witnessing).
E1 [exploratory] maximum sensitivity and its null range; W0 values; overlap of witnesses: the largest share of minimal 1-witnesses containing a given pair of edges, clique vs degree reference.

## Results (t13_step4.log)
T1 PASS (both slices; boundary 26,760 and 21,600).
R1 PASS: triangle W1 = 3 (null: 3 in 4 draws, 4 in 7, 5 in 186, 6 in 3; 5th pct 4). 4-clique W1 = 6 (null: 5 in 6 draws, 6 in 56, more than 6 in 138; 5th pct 6): passes as registered ("at or below") but weakly, 62 of 200 null draws are as short.
R2 PASS: degree >= 4: W1 = 4; degree = 5: W1 = 5; both at or below the null's 5th percentile.
R3 triangle PASS (W0 = 6 > 3); 4-clique FAIL: W0 = 3 < W1 = 6 (three absent edges forming a perfect matching exclude every 4-clique on 6 vertices). The witness asymmetry is not a property of every slice.
E1: max sensitivity: triangle 44, degree >= 4: 32 (null 37-56, median 49); 4-clique 42, degree = 5: 35 (null 37-56, median 48). Witness overlap: share through one edge = size/15 for all four families (forced by symmetry); through a pair: triangle 0.050, stars(4) 0.100, 4-clique 0.200, stars(5) 0.167.
Reading: R1 and R2 both pass, so witness size marks checkability and does not separate clique from the easy references. No one-sided measure of the cut tried here separates them.

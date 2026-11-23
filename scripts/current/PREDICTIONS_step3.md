# Pre-registration (2026-11-22, 04:45): step 3, a measure for antichains: the slice's own Fourier side (record §70)
Setting: graphs on m vertices with exactly k edges (a slice; n = C(m,2) variables). Functions on the slice split into levels j = 0..min(k, n-k) (Johnson scheme; level <= j = restrictions of degree-j polynomials). Mean level L(f) = sum_j j * (variance share at level j).
SANITY RUN (t12_sanity.py, m = 5, k = 5; seen, so not a test): positive control: a degree-3 monomial has zero variance above level 3. Triangle slice: shares 0, 0.35, 0.583, 0.067, 0 (L = 2.717); invariant null (the same class values shuffled among the 6 isomorphism classes): 5th pct 2.60, median 3.22, 95th 4.0; unstructured random: 3.47. With only 6 classes the null is coarse; the m = 6 cases below have not been computed.
[M, stated] A monotone slice circuit's literals and pseudo-complements have level <= 1 and AND/OR add levels, so depth D reaches level <= 2^D: level alone can give only a log-depth bound.
I1 [identity] m = 6: the number of independent invariant tones at level exactly j (rank of the level-j parts of the class indicators) = (graphs with j edges) - (graphs with j-1 edges) up to isomorphism = 1, 0, 1, 3, 4, 6, 6, 3 for j = 0..7 (from the counts 1, 1, 2, 5, 9, 15, 21, 24). The slice's invariant tones are subgraph counts.
C1 [control] m = 6, k = 7: a degree-3 monomial has no variance above level 3.
R1 [real] triangle, m = 6, k = 7: L(f) is below the 5th percentile of the invariant null (200 draws, seed 20261122; class values shuffled among classes; constant draws skipped).
R2 [real] 4-clique, m = 6, k = 8: the same.
(Reading fixed in advance: if R1 and R2 pass, clique is spectrally simpler than a typical graph property, so no measure that grows with spectral level can certify its hardness, and a random-like-is-large measure is ruled out twice: by natural proofs and by clique itself. If they fail, level is a candidate and we look closer.)
E1 [exploratory] variance shares by level for both; highest nonzero level.

## Results (t12_step3.log): all pass
I1 PASS: invariant tones per level 1, 0, 1, 3, 4, 6, 6, 3. C1 PASS.
R1 PASS: triangle (6,435 points, 24 classes, density 0.897): mean level 3.883 vs null 5th 4.341 (median 4.924); percentile 0.005. Shares, levels 1-7: 0, 0.115, 0.406, 0.182, 0.103, 0.167, 0.027.
R2 PASS: 4-clique (density 0.084): mean level 3.634 vs null 5th 4.146 (median 4.954); percentile 0.000. Shares: 0, 0.199, 0.262, 0.277, 0.231, 0.031, 0.
Reading as fixed in advance: clique is spectrally simpler than a typical graph property on the same slice; spectral level cannot certify its hardness.

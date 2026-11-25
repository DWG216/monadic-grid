# t73 P vs NP, next step: clique on one slice is an object over a reference (pre-registered 2026-11-24, before any code is written or run)

Where the record stood (§70-§73): every measure computable at m = 6 sees clique as simple. The route left open was asymptotic and non-local: "the slice needs its own tower ... a quantity that survives from one slice to the next".

The step taken here [I, from the grid]:
- A slice (graphs with exactly half the possible edges) is the fermionic sector: k-subsets, each edge at most once (§179). Berkowitz: P != NP iff clique is monotone-hard on a central slice.
- Razborov's yes and no instances (bare cliques, complete multipartite graphs) lie on different slices. Put on one slice, a yes instance is a clique (the object O) inside a background of padding edges (the reference R), and a no instance is background alone. The instance is the record |O + R|^2.
- Reading the record against the reference is the holographic reading: the cross term. With A_ij = +1 for an edge and -1 for a non-edge, the background averages out (the sign cancels it) and the clique adds a block of +1s. The top eigenvalue of A is that reading.
- The slice itself removes the cheapest reading: the edge count is fixed, so the degree-1 statistic carries nothing.
- Prediction from the grid: the cross-term reading recovers the object only above the root of the background, a clique of size about sqrt(n) (the same root that capped the local pairing in §73, Grover's root, §55). Below it the clique is hidden in the reference.

Model: n vertices, slice M = floor(n(n-1)/4) edges. No instance: M edges uniform. Yes instance: a k-clique planted, then M - C(k,2) further edges uniform among the rest. Statistic: top eigenvalue of the +-1 matrix (zero diagonal). Seed 73; 200 yes and 200 no per point; n in {100, 200, 400, 800}; k/sqrt(n) in {0.5, 1, 1.5, 2, 3, 4}. Score: AUC (probability a yes instance scores above a no instance).

S1 Sanity: the edge count is identical for yes and no (AUC of edge count = 0.5 exactly).
S2 Sanity: k = n/2 (clique on half the vertices) gives AUC 1 at n = 100.
G1 [M] Collapse: AUC depends on k/sqrt(n), not on n separately: at each k/sqrt(n), the AUC spread across the four n is below 0.1 for every point.
G2 [M] Threshold near the root: AUC < 0.6 at k/sqrt(n) = 0.5 and AUC > 0.95 at k/sqrt(n) = 4, for every n.
C1 Control: a degree statistic that ignores the sign structure (the variance of the degrees) needs a larger clique: its AUC at k/sqrt(n) = 2 is below the eigenvalue's AUC at the same point, for n = 800.

Verdict rule: G1 and G2 pass -> on one slice the cross-term reading sees the clique exactly above the root, and below the root the object is hidden in the reference; the P vs NP question on slices becomes: is there any polynomial reading that beats the root, worst case. G1 fails -> the threshold is not the root and the reading is revised.

## Scoring (2026-11-24)
Run 1 (t73_run1.log, script t73_slice_reading.py).
- S1 PASS: the edge count is identical for yes and no (AUC 0.5 exactly). S2 PASS: k = n/2 gives AUC 1.0.
- G1 PASS: AUC depends on k/sqrt(n) alone; spread across n = 100 to 800 is at most 0.068.
- G2 PASS: AUC 0.49-0.54 at k/sqrt(n) = 0.5 and 1.0 at 4, every n. The transition sits between k/sqrt(n) = 1 (AUC 0.58-0.63) and 1.5 (0.93-1.0).
- C1 FAIL as registered: at k/sqrt(n) = 2 and n = 800 both statistics reach AUC 1.0, so the eigenvalue cannot be above the degree variance there; the registered point was too high. Kept. Seen after the run, not scored: at k/sqrt(n) = 1.5 the eigenvalue reaches 1.0 at n = 400 and 800 while the degree variance stays at 0.90-0.92.
Verdict: on one slice the cross-term reading sees the clique exactly from the root, k about 1.2 sqrt(n), and below it the clique is hidden in the reference. The slice question is now sharp: does any polynomial reading beat the root in the worst case.

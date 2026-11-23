# Pre-registration (2026-11-22): square-root cancellation on a finite clock vs a random walk
Context: a deposited short proof of Deligne's bound (21 Nov 2026, AI-written, AI-checked, no human check) says its only estimate is Cauchy-Schwarz for a character sum. We check what that kind of estimate controls, on the simplest case: elliptic curves y^2 = x^3 + ax + b over F_p, a_p = -sum_x chi(x^3+ax+b).
D1 [theorem, Hasse] |a_p| <= 2 sqrt p for every nonsingular (a,b), p = 101, 211.
D2 [known, Birch] the second moment over the family: mean of a_p^2 / p lies in [0.90, 1.05] (Cauchy-Schwarz/Parseval-type average: typical size sqrt p).
D3 [real] the bound is exact, not just average: the fraction of curves with |a_p| > 2 sqrt p is 0, while for random +-1 walks of the same length (null, 200000 walks, seed 20261122) it is 0.03-0.06 (normal tail 4.6%).
D4 [identity] the tensor-power step: with alpha + beta = a_p, alpha beta = p, |alpha| = sqrt p exactly and |a_(p^k)| = |alpha^k + beta^k| <= 2 p^(k/2) for k = 1..12 (one curve).
D5 [real] shape: the a_p/(2 sqrt p) histogram follows the semicircle (Sato-Tate/Birch) better than the normal curve of the null: L1 distance to semicircle < L1 distance to the null's normal shape restricted to [-1,1].

## Results (all pass)
D1 max |a_p|/(2 sqrt p) = 0.9950 (p=101), 0.9982 (p=211). D2 mean a_p^2/p = 0.9999, 1.0000. D3 curves over the bound: 0 of 10100 and 0 of 44310; random walks: 0.0382 (mean S^2/p = 0.9985, same second moment). D4 |alpha| = sqrt p to 12 digits; max over k <= 12 of |a_(p^k)|/(2p^(k/2)) = 0.9926. D5 L1 to semicircle 0.189 vs normal 0.269.
Reading: the second moment (what Cauchy-Schwarz/Parseval sees) is identical for the clock and for chance; the difference is the hard edge at 2 sqrt p, which a random walk crosses 3.8% of the time and the clock never does. The tensor-power step turns an average into that edge.

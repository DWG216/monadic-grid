# t63 what fixes the first choice of w (pre-registered 2026-11-23, before run)
Q = [[0,1],[1,1]] acts on the pair (F(n), F(n+1)); seed (F(0), F(1)) = (0, 1) (the balanced zero, fixed by the mirror condition, §60).
U = [[1,1],[0,1]] (upper count +1), L = U^T = [[1,0],[1,1]] (lower count +1). w = the SL(2,3) character with w(U) = e^{2 pi i/3} (t62).
S1 Over Z: Q^2 = L U exactly (the golden double step is two forward counts); this unit-diagonal LU factorization is unique.
S2 Mod 3: w(U) = w, w(L) = w^2 (the two counts carry opposite phases), w(Q^2) = 1 (the golden double step is neutral).
S3 The seed (0,1) is fixed by L and L^-1 and moved by U and U^-1 (over Z and mod 3); its stabilizer in SL(2,3) is exactly <L> (order 3).
S4 Forward record Q^2 = L U: the first count to move the seed is U (phase w). Reversed record Q^-2 = U^-1 L^-1: the first count to move the seed is U^-1 (phase w^2).
S5 Fact to record: over Z, Q^-2 has no unit-diagonal LU factorization (it needs 1/2); it factors as U^-1 L^-1 (upper first in time is reversed).
Expected reading if S1-S4 hold: the forward arrow, starting at the balanced seed, makes w the first phase; the carrier then conserves it (§151). Matter is fixed by the arrow at the seed.

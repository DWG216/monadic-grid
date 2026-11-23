# Pre-registration (2026-11-21, evening): Millington pp. 122-123 (photo IMG_0570)
Sequence read: n = -8..8: -50, 31, -19, 12, -7, 5, -2, 3, 1, 4, 5, 9, 14, 23, 37, 60, 97 (U0 = 1, U1 = 4, e = 11).
Q1 [id] The p.123 component table is U(n)^2 and U(n-k)U(n+k), k = 1..5 (direct Catalan pairing, not the reflected U(x-k)U(-(x+k)) of EQN 10).
Q2 [id] The normalised r = 0 table is U(n-k)U(n+k) - U(n)^2 = -(-1)^(n-k) e F(k)^2: magnitudes 11, 11, 44, 99, 275 = 11 F(k)^2, sign alternating with n. Matches all 35 printed entries.
Q3 [id] p.122's "U(x-r)U(x+r) - U(x)^2 = U(r)^2" is false for unbalanced U (x = 0, r = 1: 11, not 16); correct right side is -(-1)^(x-r) e F(r)^2. (Fibonacci e = 1 hides the difference.)
Q4 [id] Q2 is the a = 0 case of the corrected p.125 identity (record section 51).
Q5 [real] His "inferred inflection point" (the element of least |U|) is n = 0 for U(1,4) and lies within one step of the minimum of |U(n)| for every U with 1 <= U0 < U1 <= 30 (the backward strand grows like phi^|n|).

## Results
Q0 sequence read correctly. Q1 pass (row 0 = 1, 12, -10, 45, -98, 276). Q2 pass: all 35 printed normalised entries reproduced; = -(-1)^(n-k) e F(k)^2. Q3 pass: printed "= U(r)^2" is wrong for unbalanced U; correct right side -(-1)^(x-r) e F(r)^2. Q4 pass.
Q5 FAIL: least |U| lies within one step of index 0 for only 250/435 sequences with 1 <= U0 < U1 <= 30. The "inferred inflection point" is a choice of origin (reindex so the smallest element sits at 0), not a property of U0, U1 as given.

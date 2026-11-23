# Pre-registration (2026-11-22, 05:15): does the §64 operator have a limit as zeros are added? (record §74)
Jacobi matrix J_N from the first N zeros (N = 100, 200, 341; zeros to height 600), weights w, no taper. A limiting operator in this form requires the leading entries a_1.., b_1.. to stabilise as N grows.
[M, expectation] The entries are fixed by the moments sum w gamma^k. With w = |1/(rho zeta'(rho))| the first moment sum gamma w ~ sum 1/|zeta'| grows without bound, so the entries cannot stabilise.
O1 [real] w = |1/(rho zeta'(rho))|: a_1 changes by more than 5% from N = 200 to N = 341 (no limit in this form).
O2 [control] w = e^(-gamma/30) |1/(rho zeta'(rho))| (a tempered reading vector): a_1..a_5 and b_1..b_5 agree to better than 0.1% between N = 200 and N = 341.

## Results (operator_limit.log)
O1 PASS: a_1 = 78.1, 115.8, 160.0 for N = 100, 200, 341 (38% change 200 -> 341); every leading entry keeps growing. No limit in this form.
O2 FAIL as registered: a_1 agrees to 0.00% and a_2, b_1, b_2 to within 0.2%, but a_3..a_5 and b_3..b_5 still move (up to 35%). Post hoc reading (labelled): with a tempered vector the entries settle from the top down; deeper entries need moments the temper e^(-gamma/30) has not yet cut off by height 600. A stronger temper or more zeros would be the fair control; not run.

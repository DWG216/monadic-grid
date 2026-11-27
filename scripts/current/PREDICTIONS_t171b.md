# PREDICTIONS t171b: t171's P2 rerun with a boundary-value solver

Registered 2026-11-26, committed before t171b_vortex_bvp.py is written or run.

Why: t171 P2 failed on its registered tail criterion because shooting in double precision reaches the vacuum only to r ≈ 8–9. The reading (R1, R2) and every other check are unchanged; only the method for P2 changes, and P2's criteria are kept as registered.

Method: the same radial N-vortex equations with ε = +1, τ = 1: f' = (N/r)(1 − a) f, a' = r(τ − f²)/(2N), solved as a boundary-value problem on [r₀, R] = [1e-4, 15] with scipy.integrate.solve_bvp (tolerance 1e-8, up to 100,000 nodes). Boundary conditions: a(r₀) = 0, f(r₀) = c r₀^N (enforced as r f' = N f at r₀), f(R) = 1, a(R) = 1. Initial guess: f = tanh(r)^N, a = tanh(r²/4) (no use of t171's shots).

P2 [M, as registered in t171]: for N = 1, 2, 3 the solver converges, f(15) and a(15) within 1e-3 of 1 (here imposed, so the scored content is that the solution satisfies the ODEs to the solver's tolerance with these boundary values: max residual < 1e-6); total flux 2πN a(R) within 1e-3 relative; energy within 1% of πτN; and f is monotone increasing with max f² ≤ τ + 1e-6 (P4 on the full range).
Consequence fixed now: if P2 passes, together with t171's P1, P3, P4 the Seiberg–Witten equations enter the record as the law of a spinor pair under R1–R2 (§319). If it fails, reported with the values.

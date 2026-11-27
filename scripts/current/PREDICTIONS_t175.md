# PREDICTIONS t175: the grain's binary groups as lattice gauge groups (Dobrushin thresholds)

Registered 2026-11-27, committed before t175_dobrushin_groups.py is written or run.

Context. Lockwood's Lean development (github.com/jlthermoelectric/4Y-M) proves strong-coupling Dobrushin bounds for SU(2) Wilson lattice gauge theory. The grid's binary groups 2T, 2O, 2I (clock of three, the flavour S₄'s double cover, clock of five) are finite subgroups of SU(2). Here the same strong-coupling criterion is computed for all four groups under one convention.

Convention (fixed now). Wilson action S = (β/2) Σ_p Re tr U_p; in quaternions Re tr(U V) = 2⟨u, v̄⟩, so the conditional law of one link given its staple sum x ∈ ℝ⁴ is p_x(u) ∝ exp(β⟨u, x⟩) on G (uniform reference; Haar on S³ for SU(2)). In d = 4 a link lies in 6 plaquettes, each with 3 other links: 18 influencing links. Classical (total-variation) Dobrushin coefficient: C_G(β) = sup TV(p_{w+v}, p_{w+v'}) over v, v' ∈ G and w ∈ ℝ⁴ with |w| ≤ 5 (the other five staples; the ball is a superset of the reachable sums for finite G, so the finite groups' values are upper bounds). Row sum 18 C_G(β); threshold β*_G = the β where 18 C_G(β) = 1. By left-multiplication symmetry v = 1 without loss. SU(2): TV computed exactly in the plane of the two staple vectors (the projection of uniform S³ onto a 2-plane is uniform on the unit disk); sup by multi-start optimisation.
This is the classical TV criterion, not Lockwood's W₁ "sharp quarter"; the two use different metrics and are not compared as a test.

Reasoning [I]. As β → 0, C_G(β)/β → c_G = mean over G of |u₀| (v' = −v), exactly. A finite subset of S³ that is a spherical t-design reproduces S³'s averages of polynomials up to degree t, so the larger t, the closer every such average, and the strong-coupling physics, to SU(2)'s.

P1 [M]: the design strengths t of 2T, 2O, 2I are computed (largest t with every harmonic of degree 1..t averaging to zero, checked to 1e-12); c_G computed in closed form; numerically C_G(1e-3)/1e-3 matches c_G to 1e-3 relative for all four groups.
P2 [M, the test]: the deviations |β*_G/β*_SU(2) − 1| strictly decrease with design strength (2T, 2O, 2I in increasing t), and 2I lies within 2% of SU(2).
P3 [M]: the same strict ordering holds for |c_G/c_SU(2) − 1|, with c_SU(2) = 4/(3π).
Consequence fixed now: if P2 passes, the record holds that at strong coupling the grain's clock-of-five group gives SU(2)'s Dobrushin region to within 2%: the record cannot tell 2I's gauge field from SU(2)'s there. If it fails, reported with the values.
Gate: mathematics; public.

## Scoring (2026-11-27), run 1 (t175_run1.log)
- Design strengths computed: 2T 5, 2O 7, 2I 11.
- P1 FAIL on threshold: C_G(1e-3)/1e-3 matches c_G to 7.5e-4 (2T), 1.2e-3 (2O), 7.6e-4 (2I), 6e-6 (SU(2)); 2O misses the registered 1e-3 (the O(β) correction and the optimiser's tolerance at β = 1e-3).
- P2 FAIL: thresholds β* = 0.1295 (2T), 0.1329 (2O), 0.1322 (2I), 0.1310 (SU(2)). Deviations from SU(2): 1.2%, 1.5%, 0.87%. 2I is within 2%, but the ordering by design strength fails (2O deviates most).
- P3 FAIL: slopes c_G = mean |u₀| = 0.4167 (2T), 0.3851 (2O), 0.4069 (2I) against 4/(3π) = 0.4244; deviations 1.8%, 9.3%, 4.1%: not ordered by design strength.
Diagnosis: the reasoning was wrong. |u₀| is not a polynomial, so a t-design need not reproduce its average better as t grows; how close each group comes depends on where its points sit relative to the equator u₀ = 0, not on t. The thresholds are close for all three groups (within 1.5% of SU(2)) because the sup over staples is dominated by configurations far from the small-β regime.
Verdict as fixed in advance: fail; the ordering claim is withdrawn. Reported: all three binary groups give SU(2)'s classical Dobrushin threshold to within 1.5%, the clock-of-five group closest (0.87%).

# PREDICTIONS t166: the 1/4 from a count of cells

Registered 2026-11-26, committed before t166_horizon_count.py is written or run.

Inputs, both fixed before this test and without reference to horizons:
- Density of the grain: one cell per Planck 4-volume, ρ = 1/l_P⁴ with l_P² = ħG/c³ (the convention of the Λ count, t72, t87, t123).
- States per straddling pair: 16 (t152: each horizon cell's balancing partner lies across the horizon in the 16̄, so a pair carries the 16 states of its inside cell; entropy ln 16 per pair).
Counting rule (prior work: Dou and Sorkin 2003; Barton, Counsell, Dowker, Gould, Jubb and Taylor, PRD 100, 126008 (2019)): a horizon molecule with respect to a spacelike hypersurface Σ is a pair p₋ ≺ p₊ in the past of Σ, p₋ on the past side of the horizon H, p₊ on its future side, with p₊ the only element in the past of Σ that lies to the future of p₋ (so the pair is a link). The expected number is a⁽⁴⁾ ρ^(1/2) × area in the continuum limit; a⁽⁴⁾ is computed here, not taken from the paper.
Geometry: flat Rindler horizon H = {t = x} in Minkowski space, Σ = {t = 0}. With ρ = 1, a⁽⁴⁾ = ∫dh ∫dx₀ V_B(h, x₀) exp(−πh⁴/3), where p₋ = (−h, x₀), the truncated future cone of p₋ below Σ has volume πh⁴/3, and V_B is the part of it on the future side of H.
Grid entropy: S = a⁽⁴⁾ ln 16 × A/l_P².
S1 [M]: the integral converges (tightening tolerances changes a⁽⁴⁾ by less than 1e-6 relative).
S2 [M]: a Monte Carlo sprinkling at ρ = 1 (transverse box with margins, 40 runs) counts molecules per unit area equal to a⁽⁴⁾ within 3 standard errors.
P1 [M, the derivation test]: a⁽⁴⁾ ln 16 = 1/4 within 10%. Pass → the 1/4 is derived from the grain's density and the pair's 16 states; fail → reported with the value, and the coefficient the count gives in place of 1/4.
Reported, not scored: a⁽⁴⁾ ln 2 (one bit per molecule, Dou–Sorkin's picture), for comparison.

## Scoring (2026-11-26), run 1 (t166_run1.log)
- S1 PASS: a⁽⁴⁾ = 0.1732050807, stable to 7e-10. Noticed after the run: this is √3/10 to 1e-11.
- S2 PASS: a Monte Carlo sprinkling counts 0.180 ± 0.016 molecules per unit area (0.4 standard errors from the integral).
- P1 FAIL: a⁽⁴⁾ ln 16 = 0.480, 1.92 times the 1/4. With the grain at one cell per Planck 4-volume and 16 states per straddling pair, the count gives S = 0.48 A/l_P², not A/4l_P².
Reported: one bit per molecule gives 0.120 (half of 1/4). The 1/4 would need e^(1/4a⁽⁴⁾) = 4.23 states per molecule at this density, or, with 16 states, a cell 4-volume 1.92² = 3.69 l_P⁴.
Post hoc (noted, not read): 4 states per molecule give 0.240, 4% below 1/4.
Verdict as fixed in advance: the 1/4 is not derived. The count with the grid's two inputs overshoots by 1.92. Open: either a horizon molecule does not carry the whole pair's 16 states, or the grain's density is not one cell per l_P⁴.

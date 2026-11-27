# PREDICTIONS t180: a slice-free meeting count (the record supplies its own "now")

Registered 2026-11-27, committed before t180_record_now.py is written or run.

Reasoning [S]. The horizon-molecule count (Barton et al.) is defined against a spacelike hypersurface Σ. Nothing in the grid chooses one; but the record has its own time: the count of events in an event's past (§276), which strictly increases along every causal chain. So the set D = {events whose past-count is below N₀} is past-closed (if q precedes p, q's past is a proper subset of p's), defined by order and count alone. Taking D as "the past of now" makes the meeting count slice-free: a meeting across the horizon is a link p₋ ≺ p₊ with both in D, p₋ outside and p₊ inside the horizon, and p₊ the only element of D in p₋'s future. Claim: this record-defined count reproduces the continuum density √3/10 per unit area of the horizon's cross-section.

Setting. Sprinkling at ρ = 1 in the future of an origin event O (a Milne universe: the past-count of p is the count in the causal interval between O and p, mean πτ⁴/24 with τ its proper time from O). Horizon: the null plane t − x = 6. N₀ = 170 (the mean count at τ = 6, π6⁴/24 = 169.6); D's boundary approximates the hyperboloid τ = 6, which meets the horizon in the surface t + x = (36 + y² + z²)/6, whose area element is dy dz. Box t ∈ [0, 8], x, y, z ∈ [−6, 6], points kept inside the future of O; molecules counted with p₊ in the window |y|, |z| < 2 (area 16). 150 sprinklings, seed 1800.

S1 [sanity]: the mean past-count of events at proper time 6 ± 0.1 lies within 5% of 169.6.
P1 [M, the test]: molecules per unit area = √3/10 = 0.1732 within 3 standard errors (over sprinklings).
Consequence fixed now: if P1 passes, the meeting count needs no chosen slice: the record's own past-count supplies the cross-section, and the density is the continuum one. If it fails, reported with the value.
Gate: physics; public.

## Scoring (2026-11-27), run 1 (t180_run1.log)
- S1 PASS: mean past-count at τ = 6 ± 0.1 is 170.4 against 169.6.
- P1 FAIL: 0.097 ± 0.007 molecules per unit area against √3/10 = 0.173 (z = −11.7).
Post hoc diagnostics (not scored, run after the result was seen):
- t180_control.py (seed 1801, 60 runs): the same count with D defined by the continuum hyperboloid τ < 6 instead of the record's past-count: 0.091 ± 0.010. The record's own "now" and the geometric hyperboloid give the same count within errors.
- t180_flatcheck.py (seed 1802, 40 runs): the same code with a flat slice t < 6 (t166's geometry): 0.156 ± 0.015, consistent with √3/10. The code is right.
Diagnosis: the shortfall comes from the slice's curvature, not from the record: at τ₀ = 6 the hyperboloid's curvature radius is six cells, and the leading-order density of Barton et al. holds only when the slice is flat on the scale of a molecule. The registration chose a geometry too small to test the continuum density. What the run does show: defining "now" by the record's past-count reproduces the geometric slice's count (0.097 against 0.091). A test of the density itself needs τ₀ much larger than the molecule scale (cost grows as τ₀⁴); not run.
Verdict as fixed in advance: fail.

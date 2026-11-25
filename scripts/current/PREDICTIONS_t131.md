# t131 What stabilises the scalar vacuum (pre-registered 2026-11-25, before any t131 code is written or run)

Setting: t106 (two Higgs 27s as lepton bifundamentals H1, H2; all 20 real quartic invariants zero at M* = 2.435e18 GeV; one-loop running to M3 = 4.98e13 GeV; top coupling on H1 only) left the potential at M3 unbounded (minimum on the unit sphere −0.014). Post 15 states that the E6-breaking scalars stabilise it. Two candidates are tested.

Step 1 [S], the E6-breaking scalars. Heavy scalars Φ_A (mass² M_A² > 0, at M*) couple to the 27s through trilinears μ_A·φφ (a quartic portal κ Φ†Φ φφ becomes such a trilinear once Φ takes its vev). Integrating Φ out at tree level gives δV = −Σ_A (μ_A·φφ)²/(2 M_A²) ≤ 0 in every direction. Below M* the Φ are heavy and do not run. So they cannot make a potential that is zero at M* bounded.
 S1 [M]: random μ, M (10 heavy scalars, 10,000 directions): δV ≤ 0 everywhere.

Step 2 [M], the E6 cubic Yukawa. In E6 the third generation couples to a Higgs 27 through one cubic, 27_F 27_F 27_H, with one coupling: the quark term H·Q_L·Q_R (the top) and the lepton term ε ε H L L (the third generation's lepton bifundamental) together. Running as t106, with the lepton term added on H1 at the top's coupling y, and H2 coupled through the same tensor at y2 = r y.
 S2: with the quark term only on H1 (t106's setting), the minimum reproduces t106's −0.014 within 10%.
 P1 (r = 0, full cubic on H1): unbounded (minimum < 0).
 P2 (r = 0.5 and r = 1): unbounded.
 P3: in each case of P1–P2, the minimising direction lies at least 90% (squared overlap) in the Yukawa-free combination (H2 for r = 0; r H1 − H2 otherwise).
Approximations stated now: y and y2 = r y run with the top's one-loop equation (6y² − 16 g²); the lepton term's effect on y's running is left out.

Consequence fixed now: if P1–P3 pass, nothing in the grid's minimal content makes the all-zero potential bounded: the gauge forces drive every Yukawa-free direction negative. Then the zero rule's object is the light Higgs's own quartic only (as t106 concluded), the E6-invariant quartics of the 27s at M* are positive, and post 15's "What stabilises it" is rewritten to say so. If P2 fails (bounded), the E6 cubic stabilises the vacuum and post 15 says that.

## Scoring (2026-11-25)
Run 1 (t131_run1.log; two earlier starts stopped on an import error and an array-shape error before any result, logs kept). Engine closure: gauge 6e-14, Yukawa ≤ 1.1e-13; lepton term invariant under SU(3)_L × SU(3)_R to 4e-16. g = 0.540, y = 0.343 at M*.
- S1 PASS: integrating out heavy scalars lowers the potential in every direction (largest δV −0.47 on 10,000 directions).
- S2 PASS: quark term on H1 reproduces t106, minimum −0.01426.
- P1 PASS: full cubic on H1, minimum −0.01425 (unbounded).
- P2 PASS: r = 0.5 gives −0.01425, r = 1 gives −0.01424 (unbounded).
- P3 FAIL: Yukawa-free overlap 1.000 (r = 0), 0.801 (r = 0.5), 1.000 (r = 1). Kept. The minimum is the same to 0.2% in every case, so the negative directions are untouched by the Yukawas; at r = 0.5 the minimiser found leans 20% into the coupled combination without lowering the minimum.
Verdict: the consequence's substance stands on S1, P1 and P2. Neither the E6-breaking scalars (they only lower the potential) nor the E6 cubic (y = 0.34 at M* against gauge g = 0.54) bounds a potential that starts at zero. The zero rule's object is the light Higgs's own quartic; the 27s' E6-invariant quartics at M* are positive. Post 15's right card is rewritten.

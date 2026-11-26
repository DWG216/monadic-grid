# PREDICTIONS t168: one cell size for the horizon and for Λ

Registered 2026-11-26, committed before t168_cell.py is written or run.

Background. t166: horizon molecules on a grain of one cell per Planck 4-volume, 16 states per straddling pair, give S = 0.480 A/l_P², 1.92 × the 1/4. Equivalently, the 1/4 with 16 states requires a cell 4-volume v_c = (4 a⁽⁴⁾ ln 16)² l_P⁴ = (0.4√3 ln 16)² l_P⁴ = 3.690 l_P⁴ (l_P² = ħG/c³; 4-volume in l_P³ t_P). Noticed before registering (not blind): t87's rough count with Planck cells, N = (1/H₀t_P)⁴, gave Λl_P² = 1.40e-122 against 2.9e-122 observed, low by about 2, and a larger cell raises the count's Λ by √(v_c/l_P⁴) = 1.92. t87 used a crude 4-volume, so this is not yet a test.
The test. The grid's count is fixed: time is the count in the causal past (§276), so N is the number of cells in the causal past of here and now. Compute that 4-volume in flat ΛCDM (Planck 2018: H₀ = 67.4 km/s/Mpc, Ω_m = 0.315, Ω_Λ = 0.685, radiation 9.1e-5 of critical): V₄ = ∫₀^{t₀} dt a(t)³ (4π/3) χ(t)³, χ the comoving distance from emission at t to us.
P1 [M]: with v_c = 3.690 l_P⁴, Λl_P² = √(v_c/V₄) equals the observed 3Ω_ΛH₀²l_P²/c² within 15%.
Reported: the same with v_c = l_P⁴ (Planck cell), and with the cell that would match exactly.
Consequence fixed in advance: P1 passes → one cell size, 3.69 Planck 4-volumes with 16 states per horizon pair, gives both the 1/4 and Λ, and the 1/4 is derived jointly with Λ. P1 fails → the cell from the horizon count and the cell from Λ disagree, reported by how much.

## Scoring (2026-11-26), run 1 (t168_run1.log)
- The causal past of here and now holds V₄ = 6.40e242 Planck 4-volumes (age 13.79 Gyr), eight times fewer than t87's crude (1/H₀t_P)⁴ = 5.2e243.
- P1 FAIL: with v_c = 3.690 l_P⁴ the count gives Λl_P² = 7.59e-122, 2.66 × the observed 2.85e-122.
- Reported: with Planck cells, 3.95e-122 (1.39 ×); the cell that matches Λ exactly is 0.520 l_P⁴. The horizon's 1/4 with 16 states needs 3.69 l_P⁴: the two cells disagree by 7.1.
Post hoc (after the run, not a test): requiring both the 1/4 and Λ from one cell fixes the states per horizon pair at d = 2.83. The integer nearest is 3, the grain's clock of three: d = 3 gives v_c = 0.579 l_P⁴ and Λ within 5.6% (d = 2: 0.67 ×; d = 4: 1.30 ×). Noted, not read; a registered test of "3 states per straddling pair" needs a consequence not yet looked at.
Verdict as fixed in advance: the 1/4 is not derived jointly with Λ at 16 states per pair; the cells disagree by a factor 7.1.

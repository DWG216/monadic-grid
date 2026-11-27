# PREDICTIONS t177: the glueball ratio m(0⁺⁺)/√σ on the grain's gauge group

Registered 2026-11-27, committed before t177_glueball.py is written or run.

Question. The pure number m(0⁺⁺)/√σ (lightest glueball mass over the square root of the string tension) is what the grid owes for Yang–Mills (§179). The grid cannot yet derive it analytically. What it does claim (t175, §321): the grain's clock-of-five group 2I ⊂ SU(2) is, to the record, indistinguishable from SU(2) as a gauge group. Test: compute the ratio on the lattice with gauge group 2I and with SU(2), same lattice, same coupling, same estimators.

Setup (fixed now). Wilson action (β/2) Σ Re tr U_p, β = 2.4, lattice 8⁴ periodic. Links as unit quaternions. SU(2): checkerboard heat bath (Kennedy–Pendleton); 2I: exact heat bath over the 120 elements (Gumbel-max sampling). Cold start; 300 thermalisation sweeps; 4,000 measurement sweeps per group; seeds 1771 (SU(2)), 1772 (2I).
Estimators. Plaquette ⟨½ Re tr U_p⟩. String tension from the Creutz ratio χ(3,3) = −ln[W(3,3) W(2,2) / (W(3,2) W(2,3))], Wilson loops averaged over all positions and planes, measured every 5 sweeps. Glueball: spatial links APE-smeared (4 steps, weight 0.5, renormalised to unit quaternions), O(t) = Σ over spatial positions and the 3 spatial planes of ½ Re tr of the smeared plaquette, connected correlator C(t) averaged over time origins, every 2 sweeps; m = ln[C(1)/C(2)]. Errors by jackknife over 20 bins.

S1 [sanity]: SU(2) plaquette within 0.5% of the literature value 0.630 at β = 2.4.
S2 [sanity]: SU(2) ratio m/√χ(3,3) within 25% of the continuum value 3.78 (Lucini, Teper, Wenger), allowing for the small lattice and the crude estimators.
P1 [M]: 2I plaquette equals SU(2)'s within 0.5%.
P2 [M, the test]: 2I's ratio equals SU(2)'s within two combined standard errors and within 10%.
Consequence fixed now: if P1–P2 pass, the record holds that the grain's gauge group gives SU(2)'s glueball ratio: the number the grid owes is the same on the grain as in SU(2). Deriving its value from the ground stays open.
Gate: physics; public.

## Scoring (2026-11-27), run 1 (t177_run1_SU2.log, t177_run1_2I.log, t177_analysis_run1.log)
- S1 PASS: SU(2) plaquette 0.63021(17) against 0.630.
- S2 FAIL: SU(2) m/√χ(3,3) = 2.24(34) against 3.78. The glueball mass is reasonable (m a = 0.85(13); literature about 0.94), but the Creutz ratio χ(3,3) = 0.142(3) is about twice σa² at β = 2.4 (literature a√σ ≈ 0.26, σa² ≈ 0.07): at R = T = 3 the Coulomb term still contributes roughly as much as the string tension. The registered estimator was too crude; kept as a fail.
- P1 PASS: 2I plaquette 0.63033(23), equal to SU(2)'s to 0.02%.
- P2 PASS, weakly: 2I ratio 2.25(29) against SU(2)'s 2.24(34): equal to 0.4%, but the statistical errors are about 15%, so this run resolves differences only above about 30%. The Creutz ratios agree to 2.4% (0.146(3) against 0.142(3)) and the glueball masses to 1.6%.
Reported, not scored: with the literature σ for SU(2) at β = 2.4 in place of χ(3,3), the measured mass gives about 3.2.
Verdict as fixed in advance: P1–P2 pass, so the record holds that on this lattice the grain's gauge group gives SU(2)'s glueball ratio, at the precision reached (about 15%). The ratio's value is not established by this run (S2), and deriving it from the ground stays open. A sharper run needs larger loops (or a fit with the Coulomb term) and more statistics.

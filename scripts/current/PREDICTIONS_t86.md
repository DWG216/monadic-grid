# t86 Everpresent Lambda against DESI DR2 distances directly: roadmap item (4) (pre-registered 2026-11-25, before any t86 code is written or run)

Bridge under test [I], as t72: Lambda = alpha W(V)/V, the record count's leftover fluctuating as V^(-1/2). t72 tested it through the CPL fit and found DESI's direction typical (61% in its quadrant), but 77% of accepted histories have rho_Lambda < 0 somewhere at z < 2, where CPL cannot follow. Here the histories meet the BAO distances themselves.

Histories: t72's run at its primary alpha = 1, regenerated exactly (seed 72, 20,000 realizations, Omega_m = 0.31, same steps); accepted = alive to a = 1 with Omega_Lambda0 in [0.65, 0.73] (347 expected, a reproduction check).
Data: DESI DR2 BAO, 13 numbers: D_V/r_d at z = 0.295 (7.942 +- 0.075); D_M/r_d and D_H/r_d at 0.510 (13.588 +- 0.167, 21.863 +- 0.425), 0.706 (17.351 +- 0.177, 19.455 +- 0.330), 0.934 (21.576 +- 0.152, 17.641 +- 0.193), 1.321 (27.601 +- 0.318, 14.176 +- 0.221), 1.484 (30.512 +- 0.760, 12.817 +- 0.516), 2.330 (38.988 +- 0.531, 8.632 +- 0.101). Errors diagonal (the published D_M-D_H correlations, about -0.4 to -0.5, are not used; the same likelihood is used for every model, so comparisons are like with like).
Model: E(z) = H(z)/H(a = 1) from each history; D_M/r_d = s * integral dz/E, D_H/r_d = s / E, D_V = (z D_M^2 D_H)^(1/3); s = c/(H0 r_d) fitted analytically (one free number for every model).
Reference: flat Lambda-CDM with the same likelihood, chi2_ref = minimum over Omega_m in [0.20, 0.40] (step 0.0005); also chi2 at Omega_m = 0.31.

S1 Sanity: a constant-Lambda history run through the same code (Omega_Lambda0 = 0.69) gives the Lambda-CDM chi2 at Omega_m = 0.31 to within 0.01.
S2 Sanity: the Lambda-CDM best Omega_m lies in [0.28, 0.32] (DESI DR2 BAO alone: about 0.297).
S3 Reproduction: the regenerated run accepts 347 histories (t72).
P1 [I] At least 5% of accepted histories have chi2 <= chi2_ref + 4. Below 1%: the distances disfavour the bridge (correction map).
P2 [I] At least one accepted history has chi2 < chi2 of Lambda-CDM at the same Omega_m = 0.31.
P3 [I] Among accepted histories with rho_Lambda < 0 somewhere at z < 2, at least 5% meet P1's criterion: negative excursions are not excluded by the distances as such.
Information: P1's passers' CPL quadrant where fittable; the best chi2 against chi2_ref.

Verdict: P1-P3 pass -> the everpresent band meets DESI's distances directly, sign excursions included. P1 below 1% -> the bridge fails at alpha = 1.

## Scoring (2026-11-25)
Run 1 (t86_run1.log). S1 PASS (constant Lambda matches Lambda-CDM to 2e-13). S2 PASS (best Omega_m = 0.2995, chi2_ref = 11.44 for 13 numbers, one free scale). S3 PASS (347 accepted, as t72).
- P1 FAIL, below the refutation line: 0 of 347 accepted histories come within chi2_ref + 4. Best chi2 29.5 (Delta chi2 = 18 over Lambda-CDM); median 467; 16-84% range 192-988.
- P2 FAIL: no history beats Lambda-CDM at Omega_m = 0.31 (12.69).
- P3 FAIL: 0 of 268 histories with a negative excursion pass.
Verdict as registered: the bridge Lambda = alpha W(V)/V with alpha = 1 (t72's model) fails DESI DR2's distances. The CPL direction t72 found typical does not carry over to the distances: the histories that survive to Omega_Lambda0 near 0.7 fluctuate far too much at z < 2.3. Correction-map entry: the everpresent-Lambda bridge as written in t72 is refuted; the record count and the N^(-1/2) scaling are not on trial here, only this implementation (a Wiener process in the four-volume of the Hubble sphere, alpha = 1, start at a = 1e-3).

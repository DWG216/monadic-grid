# t72 Everpresent Lambda against DESI DR2 (pre-registered 2026-11-24, before any code is written or run)

Bridge under test [I] (spec: "Dark energy: Sorkin count, everpresent Lambda"): Lambda is the leftover of the record count, fluctuating as N^(-1/2) with N the past four-volume (Sorkin; Ahmed, Dodelson, Greene and Sorkin 2004). The record and the count are not on trial; only this bridge is.

Model (units H0 = 1, Planck factors absorbed into alpha):
- Lambda = alpha * W(V) / V, with W a Wiener process in V (variance V): dW = sqrt(dV) * N(0, 1).
- dV / dln a = (4 pi / 3) H^-4 (four-volume of the Hubble sphere).
- H^2 = Om a^-3 + Lambda / 3, with Om = 0.31; radiation ignored.
- Start at a = 1e-3, matter dominated: V_i = (4 pi / 3) Om^-2 a_i^6 / 6, W(V_i) ~ N(0, V_i).
- Steps of 2e-4 in ln a; 20000 realizations per alpha; seed 72.
- A realization ends if H^2 <= 0 before a = 1 (recollapse).
- Accepted: it reaches a = 1 with Omega_Lambda0 = (Lambda0 / 3) / H0^2 in [0.65, 0.73].
- alpha grid {0.5, 1, 2, 4, 8}. The primary alpha is the one with the highest acceptance rate. This rule is fixed now and does not look at w.

Fit: for accepted realizations with rho_Lambda > 0 for all z < 2 (a in [1/3, 1]), least-squares fit of ln rho_Lambda(a) to the CPL form ln rho0 - 3(1 + w0 + wa) ln a - 3 wa (1 - a).

DESI DR2 BAO + CMB: w0 = -0.42 +- 0.21, wa = -1.75 +- 0.58 (3.1 sigma from Lambda-CDM, quadrant w0 > -1, wa < 0). The correlation is not used: "inside" means within 2 sigma on each axis (a box). With supernovae the best fit is near (-0.7, -1); this is reported as information only.

S1 Sanity: W replaced by c V (constant Lambda) gives w0 = -1 and wa = 0 to within 1e-6.
S2 Sanity: a synthetic CPL rho with (w0, wa) = (-0.42, -1.75) is recovered by the fit to 1e-6.

At the primary alpha:
P1 [I] The DESI box holds at least 5% of the fitted realizations (the band is compatible with DESI). Below 1% means DESI disfavours the bridge and the result goes in the correction map.
P2 [I] Everpresent Lambda evolves visibly: the median |w0 + 1| > 0.1.
P3 [I] The DESI quadrant (w0 > -1, wa < 0) holds at least 25% of fitted realizations, at least its fair share of four quadrants.
Information: the fraction of accepted realizations with rho_Lambda < 0 somewhere at z < 2 (these cannot be fitted by CPL). The same numbers at every alpha. The fraction within 2 sigma of (-0.7, -1) using the DR2+CMB widths.

Verdict rule: P1 to P3 pass -> the bridge survives DESI DR2 as a band, not a point. P1 below 1% -> the bridge fails.

## Scoring (2026-11-24)
Run 1 (t72_run1.log, script t72_everpresent.py). S1 and S2 pass (constant Lambda gives (-1, 0); a synthetic CPL is recovered).
- Acceptance by alpha: 0.5 gives 0%; 1 gives 1.7% (347 of 20000); 2 gives 0.1%; 4 and 8 give 0%. The primary alpha is 1.
- At alpha = 1, 77% of accepted realizations have rho_Lambda < 0 somewhere at z < 2, which CPL cannot fit. That leaves 79 fitted.
- P1 PASS (marginal): 6.3% of the 79 (5 of 79, binomial error about 2.7%) lie in the DESI DR2 + CMB 2-sigma box.
- P2 PASS: the median |w0 + 1| is 0.90. Everpresent Lambda evolves strongly.
- P3 PASS: 61% of the fitted realizations lie in the DESI quadrant (w0 > -1, wa < 0).
- Information: medians w0 = -0.12, wa = -0.38. 16-84% ranges: w0 from -1.02 to 0.60, wa from -2.76 to 1.76. 8.9% lie within the same widths of the supernova point (-0.7, -1).
Verdict: the bridge survives DESI DR2 as a band, not a point. DESI's direction is the typical direction (61% in its quadrant). But the band is far wider than DESI's error ellipse, and most realizations dip below zero density before z = 2. A smoothness test is needed: Lambda's sign history against BAO + supernova distances directly, not through CPL. That test (t73) is not yet pre-registered. Small sample: 79 fitted realizations.

# PREDICTIONS t155: the photon on the horizon, bulk plus edge

Registered 2026-11-26, before t155_photon_horizon.py was written or run.

Target. Sen's per-vector coefficient on a Ricci-flat horizon is C = −26/90 (4(c − a), c = 1/10, a = 31/180). Split of the heat kernel on Ricci-flat backgrounds [M, standard]: a₂(A_μ) − 2a₂(ghost) = (4 − 15 − 2)/180 Riem², i.e. two physical polarisations worth 2 × (1/180) and a curvature-coupling piece −15/180. In C units: +4/90 (two polarisations) − 30/90 (the piece that becomes Kabat's contact term on the cone, identified with edge modes by Donnelly and Wall 2015).

Grid reading [S + I]. The bulk photon is the two transverse hands of the field in the record outside the horizon. The edge modes are the balanced pairs straddling the horizon: the normal electric flux through each horizon cell is a charge on one side balanced by its partner on the other (Gauss's law as pairwise balance), and the total flux is zero (balance removes the zero mode).
Edge, derived [M]: the edge partition is Gaussian in the flux pattern on the horizon 2-sphere, so its log term is fixed by the zeta function of the sphere's Laplacian with the zero mode removed: ζ(0) = χ/6 − 1 = −2/3, and the edge entropy's log coefficient is ζ(0)/2 = −1/3 = −30/90 in ln r_s. It depends only on the horizon's topology (χ = 2), so the flat sphere and the black hole get the same edge term (flat-sphere check: Casini–Huerta bulk −16/45 plus −1/3 gives the anomaly −31/45).

Engine (bulk). As t154, with the Regge–Wheeler potential for spin 1, W = l(l + 1)/r² (no r_s/r³ term), l ≥ 1, two parities.
S1 [M]: ζ_{S²}(0) with the zero mode removed = −2/3, checked by summing Σ'(2l + 1)(l(l + 1))^(−s) analytically continued (Hurwitz form) to s = 0, within 1e-10.
P1 [M]: bulk photon c_log = +4/90 = +0.0444 within 15% (wall at 4r_s, L = 8…40).
P2 [M]: total, bulk + edge (−1/3): c_log = −26/90 = −0.2889 within 15%.
Consequence fixed in advance: P1 and P2 pass → the photon's log term on the horizon is computed from the grid's own pieces (transverse hands plus straddling balanced pairs), and S = A/4 − 0.644 ln A for astrophysical black holes rests on the grid's lattice and the edge derivation, not on a citation.

## Scoring (2026-11-26), run 1 (t155_run1.log)
- Code note: mpmath is not installed here; ζ_{S²}(0) is continued with scipy's Hurwitz zeta, the k = 0 term by Bernoulli (−B₂(a)/2) and the k = 1 pole by 1/δ − ψ(a). Changed before any result printed.
- S1 PASS: ζ_{S²}(0) = −0.66666666666664 (−2/3). Edge term −1/3.
- P1 FAIL: bulk photon (two Regge–Wheeler parities, l ≥ 1) c_log = +0.02876 against the registered +4/90 = +0.04444 (35% low).
- P2 PASS: bulk + edge = −0.30457 against −26/90 = −0.28889 (5.4%). The pass leans on the edge term, which is ten times the bulk; with the bulk 35% low, the total lands 5.4% too negative.
Post hoc (t155_posthoc.py, log t155_posthoc.log, after scoring): the registered split "two polarisations = two scalars" fails mode by mode. In units of 1/90: scalar (t154) +1.95; one Regge–Wheeler parity +1.29; scalar without l = 0 −4.97; scalar without the r_s/r³ term +10.73; the l = 0 wave alone +6.92. Individual partial waves and the curvature term carry large log pieces that cancel only in the full sums, so the heat-kernel split (4/180 − 15/180 − 2/180) does not map onto "transverse modes" and "edge" one for one. The photon's total is within 5.4% of Sen's; the bulk/edge split stays open (shortfall 1.4/90, close to 4/3 of 1/90, noted, not read).
Verdict: the photon's horizon coefficient is reproduced to 5.4% from the grid's pieces, but the registered bulk value failed; the edge term's exact form on a horizon with the record's Dirichlet seal is the open item.

# t109 Quark masses: b–τ from the single 27³ coupling (pre-registered 2026-11-25, before code)
[S] At gravity's meeting E6 has one cubic invariant 27·27·27. If the light down-type doublet sits in the same column for quarks (Q_L Q_R L) and leptons (L L L), then y_b = y_τ (and y_s = y_μ, y_d = y_e) at M*.
Engine: one-loop running of R = y_b/y_τ, d ln R/dt = (1/16π²)[3/2(y_b² − y_t² − y_τ²) + (10/3)g'² − 8g₃²], with the t101 couplings; above M3, g' = sqrt(3/5) g and g₃ = g (approximation: the trinification anomalous dimensions are taken from the unified SM form). Inputs at m_t: m_b = 2.75 GeV, m_τ = 1.75 GeV.
P1 [M] 0.9 < R(M*) < 1.1 for meeting B (n_h = 2, the t106 content). Expected by the writer: fail (non-SUSY running gives about 0.6–0.7), which would put the difference in the doublet's direction (mixing with the exotic D and the third doublet column).
Information: R(M*) for meeting A; s/μ and d/e ratios at M* (Georgi–Jarlskog-like factors 1/3 and 3 would show).

## Scoring (2026-11-25), run 1 (t109_run1.log)
- P1 FAIL: R(M*) = 0.597 (meeting B), 0.598 (A), 0.606 (SM only). As the writer expected; kept.
- Information: y_s/y_μ = 0.20 and y_d/y_e = 2.1 at M* (meeting B).
Verdict: the single 27³ coupling with quark and lepton masses from the same doublet column fails by 40%; the light doublet's direction (its mixing with the exotic D and the third column) must carry the difference. This is the same object as the hierarchy item.

## Post hoc correction (2026-11-25, found during t112; t109_posthoc.py)
Above M3 the gauge parts of the two couplings are equal in trinification, so t109's running above the meeting was wrong in its gauge term. Corrected: R(M3) = 0.69, R(M*) = 0.68 (meetings A and B). P1 still fails.

# t99 Quark masses as chords, and quark mixing at leading order (pre-registered 2026-11-25, before any t99 code is written or run)

[S, proposed in section 156] masses as a balanced chord, Q = 2/3, for every Dirac sector. [I] (t96) both quark sectors keep the same Z3, so CKM = identity at leading order.
Data: MS-bar masses at M_Z (Bethke-type table, arXiv 0905.1425): m_u 1.54(50) MeV, m_c 599(50) MeV, m_t 169.6(2.3) GeV; m_d 3.1(5) MeV, m_s 57(12) MeV, m_b 2.87(6) GeV. Q = (sum m)/(sum sqrt m)^2 is nearly scale-independent (mass ratios run slowly). CKM: |V_us| = 0.2250, |V_cb| = 0.0418, |V_ub| = 0.00369 (PDG 2024). PMNS moduli from NuFIT 6.0 central values.

P1 [M on data] Up quarks: |Q_u - 2/3| < 0.02 (with errors propagated by sampling). Expected by the writer: fail (Q_u near 0.85), which would restrict Q = 2/3 to leptons.
P2 [M on data] Down quarks: |Q_d - 2/3| < 0.02. Expected: fail (near 0.73).
P3 [M on data] Leading-order CKM = identity: the sum of squared off-diagonal CKM moduli is below 20% of the same sum for the PMNS matrix.
Information: Q for mixed triplets (s, c, b) and (c, b, t), long noted to sit near 2/3; no grid reason is claimed for them.
Verdict: P1, P2 decide whether the chord's balance (Q = 2/3) is general or lepton-only; P3 checks the small-quark-mixing reading.

## Scoring (2026-11-25)
Run 1 (t99_run1.log).
- P1 FAIL: Q_u = 0.889 +- 0.004. P2 FAIL: Q_d = 0.743 +- 0.017. As the writer expected; kept. The chord's balance Q = 2/3 holds for the charged leptons only.
- P3 PASS: off-diagonal CKM weight is 7% of the PMNS's (0.105 vs 1.53): quark mixing small, lepton mixing large, as the shared-Z3 reading says.
- Information: Q(s, c, b) = 0.48, Q(c, b, t) = 0.72 at M_Z (the mixed triplets are not near 2/3 with these masses).
Verdict: Q = 2/3 is not general: the [S] proposal of section 156 is restricted to the charged leptons (colourless Dirac sector). Quarks are chords with their own amplitudes (c_u = 1.83, c_d = 1.56 against sqrt2) and small phases; a reason for their amplitudes is open.

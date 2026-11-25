# t98 Koide's phase from the grain (pre-registered 2026-11-25, before any t98 code is written or run)

Chord form (section 125): sqrt(m_k) = A (1 + sqrt2 cos(delta + 2 pi k / 3)), k = 0, 1, 2: the three generations as one sinusoid sampled at the counting phase's three points. Q = 2/3 is the amplitude sqrt2 [S, proposed]. The phase delta has been observed (Brannen 2006) near 0.2222 for the charged leptons.
Bridge under test [I]: delta = 2/9 rad: the pair (2, the two hands) over the grain (9 points). Stated plainly: this is a reading, not a derivation; the test is how precisely the data sit on it, and what it predicts.
Data: m_e = 0.51099895000 MeV, m_mu = 105.6583755(23) MeV, m_tau = 1776.86 +- 0.12 MeV (PDG 2024).
Convention: delta is reported in [0, 2 pi / 3) for the assignment that reproduces the masses (the formula is invariant under delta -> delta + 2 pi / 3 with a relabelling of k, and under delta -> -delta with k -> -k; both are folded in, so only one number is compared).
S1 Sanity: with Q and delta fitted to the three masses, the formula reproduces all three to 1e-9 relative.
P1 [M on data] The fitted delta lies within 3 sigma of 2/9 (sigma from m_tau's error, propagated).
P2 [M on data] With Q = 2/3 and delta = 2/9 fixed, m_mu as the only input predicts m_e within 0.1% and m_tau within 3 sigma of PDG.
Information: the same fitted delta for neutrinos (section 125 masses) and for up and down quarks at M_Z (masses as in t99), each with its own Q.
Verdict: P1-P2 pass -> with the grain's 2/9 the charged-lepton masses follow from one of them; the reason for 2/9 stays an [I] reading to be derived.

## Scoring (2026-11-25)
Run 1 (t98_run1.log). All pass.
- S1 PASS (1.9e-14).
- P1 PASS: fitted delta = 0.2222296 +- 0.0000084 (from m_tau), against 2/9 = 0.2222222: pull +0.9 sigma. Fitted Q = 0.666661.
- P2 PASS: Q = 2/3, delta = 2/9 and m_mu alone give m_e = 0.510994 MeV (measured 0.510999, -1.0e-5 relative) and m_tau = 1776.967 MeV (+0.9 sigma).
- Information: neutrinos (section 125 masses) Q = 0.524, delta = 0.365; up quarks Q = 0.889, delta = 0.050; down quarks Q = 0.741, delta = 0.102.
Post hoc (t98_posthoc.py, labelled): the quark phases sit near successive halvings of 2/9 (1/9 for down: 0.102 +- 0.015, pull -0.6; 1/18 for up: 0.050 +- 0.002, pull -2.2). Noted as a pattern to test with better light-quark masses, not claimed.
Verdict: with the grain's 2/9 and Q = 2/3, one charged-lepton mass fixes the other two, to 1e-5 for the electron and 0.9 sigma for the tau. The reason for 2/9 remains an [I] reading.

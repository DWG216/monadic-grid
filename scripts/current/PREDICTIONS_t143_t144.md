# t143, t144 (pre-registered 2026-11-25, before any t143 or t144 code is written or run; the user away, the most direct design taken)

## t143 Chords across monads on E6's tones: three voices
Tones: the 27 states of E6's 27 (t136), each advancing its phase by ω_k = v·weight_k per beat (generic v, at most 0.3 rad). The grain's Z₃ (t142) labels each monad on an L × L periodic grid (L = 12) by (x + y) mod 3, and a monad with label s hears and holds only the 9 tones of block s (A, B, C for s = 0, 1, 2), the block that carries its cube root. Hearing of single tones: t140's averaged power over same-label neighbours (r = 2). Chords across monads: for each monad i and each pair of neighbours (j, l) at Chebyshev distance 1 carrying the other two labels (9 pairs), the relation ψ = φ_i,a + φ_j,b + φ_l,c over its block's tones (729 triples per pair); its record e^{iψ} is time-averaged (τ = 20 beats), coherence R = |average|; monad i turns φ_i,a toward the averaged relation with strength will × capacity × √(p_i,a p_j,b p_l,c) × 9^1.5 (capped at 1) × R; third-order hearing of tone a is the mean R over its chords. One Age, T = 600, η = 0.3, will 0.2; seeds 43000–43009.
A chord is locked when R > 0.8 for at least 5 monad-triples carrying the same three tones.
P1 [M] In ≥ 7 of 10 worlds at least one chord is locked across monads.
P2 [M] Every locked chord, in every world, is one of the cubic's terms (necessarily a trace term, one tone from each block).
C1 [M, control] With ω = 0 (no rotation, so resonance no longer filters), non-cubic chords lock in ≥ 7 of 10 worlds.
Consequence fixed now: if P1, P2 and C1 pass, three monads singing three different notes lock exactly the cubic's trace terms, and resonance is what selects them: the agreement minds hold across one another carries the gauge structure's invariant.

## t144 The light generations from the grain's Z₃ (enumeration, registered)
Generations carry charges q = a permutation of (0, 1, 2) under a Z₃ of the family; each part of 27 ⊗ 27 carries a charge h (cubic h_c, orthogonal 351′ h_o, antisymmetric 351 h_a). Entry (i, j) of a mass matrix is allowed from a part iff q_i + q_j + h ≡ 0 (mod 3) (the 351 only off the diagonal, antisymmetric). Kept: assignments in which every nonzero entry comes from exactly one symmetric part and no entry from the 351 alone (so every entry has a lepton anchor), the 3-3 entry from the 351′ (b/τ = 2/3, t113), and exactly three independent nonzero entries. For each, the three lepton entries are solved from m_e : m_μ : m_τ (2.88 × 10⁻⁴ : 0.0595 : 1, all sign choices and roots); the down matrix is the lepton matrix times each entry's Clebsch ratio (cubic −1, 351′ 2/3). Data at M*: s/μ = 0.231, d/e = 2.44, b/τ = 0.678.
P1 [M, blind] At least one kept assignment predicts s/μ and d/e within 10% and b/τ within 5%.
Reported: the number of assignments kept, every prediction, and the down-sector mixing angle θ₁₂ of each (to set beside the Cabibbo angle, 0.225, which also needs the up sector).
Consequence fixed now: if P1 passes, the grain's Z₃ fixes the light-generation texture and the lepton masses fix its sizes, so the down-quark masses follow with no new input. If it fails, Z₃ selection rules with one part per entry cannot give the light generations, and the hierarchy needs its own source.

### t144 scored (2026-11-25, t144_light_z3.py, t144_run1.log)
Kept assignments: 0. **P1 FAIL** as registered.
Why (read after the run, from the construction): with q a permutation of (0, 1, 2), each Z₃ class of entries is one diagonal entry and one off-diagonal pair, so each symmetric part (cubic, 351′) fills exactly two independent entries. If h_c = h_o every entry comes from two parts (rejected); if not, there are four entries. Exactly three is impossible, so the registered filter is empty by construction.
Post hoc (labelled, not scored; t144_posthoc.py, t144_posthoc.log): the two four-entry textures with the 3-3 entry from the 351′, one entry scanned and two solved from the lepton masses (754 lepton-consistent points), give at best s/μ = 1.35, d/e = 13.3, b/τ = 0.709 against 0.231, 2.44, 0.678. They miss by factors of 5.
Consequence (as fixed at registration): Z₃ selection rules with one part per entry cannot give the light generations; the hierarchy needs its own source. The candidate is the 3-adic grain step (sizes set by powers of a grain ratio, the texture by Z₃), to be registered separately.

### t143 scored (2026-11-25, t143_cross_chords.py, t143_run1.log)
P1 PASS: chords lock across monads in 10/10 worlds (239 to 354 locked chords each).
P2 FAIL: every world also locks non-cubic chords (214 to 328 with rotation).
C1 PASS: with ω = 0, non-cubic chords lock in 10/10 worlds (558 to 702).
Read off the table (labelled, not scored): the cubic's cross-block trace chords lock almost completely in both settings (21 to 27 of 27); rotation removes about 60% of the non-cubic locks (median about 670 to 290) and none of the cubic ones. Resonance favours the invariant but, at τ = 20 beats and ω ≤ 0.3 rad, does not exclude the rest: a slowly detuned chord stays coherent across a 20-beat window, and the will's turning holds it.
Consequence: the registered statement (resonance alone selects exactly the cubic across monads) does not hold in this design. What holds: every cubic chord is held, and resonance cuts the rest by more than half. Whether a longer window (τ ≫ 1/δ_min) makes the selection exact is a new question, to register separately; not re-run here.

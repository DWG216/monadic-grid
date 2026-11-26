# t145 Which Z₃ textures can carry the light generations (pre-registered 2026-11-25, before any t145 code)

Why this and not the grain step first: t144's post hoc scan covered every size of the textures permitted by permutation charges and all miss d/e by about 5×, so any sizing rule on those textures fails by construction. The open question is which textures can work at all.

Design: generation charges q ∈ Z₃³ (all 27, not only permutations), part charges h_c (cubic), h_o (351′) ∈ Z₃. Entry (i, j) is allowed from a part iff q_i + q_j + h ≡ 0 (mod 3). Kept: every nonzero entry from exactly one symmetric part, the 3-3 entry from the 351′, at least three independent nonzero entries, the lepton matrix of rank 3 for generic sizes. Sizes: the overall scale fixed by m_τ; three sizes solved from m_e : m_μ : m_τ = 2.88 × 10⁻⁴ : 0.0595 : 1; any further sizes drawn (400 draws per texture, magnitudes log-uniform on [10⁻⁴, 1] times m_τ, random signs). Down matrix = lepton matrix with each entry times its part's Clebsch (cubic −1, 351′ 2/3). Data at M*: s/μ = 0.231, d/e = 2.44, b/τ = 0.678.

P1 [M] At least one kept texture, at some lepton-consistent sizes, gives s/μ and d/e within 10% and b/τ within 5%.
Reported: kept textures (distinct up to relabelling of generations), the best point of each.

Consequence fixed now: if P1 passes, the surviving textures are the candidates whose sizes the grain step must then fix (t146, registered separately). If P1 fails, no Z₃ texture with one part per entry carries the light generations, at any sizes: the down/lepton split needs entries that mix the cubic and the 351′, i.e. light Higgs directions that are mixtures of the two, and the mixing angle becomes the quantity to derive.

### Scored (2026-11-25, t145_z3_textures.py, t145_run1.log)
Kept textures: 5 (up to relabelling). Lepton-consistent points: 663 to 1600 per texture. Points within tolerance: 0. **P1 FAIL.**
Read off the log (labelled): in every texture s/μ never falls below 2/3 (data 0.231), and d/e stays at most about 1.5 (data 2.44). With one part per entry the only quark-to-lepton factors are 1 and 2/3, so the ratios stay near [2/3, 3/2]; the data asks for about 1/4 and about 2.4, the same pattern as a Clebsch of 3 on the second generation (Georgi–Jarlskog).
Consequence (as fixed): no Z₃ texture with one part per entry carries the light generations at any sizes. The down/lepton split needs entries mixing the cubic and the 351′ (light Higgs directions that mix the two), and the mixing becomes the quantity to derive; or a part with Clebsch near 3 on the 2-2 entry.

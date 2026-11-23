# The monadic grid: code, pre-registrations and logs

The monadic grid derives quantum mechanics and gravity from one record, and the matter content of the world from the same steps. This package holds every computation behind it. Each script was written with its predictions fixed in a `PREDICTIONS_*.md` file before it ran, and each failure is kept.

Paper: `paper/monadic_grid.pdf` ("QM and GR from one record: the monadic grid").

## Why read this: what it solves

| Long-standing problem | What the grid does | Scripts |
|---|---|---|
| Quantum mechanics and gravity do not fit together (open since the 1930s) | Both are terms of one record \|O + R\|²: the cross terms are quantum mechanics, the meeting term is gravity's source (Bel–Robinson, checked on exact Kerr to 1 part in 10¹¹), and Einstein's equations follow as its equation of state. Geometry is never quantised. | t21–t29 |
| Why quantum mechanics needs complex numbers (1926) | Only λ = iω keeps size forever, and on the grain i is two golden steps: φ² = i in the field with nine elements. | t53 |
| Penrose's googly problem (since 1976) | Over F₉ conjugation is the polynomial D(ω, π) = (π³, ω³); both graviton helicities share one degree class mod 8 (only for q = 3), and one explicit deformation carries both, checked on all 820 points of PG(3,9). | t57, t58, t61b |
| Which symmetry group, and why this matter (grand unification, 1974) | The Fibonacci step and the hand swap generate the quaternions, SL(2,3), the Hessian group of 216 and all of SL(2, ℤ/3^k); McKay on the hand pair gives E6, whose 27 splits 1 + 16 + 10 with exactly the U(1)_ψ charges. | t53–t56, t64 |
| Where the Standard Model's gauge group comes from | Cut E6 at its dimension-3 node, the same rule that gave three generations: SU(3)_C × SU(3)_L × SU(3)_R, permuted by the counting phase so the couplings are equal. A U(1) inside gives exactly the Standard Model hypercharges, and sin²θ_W = 3/8 at the cut. The couplings meet only with the E6 extras near 10¹⁴ GeV (next test). | t66 |
| Why the proton has not decayed | The forces the cut leaves (three SU(3)s) cannot turn quarks into leptons; only E6's own bosons can, and the counting phases keep the couplings equal at any scale, so E6 may break above the Super-K bound (4.6 × 10¹⁵ GeV). The coloured triplets may sit at the cut. | t68 |
| The chirality objection (Distler–Garibaldi) | The theorem holds: the E8 content is vector-like. The mirror has no mass term of its own, but no anomaly forbids gapping it by interaction (Z16 index 0); family symmetry must break where it is gapped. | t69 |
| Why three generations (the muon, 1936) | E8 from the same steps mod 5, cut at the meeting of the hands, is E6 × SU(3): 240 = 78 + 81 + 81, each 81 the 27 three times. | t60 |
| Why matter comes first (Sakharov, 1967) | The balanced seed (0, 1) and the arrow fix the first moving count; the step conserves it. | t62, t63 |
| Why Koide's lepton relation holds (1981) | Q = 2/3 is the balance of the hands at the three-phase level; m_τ = 1776.969 MeV (world average 1776.94 ± 0.09). | t39, t40 |
| The neutrino mass scale | Normal ordering, Σmν = 59.16 ± 0.21 meV, Majorana with m_ββ = 1.16–4.11 meV, Z′_ψ near 10¹⁴–10¹⁵ GeV. | t40, t41, t65 |

Each claim carries a label in the paper: [M] computed, [S] forced by sufficient reason, [I] a reading that experiment tests.

## Run
Python 3.10+ with numpy and scipy (`pip install -r requirements.txt`).
```
python3 run_all.py --group grid          # t17–t65: the results above; compares each with its recorded log
python3 run_all.py --only t60_generations # one script
python3 run_all.py --group quick         # earlier tests (sections 28–87 of the record)
python3 run_all.py --group all -j 4 --timeout 3600
```
Each script runs in a fresh copy of its folder under `results/work/`; outputs go to `results/out/`, a summary to `results/summary.json`. For the grid group the expected output is the log recorded when the script first ran (`tNN_run1.log`, `tNN_posthoc.log`). Where the record amended a script after its first run (t21, t22), the expected output is the amended run; the first-run log stays beside the script. t25 and t27 print timings, which vary. A mismatch from a different numpy version means "inspect", not "wrong".

## Layout
- `scripts/current/`: t1–t65 with their `PREDICTIONS_*.md` and logs. Post hoc analyses are named `*_posthoc*` and labelled as such.
- `scripts/early/`: the first tests (2026-11-08 to 11-13), with pre-registrations and logs.
- `scripts/indep/`, `scripts/spiral/`, `scripts/catalogue/`: an independent re-implementation, the Euler-spiral table and the winding catalogue.
- `GRID_SPEC.md`: the grid in one file. `TEST_INDEX.md`: every test and its section. `CHANGELOG.md`.
- `lean_tools/`: text tools used on the public Lean RH archive (https://github.com/CocoSgt/riemann-hypothesis-lean).
- `visuals/`: figures (open `visuals/index.html`).

## Failures kept
Examples: t49 (a coil is not a doubling chain; that prediction was withdrawn), t58 (an ill-posed test, recorded as a fail), t60 (a fine split mispredicted while the main classes passed), t61 (two fails, then a re-registered t61b). The PREDICTIONS files state what was expected before each run.

## Not included
The source texts that motivated the work (Hockney's God Series, Millington and others) are copyrighted and are not redistributed; the paper cites them. `t65_zprime_scale.py` was rebuilt from an inline run and reproduces `t65_run1.log` exactly.

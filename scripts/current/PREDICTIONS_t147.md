# t147 Voices in unison: heart and brain (pre-registered 2026-11-25, before any value is looked up or computed)

Measure (t124): the record's gain over its diagonal for N sources of equal strength q is w = |Σ q_j e^{iφ_j}|² / Σ|q_j|². Its square root against one source, M = Q/q (Q the organ's equivalent current dipole, q one cell's), is the number of cells sounding as one; the unison fraction is f = M/N (N the organ's cells of that kind). Field strength alone (pT, mV) does not separate many weak voices in unison from a few strong ones; M and f do.
Inputs, fixed now, each taken from published values (sources recorded with the numbers): the heart's peak equivalent current dipole (QRS) and one ventricular cardiomyocyte's dipole; the brain's alpha-rhythm equivalent current dipole (resting, eyes closed) and one neocortical pyramidal cell's dipole; cell counts (ventricular cardiomyocytes; neocortical neurons). Where a range is published the geometric middle is used and the range is carried.

P1 [M] M_heart / M_brain-alpha ≥ 100.
P2 [M] f_heart ≥ 0.01 and f_brain-alpha ≤ 10⁻³.
Consequence fixed now: if both pass, the heart is the body's loudest unison (the held tone) and the brain sounds with a small fraction of its cells; the brain's standing in the grid then rests on chord order and poise, not on unison.

### Scored (2026-11-26, t147_unison.py, t147_run1.log)
Deviation, stated: no published dipole for one cardiomyocyte was found; it is computed from published cell geometry, intracellular conductivity, upstroke rate and conduction velocity (ranges carried in the script). Every other input is published (sources in the script header).
Values: one cardiomyocyte q = 4.4e-12 A m (range 6e-13 to 3e-11), about 250 times one neuron's share of the alpha rhythm (1.7e-14 A m). Heart M = 1.5e5 (range 1.2e4 to 1.7e6), f = 6e-5. Brain alpha M = 6e6, f = 3.8e-4.
P1 FAIL: M_heart / M_brain = 0.024 (range 0.001 to 0.57).
P2 FAIL: f_heart = 6e-5 (< 0.01); f_brain = 3.8e-4 (≤ 1e-3, that half holds).
Read off (labelled post hoc): the heart's field is loud because each heart cell is a strong source, not because many cells sum: at any instant only the depolarising front sounds, and across the ventricular wall's many directions the vectors cancel. By the vector sum, the brain's alpha rhythm has about 40 times more voices in unison.
Post hoc (labelled, not scored): the record's own measure is agreement of phase, not the vector sum. Every cardiomyocyte fires once per beat within about 90 ms of 833 ms: phase agreement 0.98 at the beat, about 2.4e9 voices in phase. The corresponding phase count for the brain's alpha is not available from dipoles (the folded cortex cancels too). The next test, to register: phase agreement at each organ's own rhythm from intracardiac and intracortical recordings.
Consequence (as fixed): the registered claim (the heart is the louder unison by the dipole count) does not hold; field strength mixes three things, source strength, phase agreement and geometric cancellation, which the grid's measures separate.

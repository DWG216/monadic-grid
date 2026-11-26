# PREDICTIONS t164: horizon decoherence without gravitons

Registered 2026-11-26, before t164_horizon_decoherence.py was written or run.

Prior work: Danielson, Satishchandran and Wald (arXiv:2205.06279; 2301.00026): a horizon decoheres a nearby spatial superposition because the body's field sends soft quanta into it. Their estimates (order of magnitude): electromagnetic T_D ~ ε₀ħc⁶b⁶/(G³M³q²d²); gravitational T_D^GR ~ ħc¹⁰b¹⁰/(G⁶M⁵m²d⁴), b the distance from a black hole of mass M; numerically 10 μs × (b/au)¹⁰(M☉/M)⁵(M_⊕/m)²(R_⊕/d)⁴.
Grid [S]: photons are cross terms (quantum), so the electromagnetic effect stands. The gravitational effect needs soft gravitons; gravity is the meeting term and has none. A neutral superposition decoheres at its own record rate, between E_G/ħ and 1.10 E_G/ħ (t157), and the horizon adds no term.
Comparison: T_DSW / T_grid = (b/r_g)¹⁰ r_g⁵ E_G/(Gm²c⁰…) computed from the formulas; for a uniform sphere of radius R displaced by d > 2R, E_G = Gm²(6/(5R) − 1/d).
S1 [M]: the gravitational formula reproduces DSW's numerical form (Earth mass, R_⊕, Sun mass at 1 au: 10 μs) within a factor 3.
P1 [M]: for the Bose et al. superposition (1e-14 kg diamond, d = 250 μm) at b = 6GM/c², DSW's gravitons decohere faster than the record only for black holes lighter than M*; M* = 4e21 kg within a factor 2 (from the formulas above, fixed now).
P2 [M]: for every black hole of at least one solar mass, at any b ≥ 6GM/c², the record decoheres the same superposition faster than DSW's gravitons by more than 10²⁰.
Consequence fixed in advance: the grid and quantised gravity differ near horizons only where gravitons would act faster than the record, i.e. near black holes lighter than about 10²¹ kg (primordial); for astrophysical black holes the record's own decoherence hides the difference. The electromagnetic effect is the same in both.

## Scoring (2026-11-26), run 1 (t164_run1.log)
- Procedure note: this registration was written and the script run in the same step, without a separate commit first; the predicted numbers (M* ≈ 4e21 kg, ratio > 1e20) were worked out by hand from the formulas before the script existed (M* ≈ 3.7e21 kg by hand). The "Comparison" line above contains a garbled expression; the script's formula is the one stated in S1–P2.
- S1 PASS: 2.1e-5 s against DSW's 10 μs (factor 2.1).
- P1 PASS: the record decoheres the Bose superposition in 0.0105–0.0116 s; DSW's gravitons act faster only for black holes lighter than M* = 2.9e21 kg.
- P2 PASS: at one solar mass and 6GM/c² the record is faster by 1.5e44, and the gap grows with M.
Verdict as fixed in advance: near astrophysical black holes the record's own decoherence hides the difference; the grid and quantised gravity part ways only near black holes lighter than about 3e21 kg, where gravitons would decohere faster and the grid says they do not. The electromagnetic effect is the same in both.

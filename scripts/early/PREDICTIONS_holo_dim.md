# Pre-registered before running holo_dim.py (2026-11-13). Label: math (known classical results, re-derived numerically).
Question (the holographic monad link, made computable): monads link to a bulk holographically. Our three linking conditions are
(1) a coherent source, (2) a medium that carries images sharply (no blur), (3) a lasting recorder. Which bulk dimensions d (spatial) allow all three?
This tests whether the corpus's linking conditions select 3+1 spacetime. It does not test whether monads exist.

D1 [sharpness = light cones]: a brief coherent impulse propagated by the wave equation in d = 1..6 leaves a field that is zero inside the
   light cone after the pulse passes (sharp image) only for odd d >= 3 (d = 3, 5). For d = 1, 2, 4, 6 a tail remains (images blur).
   Measure: tail amplitude inside the cone at t = 1, relative to the peak on the cone; "sharp" means < 1e-3.
D2 [lasting recorder, classical]: circular orbits under the d-dimensional Gauss-law force F ~ r^(1-d) are stable only for d < 4 (d = 1, 2, 3).
   Measure: perturbed orbit stays within 2x of its starting radius for 50 periods.
D3 [lasting recorder, quantum]: the d-dimensional Coulomb potential V = -r^(2-d) (log r for d = 2) has a ground state bounded below for d <= 3,
   with a finite ionisation threshold only for d = 3; for d >= 5 the energy falls without bound as the grid is refined (fall to the centre).
D4 [joint]: only d = 3 passes D1 and D2 and D3.
Controls: drop condition (2) and d = 1, 2, 3 pass; drop condition (3) and d = 3, 5 pass. Each condition removes different dimensions.
Interpretation fixed in advance: if D4 holds, the holographic linking conditions, as we stated them earlier, single out 3+1 dimensions:
light cones are sharp and records last only there.

# Scored after run (2026-11-13)
D1 PASS: tail/peak inside the light cone: d=1 1.0, d=2 0.42, d=3 1.9e-8, d=4 0.079, d=5 2.2e-7, d=6 0.022. Sharp only for d = 3, 5.
D2 PASS: perturbed orbits stay within 3-6% for d = 1, 2, 3; escape (radius to 17, 180, 221) for d = 4, 5, 6.
D3 PASS (after fixing a discretisation artefact in the first script: the u = r^((d-1)/2) R substitution put the first grid point too close to the
   critical 1/r^2 term; rerun with a finite-volume radial operator, holo_dim_d3.py): ground energy converges for d = 1 (0.809), 2 (0.180), 3 (-0.500, hydrogen);
   falls without bound for d = 4, 5, 6. d = 1, 2 confine (no release); only d = 3 has bound states that can also be released.
D4 PASS: only d = 3 passes all three.
Controls PASS: without sharpness d = 1, 2, 3 remain; without the recorder d = 3, 5 remain.
Caveats: these are classical results (Hadamard/Huygens; Ehrenfest 1917; Tegmark 1997). The wave equation and Gauss-law forces are assumed, so light
cones are input; what the conditions select is the number of space dimensions. The number of time dimensions was not tested.

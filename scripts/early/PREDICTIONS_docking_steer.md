# Pre-registered before running docking_steer.py (2026-11-08)
New facts (Dehapiot et al., PLOS Biol 2021 / bioRxiv 2020, mouse): MII spindle parallel to cortex until fertilization; after activation,
anaphase ~3 min, cortical protrusions 3-15 min, spindle rotation ~20-30 min, ring closure ~60 min. Direction "not biologically
predetermined", but the chromatid cluster initially closer to the cortex is extruded in 76.4% of oocytes (83.7% in their model):
a random initial geometric asymmetry plus noise decides. Human: no rotation data found (human spindle papers did not load).

STEP 1 (human evidence) H1: we report what we found and did not find; no prediction.

STEP 2 (can the calcium signal steer the choice, and can it be tested?)
D1 [correction of the previous budget]: decision window ~ first 30 min after the sperm-triggered rise -> at most one inter-spike
   interval (human intervals 10-35 min). Capacity of one interval: 0.8 bits (pessimistic jitter) to 3.9 bits (optimistic).
   Prediction: under pessimistic jitter the signal can NOT carry the 1 bit in time (B1 of the previous run is withdrawn).
D2 [model]: outcome = sign(asymmetry + noise + nudge). Calibrating to 76.4% gives sigma_asym/sigma_noise ~ 1.1.
   Prediction: a nudge that makes ANY chosen lot win >= 84% of the time must be >= 1.4 x the combined spread; for >= 99%, >= 3 x.
   Control: nudge 0 reproduces 76.4%.
D3 [experiment power]: mouse eggs fertilised by sperm (natural Ca oscillations), imaging Ca + spindle + chromatids; test whether a
   binary Ca feature (a second Ca spike during rotation, present in ~half of eggs) changes the "reversal" rate (farther cluster
   extruded; base 23.6%). Prediction: odds ratio 2 needs n ~ 300-400 eggs at 80% power, alpha 0.05; odds ratio 1.5 needs > 1000.
Falsification frame fixed in advance: if Ca features predict reversals beyond geometry, the calcium rhythm is a physical steering
channel for the docking choice (supports a mechanistic reading of "Fourier docking"). If not, the choice is geometry + noise; a
monadic selection could still act through the noise but would be invisible.

# Scored after run (2026-11-08)
H1: no human data found on second-division spindle rotation; the human MII spindle studies we tried did not load.
D1 PASS: one interval carries 0.81 (pessimistic), 1.90 (median), 3.85 (optimistic) bits; under pessimistic jitter the 1 bit cannot
   be carried in time. Previous run's B1 ("worst case 3.2 bits") is WITHDRAWN: its 2.5 h window was wrong.
D2 numeric thresholds FAILED (we overestimated): 84% needs 0.99x combined spread (predicted >= 1.4x); 99% needs 2.33x (predicted >= 3x).
   sigma_asym/sigma_noise = 1.09 (predicted ~1.1, PASS). Control PASS: 0.764.
D3: odds ratio 2 -> 314 eggs total (PASS, predicted 300-400); odds ratio 1.5 -> 964 (predicted > 1000: narrowly FAILED); odds ratio 3 -> 118.

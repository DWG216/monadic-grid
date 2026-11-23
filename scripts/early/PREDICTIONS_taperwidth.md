# Pre-registered before running taperwidth.py (2026-11-07)
Claim tested: the light-cone taper is a sampling profile set by temperature, width = beta*v/pi.
Method: stretch the thermal length by factor s (s=1 is the thermal light-cone weight), scan s in [0.2, 5], at beta = 5, 10, 20.
PREDICTION: the s that minimises drift lies within 20% of 1 (0.8..1.25) at all three temperatures.
FAILURE: best s outside 0.8..1.25 at any temperature, or drifting systematically with beta.
Tier labels: temperature, chirality = tier 2 inputs; drift = tier 3 computed. Nothing tier 1 is claimed from this run.

# Result of run 1: best s = 0.99, 1.09, 1.24 (beta 5,10,20): inside window but drifting up -> partial failure by our own criterion.
# Post-hoc hypothesis, pre-registered before run 2: the drift is the cone tilt. Chirality lam gives right/left speeds 2+4lam, 2-4lam.
# PREDICTION 2: at beta=20, best s tracks the faster speed / 2:  lam=0 -> s ~ 1.0 ; lam=0.2 -> s ~ 1.4 (within 0.1).
# FAILURE 2: lam=0 still gives s ~ 1.2, or lam=0.2 gives s ~ 1.2.

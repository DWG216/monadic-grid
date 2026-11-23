# Pre-registered before running cycles.py (2026-11-09 ~12:00 ET). Label: math (simulation of a toy model).
Claim under test (user): the cosmic cycle is a repeated game whose starting conditions are set by the previous cycle's symmetry breaking.
Corpus: each Big Bang wipes all "RAM" (records); only "ROM" (the laws) and the monads persist.
MODEL
- Monads: 200 per cycle. Each holds one strategy: ALLC (always cooperate), ALLD (always defect: the free-rider), TFT (copy your partner's
  last move: needs memory).
- Stage game: prisoner's dilemma, payoffs T=5 (exploit), R=3 (both cooperate), P=1 (both defect), S=0 (exploited).
- Within a cycle (spacetime exists, records exist): pairs play 5 rounds with 2% execution errors; strategies spread by replicator
  dynamics (selection strength 1) for 60 generations, with 1% mutation. This is the "life" part of the cycle.
- The Crunch: everything is wiped except a k-bit summary of how cooperative the cycle ended (share of TFT+ALLC, rounded to 2^k levels).
- The next Big Bang: the new population of 200 is drawn from that summary (cooperators split evenly between TFT and ALLC, the rest ALLD).
  k = 0 means nothing passes: every cycle starts from equal thirds.
- 30 cycles per history, 20 histories for each k in {0, 1, 2, 4, 8}.
Measured: cooperation at the end of each cycle (fraction of moves that are cooperative).
C1 [built-in]: k = 0: cycles are independent (correlation between consecutive cycles near 0, |r| < 0.2) and show no trend.
C2: k >= 1: consecutive cycles strongly correlated (r > 0.8): histories lock into a regime.
C3 (the ratchet): mean cooperation over cycles 21-30 is higher for k >= 1 than for k = 0.
C4: one bit is already enough: k = 1 reaches at least 90% of the k = 8 level.

# Scored after run 1
C1 PASS: k = 0 lag-1 correlation -0.00.
C2 FAILED: k >= 1 correlations are also ~0 (0.03, -0.04, -0.03, 0.05).
C3 marginal: 0.941 (k >= 1) vs 0.931 (k = 0): higher, but only because k = 0 had rare collapsed cycles.
C4 PASS (trivially).
Reason: with 5 rounds per pairing, cooperation (TFT) wins inside almost every cycle from almost any start, so the starting signal has
nothing to decide. The test needs the regime where a cycle's outcome depends on how it starts.

# Pre-registered BEFORE run 2
Rule fixed in advance: take the smallest number of rounds in {2, 3, 4} at which k = 0 cycles end cooperative (> 0.5) in 20%-80% of cases
(the regime where the start matters). Rerun the k sweep there with C1-C4 unchanged.

# Scored after run 2 (rounds = 4, chosen by the fixed rule: k = 0 ends cooperative 45% of the time)
C1 PASS: k = 0 lag-1 correlation 0.03.
C2 PASS: k >= 1 correlations 1.00, 0.99, 0.99, 0.99: each history locks into one regime for all 30 cycles.
C3 FAILED: mean cooperation (cycles 21-30) k = 0: 0.524; k = 1: 0.533; 2: 0.442; 4: 0.575; 8: 0.327. No ratchet: the signal preserves
   whichever regime the first cycle fell into (about half cooperative, half not), it does not improve on it.
C4 not meaningful given C3.
Reading: a symmetry-breaking signal produces inheritance (path dependence), not progress. A ratchet would need a bias in who writes the
signal or how faithfully cooperative endings are transmitted.

# Pre-registered BEFORE ratchet.py
Same model, 4 rounds, k = 1. New: at each Crunch the signal is lost (the next cycle starts from equal thirds) with probability
nu = 0.2, adjusted by an authorship EDGE e: cooperative endings are lost with probability nu(1-e), defecting endings with nu(1+e).
e = 0: noise is symmetric. e > 0: cooperative endings are written more faithfully (the corpus's "mathematical Gods" authoring the break).
Prediction (two-state chain, p = 0.45 = chance a fresh cycle ends cooperative): long-run share of cooperative cycles
  pi(e) = (1+e)p / ((1+e)p + (1-e)(1-p)): 0.45 (e=0), 0.55 (0.25), 0.71 (0.5), 0.85 (0.75), 1.00 (1).
R1 [built-in check]: simulated long-run shares (200 cycles x 40 histories, cycles 51-200) within 0.07 of pi(e) at every e.
R2 [the informative number]: the edge needed for 75% cooperative cycles is about e = 0.57, for 90% about e = 0.83.
Tier: the ratchet follows from the assumed edge; what the run measures is how large the edge must be.

# Scored after ratchet.py
(Correction to the pre-registration text: the formula, not the hand-typed list, is the prediction; pi(0.25) = 0.577, not 0.55.)
R1 PASS: simulated vs predicted share of cooperative cycles: e=0 0.475/0.450; 0.25 0.592/0.577; 0.5 0.704/0.711; 0.75 0.832/0.851;
   1.0 0.979/1.000. All within 0.03.
R2 PASS: 75% cooperative needs e ~ 0.57-0.6 (cooperative endings kept about 3.7x more faithfully than defecting ones); 90% needs
   e ~ 0.83 (about 11x).

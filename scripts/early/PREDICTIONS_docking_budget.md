# Pre-registered before running docking_budget.py (2026-11-08)
Question: does the "Fourier docking" signal (fertilization calcium oscillations) have the bandwidth to address the choices
settled after the sperm arrives?

Inputs (sourced):
- Human IVF eggs: first Ca rise 20-35 min after sperm; spikes every 10-35 min; spike width 100-120 s (Taylor et al., via
  IntechOpen review). Oscillations stop at pronucleus formation (~11 h; EHD Carnegie stage 1).
- Second polar body ~3 h after fusion (EHD).
- Mouse: which chromatid lot is discarded is NOT predetermined; spontaneous symmetry breaking during spindle rotation after
  activation (Dehapiot et al. 2020). The two lots (one sister of each of the 23 chromosomes) are fixed earlier by spindle attachment.
- A few hundred sperm reach the ampulla (embryology.ch).
Assumption, unmeasured: spike-timing jitter sigma = 0.5 min (optimistic), 2 min (median), 5 min (pessimistic). The egg may set
each interval anywhere in 10-35 min. Capacity per interval = 0.5*log2(1 + (R^2/12)/sigma^2), R = 25 min.

Required bits:
- after sperm entry, mouse-style model: 1 bit (which lot);
- naive model (each chromatid independent): 23 bits;
- sperm choice: log2(200..500) = 7.6-9 bits, but it happens BEFORE the signal starts (the sperm triggers it): not addressable.

B1 [prediction]: in the causal window (first Ca spike to polar-body extrusion, ~2.5 h), capacity exceeds 1 bit under ALL jitter
   assumptions.
B2 [prediction]: in the same window, capacity reaches 23 bits only under optimistic jitter AND fast spiking.
B3 [prediction]: over the whole train (to ~11 h), capacity exceeds 23 bits under median assumptions.
B4 [literature check]: the readout biology has demonstrated (spike number/frequency regimes changing gene expression, Ozil 2006)
   carries a few bits (<= 4): enough for 1 bit, not for 23.
Control: as sigma -> R (jitter as large as the whole range), capacity -> ~0.
Interpretive frame fixed in advance: if B1 holds, the corpus's docking needs only to settle a single symmetry-breaking choice,
and the docking signal has ample bandwidth for it; the choice is 50:50 and not predetermined, so any "selection" is
statistically invisible.

# Scored after run (2026-11-08)
B1 PASS: causal-window capacity >= 3.2 bits in the worst case (slow spiking, pessimistic jitter); need 1.
B2 PARTLY FAILED (more permissive than predicted): >= 23 bits in the causal window also for fast+median and typical+optimistic,
   not only fast+optimistic.
B3 PASS: whole train, typical spacing, median jitter = 53 bits (> 23).
B4 PASS: demonstrated readout (three oscillation regimes in Ozil 2006) ~ 1.6 bits: enough for 1 bit, far below 23.
Control PASS: sigma = R -> 0.06 bits per interval.
Caveat: the jitter values are assumptions (no measured human value found); the lot-choice result is from mouse; human spindle
behaviour at this step is not verified here.

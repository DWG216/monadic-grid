# Pre-registered before running time_dim.py (2026-11-13). Label: math.
Question: with n space and m time dimensions (wave equation sum_time d^2 u = sum_space d^2 u), is the linking image determined stably by its
boundary data (a well-posed Cauchy problem from a hypersurface of one coordinate)? A monad's record must be reconstructible from boundary data
without small errors exploding.
T1 [real test]: m = 1: every Fourier mode evolves with growth rate 0 (pure oscillation) for every n: well-posed.
T2 [real test]: m = 0 (all directions alike, elliptic): some modes grow like e^(K) with frequency K: amplification after unit "time" grows without
   bound as K increases (Hadamard ill-posedness).
T3 [real test]: m >= 2: modes whose extra-time frequency exceeds their space frequency grow exponentially, again unboundedly in K: ill-posed.
T4 [simulation]: finite-difference evolution with 1e-10 random noise on the data: noise stays at 1e-10 for m = 1, explodes (> 1) for m = 0 and m = 2.
T5 [joint with section 22]: only (n, m) = (3, 1) passes sharpness, lasting records and well-posedness.

# Scored after run (2026-11-13)
T1 PASS: m = 1, every n: amplification 1 at all frequencies.
T2 PASS: m = 0 (n >= 2 transverse directions): amplification e^K = 1.5e2, 2.2e4, 4.9e8, 2.4e17 for K = 5..40 (n = 1 is degenerate: no transverse direction).
T3 PASS: m = 2, 3: same unbounded growth.
   (T1-T3 are the analytic mode growth rates; T4 is the real computation.)
T4 PASS: finite-difference noise 1e-10 stays 1.8e-10 for one time; explodes past 1e6 for the same-sign case.
T5 PASS: with section 22, only (3 space, 1 time) gives sharp images, lasting records and stable reconstruction from boundary data.

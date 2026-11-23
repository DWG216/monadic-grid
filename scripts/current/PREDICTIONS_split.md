# Pre-registration (2026-11-22, 15:50): both hands on one real space (split signature) (record §79)
Split signature (2,2): a real point is a real 2x2 matrix x^{AA'}; twistors are real, Z = (omega, pi) with omega^A = x^{AA'} pi_A' (no i); pi = (cos t, sin t) runs over a real circle. Twistor functions are made real and smooth on real lines from a complex form d.Z (real and imaginary parts independent, so d.Z != 0 on every real line).
Positive hand (helicity +2): f = Re (d.Z)^(-6) (homogeneity -6); psi_k(x) = integral over t in [0, pi) of cos^(4-k) t sin^k t f dt. Field equation: d psi_(k+1)/dx^(A0') - d psi_k/dx^(A1') = 0, A = 0, 1, k = 0..3.
Negative hand (helicity -2): g = Re[(c.Z)^6 (d.Z)^(-4)] (homogeneity +2); phi_m(x) = integral of the m-th component of d^4 g / d omega^4 (exact, by the product rule); field equation d phi_(m+1)/dx^(0A') - d phi_m/dx^(1A') = 0, A' = 0, 1, m = 0..3.
S1 [identity] both fields are real (imaginary part 0) and both satisfy their field equations: relative residual below 1e-7 at 20 random real points (central differences, step 1e-5).
S2 [null] scrambled index weights (cos^(4-k) sin^(2k) in psi; components shifted in phi) fail: residual above 1e-2.
S3 [identity, Lorentzian contrast] in Lorentzian signature (x Hermitian, omega = i x pi, contour integral as in §76) the helicity +2 field psi is complex, and its complex conjugate satisfies the OTHER hand's equation (primed and unprimed indices swap): reality pairs the hands. Pass: residual of the swapped equation for conj(psi) below 1e-7, and |Im psi| / |psi| above 0.1.
Reading fixed in advance: if S1 and S3 pass, split signature is where the two hands are independent and real on one space (no pairing by reality), while Lorentzian reality is itself the pairing of the hands. This does not solve the googly problem; it locates the pairing.

## First run (split_run1.log): FAIL, construction errors; treated as the sanity run (disclosed)
S1 failed with residual 2.0 because psi was identically zero (|psi| ~ 1e-17): Re of a holomorphic twistor function integrates to zero over a closed real circle (one pole on the Riemann sphere, residues sum to zero). [M] In split signature the real Penrose (X-ray) transform needs genuinely real functions on real twistor space, not real parts of holomorphic ones. S3 failed from an index-order bug (derivatives taken along x^{0A} instead of x^{A0}).
AMENDMENT (before the second run; thresholds and readings unchanged): f = q^(-3), g = (c.Z)^6 q^(-2), with q = (a.Z)^2 + (b.Z)^2 and a, b, c REAL (q > 0 on every real line); the 4th omega-derivative of g by exact power-series in the shift parameter. S3 derivative indices corrected to x^{A0}, x^{A1}.

## Second run (split.log), after the amendment
S1 FAIL as registered: fields real (True); residuals 1.9e-6 (helicity +2) and 5.9e-4 (helicity -2), above the 1e-7 threshold. Post hoc (split_posthoc.py, labelled): the residual falls by 100 for each tenfold smaller step (h = 1e-4 -> 1e-5), i.e. as h^2: finite-difference error on a sharply peaked integrand (|phi| up to 2.5e7), not a failure of the equations; analytically both equations hold identically (derivative under the integral, record §79).
S2 PASS: scrambled weights 1.50 and 1.78.
S3 PASS: Lorentzian psi is complex (|Im psi|/|psi| median 0.83); its conjugate satisfies the other hand's equation to 2.1e-9.

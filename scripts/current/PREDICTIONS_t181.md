# PREDICTIONS t181: the ln 3 line spectrum of small black holes: sharp or smeared?

Registered 2026-11-28, committed before t181_lines.py is written or run. Disclosure: a rough mental estimate of both ratios was made while designing this test (about 0.03 and about 0.5); the thresholds below are set from the physical criterion (lines resolved when their width is well below their spacing), not tuned to those estimates.

Reading [S]. Each meeting across a horizon hides ln 3 (§308) and S = A/4G, so the area changes in steps of 4 ln 3 Planck areas. Following Bekenstein and Mukhanov (who used ln 2), Hawking radiation is then a line spectrum at ω_n = n ω₀ with ω₀ = T_H ln 3, under the thermal envelope. Each line's width is set by the lifetime of the black hole's state, the total rate at which it emits quanta, Γ = Ṅ. R = Γ/ω₀ is a pure number for a given particle content (Ṅ ∝ 1/M and ω₀ ∝ 1/M).

Inputs (Planck units, Schwarzschild, greybody effects absorbed in Page's coefficients). Page (1976): dM/dt = −α/M² with α = 2.011 × 10⁻⁴ for photons, three neutrino species and gravitons; fractions 81.4% (neutrinos), 16.7% (photons), 1.9% (gravitons). Per degree of freedom: fermion 2.73 × 10⁻⁵, vector 1.68 × 10⁻⁵, graviton 1.9 × 10⁻⁶. Mean energy per quantum taken as the blackbody value (bosons 2.701 T, fermions 3.151 T), which overestimates Ṅ and so R (conservative for P1). High temperature (above the electroweak scale): all Standard Model degrees of freedom: 90 fermion (quarks 72, charged leptons 12, neutrinos 6), 27 vector (gluons 16, W and Z 9, photon 2), the Higgs counted as one degree with the fermion coefficient (no spin-0 coefficient in the inputs; noted).

P1 [M]: cold black holes (T below 0.5 MeV, photons, neutrinos and gravitons only): R < 0.1: the ln 3 lines are sharp.
P2 [M]: in the final burst (T above 100 GeV, full Standard Model): R > 0.3: neighbouring lines overlap and the spectrum is smeared.
Consequence fixed now: if P1 and P2 pass, the ln 3 line spectrum is a sharp property of cold black holes, whose radiation is too faint to observe, and is smeared in the bursts of exploding primordial black holes: a burst without lines is not evidence against the grid, and no current gamma-ray or neutrino instrument can test the spacing. If P2 fails, the lines survive into the burst and the test becomes observational.
Gate: physics; public.

## Scoring (2026-11-28), run 1 (t181_run1.log)
- Check: the cold-hole coefficients sum back to Page's α = 2.011 × 10⁻⁴.
- P1 PASS: R = 0.038 for cold black holes: lines sharp (width under 4% of the spacing).
- P2 PASS: R = 0.55 in the final burst: lines overlap.
Reported: with Bekenstein–Mukhanov's ln 2 spacing the ratios would be 0.060 and 0.87; the grid's wider ln 3 spacing makes its lines sharper than theirs, but not sharp enough to survive the burst.
Verdict as fixed in advance: the ln 3 line spectrum is a sharp property of cold black holes and smeared in the bursts of exploding primordial black holes; a burst without lines is not evidence against the grid, and current gamma-ray or neutrino instruments cannot test the spacing.

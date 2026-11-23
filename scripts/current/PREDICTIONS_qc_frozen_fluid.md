# Pre-registration (2026-11-22): the frozen/fluid line as the classical/quantum line
Q1 [identity, Niven] 2cos(2 pi / r) is an integer exactly for r in {1, 2, 3, 4, 6} among r = 1..60 (the crystallographic orders); equivalently the strand dimension d = 2cos(pi/r) has integer d^2 = 2 + 2cos(2 pi/r) exactly there (weak integrality, section 11).
Q2 [real, numerical; Jones 1986 says finite exactly for r in {1,2,3,4,6,10}] the image of the 3-strand braid group in the reduced Burau/Jones representation at t = e^(2 pi i/r), taken modulo scalars, closes under breadth-first search (cap 20000 elements) exactly for r in {3, 4, 6, 10} among r = 3..12, and exceeds the cap for r = 5, 7, 8, 9, 11, 12.
Q3 [real] at r = 10 the projective image has order 60 (A5, the icosahedral group: the golden frame's 3-strand shadow, section 11); at r = 5 (the Fibonacci anyon point, d = phi) it is infinite.
Reading to test against the literature (not a numerical prediction): the finite cases are where exact Jones evaluation is classically easy (Jaeger-Vertigan-Welsh: r in {1,2,3,4,6}) and the infinite golden case r = 5 is where approximating the Jones polynomial is BQP-complete (Freedman-Larsen-Wang; Aharonov-Jones-Landau).

## Results
Q1 pass: r in {1, 2, 3, 4, 6}.
Q2 FAIL as pre-registered (one case): the closed set is {4, 6, 10}, not {3, 4, 6, 10}. r = 3 runs past the cap. Post hoc (labelled): at t = e^(2 pi i/3) the reduced Burau form is not the Jones form; s1 s2^-1 has normalised trace exactly 2 and is not scalar, so it is unipotent of infinite order (the "two lines", non-semisimple case). The Jones/Temperley-Lieb representation itself has d = 1 there, and its 3-strand block collapses to dimension 1, so the Jones image is trivially finite. All other cases match: closed for r = 4 (24), 6 (12), 10 (60); unbounded for 5, 7, 8, 9, 11, 12.
Q3 pass: r = 10 projective image order 60 (A5, icosahedral); r = 5 (Fibonacci, d = phi) unbounded.

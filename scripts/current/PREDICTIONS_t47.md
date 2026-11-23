# t47 meeting-as-source bridge (pre-registered 2026-11-23, before run)
Bridge: two hands = two drives at the ends of a lossless ladder (series Z1, shunt Z2 at interior nodes).
Hyperbolic face (stopband): Z1 = iwL, Z2 = i w 2L -> cosh g = 1 + Z1/(2 Z2) = 1.25, cell factor e^g = 2.
Claim: real power reaches the network ONLY through the meeting term Im(Va* Vb), and moving the reverse drive s cells closer multiplies it by sinh(N ln2)/sinh((N-s) ln2) -> 2^s.
H1 sanity: fitted cell factor = 2 (|err| < 1e-9).
H2 one hand alone (Vb = 0, or far end in image impedance): real power |P| < 1e-12.
H3 meeting conserved: real power through every series element equal (rel spread < 1e-9).
H4 shift law, quadrature drives, N=12: P(s)/P(0) for s=0,1,2 within 1e-6 (relative) of exact sinh ratio, and within 1e-3 of 1:2:4.
H5 phase law: P proportional to sin(theta), theta = phase gap (max dev < 1e-9 after normalising).
Negative control (circle face, passband: series L, shunt C, w^2 LC = 1):
C1 one hand into matched real image impedance carries power alone (P > 0.01 Va^2/|Z0|).
C2 shift ratios differ from 1:2:4 by > 0.1 in at least one of s=1,2.
Amendment (before any H/C output was printed): control w^2 LC = 1 gives cell phase 60 deg, N=12 is resonant (singular). Control changed to w^2 LC = 0.7.

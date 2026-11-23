# t48 the p.204 winding as two hands; low-pass ladder face (pre-registered 2026-11-23, before run)
W1 [M] On grey residues {1,4,7} the +15-slot step (= +6 mod 9) equals multiplication by 7 = -2; on brown {2,5,8} it equals multiplication by 4 = (-2)^-1 mod 9. Check all 12 passes of each wire: 24/24.
W2 [M] 7 * 4 = 1 mod 9 (inverse multipliers: forward and reverse hands).
Bridge [I]: coil = low-pass L-C ladder (series L per pass, shunt C between passes). Above cutoff w_c = 2/sqrt(LC): cosh g = 1 - w^2 LC/2. Cell factor -2 at w^2 LC = 9/2, i.e. w = (3/(2 sqrt2)) w_c = 1.0607 w_c.
L1 sanity: cell factor = -2 at w^2LC = 4.5 (err < 1e-9).
L2 one drive alone: real power |P| < 1e-12.
L3 two drives in quadrature, N=12: |P(s)/P(0)| within 1e-3 of 1, 2, 4 for s = 0,1,2; signs alternate (+, -, +).
L4 conserved: same power through every series element (rel spread < 1e-9).
Control: same ladder at w^2LC = 2 (passband): |ratios| differ from 1,2,4 by > 0.1 in at least one of s = 1,2.
Amendment (after L1-L4 printed, before control output): control w^2LC = 2 gives 90 deg/cell, N=12 resonant (singular). Control changed to w^2LC = 1.4.

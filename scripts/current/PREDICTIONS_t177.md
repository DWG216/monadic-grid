# PREDICTIONS t177: the glueball ratio m(0⁺⁺)/√σ on the grain's gauge group

Registered 2026-11-27, committed before t177_glueball.py is written or run.

Question. The pure number m(0⁺⁺)/√σ (lightest glueball mass over the square root of the string tension) is what the grid owes for Yang–Mills (§179). The grid cannot yet derive it analytically. What it does claim (t175, §321): the grain's clock-of-five group 2I ⊂ SU(2) is, to the record, indistinguishable from SU(2) as a gauge group. Test: compute the ratio on the lattice with gauge group 2I and with SU(2), same lattice, same coupling, same estimators.

Setup (fixed now). Wilson action (β/2) Σ Re tr U_p, β = 2.4, lattice 8⁴ periodic. Links as unit quaternions. SU(2): checkerboard heat bath (Kennedy–Pendleton); 2I: exact heat bath over the 120 elements (Gumbel-max sampling). Cold start; 300 thermalisation sweeps; 4,000 measurement sweeps per group; seeds 1771 (SU(2)), 1772 (2I).
Estimators. Plaquette ⟨½ Re tr U_p⟩. String tension from the Creutz ratio χ(3,3) = −ln[W(3,3) W(2,2) / (W(3,2) W(2,3))], Wilson loops averaged over all positions and planes, measured every 5 sweeps. Glueball: spatial links APE-smeared (4 steps, weight 0.5, renormalised to unit quaternions), O(t) = Σ over spatial positions and the 3 spatial planes of ½ Re tr of the smeared plaquette, connected correlator C(t) averaged over time origins, every 2 sweeps; m = ln[C(1)/C(2)]. Errors by jackknife over 20 bins.

S1 [sanity]: SU(2) plaquette within 0.5% of the literature value 0.630 at β = 2.4.
S2 [sanity]: SU(2) ratio m/√χ(3,3) within 25% of the continuum value 3.78 (Lucini, Teper, Wenger), allowing for the small lattice and the crude estimators.
P1 [M]: 2I plaquette equals SU(2)'s within 0.5%.
P2 [M, the test]: 2I's ratio equals SU(2)'s within two combined standard errors and within 10%.
Consequence fixed now: if P1–P2 pass, the record holds that the grain's gauge group gives SU(2)'s glueball ratio: the number the grid owes is the same on the grain as in SU(2). Deriving its value from the ground stays open.
Gate: physics; public.

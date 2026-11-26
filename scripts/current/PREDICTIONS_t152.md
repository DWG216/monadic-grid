# PREDICTIONS t152: horizon microstates, repaired

Registered 2026-11-26, after t150 failed and before t152_microstates.py was written or run.

Diagnosis of t150 [M]. The bare count treated the n horizon cells as independent, with one global balance on r = 5 charges. The total charge then fluctuates with variance ∝ n ∝ A, and fixing it costs (r/2) ln A. In a 4D black hole the gauge-charge fluctuation is O(1), not ∝ A, which is why Sen's formula has no gauge-charge log term in D = 4 (coefficient (D − 4)/2 = 0).

Repair 1, balance is pairwise [S]. The grid's content is balanced pairs (+ω, −ω), not cells with a global sum. A horizon cell's charge is balanced by its partner across the horizon (the record of a meeting has two sides). Then the charge fixing costs nothing that grows with A: no −(r/2) ln A. Read in field language, the straddling pairs are the edge modes of the gauge fields at the horizon (Donnelly and Wall 2015, who showed edge modes supply the contact term that makes the entanglement of a Maxwell field match its anomaly).

Repair 2, the record's fields carry the log [M, others]. The horizon entropy is the record's entanglement across the horizon (t27). Its leading term is the area term (A/4, the cells); its log term is fixed by the trace anomaly of the fields massless at the horizon's scale (Solodukhin; Casini and Huerta; for a sphere in flat space the free scalar gives −1/90 ln(R/ε), confirmed numerically on Srednicki's lattice, the t27 lattice, by Lohmayer, Neuberger, Schwimmer and Theisen 2010). On a Ricci-flat horizon the local coefficient is Sen's C = Σ 4(c − a) per field: (2n_S − 26n_V + 7n_F)/90, n_F Dirac.

The grid's departure [S, bridge §102]. Gravity is the meeting term, which carries no relative phase: it is not a quantum field and has no loop. So the graviton's 424/90 is absent from C. The rotational zero mode and the ensemble terms are kept (they are classical statistics of a conserved J).

Prediction. Microcanonical Schwarzschild in D = 4: S = A/4G + ((C_matter − 1)/2) ln A, C_matter over fields massless at the horizon scale, no graviton loop.
P1 [I, number fixed here]: astrophysical black holes (larger than the lightest neutrino's Compton length, about 0.5 mm; t41 gives m₁ = 0.37 meV), the only massless field is the photon: C = −26/90, coefficient (−26/90 − 1)/2 = −0.6444. With a quantised graviton (Sen): ((424 − 26)/90 − 1)/2 = +1.7111. The two readings differ in sign.
P2 [M] in t152_microstates.py: the pairwise-balanced count of n straddling pairs of 16-state cells has zero log coefficient (exactly 16^n), against −5/2 for the t150 count; and the arithmetic of P1.
Not computed here: the scalar −1/90 on the t27 lattice (needs the large-l tail treatment of Lohmayer et al.; cited, to be reproduced as t153).
Consequence fixed in advance: if P2 passes, the microstate count is: cells for the area term, edge-mode pairs for the gauge charges, the record's field entanglement for the log term, and no graviton loop. The sign of the log term then separates classical gravity (grid, Oppenheim) from quantised gravity (Sen's +1.71).

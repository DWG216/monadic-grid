# Pre-registered before running arena.py (2026-11-09 ~11:30 ET). Label: math (simulation of a toy model).
Question: in an arena where patterns are copied with errors and room is finite, does cooperation (a hypercycle: patterns that help copy
each other) beat selfish patterns, and does the answer depend on the arena being SPATIAL (local copying, finite speed: a light-cone arena)?
Model: copy error 1% per symbol; fidelity q = 0.99^L. Junk (non-functional copies) replicates at rate 1, perfectly.
  simple pattern L=20 (q=0.82), rate 1.5 · complex pattern L=100 (q=0.37), rate 2 · hypercycle: 4 complex patterns, each boosted by its
  predecessor (catalysis c=10) · parasite: L=20, boosted by member 1 (1.2c), helps no one.
"Carried structure" E = sum of (share x length L): how much organised pattern the arena holds.
R1 [built-in]: a lone complex pattern dissolves into junk (error catastrophe, 2 x 0.37 < 1); a lone simple pattern survives (1.5 x 0.82 > 1).
R2 [calculation]: the complex hypercycle survives, although each member alone dissolves, and carries more structure E than the lone simple
   pattern.
R3 [calculation, known risk stated in advance]: in a WELL-MIXED arena a parasite destroys the hypercycle (Maynard Smith's objection).
R4 [calculation, the decisive one]: in a SPATIAL arena (local copying on a grid) the hypercycle survives the parasite in at least half
   of 10 runs (Boerlijst-Hogeweg).
Interpretation fixed in advance: if R2-R4 hold, synthesis beats selfishness only when copying is local and finite-speed, i.e. the
spacetime arena itself is what lets cooperation win.

# Scored after run 1 (2026-11-09)
R1 PASS: lone simple survives (share 0.45, E 9.1); lone complex dissolves.
R2 FAILED: the hypercycle of four L=100 members dissolved (all members 0, junk 1.0), even with no parasite.
   Reason found after the run: in a closed, normalised arena a member must out-copy the population average, and with fidelity 0.37
   no level of help suffices (the steady-state equation has no positive root). The model set the task wrong: Eigen's actual claim is
   NOT that cooperation rescues members that are each too long, but that several members, each short enough to be copied, can together
   hold more information than any single replicator could.
R3, R4 not informative (nothing to protect). Spatial control without parasite also died.

# Pre-registered BEFORE run 2 (Eigen's claim stated correctly)
Same arena. Compare (a) ONE long pattern of length 200 (q=0.13; must dissolve) with (b) a hypercycle of 4 members of length 50 each
(q=0.61; together 200 symbols). Parasite and spatial setup as before, with members L=50.
R2': the hypercycle persists and carries E > 9.1 (the lone simple pattern); the single L=200 pattern dissolves.
R3: in a well-mixed arena the parasite destroys the hypercycle.
R4: in the spatial arena the hypercycle survives the parasite in at least 5 of 10 runs.

# Scored after run 2
R2' PASS: hypercycle of four L=50 members persists (0.102 each, junk 0.59), E = 20.5 vs 9.1 for the lone simple pattern; the single
   L=200 pattern dissolves. Cooperation lets the arena hold more structure than any lone replicator.
R3 PASS: well-mixed + parasite: all members -> 0; parasite 0.64.
R4 NOT INTERPRETABLE: the spatial model failed its own control (hypercycle died with no parasite too). The spatial rules, not the parasite,
   were killing it.

# Pre-registered BEFORE run 3 (procedure fixed in advance)
Tune ONLY the spatial arena's death rate / empty weight / catalysis scale on the parasite-FREE control (3 seeds) and take the first
setting in the list [(0.1,0.5,1),(0.1,0.5,2),(0.05,0.3,2),(0.05,0.3,4)] where the hypercycle survives 3/3. Then, with that setting
frozen, run the parasite test on 10 NEW seeds (100-109). R4 prediction unchanged: survives in at least 5 of 10.

# Scored after run 3
No setting passed the parasite-free control. Diagnosis (shares over time): junk (perfectly copied, rate 1) fills the grid; members fall
from 0.20 to 0. In our spatial rules, copy errors plus local crowding defeat the cycle even without a parasite. R4 NOT ESTABLISHED.

# Pre-registered BEFORE run 4 (code validation against the literature)
Boerlijst-Hogeweg's spatial result assumes error-free copying. Run the same spatial code with errors OFF (all fidelities 1, no junk),
setting (0.1, 0.5, 1). Control (no parasite, 3 seeds) must survive; then parasite test on seeds 100-109.
Prediction: hypercycle survives the parasite in >= 5/10 (reproducing the known result). If not, our spatial code does not reproduce
the literature and no spatial conclusion is drawn.

# Scored after run 4
Control (errors off, no parasite): survives 3/3. Parasite test: full cycle survives in 0/10 (members 0.19 of the grid, parasite 0.68).
Our spatial code does NOT reproduce the Boerlijst-Hogeweg parasite resistance. As fixed in advance, no spatial conclusion is drawn.
Established by this study: (1) under copy errors a cooperating cycle holds more structure (E 20.5) than any lone replicator (9.1; a
single long pattern dissolves); (2) in a well-mixed arena a free-riding parasite destroys the cycle. Open: whether local, finite-speed
copying protects cooperation; our model could not test it.

# Pre-registered BEFORE bh.py (faithful-as-possible Boerlijst-Hogeweg, from memory of the 1991 model)
Rules: grid 100x100; empty or species 1..n (n = 6, since spirals need n >= 5), parasite P. Each step: decay d = 0.2; an empty cell x is
claimed by neighbour y of type s with weight k + K*(number of s-1 around y), k = 1, K = 100; staying empty has weight 11; Margolus
block-rotation diffusion once per step. Parasite: supported by species 1 with K_p = 150, supports no one, seeded into 1% of cells at t = 300.
V1 (validation): without parasite the 6-cycle survives 3/3.
V2 (validation, the literature result): with parasite the 6-cycle survives in >= 5/10 runs. If V2 fails, our model is still not faithful
   and no conclusion is drawn about space.
E (only if V2 passes): copy errors on (member fidelity q, errors become junk that replicates with weight k = 1 and is never catalysed);
   exploratory, no prediction for q = 0.9 and q = 0.6; reported either way.

# Scored after bh.py
V1 PASS: 6-cycle without parasite survives 3/3 (members ~0.79 of the grid).
V2 FAILED the pre-registered bar: with parasite the full 6-cycle survives in 3/10 (members 0.27, parasite 0.32 on average).
   Below the >= 5/10 needed to count as reproducing the literature, so, as fixed, no conclusion about space. Observed, not claimed:
   3/10 survival versus certain collapse in the well-mixed arena. E (errors on) not run, as fixed in advance.
Likely reason (not tested): our parameters (parasite strength, diffusion rate, update scheme) are recalled, not taken from the paper.

# Pre-registered BEFORE bh_pde.py (published parameters, not memory)
Source: the reaction-diffusion version of Boerlijst-Hogeweg in q-bio/0406035 ("Spatio-temporal dynamics in the origin of genetic
information"): dX_i/dt = -delta X_i + (1 - sum X)(rho + kappa X_{i-1}) X_i + D lap X_i; delta = 1, rho = 2, kappa = 500, D = 1;
grid 147 x 147, Neumann boundaries, D dt/dx^2 = 0.1, extinction threshold 1e-3. Parasite = species 7, supported by species 6 with
kappa_76 = 530, D_7 = 1, supports no one (their Fig. 2).
S1: the 6-species hypercycle persists (every species domain mean > 1e-3) and forms waves (spatial variance of X_1 > 0).
S2 (well-mixed control): the same equations on a single site (no space): the parasite takes over and the hypercycle collapses.
S3 (decisive): with space, parasite introduced after the waves have developed (their case B) is driven out (X_7 max < 1e-3 at the end)
   while all 6 members persist. One run, seed fixed; a second seed as replication.

# Scored after bh_pde.py
S1 PASS: 6-cycle persists with waves (member means ~0.10-0.12 each; spatial variance of X1 0.04), both seeds.
S2 PASS: well-mixed: all members -> 0, parasite 0.50.
S3 FAILED: with space, parasite seeded after development took over (mean 0.36, max 1); member 2 extinct, 3 and 4 near extinct; both seeds.
Possible protocol mismatch (stated, not tested): we seeded the parasite throughout the domain, including spiral cores (0.01 wherever
X6 > 0.01), whereas "invasion" in the source may mean entry from outside a developed spiral. Not adjusted after the fact.

# Pre-registered BEFORE bh_edge.py (last attempt; stop rule fixed)
Same published equations and parameters as bh_pde.py. Only change: after development (t = 1500) the free-rider enters from OUTSIDE,
as a strip along the left edge (columns 0-4, X7 = 0.01), instead of being seeded everywhere including spiral cores.
S3': the free-rider is driven out (X7 max < 1e-3 at t = 3000) while all 6 members persist (each domain mean > 1e-3), in both seeds.
Stop rule: if S3' fails, we record that we could not reproduce spatial protection and stop this line.

# Scored after bh_edge.py
S3' FAILED: free-rider entering from the edge was not driven out in either seed (mean 0.37 and 0.32, max 1). Seed 0: members 2 and 3
extinct. Seed 1: all six members persist alongside the free-rider (means 0.03-0.10): coexistence, not expulsion.
Per the stop rule: we could not reproduce spatial protection of the cooperating cycle. This is a failure to reproduce, not evidence
that the published result is wrong (our time integration, initial conditions and run length may differ from the source).
Observed, not claimed: in one of two spatial runs the full cycle coexisted with the free-rider; in the well-mixed arena it never did.

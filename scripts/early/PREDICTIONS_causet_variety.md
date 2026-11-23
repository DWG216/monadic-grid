# Pre-registered before running causet_variety.py (2026-11-10 ~16:55 ET). Label: math (computational pilot).
Question: does a growth rule enacting Leibniz's identity of indiscernibles (maximal variety) grow more spacetime-like causal sets than
transitive percolation?
Size 256 events, 5 runs per rule.
Rules: A transitive percolation (link prob p, then close the order). B-strict: each new event is offered 30 candidate pasts (random
link sets with link probability drawn uniformly in [0.02, 0.5], each closed to a consistent past) and takes the one whose past is
farthest (Hamming distance) from every existing event's past (maximise the minimum). B-soft: same, chosen with probability ~ exp(5 x
normalised min distance). Matching: A's p is set by bisection so its ordering fraction matches B-strict's mean.
Controls: + random sprinkles into 2D, 3D, 4D Minkowski diamonds (spacetime-like); - random three-layer orders (Kleitman-Rothschild type).
Measures: (1) d_MM, dimension from the fraction of related pairs; (2) d_mid, dimension from midpoint scaling of the largest interval;
(3) abundance distance: L1 distance between the profile of intervals with 0..5 interior events and that of a sprinkle of the nearest
integer dimension (2, 3 or 4) at the same size; (4) height (longest chain).
Score S = |d_MM - d_mid| + abundance distance (lower = more spacetime-like).
P1: controls behave: sprinkles have S below every three-layer order's S; three-layer height = 3.
P2 (decisive): mean S of B-strict < mean S of A (matched ordering fraction).
P3: B-strict never yields height <= 3.
Exploratory: which dimension B settles near, if its estimates agree.

# Scored after run (2026-11-10)
P1 PASS: sprinkles S = 0.07 (2D), 0.15 (3D), 0.14 (4D), dimensions recovered (d_MM 1.96/3.11/3.90, d_mid 2.01/3.17/3.97); three-layer
   orders S = 4.79, height 3.
P2 FAILED: B-strict S = 0.78 vs matched percolation (p = 0.082) S = 0.67. Maximal variety did not beat random growth.
P3 PASS: B-strict height 244-252 of 256 (never layered).
Exploratory: B-strict and B-soft grow near-total orders (related-pair fraction 0.76 and 0.93; the longest chain holds ~97% of events;
   dimension ~1.1-1.4). Reason: the easiest way to make every past different is to make each past contain all the earlier ones, so
   distinctness by inclusion produces a single line of time with almost no space. Identity of indiscernibles alone selects TIME, not
   spacetime. The matched percolation runs sit in the same near-chain regime, so P2 compared two degenerate cases.

# Pre-registered BEFORE coexist.py (test 1: distinctness of coexisting events)
Rule C (Leibniz in full: time = order of succession, space = order of coexistence). New event, candidate past S (same 30 candidates
as before). Events in S are its predecessors: their pasts may be contained in S (succession). Events NOT in S coexist with it: each
must differ from it, scored by Jaccard distance between S and that event's past. Score(S) = minimum Jaccard distance to any
coexisting event; a candidate with no coexisting events scores 0 (no space at all). C-strict takes the best candidate; C-soft weights
by exp(5 x score). Same size (256), seeds, measures, controls and score S as before; percolation matched to C-strict's ordering
fraction.
P2': mean S of C-strict < mean S of matched percolation.
P4: C-strict is neither a chain nor layered: 3 < height < N/2, and its two dimension estimates agree within 0.5.
Exploratory: the dimension C settles near.

# Scored after coexist.py
P2' FAILED: C-strict S = 0.40 vs matched percolation (p = 0.197) S = 0.34.
P4 FAILED: C-strict is again a near-total order (height 255-256 of 256; dimensions ~1.0-1.1).
Diagnosis (after the run, stated as such): two events with identical pasts are indiscernible if only pasts count, and at birth all
pasts are empty or nearly so. So the rule forbids a second "first" event and forces succession from the start. Once the set is a
chain it can never leave: in a total order every consistent past is a prefix, so no candidate can create coexistence. The
principle, applied to pasts alone, permits only time.
Lesson: Leibniz's indiscernibility concerns ALL relations, future as well as past. Two events with the same past can still be told
apart by different futures. A faithful rule should let new events resolve the indiscernibility of earlier ones.

# Pre-registered BEFORE fullrel.py (rule D: indiscernibility over ALL relations)
Each event's profile = its past and its future. Distance between two events = number of events in which their profiles differ.
Variety deficit V = sum over pairs of 1/(1 + distance) (near-identical pairs cost most; identical pairs cost 1).
Each new event takes, from the same 30 candidate pasts, the one that leaves V smallest after it is added (it may split earlier
near-identical pairs by lying above one and not the other). Same size, seeds, measures, controls; percolation matched in density.
Predictions (as stated to the user): D1 coexisting branches survive: height < N/2; D2 the two dimension estimates agree within 0.5;
D3 mean S of D < matched percolation.

# Scored after fullrel.py
D1 FAILED: height 246-250 of 256 (a near-chain). D2 FAILED: d_MM 1.54 vs d_mid 0.90. D3 FAILED: S 0.87 vs matched percolation 0.77.
Across three formulations (pasts, coexisting pasts, full past+future profiles) maximal distinctness grows near-total orders.
Reading: a total order is the most discernible structure possible (every element unique, no symmetries), so pure indiscernibility
selects a line of time. Spacetime is the opposite in one respect: it is full of near-identical, symmetric events (homogeneity,
isotropy, Lorentz symmetry). Caveat: all comparisons here sit in a dense regime (related-pair fraction ~0.7-0.9, 4D spacetime ~0.1),
partly set by the candidate generator.

# Pre-registered BEFORE leibniz2.py (Leibniz's full criterion: variety + order, equal weight; stop rule applies)
Variety term: V after adding the candidate (as in rule D; lower = more variety).
Order term (homogeneity, "the same everywhere"): |links(candidate) - mean link count of existing events| / (mean + 1), where links =
the newcomer's immediate predecessors (maximal elements of its past). Lower = the newcomer looks like a typical event.
Choice: among the same 30 candidates, standardise each term across the candidates (z-scores) and take the candidate with the smallest
sum. Equal weight, fixed now, not tuned. Same size, seeds, measures, controls; percolation matched in density.
E1: height < N/2. E2: the two dimension estimates agree within 0.5. E3: mean S < matched percolation.
Stop rule: if E3 fails, this line ends with "Leibniz's criterion, in this form, does not grow spacetime-like causal sets."

# Scored after leibniz2.py
E1 FAILED: height 237-247 of 256. E2 FAILED: d_MM 1.51 vs d_mid 0.89. E3 FAILED: S 0.85 vs matched percolation 0.74.
Stop rule applied: Leibniz's criterion, in this form, does not grow spacetime-like causal sets. Line closed.
Unresolved confound (noted, not chased): every run, including matched random growth, sits in a dense near-chain regime (pair fraction
~0.7 vs ~0.1 for 4D) created by the candidate generator; the principles were only ever choosing among chain-prone options.

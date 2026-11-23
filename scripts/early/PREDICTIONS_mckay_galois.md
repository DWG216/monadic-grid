# Pre-registered before running mckay_galois.py (2026-11-08 ~23:50 ET)
Question asked: do the Galois pairs of 2I (2/2', 3/3', 4/4') line up with the Monster's paired classes (2A/2B, 3A/3C, 4A/4B) on affine E8?
Honest pre-check: as stated this CANNOT fail. Affine E8 marks equal 2I dimensions, Galois pairs have equal dimensions, and the Monster pairs are
exactly the nodes with equal marks. So the alignment is built in. We register a sharper version that can fail.
M1 [math, 2I side]: the Galois swap s (sqrt5 -> -sqrt5) is a symmetry of 2I's representation ring: tensoring with 2' instead of 2 gives the
   SAME affine E8 shape, with every node relabelled by s (2<->2', 3<->3', 4<->4'; 1, 5, 6 fixed).
M2 [the real question, Monster side]: if the Monster's pairing were the same Galois twin, 2B would play 2A's role: products of two 2B
   involutions would also have orders <= 6 and land in the swapped E8 classes. Prediction (from what is known about the Monster):
   this FAILS: 2A involutions are 6-transpositions (Conway-Norton / Fischer), 2B involutions are not. If so, the Monster's E8 is not
   Galois-symmetric the way 2I's is, and the grid's "same E8 via the Galois twist" hypothesis is undermined.

# Scored (2026-11-08)
M1 PARTIAL: graph(tensor 2') = swap(graph(tensor 2)) holds exactly. But the Galois swap (7th power map) exchanges only 2<->2' and 3<->3';
   4 and 4' are each FIXED (4 is spinorial, 4' is not: they differ by the central sign, not by sqrt5). Our earlier statement "4/4' are Galois
   partners" was wrong.
M2: we could not obtain the Monster character table here (no GAP; repository access unavailable), so the 2B-product version was not run.
   Substitute argument (from memory, flagged): Out(Monster) = 1, and all nine E8 classes (1A 2A 3A 4A 5A 6A 4B 2B 3C) are rational, so no
   automorphism or Galois action of the Monster moves 2A<->2B or 3A<->3C. Literature (Lam, kokyuroku 1656): equal-order classes are
   lettered by centralizer size; the E8 correspondence is one-to-one, while the E7 (Baby Monster) and E6 (Fi24) ones hold only up to
   diagram automorphisms.
VERDICT: grid hypothesis "the Monster's E8 is the sky frame's E8 seen through the Galois twist" is UNDERMINED (no twist on the Monster side).
Survives (known math): the ladder 2T/2O/2I <-> affine E6/E7/E8 <-> Fi24'/Baby Monster/Monster.
New observation, to test: the sporadic match is one-to-one exactly on the rung whose binary group is perfect (2I, no 1-dim reps -> affine E8
   has no diagram automorphism); 2O and 2T have 1-dim reps, whose tensoring gives the diagram automorphisms that blur E7 and E6.

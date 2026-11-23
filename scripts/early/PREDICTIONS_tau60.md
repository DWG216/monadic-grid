# Pre-registered before running tau60.py (2026-11-08)
Source: Kubischta & Teixeira, arXiv:2305.07023: tau60 = (1/sqrt(5phi+7)) [[i(2+phi), 1+i], [-1+i, -i(2+phi)]], the one "expensive" gate
added to the transversal group 2I (super golden gate set, Parzanchevski-Sarnak).

Conceptual point fixed in advance: magic is relative to what is free. In the Clifford world the free states are the 6 octahedron
points. In the icosahedral-code world the free gates are 2I, and |0_L> is an icosahedron vertex, so ALL 12 vertices are free
(2I images of |0_L>). Our earlier "vertex distillation" (threshold 0.305) therefore refined states that are magic only from the
Pauli point of view, not from the code's own point of view. That result stays true but is re-labelled.

U1 [identity]: tr(tau60)=0, so tau60 is a 180-degree rotation; axis n_tau ∝ (1, 1, phi^2+1) (sign aside). Its injection state is
    its eigenstate |tau> along n_tau (same pattern as H, a 180-degree rotation about (1,0,1), with the H-type state as its eigenstate).
U2 [geometry]: n_tau lies on no symmetry axis or mirror plane of the icosahedron; the +-orbit under the 60 rotations has 120 points.
U3 [identity]: the 2I orbit of |0_L> (logical frame) is exactly the 12 logical icosahedron vertices.
U4 [real test, prediction]: the 7-qubit icosahedral code does NOT distill tau-class states: projecting 7 copies of |tau> does not
    return a tau-class state, and noisy tau inputs never improve. Expected fixed points of the code's pure-state map lie only on
    symmetry axes (5-fold vertices, 3-fold face centres, maybe 2-fold edges).
U5 [real test]: among the fixed points, the ones that are NOT free in the 2I world (face centres / edges, if attracting) are the
    code's genuine magic states. We report their threshold under ideal noise (expect lower than 0.305).
U6 [hardware noise, stated model]: per-qubit depolarizing p_pre = k*p2 before projection and p_post = k*p2 after (then ideal
    single-error recovery), false-accept probability p_m. k = 6 (assumed two-qubit gates touching each qubit; the code is not a
    stabilizer code, so the projection circuit is not standard: this k is a guess and is labelled so).
    Hardware levels: p2 = 1e-3 (best current), 3e-3 (typical), 1e-2 (early). p_m = 5e-3.
    Prediction: hardware noise puts a floor under the output error of order k*p2*(small constant) for both codes; the
    icosahedral code's advantage in raw-state cost shrinks but survives at p2 = 1e-3.
Control: input = maximally mixed must give maximally mixed output (no magic from nothing).

# Scored after run (2026-11-08)
Frame correction logged mid-run: first U4 compared outputs to the PHYSICAL icosahedron; redone against the LOGICAL one (all 4 tau/tau' pairings).
U1 PASS: trace 0; axis (1,1,phi^2+1)/sqrt(7+5phi) = (0.2574,0.2574,0.9314); 21.9 deg from nearest vertex, 15.9 from face and edge.
U2 PASS: 120-point orbit; nearest mirror |n.normal| = 0.049 (close, not on it).
U3 PASS (logical frame): |0_L> orbit = 12 logical icosahedron vertices.
U4 PASS: tau60 state is not distilled (exponent 1.00, output = input to first order; noiseless image 0.144 off the tau class).
U5 PARTLY FAILED: face and edge classes are fixed but repelling. The non-free attracting classes are generic: one on a mirror
   (16.2534 deg from a vertex, cos^2 = 0.921664) and a chiral pair (16.2636 deg, azimuth +-12.007 deg). Thresholds 0.225 (lower than 0.305 as
   predicted) BUT suppression is only LINEAR (factor 0.57/round): 29 rounds, ~1e41 raw states to go 1e-3 -> 1e-10. Not usable distillation.
EXTRA: transversal CNOT/CZ between two blocks leak (0.97/0.99): no cheap entangler inside this code.
U6 MIXED: floors ~ 0.06*k*p2 for BK (as predicted). For the only non-free icosahedral classes the advantage does NOT survive at any p2.
RETRACTION of push.py's headline: the 59-100,000x saving refined vertex states, which are free in the 2I world. True as arithmetic, irrelevant to universality.

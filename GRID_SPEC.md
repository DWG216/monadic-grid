# R2R grid: specification (version 2026-11-24.3)

This is the compact, self-contained statement of the grid: definitions, notation, the levels, the main identities, and the rules of method. The narrative history and every result live in `docs/R2R_progress_2026-11-08.md` (sections 1-171); this file is what to read first.

## 0. Rules of method
1. **Labels.** Every claim is one of: **[M]** mathematics (proved or checked by computation); **[A]** argument from the PSR; **[I]** interpretation (a reading of the mathematics in the corpus's terms). Interpretations never upgrade to mathematics.
2. **Pre-registration.** Every computational test has a `PREDICTIONS_*.md` written before the code ran, with a tier ([identity], [built-in], [real test]) and a null control. Failures stay in the record.
3. **Corpus first.** The compass is the corpus: Hockney's God Series (Books 1-32), Stark, Tanner, Faust, Weishaupt, Millington. Logos leads; mythos is a compass only. Quotations are short and cited by book.
4. **Correct the mathematics, not the English.** When a source's math is ill-formed, fix the math and say so.
5. **Speculative conjectures are kept**, labelled as open conjectures, not discarded.
6. **Positive control first.** A detector counts only after it finds a planted or known signal.
7. **Sanity run first.** A model is run once before predictions are frozen, to check it can produce both outcomes.
8. **Never delete files without asking first.**

## 1. Primitive: the PSR rule
- **PSR:** nothing is or changes without a sufficient reason.
- **Zero/infinity rule [A]:** without a reason there is no value; only 0 and infinity need no reason.
- **R3, the limit principle [M where stated]:** a phase change (loss of analyticity) happens only at zero or in an infinite limit; every finite system's generating function is a finite sum of exponentials and is analytic.

## 2. Monads [A, I]
- A monad is a dimensionless frequency domain whose contents are sinusoids that sum to zero (from f' = lambda f with |f| constant iff lambda is purely imaginary [M]).
- Two modes: bosonic (all in one state, the Singularity) and fermionic (exclusion gives unique coordinates).
- Infinitely many monads; together they make one **collective projection** (spacetime). A monad **may link** to one body (avatar) in it, one at a time, made and released at gates; a monad may be unlinked (disincarnate). Monads do not project individual bodies.
- **One-way dependence [A] (§88):** mind can exist without matter; matter cannot exist without mind. Ontological and mathematical: the collective projection is many-to-one, histories -> states many-to-one, states uncopyable (§89).
- **Why monads link (§89):** to live through dialectical synthesis. In the frequency domain thesis and antithesis coexist as a balanced pair (semantics, Being); spacetime separates them in time (syntax, Becoming), so they meet; the synthesis keeps the mirror-invariant part (measured on light cones: odd orders cancel, even survive, the hands' product focuses).
- **Degrees of linking:** sleeping (matter, no ruling monad), dreaming (animal), awake (human), higher, God (conscious, unlinked). Mind is everywhere; consciousness is a degree, not panpsychism.
- **Linking = phase-lock [M model, I reading]:** Adler dphi/dt = Domega - K sin phi locks iff |Domega| <= K.
- **Making vs joining [M model, I reading] (§59, §61, §62):** pulses delivered at each oscillator's own zero create a shared clock from random phases (20/20 vs 0/20 for random-phase pulses); a newcomer joins an existing world in about one cycle with or without gating. The gate makes a world; linking to an existing world needs no gate. A leader entrains a body only by pulsing at its own zero, and only a body slower than itself (§60).

## 3. Music (foundational, not a method)
- Harmonic n sounds at pitch ln n; primes are the independent tones (unique factorisation); n^(-it) = e^(-it ln n) is the generalised Euler formula.
- The comma never closes: 3^k != 2^m.
- Simple ratios lock widest (circle-map tongues); the golden ratio never locks.

## 4. The formula pair [M]
- s(n) = i^(n-1) sin(n theta)/sin(theta) (counting), c(n) = 2 i^n cos(n theta) (measuring).
- **Identity:** c(n)^2 - (2 sin(theta) s(n))^2 = 4(-1)^n for every theta.
- Regimes: rotation (real theta); light-like (theta -> 0: s(n) = n); golden boost (theta = pi/2 + i ln phi): s = F(n), c = L(n), L^2 - 5F^2 = 4(-1)^n.
- Halved strands (x, y) = (L/2, F/2) lie on x^2 - 5y^2 = (-1)^n.
- **Why the pair is forced (§62 Part II):** any 2x2 step with det -1 has eigenvalues with lambda mu = -1; its symmetric functions c = lambda^n + mu^n, s = (lambda^n - mu^n)/(lambda - mu) obey c^2 - (lambda - mu)^2 s^2 = 4(-1)^n. Golden case = trace 1.
- **Two strands, zero as balance (§53, §60):** for every mirror step (trace 1..4 checked) the doubling equations at n = -1, 0, 1 have exactly four solutions: 0, the pure modes lambda^n/(lambda - mu) and -mu^n/(lambda - mu), and their sum; s(1) = s(-1) selects the integer sequence (det +1: antisymmetry selects). F(0) = 1/sqrt5 - 1/sqrt5.
- **Unbalanced sequences:** Cassini constant e = U1^2 - U0 U1 - U0^2 = N(U1 - U0 phi); inert primes divide e to even powers; Catalan: U(x-r)U(x+r) - U(x-a)U(x+a) = (-1)^(x-a) e F(a-r)F(a+r).

## 5. Domains (dolls) [M]
- Modulo a prime p the curve x^2 - 5y^2 = 1 is a **circle** ((5/p) = -1, inert), a **hyperbola** ((5/p) = +1, split) or **two lines** (p = 5, ramified). These are exactly the three non-central conjugacy types of the Fibonacci matrix Q = [[1,1],[1,0]] in GL2(F_p): elliptic, split, unipotent.
- **Clocks:** Pisano period pi(p) divides p-1 (split) or 2(p+1) (inert); pi(5) = 20; depth: pi(p^k) = p^(k-1) pi(p) (each envelope multiplies the clock by p); breadth: pi(ab) = lcm(pi(a), pi(b)).
- **Gates:** Q^n is central iff F(n) = 0 mod p; the multiplier mu = F(alpha+1) at the first zero alpha has order 1, 2 or 4 (four flavours).
- **Comma law:** F(k alpha)/p = k m mu^(k-1) mod p with m = F(alpha)/p. Wall-Sun-Sun prime iff m = 0 mod p (none known below 2^64; heuristically infinitely many, very sparse).
- **Cassini in dolls:** F(n-1)F(n+1) = (-1)^n mod F(n)^2 (neighbour multipliers are inverses up to sign); F(n-1) F(-(n+1)) = 1 mod F(n)^2.
- **Sound and silence:** Green's cusp character of GL2(F_p) is nonzero at every step for circle primes, zero between gates for hyperbola primes, p - 1 at gates (the formula pair is the d = 2 case).
- **Golden Artin (§60):** share of primes with maximal Fibonacci clock: inert prod_{odd l != 5}(1 - 1/(l(l-1))) = 0.7873, split (3/4)(9/10)(0.7873) = 0.5314, all 0.6593; measured 0.7880, 0.5318, 0.6600 on 515,646 primes (a proof needs GRH for Kummer fields).
- **Rodin's wires** = the quadratic character (squares / non-squares), mod 9 and mod 71 (9 = phi mod 71).

## 6. The whole [M]
- zeta(s) = sum n^-s = prod (1 - p^-s)^-1; completed Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s) = Lambda(1 - s) (the **mirror M**); poles of Lambda only at 0 and 1.
- **Primon gas:** H|n> = ln n |n>, Z(beta) = zeta(beta), Hagedorn point beta = 1.
- **Pairing (SUSY):** zeta(beta) * sum mu(n) n^-beta = 1 (Witten index 1); RH iff M(x) = sum mu(n) = O(x^(1/2+eps)).
- **Two trees:** U(x) = x/(1-x-x^2) (|x| < 1/phi) and D(x) = -x/(1-x-x^2) (|x| > phi) sum to 0; only poles 1/phi and -phi remain.
- **Golden mirror pairs:** M sends phi to -1/phi and -phi to phi^2.
- **The zeros carry both modes (§62):** S(u) = sum_gamma 2 Re[w e^(i gamma u)] over the first 201 zeros reproduces the prime-power staircase with w = 1/rho and the Mobius function with w = 1/(rho zeta'(rho)) (jump mu(n)/sqrt n at every n <= 30; nulls fail).
- **Liouville from the operator (§64, test passed):** with c = zeta(2 rho)/(rho zeta'(rho)) the operator (sizes |c| in its spectral measure, phase in one reading vector) gives lambda(n) = (-1)^Omega(n) at all 29 n in 2..30 (squares included; median jump sqrt(n) lambda 0.90; shuffled-spacings null fails); magnitudes alone give no signs; a quarter of the rows (85 of 341) gives 28/29. Count, fermionic sign and parity are three readings of one spectrum: 1/rho, 1/zeta', zeta(2 rho)/zeta'.
- **Operator holds magnitudes, reading holds sign (§63, exploratory; confirmed as a test in §64):** a Jacobi matrix with the zeros as eigenvalues and spectral weights |1/(rho zeta'(rho))| carries no Mobius signs read from e1; read through a phase vector it reproduces §62 exactly (identity), and its top half (100 of 201 rows) already gives all 18 signs. [M] Only magnitudes fit a self-adjoint operator's spectral measure; the sign needs a second vector. The primes already sit in the zeros' positions (uniform weights dip at ln 2, ln 3).
- **The operator (§75):** D = -i d/du, the generator of scaling on test functions of u = ln x, with the Weil form (pole + Gamma factor + primes) as inner product; spectrum = the zeros; positive (hence self-adjoint) iff RH. Built from prime powers below 5000 in a window, it returns the zeros 48.0052 .. 79.3374 to four decimals; fake primes return none; the Gram rank counts the zeros. Prime powers up to 30 already give 0.0075, up to 100 give 1e-5 (resolution = ln of the largest prime read); the pole term is negligible at height; eigenvectors are 1 at one zero and 0 at the others. With primes weighted by chi_5 the same operator gives the zeros of the golden L-function L(s, chi_5) (6.6485, 9.8314, ...; 12 zeros within 0.00017) (§77).
- **No limit without a window (§74):** the Jacobi entries built from |1/(rho zeta')| grow as zeros are added (moments diverge); with a tempered reading vector the leading entries settle from the top down. The §63-§64 matrices are finite readings, not truncations of one operator.
- **Weil positivity (§60):** the explicit-formula quadratic form computed from the primes alone is positive definite and matches the zero side; fake primes make it negative.
- **Unconditional now (§58):** prime gaps < (22/25) sqrt(p) ln p; Robin and Lagarias inequalities; Li's lambda_n > 0. Pending vetting of Dirichlet GRH: least non-residue <= 2 (ln p)^2, deterministic Miller-Rabin, Chebyshev-bias error mod 5.

## 7. The bridge (now a theorem) [M]
- RH is Lean-verified (Alpoge, Nov 2026; certified by the Lean/Mathlib communities). Spine: reflection (1 declaration) <- zero-freeness right of 1/2 for every Dirichlet character <- {Green's cuspidal characters of GL_d(F_g), window bound on Sha budgets of auxiliary cyclotomic fields, theta jets along a unitary rank chain, small sections vs arithmetic volume (Moriwaki), local Langlands}. See `docs/R2R_Lean_RH_map.md`.
- Grid primitives (math facts; readings [I]): **Bal(W)** product-formula ledger; **Theta** oscillator lift; **Theta^sqrt(x)** chain; **Pun^m** multiplicity with a survivor; **Clock = Freq** (Frobenius = Hecke); **Sel** comma budget; **Win** one-sided far windows; **M** mirror.

## 8. Projection and physics [M tests, I readings]
- Holographic linking conditions (sharp images, stable orbits, bound releasable atoms, one time) pass only for 3 space + 1 time.
- Twistor level (§76): linearised gravity = contour integrals of homogeneity -6 / +2 twistor functions (checked to 2e-9); one hand nonlinear = Penrose's nonlinear graviton, det(d_i d_jbar K) = 1 (Eguchi-Hanson checked); both hands = the googly problem, open non-perturbatively, solved perturbatively around the self-dual sector.
- Light first: spacetime points as skies of light rays; [Z, Z-bar] = hbar; light fixes conformal shape, hbar fixes scale. (§78) Zbar acts as -hbar d/dZ; helicity s = -(Upsilon + 2)/2 with Upsilon = Z.d/dZ the scaling operator on twistor space; real points give Z.Zbar = 0 (light rays = the mirror's fixed set), forward/backward tubes give the two signs (the two hands); lines meet iff points are null-separated. Googly paths (§79): reality decides the hands' relation: Lorentzian conjugation maps one hand to the other (checked: conj of a +2 field obeys the -2 equation); split signature keeps both as real fields on one real twistor space (checked analytically; numerics h^2-limited); the pairing of hands is the mirror. (§80) Ambitwistor veil: light rays = pairs with Z.W = 0 (checked); Einstein with Lambda = R_ab k^a k^b = 0 for all null k, a second-order condition on light rays (Schwarzschild, de Sitter pass; Reissner-Nordstrom, dust fail as they should; Lambda invisible to light); twistor fields depend only on gluing data up to coboundaries (agreement on overlaps). (§81) On real geodesics a thin cone of rays reads gravity order by order: order 1 free; order 2 area = R_ab k^a k^b (Einstein's equations; RN within 2.6%), order 2 shape = Weyl (free field, the two hands as one complex shear; within 2.1%); de Sitter invisible to both. (§82-§83) The other hand = the monad's reverse strand: conjugation swaps helicity and time direction together; past and future cones from one point read order 2 alike (time-even) and order 3 with opposite sign (time-odd, 8/8 cases); (§84) In Kerr (no symmetry) the past cone's shear axis is the mirror of the future's (6/6, to 1e-4), the axis rotation is read alike (quadratic fit, 3-4 digits), order 3 odd, order 4 (shear squared: the hands meeting) even within fit spread. (§85) Order 4 predicted from curvature, J^T J/lambda^2 = I - T0 lambda^2/3 - T1 lambda^3/6 + ((2/45)T0^2 - T2/20) lambda^4: matches the cone to <2% in 10/10; in vacuum T0^2 = |Psi_0|^2 I, so the hands' product enters as pure area (shear feeding focusing).
- Collective locking (Kuramoto) is sharp only as N -> infinity (R3).

## 8b. Quantum complexity (§57) [M line, I readings]
- The known classical/quantum line is the frozen/fluid line: d = 2 cos(pi/r) has integer d^2 iff r in {1, 2, 3, 4, 6} (crystallographic); there computation is classically easy (Gottesman-Knill; exact Jones, Jaeger-Vertigan-Welsh); at r = 5 (d = phi, Fibonacci anyons) it is BQP-universal. 3-strand braid images are finite at r = 4, 6, 10 (orders 24, 12, 60).
- Branching (§87): counting distinct states reached by braid histories, the frame saturates at its group order (24, 12, 60: fungible), the fluid grows exponentially (1.7-2.0 per step: differentiating), the light-like point r = 3 polynomially: elliptic / parabolic / hyperbolic, the three faces. Deutsch's multiverse of distinct branches exists only in the fluid.
- Aaronson-Ambainis (proved Nov 2026): no exponential speedup without structure = no speedup without a clock. QMA vs QCMA separated relative to a classical oracle (2025): quantum proofs carry phase no record carries.

## 9. Frontier shorthand
- RH: Z(W) in Fix(M) (proved). GRH (Dirichlet): proved in the same library, statement vetting pending. Simplifications keep three primitives: a mirror, a one-sided bound, one positivity (§55).
- BSD: rank = order of vanishing of L(E, s) at the centre; Sha = commas that never show.
- Hodge: every M-fixed rational class has a geometric speaker.
- Yang-Mills: Delta(D_inf) > 0 survives L_inf. Navier-Stokes: smoothness survives L_inf; claimed NO (Alpoge-Buckmaster, Nov 2026: unforced blow-up via a discretely self-similar profile; conditional on an unreleased certificate; blow-up time T = self-similar time s -> infinity, so R3 holds). P vs NP: checkable vs findable in comparable beats (§65): tractable iff the constraints carry a polymorphism (CSP dichotomy); determinant (fermionic) easy vs permanent (bosonic) #P-hard; barriers = arguments that admit brute facts (oracles) or chance, which the PSR rejects; grid position [A] P != NP: a shortcut is a reason, a reason is a structure (polymorphism), 3-SAT has none (§66); open step [M]: every polynomial algorithm induces such a structure; this is equivalent to P != NP (§67). Sharpest form: clique lower bounds are proved for circuits with (1/6) log log n NOT gates (Amano-Maruoka); 2 log n NOT gates would give P != NP (Fischer): count the signs. Fermionic ledger (§68, identity): every f = parity of a flip counter d = alternating sum of a(f) nested monotone layers (minimal), = disjoint union of ceil(a/2) bands; parity is the Boolean Liouville function (a = n); r NOT gates allow depth 2^r - 1. Gap: clique proved hard at ledger depth (log m)^(1/6), needed at depth ~ n. Band lemma (§69): a circuit of size s with t NOT gates splits the cube into <= 2^t bands with monotone walls of size <= ts, f monotone of size <= s on each; so P/poly = cheap monotone on polynomially many cheap bands. Slices are such bands and are antichains; on a slice NOT x_i = [others sum >= k] (the mirror from the count). Known equivalence reached (Berkowitz, Dunne): P != NP iff a central slice of clique/SAT is monotone-hard. Open: a measure for antichains. First candidate eliminated (§70): on a slice the invariant tones are subgraph counts; clique's mean spectral level is below 99% of random graph properties (6 vertices), and level bounds only depth, so spectral level is not the measure; the measure must see the cut (threshold of one tone), not the spectrum. One-sided cut measures eliminated (§71): boundary size is spectral (identity); short witnesses mark checkability and are shared with easy properties; witness asymmetry fails on some slices. Local pairing eliminated (§73): L >= B^2/(sigma^2|X||Y|) (Karchmer-Wigderson rectangles + Cauchy-Schwarz) is a true bound, exact on a single edge, but puts clique below every random graph property on 6 vertices. Small cases exhausted; what remains is a non-local pairing analysed as the number of vertices grows. Zero/infinity rule: ETH constant 0 (claimed refutation, Oct 2026), omega = 2 (predicted). WSS: comma of D_p = 0.

## 10. Terms not to use (project conventions)
- Do not describe the grid as "Kant inverted". Monads' existence is shown by argument; do not hedge on it. Music is foundational.

## 11. Status of results since 21 Nov (holds / failed / withdrawn)
| Result | Status |
| --- | --- |
| Four solutions for every mirror step; mirror selects the integer sequence | holds (§60) |
| Golden Artin densities 0.7873 / 0.5314 | holds on new primes (§60) |
| Zeros weighted by 1/(rho zeta'(rho)) give mu(n) | holds (§62) |
| Weil form positive from the primes | holds after a labelled fix (§60) |
| Gate makes a world; joining needs no gate | holds (§59, §61, §62) |
| Queen entrains a slower body only at her zero | holds post hoc (§60) |
| Frozen/fluid = classical/quantum line | holds except r = 3 in the Burau form (§57) |
| "Naive operator scrambles the primes" (§60) | withdrawn (detector blind, §61); detector retired (blind to a huge plant, §63) |
| Entries-only operator readout (§63) | positive control P3 failed in §63; controls pass in §64 (difference detector, sparse plant) |
| Liouville signs from the operator; magnitudes alone carry none; a quarter of the rows suffices (§64) | holds |
| "Re-link only at gates" (§33) | replaced by making vs joining (§61, §62) |
| Pre-registered thresholds missed: gap ratio < 0.10; Artin range 0.20-0.45; operator detector | failed, kept in the record |


## 90. Syntax and semantics
Every monad is a language: syntax (objective sinusoidal mathematics, copyable) and semantics (subjective meaning, uncopyable), both present in monad and spacetime. Spacetime is the semantic expression of the syntax. The dialectic is semantic; linking separates thesis and antithesis so semantic thinking becomes conscious. Instance: one spectrum, many readings. Syntax rules at the start, semantics at the end.

## 91. Integers as a language
Primes = words, factorization = grammar, multiplicative functions = compositional meanings (Liouville sign, Moebius exclusion, characters), each with its L-function zeros (operator). Ambiguous grammar in Z[sqrt(-5)] is synthesised by ideals: (6) = P2^2 P3 P3' (t17). Class number = amount of synthesis needed.

## 92. Class field synthesis
In H = Q(i, sqrt5) the ideals of Q(sqrt-5) become principal: 6 = [(1+i)(1-i)][alpha beta] = [(1+i)alpha][(1-i)beta], alpha = phi + i(phi-1). Two parses = two groupings of the same atoms (t18). Resolving field generated by i (chi_-4) and phi (chi_5); towers can be infinite (R3).

## 93. Action vs loss
Shared: stationarity, multipliers, adjoint = backprop. Contrasts: stationary vs least (Morse index = conjugate points, t19), two-point vs initial, phase e^(iS) vs weight e^(-L) (Wick), conservation vs dissipation, intrinsic vs designed functional, isolated vs degenerate minima.

## 95. Holographic hands
The link's record |O+R|^2 holds O, conj(O) and |O|^2; conjugate reference reads the other hand; carrier separates (t20). Construction: real record on the veil -> f (SD, twistor space) and fbar (ASD, dual twistor space) -> meet on ambitwistor space; zero order = hands' product = focusing; carrier = collective reference = time direction.

## 96. Nonlinear hands
Nonlinear record: second orders O^2, conj(O)^2 (windings +-4), first orders keep helicity, +n and -n equal to all orders (t21 N). Gravity: (CC + *C*C)(k,k,k,k) = 4|Psi0|^2, zero for one hand (t21 G, run 2 after a disclosed index fix): Bel-Robinson = hands' product = order-4 focusing = holographic zero order.

## 97. Interaction term
Sachs: sigma = Psi0 lam/3, area A/A_flat = 1 - Phi00 lam^2/3 - |Psi0|^2 lam^4/90 (t22). Checklist: bilinear, type (4,4) forces Bel-Robinson, positive, conserved in vacuum, order 4 coefficient 1/90, helicity 0.

## 98. Checklist on Kerr
t23: on exact Kerr, T(k,k,k,k) = 4|Psi0|^2 (CV 1e-11), single hands give 0, T symmetric trace-free, positive on 60k causal quadruples (C C alone is not), divergence 5e-9 (Kerr-Newman 0.07), helicity 0. Target fixed; twistor construction open.

## 99. Gluing design
A record (real, on light rays) -> B carrier separates hands -> C each hand deforms alone (nonlinear graviton / H-space) -> D glue on one ambitwistor space (third neighbourhood; LCCE eth^2 ethbar^2 Z = F, two per hand) -> E order-by-order tower graded by t23 -> F closure in one step for Kerr. Tests P1-P4 next.

## 100. P1-P4
t24: carrier separation through the Penrose transform (Gabor fails); LCCE real, H-space complex unless pure electric; order-4 deficit Psi0 Psitilde0/90, zero for one hand; Kerr twistors on one quadric, same-l Kerr-Schild superposition exact (different-l control below threshold at 2/3 points, recorded).

## 101. Quantum complexity
Monadic record = quantum code (no part knows, any two know all; t25); witness = state (QMA, unforgeable); harmony = shared entanglement (MIP* = RE; infinite dimension needed); bosons/permanent hard, fermions/determinant easy (sign = cancellation = shortcut); complexity = volume/action.

## 102. QM and GR from monads
PSR -> e^(i omega t). QM = phase (superposition, |.|^2 record, uncertainty, no-cloning, e^(iS)). GR = light rays (meeting = geometry, focusing = gravity, Einstein on null rays). One record: cross terms = QM, product = GR. Open: hbar, G values, matter content, nonlinear gluing.

## 103. More whys
QM: i keeps size fixed; Schrodinger = a chord; measurement = copying (t26, plateau H(p)); Tsirelson 2 sqrt2. GR: light = balance between PT+ and PT-; 3+1 from linking; attraction = positive focusing; equivalence = one meeting structure; Lambda invisible to light.

## 104. Program for hbar, G, Lambda, matter, gluing
hbar = unit of phase area; G = 1/(4 eta) from area-law entanglement (t27: c = 0.295, G = 10.6 a^2 per species); Lambda ~ N^-1/2 (Sorkin); matter = excitations of the collective code (t28 next); gluing = entropy balance on every local light cone, shear term = entropy production (t29 next).

## 105. t28, t29
Toric code: e, m bosons, eps fermion (T-junction -1), mutual -1. Equation of state on every light cone: Kerr R_kk = 0; Kerr-Newman R_kk = 8 pi T_kk (6e-8); wrong charge fails; hands' meeting >= 0 = entropy production.

## 106. eta/s and the content route
t30: eta/s = 1/4pi from horizon optics (6e-10). t31: lattice net chirality 0 (20/20); 4D doublers 8+8; Fidkowski-Kitaev unique only at N = 8. Route: hidden mirror hand gapped in blocks of 16 = one generation. Open: three generations, gauge group, cutoff/species.

## 108. The hands
Across domains: monad, twistor, holography, gravity, light, fermions, time, dialectic. t32: Maxwell stress = phi phibar (one hand 0); Dirac chirality -cos 2mt (mass = hands' exchange rate). Rules 1-9; energy sits where the hands meet.

## 117. Restated as stability
Label [S] = the only stable configuration of existence (replaces [A]). Levels: existence, net zero, balanced pairs, sinusoids, no privileged frequency, points, infinite number, phase-agreed projection, linking (3+1), no one-handed persistence, positive meeting, pointer records, unitary QM, anomaly-free 16s, synthesis towers.

## 129-137. Millington's coil
p.204 winding: wires on {1,4,7} and {2,5,8} mod 9, stepping x7 and x4 (inverse multipliers). Carrier 2^s = product of forward and reversed sequences. Meeting-as-source bridge: in a stopband network real power passes only through V1 V2 sin(delta)/X; doubling chain gives 2^s (t47, t48). The bare coil is not such a chain (t49, withdrawn prediction). Bench test as intended (§137): copper vs non-FCC coil, six-step counter-rotating drive; discriminator s = 1 vs s = 5.

## 138-139. Cycles and lattices
Fibonacci digital roots: period 24, opposite pairs sum to 9. Mod 3^k periods 8, 24, 72, 216, sign flip at half. 13 = F(7) = FCC 12 + 1; tet-oct mesh = FCC; 24-cell slices 12 + 6 + 6. Hessian 216 = ASL(2,3) = 9 x 24.

## 140-142. Golden field and groups
F9 = F3(phi); Q = x phi, phi^2 = i; Frobenius = hand swap = conjugation; det Q^n = (-1)^n (Cassini). <Q, swap> -> quaternions; <Q^2, U> = SL(2,3) = 2T; with shifts, Hessian 216; mod 3^k all of SL(2, Z/3^k); mod 5, SL(2,5) = 2I, F(n) = n 3^(n-1). McKay on the hand pair: D4, E6, E8. Golden cut-and-project: visible = phi, hidden = psi.

## 143, 148, 151. Matter
E6 from McKay minus vacuum: gauge 72 (hand pair), 27 = 1 + 16 + 10 by the counting phase. E8 cut at the meeting triplet: SU(3) x E6, 240 = 78 + 81 + 81, 81 = 27 x 3 (three generations). One golden step and the hand swap each swap w and w^2; together they preserve w (chirality conserved, chosen once).

## 144-150. Twistors and the googly
PT = PG(3,9): 280 null twistors, 112 spacetime lines (10 points each, 4 per light ray). Conjugation D(omega, pi) = (pi^3, omega^3) polynomial; helicity swap n -> -n-4 = 3n (odd) or 3n + 4 (even) mod 8; q = 3 unique; graviton helicities one degree class. Googly graviton: one fiber shear of amplitude c_A + sigma(c_S) (t61b). Hensel for Kodaira: formal sections survive nonlinear patching; small 3-adic deformation curves spacetime one level up (t59). The grain is the ground; the continuum is the projection (§150).

## Reconciliation of QM and GR
One record |O + R|^2 of the two hands: cross terms = QM (phase i = phi^2), meeting term = GR (positive, conserved; equation of state gives Einstein; its degree class bends twistor space, both helicities in one deformation). Quantum at the grain, classical curvature as the first correction up the 3-adic tower.

## 152-157. Chirality, Z'_psi, predictions, launch
The seed (0, 1) and the arrow fix the first moving count; the step conserves it (t62, t63). U(1)_psi is the counting U(1); Z'_psi near 1e14 GeV, broken with the forces at the meeting (t64, t65, t71). Positive predictions: normal ordering, Sum m_nu = 59.16 +- 0.21 meV, m_bb = 1.16-4.11 meV, m_beta = 8.84 meV, m_tau = 1776.969 MeV, tensor-only gravitational waves. PSR review: matter as the 27 and Q = 2/3 are [S].

## 158. Against the Standard Model; correction map; roadmap
Shared: the SO(10) 16 per generation, three generations, chirality. Added: gravity (meeting term), the 27's 1 and 10, U(1)_psi, Majorana masses, Q = 2/3. Not derived: couplings, quark masses and mixing, Higgs, theta_QCD, dark matter, inflation. Dark energy: Sorkin count, everpresent Lambda (bridge; survives DESI DR2 as a band, t72). Tension: hierarchical thermal leptogenesis needs M_R1 ~ 6e10 GeV, the grid's SO(10) Dirac bridge gives 1e7 GeV (fix: Dirac masses from the record). Correction map in the record, §158.

## 159. The Standard Model from the same cut (t66)
Cutting E6 at its dimension-3 node (the rule that gave three generations in E8) leaves SU(3) x SU(3) x SU(3); the counting phases permute the three factors cyclically, so their couplings are equal at the cut. The 27 is three bifundamentals; a U(1) in the commutant of SU(3)_C x SU(2)_L gives exactly the Standard Model hypercharges plus the E6 extras; sin^2 theta_W = 3/8 at the cut [M]. Open: hypercharge selection (SU(3)_L x SU(3)_R breaking) and coupling meeting with thresholds (t67).


## 160. Proton decay (t68)
The su(3)^3 bosons carry no colour triplet; only E6's 54 can mediate proton decay. Equal Dynkin index (3) for the three SU(3)s keeps the couplings equal above the cut, so E6 may break above the Super-K bound, 4.6e15 GeV. Triplet scalars with first-generation Yukawas need only 5.5e11 GeV and may sit at the cut [M]. Open: the E6 breaking scale.

## 161. The mirror and Distler-Garibaldi (t69)
E8 content is vector-like (index 0): the theorem holds. The mirror 27bar has no bilinear mass, no SM anomaly, Z16 index 0, so interacting gapping is allowed; family SU(3) anomaly 27 ties mirror gapping to family breaking [M checks, I escape].

## 162. Known objections and prior work
Recorded in the paper and in the record, §163: proton decay, chirality, DESI Sum m_nu < 53 meV, numerology, googly above the grain, gravity and phase; prior work from trinification to p-adic physics, finite-field quantum theory, twistors, lattice chirality, constructor theory, and Coldea's E8 in cobalt niobate.

## 163. The couplings meet (t67)
The 27's extras beyond the 16 form a complete 5 + 5bar and cannot shift the meeting at one common mass. With two or three pairs of its lepton-like doublets light (two pairs at 1e3-3e5 GeV, three at 4e4-2e8 GeV) and the triplets heavy, the three couplings meet at 4-6e13 GeV with alpha^-1 = 37-39 [M, one loop]. Prediction: vector-like lepton doublets below 2e8 GeV.

## 164. VP != VNP (claimed, 24 Nov 2026)
Claude/Anthropic, Lean 4: the permanent (characteristic != 2) and the Hamiltonian cycle polynomial (every field) need superpolynomial algebraic circuits [M claim, pending human vetting]. First proved instance of "the fermionic sign is the shortcut"; holds over F9; the characteristic-2 exception is the sign being invisible. Boolean P vs NP still open.

## 165. The meeting at two loops (t70)
Two-loop gauge running with the top Yukawa keeps the meeting: M3 = 3.7-5.6e13 GeV, alpha^-1 = 37-39; two light doublet pairs at 1e3-7.5e6 GeV or three at 4e5-1.3e9 GeV [M]. Pre-registered bound 2e8 exceeded (recorded fail); wording "below about 1e9 GeV". LHC excludes vector-like e/mu doublets below about 1.3 TeV, cutting only the bottom of the window.

## 166. Posted numbers against the newest data
m_tau 0.4 sigma from PDG 2026; JUNO-era global fit prefers normal ordering (inverted at p = 2-2.6%); m_bb far below KamLAND-Zen and LEGEND-200; tensor-only holds (GWTC-4.0/5.0), with the mixed Bayes factors a watch item.

## 167. Posts agree (t71)
E6 bound with the run coupling 4.6-4.8e15 GeV; U(1)_psi in the SU(3)_L x SU(3)_R Cartan, so Z'_psi is broken at M3: near 1e14 GeV (ratio 1.3 to M3) [M]. Triplets between 5.5e11 GeV and M3/g in 577 of 1203 meetings; doublet windows unchanged.

## 168. Everpresent Lambda against DESI (t72)
Lambda = alpha W(V)/V: at alpha = 1, 61% of fitted runs lie in DESI's quadrant, 6% in its 2-sigma box, median |w0 + 1| = 0.9; 77% dip below zero at z < 2 [I]. A band, not a point; direct distance test next.

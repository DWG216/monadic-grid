"""
Catalogue of 'stable' sinusoid configurations for SU(3)xSU(2)xU(1).

Each configuration is three phase windings on circles:
  colour   : triality t  -> phase 2*pi*t/3   (120 deg steps)
  isospin  : doublet d   -> phase pi*d       (180 deg steps)
  hypercharge n = 6Y     -> phase 2*pi*n/6   (60 deg steps)
Net phase = 2*pi*(2t + 3d + n)/6.

Stability rule 1 (closure): net phase is a whole turn, i.e. 2t+3d+n = 0 mod 6.
  (This is the Z6 quotient of the real Standard Model gauge group.)
Stability rule 2 (anomaly freedom): a set of chiral configurations must cancel
  every gauge anomaly, otherwise the quantum theory is inconsistent.
"""
from itertools import combinations_with_replacement
from fractions import Fraction as F

SU3 = {"1": (1, 0, 0), "3": (3, 1, 1), "3b": (3, 2, -1)}   # name: (dim, triality, cubic index)
SU2 = {"1": (1, 0), "2": (2, 1)}                          # name: (dim, doublet parity)

def closed(t, d, n):
    return (2 * t + 3 * d + n) % 6 == 0

cands = []
for c, (d3, t, a3) in SU3.items():
    for w, (d2, dp) in SU2.items():
        for n in range(-6, 7):
            if closed(t, dp, n):
                cands.append((c, w, n))

print(f"Closed configurations (n = 6Y in -6..6): {len(cands)} of {3*2*13}")
for c, w, n in cands:
    d2 = SU2[w][0]
    t3 = [F(1, 2), F(-1, 2)] if d2 == 2 else [F(0)]
    Q = sorted({str(x + F(n, 6)) for x in t3})
    print(f"  ({c:>2},{w},Y={str(F(n,6)):>5})  phase steps 2t+3d+n={2*SU3[c][1]+3*SU2[w][1]+n:>3}  charges Q={Q}")

def anomalies(fs):
    s33 = s33y = s22y = y3 = grav = wit = 0
    for c, w, n in fs:
        d3, t, a3 = SU3[c]; d2, dp = SU2[w]
        s33 += d2 * a3
        if d3 == 3: s33y += d2 * n
        if d2 == 2: s22y += d3 * n; wit += d3
        y3 += d3 * d2 * n**3
        grav += d3 * d2 * n
    return (s33, s33y, s22y, y3, grav, wit % 2)

def conj(f):
    c, w, n = f
    return ({"1": "1", "3": "3b", "3b": "3"}[c], w, -n)

# search: chiral (no field together with its conjugate, no neutral singlets), all anomalies cancel
pool = [f for f in cands if not (f[0] == "1" and f[1] == "1" and f[2] == 0)]
sols = []
for size in range(1, 7):
    for fs in combinations_with_replacement(pool, size):
        if any(conj(f) in fs for f in fs):
            continue
        if anomalies(fs) == (0, 0, 0, 0, 0, 0):
            sols.append(fs)
    if sols:
        print(f"\nSmallest chiral anomaly-free sets: size {size}, {len(sols)} found")
        for s in sols:
            print("  ", s)
        break


# ---------------------------------------------------------------------------
# Part 2: the book's geometry, formalised
# ---------------------------------------------------------------------------
import numpy as np
from itertools import product
rng = np.random.default_rng(1)

print("\n=== 6D frequency domain as C^3 (3 real cosine axes + 3 imaginary sine axes) ===")
# random SU(3): rotation of the three complex axes that preserves complex volume
A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
U, _ = np.linalg.qr(A)
U = U / np.linalg.det(U) ** (1 / 3)
print("det U =", np.round(np.linalg.det(U), 12), " unitary:", np.allclose(U.conj().T @ U, np.eye(3)))
w = np.exp(2j * np.pi / 3)
print("120-degree rotation of all three complex planes, det(wI) =", np.round(np.linalg.det(w * np.eye(3)), 12), "-> lies in SU(3): colour triality")
z1, z2, z3 = (rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3))
vol = lambda a, b, c: np.linalg.det(np.column_stack([a, b, c]))
print("baryon (3 quarks, one per complex axis = complex volume) invariant:",
      np.isclose(vol(U @ z1, U @ z2, U @ z3), vol(z1, z2, z3)))
print("meson (quark x antiquark = Hermitian length) invariant:",
      np.isclose(np.vdot(U @ z1, U @ z2), np.vdot(z1, z2)))

print("\n=== Mind -> matter: which pairings with the Higgs close (Yukawa couplings) ===")
gen = {"Q": ("3", "2", 1), "u^c": ("3b", "1", -4), "d^c": ("3b", "1", 2),
       "L": ("1", "2", -3), "e^c": ("1", "1", 6), "nu^c": ("1", "1", 0)}
higgs = {"H": ("1", "2", 3), "H*": ("1", "2", -3)}
def colour_singlet(a, b):
    return {a, b} == {"3", "3b"} or (a == "1" and b == "1")
found = []
names = list(gen)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        for h, (hc, hw, hn) in higgs.items():
            ca, wa, na = gen[a]; cb, wb, nb = gen[b]
            doublets = [wa, wb, hw].count("2")
            if colour_singlet(ca, cb) and doublets == 2 and na + nb + hn == 0:
                t = {"1": 0, "3": 1, "3b": 2}
                wind = sum(2 * t[c] + 3 * (w_ == "2") + n for c, w_, n in [gen[a], gen[b], (hc, hw, hn)])
                found.append((a, b, h))
                print(f"  {a:>4} x {b:<5} x {h:<2}  hypercharge sum 0, total winding {wind} (closes)")
print(f"  {len(found)} closing pairings; every charged fermion gets one; neutrinos only if nu^c is added")

print("\n=== After the Higgs settles at the zero-frequency point: who stays on the null cone ===")
# Higgs vev sits in the lower doublet component: T3 = -1/2, Y = +1/2
T3v, Yv = F(-1, 2), F(1, 2)
for a, b in [(1, 0), (0, 1), (1, 1), (1, -1)]:
    print(f"  generator {a}*T3 + {b}*Y on vacuum: {a * T3v + b * Yv}", "<- unbroken (photon)" if a * T3v + b * Yv == 0 else "")
print("  W+ and W- shift T3 by +-1, so they cannot leave the vacuum alone -> massive")

print("\n=== Tilt off the null line at E = 1 TeV: chi = arcsin(m/E) ===")
masses = {"photon": 0, "gluon": 0, "neutrino (<1 eV)": 1e-9, "electron": 0.000511, "muon": 0.1057,
          "tau": 1.7769, "up": 0.00216, "down": 0.0047, "strange": 0.0935, "charm": 1.27, "bottom": 4.18,
          "W": 80.37, "Z": 91.19, "Higgs": 125.2, "top": 172.6}
E = 1000.0
for k, m in sorted(masses.items(), key=lambda kv: kv[1]):
    print(f"  {k:<18} m = {m:>10.6g} GeV   chi = {np.degrees(np.arcsin(m / E)):.3g} deg")

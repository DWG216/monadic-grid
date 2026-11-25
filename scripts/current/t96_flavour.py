"""t96: A4 from the Hurwitz units; Delta(27) from the grain's clock and shift; critical directions; residual symmetries; TM2. Pre-registration: PREDICTIONS_t96.md."""
import numpy as np, itertools
w = np.exp(2j*np.pi/3); out = {}
# Hurwitz units (2T)
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
units = [tuple(s*e for e in v) for v in np.eye(4) for s in (1, -1)] + [tuple(0.5*np.array(s)) for s in itertools.product((1, -1), repeat=4)]
key = lambda q: tuple(np.round(q, 9))
closed = all(key(qmul(a, b)) in {key(u) for u in units} for a in units for b in units)
def rot(q):
    q = np.array(q); conj = q*np.array([1, -1, -1, -1]); R = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(4); e[j+1] = 1; R[:, j] = np.array(qmul(qmul(q, e), conj))[1:]
    return R
A4 = []
for u in units:
    R = np.round(rot(u), 9)
    if not any(np.allclose(R, X) for X in A4): A4.append(R)
# Delta(27)
C = np.roll(np.eye(3), 1, axis=0); D = np.diag([1, w, w**2])
G27 = []; frontier = [np.eye(3, dtype=complex)]
while frontier:
    g = frontier.pop()
    if any(np.allclose(g, h) for h in G27): continue
    G27.append(g); frontier += [g @ C, g @ D]
out['S1'] = dict(units=len(units), closed=closed, A4=len(A4), D27=len(G27), pass_=closed and len(units) == 24 and len(A4) == 12 and len(G27) == 27)
# P1: critical axes of A4: fixed lines of nontrivial elements, stabiliser sizes
axes = {}
for R in A4:
    if np.allclose(R, np.eye(3)): continue
    wv, V = np.linalg.eig(R)
    for k in range(3):
        if abs(wv[k] - 1) < 1e-9:
            a = np.real(V[:, k]); a /= np.linalg.norm(a); a *= np.sign(a[np.argmax(np.abs(a) > 1e-9)])
            kk = key(a); axes.setdefault(kk, 0); axes[kk] += 1
stab = {k: v + 1 for k, v in axes.items()}
classes = sorted(set(stab.values()))
out['P1'] = dict(n_axes=len(stab), stabiliser_orders=sorted(stab.values()), pass_=len(stab) == 7 and sorted(stab.values()) == [2, 2, 2, 3, 3, 3, 3])
# P2: Delta(27) critical lines: eigenlines; stabiliser = elements having the line as eigenline (projectively)
lines = []
for g in G27:
    if np.allclose(g, g[0, 0]*np.eye(3)): continue
    wv, V = np.linalg.eig(g)
    for k in range(3):
        v = V[:, k]/np.linalg.norm(V[:, k])
        if not any(abs(np.vdot(v, l)) > 1 - 1e-9 for l in lines): lines.append(v)
def stabsize(v): return sum(1 for g in G27 if abs(abs(np.vdot(v, g @ v)) - 1) < 1e-9)
sizes = [stabsize(v) for v in lines]; mx = max(sizes); crit = [v for v, s in zip(lines, sizes) if s == mx]
# group into orthonormal bases
bases = []
for v in crit:
    placed = False
    for b in bases:
        if all(abs(np.vdot(v, u)) < 1e-9 for u in b): b.append(v); placed = True; break
    if not placed: bases.append([v])
mub = all(abs(abs(np.vdot(a, b))**2 - 1/3) < 1e-9 for i, B1 in enumerate(bases) for B2 in bases[i+1:] for a in B1 for b in B2)
out['P2'] = dict(n_critical=len(crit), stabiliser=mx, bases=[len(b) for b in bases], mutually_unbiased=mub, pass_=len(crit) == 12 and len(bases) == 4 and all(len(b) == 3 for b in bases) and mub)
U_c1 = np.array([[np.vdot(a, b) for b in bases[1]] for a in bases[0]])
out['C1'] = dict(moduli_sq=np.round(np.abs(U_c1)**2, 6).tolist(), pass_=np.allclose(np.abs(U_c1)**2, 1/3))
# P3: charged leptons keep Z3 = <T> (T = cyclic permutation in A4's basis), neutrinos keep Z2 = <S>
T = next(R for R in A4 if np.allclose(R @ R @ R, np.eye(3)) and not np.allclose(R, np.eye(3)) and np.allclose(np.abs(R), np.abs(np.roll(np.eye(3), 1, axis=0))))
S = next(R for R in A4 if np.allclose(R @ R, np.eye(3)) and not np.allclose(R, np.eye(3)) and np.allclose(R, np.diag(np.diag(R))))
wT, Ue = np.linalg.eig(T)                                         # charged-lepton basis
wS, US = np.linalg.eigh(S)                                        # S eigenbasis (+1 line and -1 plane)
ok3 = True; rng = np.random.default_rng(96)
for _ in range(2000):
    th, ph = rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi)
    plane = [k for k in range(3) if wS[k] < 0]; line = [k for k in range(3) if wS[k] > 0][0]
    Rn = np.eye(3, dtype=complex); i, j = plane
    Rn[np.ix_([i, j], [i, j])] = [[np.cos(th), np.sin(th)*np.exp(-1j*ph)], [-np.sin(th)*np.exp(1j*ph), np.cos(th)]]
    Un = US @ Rn; Upmns = Ue.conj().T @ Un
    ok3 &= any(np.allclose(np.abs(Upmns[:, c])**2, 1/3) for c in range(3))
out['P3'] = dict(pass_=bool(ok3))
s13 = 0.02215; s12 = 1/(3*(1 - s13))
out['P4'] = dict(sin2_12_TM2=s12, nufit_3sigma=(0.275, 0.345), pull_nufit=(s12 - 0.307)/0.012, pull_JUNO=(s12 - 0.3092)/0.0087, pass_=0.275 <= s12 <= 0.345)
# information: TM2 theta23-delta curve at measured theta13 (scan the free angle/phase, keep points with s13 within 1e-3)
pts = []
for _ in range(200000):
    th, ph = rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi)
    Rn = np.eye(3, dtype=complex); i, j = plane
    Rn[np.ix_([i, j], [i, j])] = [[np.cos(th), np.sin(th)*np.exp(-1j*ph)], [-np.sin(th)*np.exp(1j*ph), np.cos(th)]]
    U = Ue.conj().T @ (US @ Rn)
    c = [k for k in range(3) if np.allclose(np.abs(U[:, k])**2, 1/3)][0]; others = [k for k in range(3) if k != c]
    for order in (others, others[::-1]):
        M = U[:, [order[0], c, order[1]]]                         # trimaximal column placed second (TM2)
        for rows in itertools.permutations(range(3)):
            V = M[list(rows), :]
            if abs(abs(V[0, 2])**2 - s13) > 1e-3: continue
            s23 = abs(V[1, 2])**2/(1 - abs(V[0, 2])**2)
            J = np.imag(V[0, 0]*V[1, 1]*np.conj(V[0, 1])*np.conj(V[1, 0]))
            pts.append((s23, J))
pts = np.array(pts) if pts else np.zeros((0, 2))
out['info'] = dict(n_points=len(pts), s23_range=[float(pts[:, 0].min()), float(pts[:, 0].max())] if len(pts) else None,
                   Jmax=float(np.abs(pts[:, 1]).max()) if len(pts) else None)
for k, v in out.items(): print(k, v)

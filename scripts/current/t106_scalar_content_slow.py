"""t106: scalar content from the breaking; two-bifundamental quartics from zero at M*; vacuum stability; Coleman-Weinberg scale. Pre-registration: PREDICTIONS_t106.md."""
import os, itertools, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
src = open('t105_scalar_sector.py').read(); ns = {'__file__': os.path.abspath('t105_scalar_sector.py')}
exec(src[:src.index('# ---------------- S1')], ns)
gm, realgen, scalar_from_complex, pair3, quartic_tensor, k16 = ns['gm'], ns['realgen'], ns['scalar_from_complex'], ns['pair3'], ns['quartic_tensor'], ns['k16']
I3 = np.eye(3); out = {}
# ---------- Step 1: unbroken generators ----------
def gens_on(nbif):
    L = [np.kron(np.eye(nbif), np.kron(t, I3)) for t in gm(3)]; R = [np.kron(np.eye(nbif), -np.kron(I3, t.T)) for t in gm(3)]
    return L + R
def unbroken(z, nbif):
    G = gens_on(nbif); vecs = [T @ z for T in G]
    M = np.array([[np.real(np.vdot(a, b)) for b in vecs] for a in vecs])
    return 16 - np.linalg.matrix_rank(M, tol=1e-9)
rng = np.random.default_rng(106)
z1 = np.zeros(9, complex); z1[6:9] = rng.normal(size=3) + 1j*rng.normal(size=3)              # row 3 of one bifundamental, generic
z2 = np.zeros(18, complex); z2[3*2 + 2] = 1.3; z2[9 + 3*2 + 1] = 0.7                          # H1_33, H2_32
out['P1a'] = dict(unbroken=int(unbroken(z1, 1)), pass_=unbroken(z1, 1) == 7)
out['P1b'] = dict(unbroken=int(unbroken(z2, 2)), pass_=unbroken(z2, 2) == 4)
print('P1a', out['P1a'], 'P1b', out['P1b'], flush=True)
# ---------- Step 2: two bifundamentals ----------
nC = 18; J = scalar_from_complex(nC); nR = 2*nC
th = [realgen(T) for T in gens_on(2)]
# fermions and Yukawa (top on H1 only), as t105
nF = 18; fg = []
for t in gm(3):
    M = np.zeros((nF, nF), complex); M[:9, :9] = np.kron(t, I3); M[9:, 9:] = -np.kron(t.T, I3); fg.append(M)
for t in gm(3):
    M = np.zeros((nF, nF), complex); M[:9, :9] = -np.kron(I3, t.T); fg.append(M)
for t in gm(3):
    M = np.zeros((nF, nF), complex); M[9:, 9:] = np.kron(I3, t); fg.append(M)
Y1 = np.zeros((nR, nF, nF), complex)
for a in range(3):
    for i in range(3):
        for r in range(3):
            for p in range(nR):
                v = J[3*i + r, p]; Y1[p, 3*a + i, 9 + 3*a + r] += v; Y1[p, 9 + 3*a + r, 3*a + i] += v
# invariant basis: X_ij[r,s] = sum_i' conj(H_i[i',r]) H_j[i',s] = phi^T M phi (complex)
def Xmat(i, j, r, s):
    M = np.zeros((nR, nR), complex)
    for q in range(3): M += np.outer(J[9*i + 3*q + r].conj(), J[9*j + 3*q + s])
    return M
polys = []
idx = [(i, j) for i in range(2) for j in range(2)]
for (i, j), (k, l) in itertools.combinations_with_replacement(idx, 2):
    TrA = sum(Xmat(i, j, r, r) for r in range(3)); TrB = sum(Xmat(k, l, r, r) for r in range(3))
    polys.append([(1.0, TrA, TrB)])
    polys.append([(1.0, Xmat(i, j, r, s), Xmat(k, l, s, r)) for r in range(3) for s in range(3)])
tens = []
for P in polys:
    for part in ('re', 'im'):
        T = np.zeros((nR,)*4)
        for c, A, B in P:
            Aa = (A + A.T)/2; Bb = (B + B.T)/2
            X = np.einsum('ab,cd->abcd', Aa, Bb); X = X + X.transpose(2, 3, 0, 1)
            T += 4*c*(np.real(pair3(X)) if part == 're' else np.imag(pair3(X)))
        if np.linalg.norm(T) > 1e-9: tens.append(T)
F = np.array([t.ravel() for t in tens]).T
U_, sv, Vt = np.linalg.svd(F, full_matrices=False); rank = int((sv > 1e-8*sv[0]).sum())
basis = U_[:, :rank]; print('quartic invariants (real, independent):', rank, flush=True)
def proj(T): c = basis.T @ T.ravel(); r = np.linalg.norm(basis @ c - T.ravel())/max(np.linalg.norm(T), 1e-300); return c, r
def unflat(c): return (basis @ c).reshape((nR,)*4)
# gauge pieces at g = 1
S = [(ta @ tb + tb @ ta).real for ta in th for tb in th]
Xg = sum(np.einsum('ab,cd->abcd', m, m) for m in S); A1 = pair3(Xg)
C2S = np.diag(sum(t @ t for t in th).real)
Yd = np.conj(Y1.transpose(0, 2, 1))
Mab = np.einsum('aij,bjk->abik', Y1, Yd).reshape(nR*nR, nF*nF)
T4 = (Mab @ Mab.reshape(nR, nR, nF, nF).transpose(0, 1, 3, 2).reshape(nR*nR, nF*nF).T).reshape((nR,)*4)
H1 = sum(T4.transpose(p) for p in itertools.permutations(range(4)))/4
Y2 = 0.5*np.real(np.einsum('aij,bji->ab', Yd, Y1) + np.einsum('bij,aji->ab', Yd, Y1)); y2d = np.diag(Y2)
cA, rA = proj(3*A1); cH, rH = proj(-4*np.real(H1)); print('closure residuals: gauge', rA, 'yukawa', rH, flush=True)
def beta_vec(c, g, y):
    lam = unflat(c); L2 = (lam.reshape(nR*nR, nR*nR) @ lam.reshape(nR*nR, nR*nR)).reshape((nR,)*4); L2 = pair3(L2)
    s4 = lambda v: v[:, None, None, None] + v[None, :, None, None] + v[None, None, :, None] + v[None, None, None, :]
    rest = -3*g**2*lam*s4(C2S) + 2*0.5*y**2*lam*s4(y2d)
    cq, _ = proj(L2 + rest)
    return k16*(cq + g**4*cA + y**4*cH)
# couplings (as t105) with n_h = 2
src2 = open('t101_higgs_full.py').read(); ns2 = {'__file__': os.path.abspath('t101_higgs_full.py')}; exec(src2[:src2.index('\nout = {}')], ns2)
lam_mt, make_beta = ns2['lam_mt'], ns2['make_beta']; Mt = 172.57; M3 = 4.98e13; Mstar = 2.435e18
y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(125.2, Mt)]
s = solve_ivp(make_beta(1.0e3, 2, 3.16e12, None, 0), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12); g1, g2, g3, yt, _ = s.y[:, -1]
gM = float(np.mean([g3, g2, np.sqrt(5/3)*g1]))
up = solve_ivp(lambda t, z: [(-5 + 2)*k16*z[0]**3, k16*z[1]*(6*z[1]**2 - 16*z[0]**2)], [np.log(M3), np.log(Mstar)], [gM, yt], dense_output=True, rtol=1e-10)
ts = np.linspace(np.log(Mstar), np.log(M3), 61); c = np.zeros(rank)
for t0, t1 in zip(ts[:-1], ts[1:]):                      # RK4 downward
    h = t1 - t0; f = lambda t, c: beta_vec(c, *up.sol(t))
    k1 = f(t0, c); k2 = f(t0 + h/2, c + h/2*k1); k3 = f(t0 + h/2, c + h/2*k2); k4 = f(t1, c + h*k3); c = c + h/6*(k1 + 2*k2 + 2*k3 + k4)
lamM3 = unflat(c)
def V(phi): return np.einsum('abcd,a,b,c,d->', lamM3, phi, phi, phi, phi)/24
best = np.inf
for _ in range(20000):
    v = rng.normal(size=nR); v /= np.linalg.norm(v); best = min(best, V(v))
starts = [rng.normal(size=nR) for _ in range(40)]
for v0 in starts:
    r = minimize(lambda v: V(v/np.linalg.norm(v)), v0, method='BFGS', options=dict(maxiter=300)); best = min(best, r.fun)
out['P2'] = dict(n_invariants=rank, min_V_unit_sphere=float(best), pass_=best > 0)
print('P2', out['P2'], flush=True)
# ---------- Step 3: Coleman-Weinberg scale for t105's single bifundamental ----------
C1 = ns  # t105 polynomial coefficients are recomputed cheaply here
src3 = open('t105_scalar_sector.py').read(); ns3 = {'__file__': os.path.abspath('t105_scalar_sector.py')}
exec(src3[:src3.index('res = {}')].replace('print(', '(lambda *a, **k: None)('), ns3)
bl = ns3['bl']; up1 = solve_ivp(lambda t, z: [(-5 + 1)*k16*z[0]**3, k16*z[1]*(6*z[1]**2 - 16*z[0]**2)], [np.log(M3), np.log(Mstar)], [gM, yt], dense_output=True, rtol=1e-10)
tt = np.linspace(np.log(Mstar), np.log(M3), 4000)
dn = solve_ivp(lambda t, l: list(bl(l, *up1.sol(t))), [np.log(Mstar), np.log(M3)], [0, 0], t_eval=tt, rtol=1e-10, atol=1e-14)
le = dn.y[0] + dn.y[1]; be = np.array([sum(bl([a, b], *up1.sol(t))) for a, b, t in zip(dn.y[0], dn.y[1], tt)])
f = 4*le + be; i = int(np.argmax(np.sign(f) != np.sign(f[0]))) if np.any(np.sign(f) != np.sign(f[0])) else None
muCW = float(np.exp(tt[i])) if i else None
out['P3'] = dict(mu_CW=muCW, ratio_to_Mstar=(muCW/Mstar if muCW else None), pass_=bool(muCW) and Mstar/10 <= muCW <= Mstar*10)
for k, v in out.items(): print(k, v)

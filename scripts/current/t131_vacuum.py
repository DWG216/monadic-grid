"""t131: what stabilises the scalar vacuum. Pre-registration: PREDICTIONS_t131.md."""
import os, sys, itertools, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
src = open('t106_scalar_content.py').read()
cut = src.index('# fermions and Yukawa'); start = src.index('# ---------- Step 2')
pre = src[:cut]
ns = {'__file__': os.path.abspath('t106_scalar_content.py')}; exec(pre, ns)
J, nR, pair3, k16, gm = ns['J'], ns['nR'], ns['pair3'], ns['k16'], ns['gm']
rng = np.random.default_rng(131); out = {}
# ---------- S1: heavy scalars at tree level ----------
nA, nr = 10, 12
mu = rng.normal(size=(nA, nr, nr)); mu = (mu + mu.transpose(0, 2, 1))/2; M2 = rng.uniform(0.5, 2, nA)
P = rng.normal(size=(10000, nr)); P /= np.linalg.norm(P, axis=1)[:, None]
dV = -sum(np.einsum('bi,ij,bj->b', P, mu[A], P)**2/(2*M2[A]) for A in range(nA))
out['S1'] = dict(max_dV=float(dV.max()), pass_=bool(dV.max() <= 0)); print('S1', out['S1'], flush=True)
# ---------- fermions: Q_L (0-8), Q_R (9-17), L (18-26) ----------
nF = 27
eps = np.zeros((3, 3, 3))
for (i, j, k), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]: eps[i, j, k] = s
def yuk(h, quark=True, lepton=True):          # h = 0 for H1, 1 for H2; complex index 9h + 3i + r (i: L row, r: R column)
    Y = np.zeros((nR, nF, nF), complex)
    for p in range(nR):
        for i in range(3):
            for r in range(3):
                v = J[9*h + 3*i + r, p]
                if v == 0: continue
                if quark:
                    for a in range(3): Y[p, 3*a + i, 9 + 3*a + r] += v; Y[p, 9 + 3*a + r, 3*a + i] += v
                if lepton:
                    for j, k, s, t in itertools.product(range(3), repeat=4):
                        e = eps[i, j, k]*eps[r, s, t]
                        if e: Y[p, 18 + 3*j + s, 18 + 3*k + t] += e*v
    return Y
YqH1, YlH1, YqH2, YlH2 = yuk(0, True, False), yuk(0, False, True), yuk(1, True, False), yuk(1, False, True)
# gauge invariance of the lepton term under random SU(3)_L x SU(3)_R (complex check)
from scipy.linalg import expm
def su3(): A = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); A = A - A.conj().T; A -= np.trace(A)/3*np.eye(3); return expm(A/2)
UL, UR = su3(), su3(); H = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); L = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3))
f = lambda H, L: np.einsum('ijk,rst,ir,js,kt->', eps, eps, H, L, L)
tr = lambda X: UL @ X @ UR.conj().T
out['inv_lepton'] = float(abs(f(tr(H), tr(L)) - f(H, L))/abs(f(H, L))); print('lepton term invariance residual', out['inv_lepton'], flush=True)
# ---------- quartic basis (as t106) ----------
def Xmat(i, j, r, s):
    M = np.zeros((nR, nR), complex)
    for q in range(3): M += np.outer(J[9*i + 3*q + r].conj(), J[9*j + 3*q + s])
    return M
polys = []; idx = [(i, j) for i in range(2) for j in range(2)]
for (i, j), (k, l) in itertools.combinations_with_replacement(idx, 2):
    TrA = sum(Xmat(i, j, r, r) for r in range(3)); TrB = sum(Xmat(k, l, r, r) for r in range(3))
    polys.append([(1.0, TrA, TrB)]); polys.append([(1.0, Xmat(i, j, r, s), Xmat(k, l, s, r)) for r in range(3) for s in range(3)])
tens = []
for Pl in polys:
    for part in ('re', 'im'):
        T = np.zeros((nR,)*4)
        for c, A, B in Pl:
            Aa = (A + A.T)/2; Bb = (B + B.T)/2; X = np.einsum('ab,cd->abcd', Aa, Bb); X = X + X.transpose(2, 3, 0, 1)
            T += 4*c*(np.real(pair3(X)) if part == 're' else np.imag(pair3(X)))
        if np.linalg.norm(T) > 1e-9: tens.append(T)
F = np.array([t.ravel() for t in tens]).T; U_, sv, _ = np.linalg.svd(F, full_matrices=False); rank = int((sv > 1e-8*sv[0]).sum()); basis = U_[:, :rank]
def proj(T): c = basis.T @ T.ravel(); return c, np.linalg.norm(basis @ c - T.ravel())/max(np.linalg.norm(T), 1e-300)
def unflat(c): return (basis @ c).reshape((nR,)*4)
th = [ns['realgen'](T) for T in ns['gens_on'](2)]
S = [(ta @ tb + tb @ ta).real for ta in th for tb in th]; A1 = pair3(sum(np.einsum('ab,cd->abcd', m, m) for m in S))
C2S = np.diag(sum(t @ t for t in th).real); cA, rA = proj(3*A1)
def yterms(Y):                                   # Y includes its couplings
    Yd = np.conj(Y.transpose(0, 2, 1))
    Mab = np.einsum('aij,bjk->abik', Y, Yd).reshape(nR*nR, nF*nF)
    T4 = (Mab @ Mab.reshape(nR, nR, nF, nF).transpose(0, 1, 3, 2).reshape(nR*nR, nF*nF).T).reshape((nR,)*4)
    Hs = sum(T4.transpose(p) for p in itertools.permutations(range(4)))/4
    Y2 = 0.5*np.real(np.einsum('aij,bji->ab', Yd, Y) + np.einsum('bij,aji->ab', Yd, Y))
    cH, rH = proj(-4*np.real(Hs)); return cH, rH, Y2
def contractY2(lam, Y2):
    return (np.einsum('ea,ebcd->abcd', Y2, lam) + np.einsum('eb,aecd->abcd', Y2, lam) + np.einsum('ec,abed->abcd', Y2, lam) + np.einsum('ed,abce->abcd', Y2, lam))
# unit-coupling pieces per case; Y = y*(Ybase), so H term scales y^4 and Y2 y^2
cases = {'S2 (t106: quark term on H1)': YqH1, 'P1 r=0 (full cubic on H1)': YqH1 + YlH1}
for r in (0.5, 1.0): cases[f'P2 r={r}'] = YqH1 + YlH1 + r*(YqH2 + YlH2)
pre_ = {k: yterms(Y) for k, Y in cases.items()}
for k, (cH, rH, Y2) in pre_.items(): print('closure', k, 'gauge', rA, 'yukawa', rH, flush=True)
# couplings (as t106)
src2 = open('t101_higgs_full.py').read(); ns2 = {'__file__': os.path.abspath('t101_higgs_full.py')}; exec(src2[:src2.index('\nout = {}')], ns2)
lam_mt, make_beta = ns2['lam_mt'], ns2['make_beta']; Mt = 172.57; M3 = 4.98e13; Mstar = 2.435e18
y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(125.2, Mt)]
s = solve_ivp(make_beta(1.0e3, 2, 3.16e12, None, 0), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12); g1, g2, g3, yt, _ = s.y[:, -1]
gM = float(np.mean([g3, g2, np.sqrt(5/3)*g1]))
up = solve_ivp(lambda t, z: [(-5 + 2)*k16*z[0]**3, k16*z[1]*(6*z[1]**2 - 16*z[0]**2)], [np.log(M3), np.log(Mstar)], [gM, yt], dense_output=True, rtol=1e-10)
print('g, y at M*:', up.sol(np.log(Mstar)), flush=True)
def run(cH, Y2):
    def beta(c, g, y):
        lam = unflat(c); L2 = pair3((lam.reshape(nR*nR, nR*nR) @ lam.reshape(nR*nR, nR*nR)).reshape((nR,)*4))
        sC = C2S; s4 = sC[:, None, None, None] + sC[None, :, None, None] + sC[None, None, :, None] + sC[None, None, None, :]
        rest = -3*g**2*lam*s4 + y**2*contractY2(lam, Y2)
        cq, _ = proj(L2 + rest); return k16*(cq + g**4*cA + y**4*cH)
    ts = np.linspace(np.log(Mstar), np.log(M3), 61); c = np.zeros(rank)
    for t0, t1 in zip(ts[:-1], ts[1:]):
        h = t1 - t0; fb = lambda t, c: beta(c, *up.sol(t))
        k1 = fb(t0, c); k2 = fb(t0 + h/2, c + h/2*k1); k3 = fb(t0 + h/2, c + h/2*k2); k4 = fb(t1, c + h*k3); c = c + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return unflat(c)
def vmin(lam):
    L2d = lam.reshape(nR*nR, nR*nR)
    Vb = lambda P: np.einsum('bi,ij,bj->b', np.einsum('ba,bc->bac', P, P).reshape(len(P), -1), L2d, np.einsum('ba,bc->bac', P, P).reshape(len(P), -1))/24
    best, bu = np.inf, None
    for _ in range(20):
        P = rng.normal(size=(1000, nR)); P /= np.linalg.norm(P, axis=1)[:, None]; v = Vb(P); i = int(v.argmin())
        if v[i] < best: best, bu = float(v[i]), P[i]
    def fun(v):
        n = np.linalg.norm(v); u = v/n; val = Vb(u[None])[0]; g = np.einsum('abcd,b,c,d->a', lam, u, u, u)/6; return val, (g - u*np.dot(g, u))/n
    for _ in range(40):
        rr = minimize(fun, rng.normal(size=nR), jac=True, method='BFGS', options=dict(maxiter=300))
        if rr.fun < best: best, bu = float(rr.fun), rr.x/np.linalg.norm(rr.x)
    return best, bu
def yfree_overlap(u, r):
    # real components: J maps real -> complex; complex field z = J @ phi. Yukawa-free combination: r*H1 - H2 (r = 0: H2)
    z = J @ u; h1, h2 = z[:9], z[9:]
    if r == 0: return float(np.linalg.norm(h2)**2/np.linalg.norm(z)**2)
    w = (r*h1 - h2)/np.sqrt(1 + r*r)                 # coefficient along the Yukawa-free combination (per component)
    return float(np.linalg.norm(w)**2/np.linalg.norm(z)**2)
res = {}
for k, (cH, rH, Y2) in pre_.items():
    lam = run(cH, Y2); m, u = vmin(lam)
    r = 0.0 if ('S2' in k or 'r=0' in k) else float(k.split('r=')[1])
    res[k] = dict(min_V=m, yfree_overlap=yfree_overlap(u, r)); print(k, res[k], flush=True)
out['S2'] = dict(**res['S2 (t106: quark term on H1)'], pass_=abs(res['S2 (t106: quark term on H1)']['min_V']/-0.014 - 1) < 0.10)
out['P1'] = dict(**res['P1 r=0 (full cubic on H1)'], pass_=res['P1 r=0 (full cubic on H1)']['min_V'] < 0)
out['P2'] = dict(r05=res['P2 r=0.5'], r1=res['P2 r=1.0'], pass_=res['P2 r=0.5']['min_V'] < 0 and res['P2 r=1.0']['min_V'] < 0)
out['P3'] = dict(overlaps=[res[k]['yfree_overlap'] for k in res if not k.startswith('S2')], pass_=all(res[k]['yfree_overlap'] >= 0.9 for k in res if not k.startswith('S2')))
for k, v in out.items(): print(k, v)

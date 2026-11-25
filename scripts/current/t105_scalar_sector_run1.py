"""t105: Higgs mass from the full scalar sector above the meeting. One-loop general-formula engine (Machacek-Vaughn) on component tensors.
Pre-registration: PREDICTIONS_t105.md."""
import os, itertools, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
k16 = 1/(16*np.pi**2); KAPPA = 0.5
def gm(n):
    G = []
    for i in range(n):
        for j in range(i + 1, n):
            A = np.zeros((n, n), complex); A[i, j] = A[j, i] = 1; G.append(A/2)
            B = np.zeros((n, n), complex); B[i, j] = -1j; B[j, i] = 1j; G.append(B/2)
    for d in range(1, n):
        D = np.zeros((n, n), complex); D[:d, :d] = np.eye(d); D[d, d] = -d; G.append(D/np.sqrt(2*d*(d + 1)))
    return G
def realgen(T):
    """complex generator T (z -> T z) to the imaginary antisymmetric theta on phi = (Re z, Im z) * sqrt2."""
    TR, TI = T.real, T.imag
    R = np.block([[TI, TR], [-TR, TI]]); return 1j*R
def scalar_from_complex(n):
    """d z_k / d phi_a, phi = (x, y), z = (x + i y)/sqrt2: returns n x 2n complex matrix."""
    J = np.zeros((n, 2*n), complex); J[:, :n] = np.eye(n)/np.sqrt(2); J[:, n:] = 1j*np.eye(n)/np.sqrt(2); return J
def pair3(X):
    """X_abcd -> X_abcd + X_acbd + X_adbc."""
    return X + X.transpose(0, 2, 1, 3) + X.transpose(0, 3, 1, 2)
class Model:
    def __init__(s, thetas, fgens, Ytens, basis):
        s.th = thetas                      # list of (coupling_name, theta matrix) for scalars
        s.fg = fgens                       # list of (coupling_name, fermion generator) (complex, hermitian)
        s.Y = Ytens                        # list of (coupling_name, Y^a array [a, j, k]) at unit coupling
        s.B = basis                        # list of quartic basis tensors
        s.Bf = np.array([b.ravel() for b in basis]).T
    def proj(s, T):
        c, res, *_ = np.linalg.lstsq(s.Bf, T.ravel().real, rcond=None)
        r = np.linalg.norm(s.Bf @ c - T.ravel().real)/max(np.linalg.norm(T.ravel()), 1e-300); return c, r
    def beta_lambda(s, lams, g, y):
        lam = sum(l*b for l, b in zip(lams, s.B))
        L2 = pair3(np.einsum('abef,efcd->abcd', lam, lam))
        thg = [g[n]*t for n, t in s.th]
        C2S = sum(t @ t for t in thg).real
        LS = (np.einsum('aa,abcd->abcd', np.diag(np.diag(C2S)), lam) if False else
              lam*(np.diag(C2S)[:, None, None, None] + np.diag(C2S)[None, :, None, None] + np.diag(C2S)[None, None, :, None] + np.diag(C2S)[None, None, None, :]))
        S = [(ta @ tb + tb @ ta).real for ta in thg for tb in thg]
        X = sum(np.einsum('ab,cd->abcd', m, m) for m in S); A = pair3(X)
        Ya = sum(y[n]*Yt for n, Yt in s.Y)
        if np.any(Ya):
            Yd = np.conj(Ya.transpose(0, 2, 1))
            T4 = np.einsum('aij,bjk,ckl,dli->abcd', Ya, Yd, Ya, Yd)
            Hs = sum(T4.transpose(p) for p in itertools.permutations(range(4)))/4
            Y2 = 0.5*np.real(np.einsum('aij,bji->ab', Yd, Ya) + np.einsum('bij,aji->ab', Yd, Ya))
            y2 = np.diag(Y2); LY = lam*(y2[:, None, None, None] + y2[None, :, None, None] + y2[None, None, :, None] + y2[None, None, None, :])
        else:
            Hs = 0; LY = 0
        beta = L2 - 8*KAPPA*np.real(Hs) + 2*KAPPA*LY - 3*LS + 3*A
        return k16*beta
    def beta_y(s, g, y, name):
        Ya = sum(y[n]*Yt for n, Yt in s.Y); Yd = np.conj(Ya.transpose(0, 2, 1))
        Y2F = np.einsum('bij,bjk->ik', Yd, Ya)
        Y2S = 0.5*(np.einsum('aij,bji->ab', Yd, Ya) + np.einsum('bij,aji->ab', Yd, Ya))
        C2F = sum((g[n]**2)*(t @ t) for n, t in s.fg)
        b = (0.5*(np.einsum('ij,ajk->aik', Y2F.T, Ya) + np.einsum('aij,jk->aik', Ya, Y2F))
             + 2*np.einsum('bij,ajk,bkl->ail', Ya, Yd, Ya) + 2*KAPPA*np.einsum('bij,ba->aij', Ya, Y2S)
             - 3*(np.einsum('ij,ajk->aik', C2F, Ya) + np.einsum('aij,jk->aik', Ya, C2F)))
        Yb = dict(s.Y)[name]; c = np.vdot(Yb.ravel(), b.ravel())/np.vdot(Yb.ravel(), Yb.ravel())
        return k16*c.real
def quartic_tensor(pairs, n):
    """V = sum c (phi^T A phi)(phi^T B phi) with A, B complex symmetric; returns the real 4-tensor d^4 V."""
    T = np.zeros((n, n, n, n))
    for c, A, B in pairs:
        A = (A + A.T)/2; B = (B + B.T)/2
        X = np.einsum('ab,cd->abcd', A, B); X = X + X.transpose(2, 3, 0, 1)
        T += 4*c*np.real(pair3(X))
    return T
# ---------------- S1: Standard Model limit ----------------
def sm_model():
    nS = 2; J = scalar_from_complex(nS)
    th = [('g2', realgen(t)) for t in gm(2)] + [('gp', realgen(0.5*np.eye(2, dtype=complex)))]
    # fermions: Q (a, alpha) 6, tc (a) 3; total 9
    nF = 9; Qidx = lambda a, al: 2*a + al; tidx = lambda a: 6 + a
    fg = []
    for t in gm(3):
        M = np.zeros((nF, nF), complex); M[:6, :6] = np.kron(t, np.eye(2)); M[6:, 6:] = -t.T; fg.append(('g3', M))
    for t in gm(2):
        M = np.zeros((nF, nF), complex); M[:6, :6] = np.kron(np.eye(3), t); fg.append(('g2', M))
    M = np.zeros((nF, nF), complex); M[:6, :6] = np.eye(6)/6; M[6:, 6:] = -2/3*np.eye(3); fg.append(('gp', M))
    eps = np.array([[0, 1], [-1, 0]])
    Y = np.zeros((2*nS, nF, nF), complex)
    for a in range(3):
        for al in range(2):
            for be in range(2):
                if eps[al, be] == 0: continue
                for p in range(2*nS):
                    v = eps[al, be]*J[be, p]
                    Y[p, tidx(a), Qidx(a, al)] += v; Y[p, Qidx(a, al), tidx(a)] += v
    # V = lam (H^dag H)^2 : H^dag H = phi^T (J^dag J) phi (real part)
    P = np.real(J.conj().T @ J); B = quartic_tensor([(1.0, P, P)], 2*nS)
    return Model(th, fg, [('yt', Y)], [B])
sm = sm_model(); rng = np.random.default_rng(105); ok = True; worst = 0
for _ in range(5):
    g = dict(g2=rng.uniform(.3, .8), gp=rng.uniform(.2, .5), g3=rng.uniform(.5, 1.2)); y = dict(yt=rng.uniform(.3, 1.)); lam = rng.uniform(-.2, .3)
    bl = sm.proj(sm.beta_lambda([lam], g, y))[0][0]
    G2, GP, YT = g['g2']**2, g['gp']**2, y['yt']
    ref = k16*(24*lam**2 - 6*YT**4 + 12*lam*YT**2 - 3*lam*(GP + 3*G2) + 3/8*(2*G2**2 + (G2 + GP)**2))
    by = sm.beta_y(g, y, 'yt'); refy = k16*YT*(9/2*YT**2 - 8*g['g3']**2 - 9/4*G2 - 17/12*GP)
    worst = max(worst, abs(bl - ref)/abs(ref), abs(by - refy)/abs(refy))
out = {'S1': dict(max_rel_err=worst, pass_=worst < 1e-9)}
print('S1', out['S1'], flush=True)
# ---------------- trinification model ----------------
def tri_model():
    nH = 9; J = scalar_from_complex(nH); I3 = np.eye(3)
    th = [('g', realgen(np.kron(t, I3))) for t in gm(3)] + [('g', realgen(-np.kron(I3, t.T))) for t in gm(3)]
    nF = 18                                   # Q (a,i) 0..8 ; Qc (a,r) 9..17
    fg = []
    for t in gm(3):                           # colour
        M = np.zeros((nF, nF), complex); M[:9, :9] = np.kron(t, I3); M[9:, 9:] = -np.kron(t.T, I3); fg.append(('g', M))
    for t in gm(3):                           # L acts on Q's i
        M = np.zeros((nF, nF), complex); M[:9, :9] = -np.kron(I3, t.T); fg.append(('g', M))
    for t in gm(3):                           # R acts on Qc's r
        M = np.zeros((nF, nF), complex); M[9:, 9:] = np.kron(I3, t); fg.append(('g', M))
    Y = np.zeros((2*nH, nF, nF), complex)
    for a in range(3):
        for i in range(3):
            for r in range(3):
                for p in range(2*nH):
                    v = J[3*i + r, p]
                    Y[p, 3*a + i, 9 + 3*a + r] += v; Y[p, 9 + 3*a + r, 3*a + i] += v
    # invariants: I1 = (Tr H^dag H)^2 ; I2 = sum_rs |(H^dag H)_rs|^2
    P = np.real(J.conj().T @ J)
    B1 = quartic_tensor([(1.0, P, P)], 2*nH)
    pairs = []
    for r in range(3):
        for s_ in range(3):
            M = np.zeros((2*nH, 2*nH), complex)
            for i in range(3):
                M += np.outer(J[3*i + r].conj(), J[3*i + s_])          # (H^dag H)_rs = sum_i conj(H_ir) H_is
            A = M; Bc = M.conj()                                         # |X|^2 = X * conj(X); X = phi^T M phi (phi real)
            pairs.append((1.0, A, Bc))
    B2 = quartic_tensor(pairs, 2*nH)
    return Model(th, fg, [('y', Y)], [B1, B2])
tri = tri_model()
# S2: direction-based gauge coefficient from the engine's A tensor along phi = Re H_11
g1 = dict(g=1.0); A = tri.beta_lambda([0, 0], g1, dict(y=0.0))/k16      # pure gauge term (3 A) when lambdas vanish
e = np.zeros(18); e[0] = 1.0; c_dir = np.einsum('abcd,a,b,c,d->', A, e, e, e, e)/6*(0.5)**0
# V = lam |H_11|^4 = lam (phi0^2/2)^2 = lam phi0^4/4 -> d^4 V = 6 lam; so beta_lambda(dir) = (d^4 beta)/6
out['S2'] = dict(c_engine=c_dir, c_t102=17/3, pass_=abs(c_dir - 17/3) < 1e-9)
print('S2', out['S2'], flush=True)
# closure check
bt = tri.beta_lambda([0.1, -0.05], dict(g=0.6), dict(y=0.5)); _, resid = tri.proj(bt); print('closure residual', resid, flush=True)
# ---------------- running ----------------
src = open('t101_higgs_full.py').read(); ns = {'__file__': os.path.abspath('t101_higgs_full.py')}; exec(src[:src.index('\nout = {}')], ns)
beta_sm, lam_mt, make_beta = ns['beta_sm'], ns['lam_mt'], ns['make_beta']
Mstar = 2.435e18; MH, nHp, MD, M3 = 1.0e3, 2, 3.16e12, 4.98e13; Mt = 172.57
def low_to_M3(mh):
    y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(mh, Mt)]
    s = solve_ivp(make_beta(MH, nHp, MD, None, 0), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12); return s.y[:, -1]
def coeffs():
    """precompute beta_lambda as polynomial: quadratic in lambdas, g^4, y^4, y^2 lambda, g^2 lambda."""
    C = {}
    for name, (l, g, y) in dict(l11=([1, 0], 0, 0), l22=([0, 1], 0, 0), l12=([1, 1], 0, 0), g4=([0, 0], 1, 0), y4=([0, 0], 0, 1)).items():
        C[name] = tri.proj(tri.beta_lambda(l, dict(g=g), dict(y=y)))[0]
    C['l12'] = C['l12'] - C['l11'] - C['l22']
    # linear pieces: beta at (l, g, 0) minus quadratic minus g^4 part, per unit
    for i, l in enumerate(([1e-3, 0], [0, 1e-3])):
        bg = tri.proj(tri.beta_lambda(l, dict(g=1.0), dict(y=0.0)))[0] - C['g4']
        by = tri.proj(tri.beta_lambda(l, dict(g=0.0), dict(y=1.0)))[0] - C['y4']
        quad = (C['l11']*l[0]**2 + C['l22']*l[1]**2 + C['l12']*l[0]*l[1])
        C[f'gl{i}'] = (bg - quad)/1e-3; C[f'yl{i}'] = (by - quad)/1e-3
    C['by_y3'] = tri.beta_y(dict(g=0.0), dict(y=1.0), 'y'); C['by_g2y'] = tri.beta_y(dict(g=1.0), dict(y=1e-6), 'y')/1e-6
    return C
C = coeffs()
print('beta coefficients (per 16 pi^2 already applied):', {k: np.round(v/k16, 6).tolist() if np.ndim(v) else round(v/k16, 6) for k, v in C.items()}, flush=True)
def bl(l, g, y):
    return (C['l11']*l[0]**2 + C['l22']*l[1]**2 + C['l12']*l[0]*l[1] + C['g4']*g**4 + C['y4']*y**4
            + g**2*(C['gl0']*l[0] + C['gl1']*l[1]) + y**2*(C['yl0']*l[0] + C['yl1']*l[1]))
def predict(nh, mh_guess=125.2):
    g1, g2, g3, yt, _ = low_to_M3(mh_guess); g = float(np.mean([g3, g2, np.sqrt(5/3)*g1])); b = -5 + nh
    up = solve_ivp(lambda t, z: [b*k16*z[0]**3, C['by_y3']*z[1]**3 + C['by_g2y']*z[0]**2*z[1]], [np.log(M3), np.log(Mstar)], [g, yt], dense_output=True, rtol=1e-10, atol=1e-12)
    def rhs(t, l):
        gg, yy = up.sol(t); return list(bl(l, gg, yy))
    down = solve_ivp(rhs, [np.log(Mstar), np.log(M3)], [0.0, 0.0], rtol=1e-10, atol=1e-13)
    l1, l2 = down.y[:, -1]
    if l1 + l2 <= 0: return dict(l1=l1, l2=l2, lsm=None, mh=None)
    lsm = (l1 + l2) - l1**2/(l1 + l2)
    yM3 = up.sol(np.log(M3))[1]
    s = solve_ivp(make_beta(MH, nHp, MD, None, 0), [np.log(M3), np.log(Mt)], [g1, g2, g3, yM3, lsm], rtol=1e-10, atol=1e-12)
    lmt = s.y[4, -1]; mh = 125.15 + (lmt - 0.12604 + 0.00004*(Mt - 173.34))/0.00206
    return dict(l1=float(l1), l2=float(l2), lsm=float(lsm), mh=float(mh))
res = {}
for nh in range(4):
    r = predict(nh)
    if r['mh'] is not None: r = predict(nh, r['mh'])
    res[nh] = r; print('n_h', nh, r, flush=True)
out['P1'] = dict(mh={nh: (round(r['mh'], 2) if r['mh'] is not None else None) for nh, r in res.items()},
                 pass_=all(r['mh'] is not None and abs(r['mh'] - 125.20) <= 1.0 for r in res.values()))
for k, v in out.items(): print(k, v)

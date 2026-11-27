"""t177: m(0++)/sqrt(sigma) for SU(2) and for its binary icosahedral subgroup 2I, Wilson action, beta = 2.4, 8^4.
Pre-registration: PREDICTIONS_t177.md. Usage: python3 t177_glueball.py SU2|2I"""
import numpy as np, sys, time, json
L, BETA, THERM, MEAS = 8, 2.4, 300, 4000
group = sys.argv[1]
rng = np.random.default_rng(1771 if group == 'SU2' else 1772)

def qmul(a, b):
    a0, a1, a2, a3 = np.moveaxis(a, -1, 0); b0, b1, b2, b3 = np.moveaxis(b, -1, 0)
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0], -1)
def cj(a): return a*np.array([1., -1, -1, -1])
def sh(A, mu, s): return np.roll(A, -s, axis=mu)                 # A(x + s mu)

def closure(gens):
    G = {tuple(np.round([1., 0, 0, 0], 9))}; P = [np.array([1., 0, 0, 0])]; fr = list(P)
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h); k = tuple(np.round(p, 9) + 0.0)
                if k not in G: G.add(k); P.append(p); new.append(p)
        fr = new
    return np.array(P)
phi = (1 + 5**0.5)/2
G2I = closure([np.array([.5, .5, .5, .5]), np.array([phi/2, 1/(2*phi), .5, 0])])
assert len(G2I) == 120

U = np.zeros((4, L, L, L, L, 4)); U[..., 0] = 1.0
idx = np.indices((L, L, L, L)).sum(0) % 2

def staple(U, mu):
    S = np.zeros_like(U[0])
    for nu in range(4):
        if nu == mu: continue
        S += qmul(qmul(sh(U[nu], mu, 1), cj(sh(U[mu], nu, 1))), cj(U[nu]))
        S += qmul(qmul(cj(sh(sh(U[nu], mu, 1), nu, -1)), cj(sh(U[mu], nu, -1))), sh(U[nu], nu, -1))
    return S

def kp_x0(alpha):
    out = np.empty_like(alpha); todo = np.arange(alpha.size)
    while todo.size:
        a = alpha[todo]; r1, r2, r3, r4 = (1 - rng.random((4, todo.size)))
        lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3))/(2*a)
        ok = r4**2 <= 1 - lam2
        out[todo[ok]] = 1 - 2*lam2[ok]; todo = todo[~ok]
    return out

def heatbath(a):
    """a: (n,4) = conj(staple); returns links with weight exp(beta <u, a>)."""
    if group == 'SU2':
        k = np.linalg.norm(a, axis=1); v = a/k[:, None]
        x0 = kp_x0(BETA*k); d = rng.normal(size=(len(k), 3)); d /= np.linalg.norm(d, axis=1)[:, None]
        X = np.concatenate([x0[:, None], d*np.sqrt(np.clip(1 - x0**2, 0, None))[:, None]], 1)
        return qmul(X, v)
    logits = BETA*(a @ G2I.T) + rng.gumbel(size=(len(a), 120))
    return G2I[np.argmax(logits, 1)]

def sweep(U):
    for mu in range(4):
        for par in (0, 1):
            m = idx == par
            a = cj(staple(U, mu))[m]
            U[mu][m] = heatbath(a)

def plaq(U):
    s = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(cj(sh(U[mu], nu, 1)), cj(U[nu])))
            s += P[..., 0].mean()
    return s/6

def line(U, mu, n):
    out = U[mu].copy()
    for k in range(1, n): out = qmul(out, sh(U[mu], mu, k))
    return out

def wloops(U, Rmax=4):
    W = np.zeros((Rmax + 1, Rmax + 1)); cnt = 0
    lines = {(mu, n): line(U, mu, n) for mu in range(4) for n in range(1, Rmax + 1)}
    for mu in range(4):
        for nu in range(4):
            if mu == nu: continue
            for R in range(1, Rmax + 1):
                for T in range(1, Rmax + 1):
                    w = qmul(qmul(lines[(mu, R)], sh(lines[(nu, T)], mu, R)), qmul(cj(sh(lines[(mu, R)], nu, T)), cj(lines[(nu, T)])))
                    W[R, T] += w[..., 0].mean()
            cnt += 1
    return W/cnt

def ape(U, steps=4, alpha=0.5):
    V = U.copy()
    for _ in range(steps):
        N = V.copy()
        for i in (1, 2, 3):
            S = np.zeros_like(V[i])
            for j in (1, 2, 3):
                if j == i: continue
                S += qmul(qmul(V[j], sh(V[i], j, 1)), cj(sh(V[j], i, 1)))
                S += qmul(qmul(cj(sh(V[j], j, -1)), sh(V[i], j, -1)), sh(sh(V[j], j, -1), i, 1))
            X = V[i] + alpha*S
            N[i] = X/np.linalg.norm(X, axis=-1, keepdims=True)
        V = N
    return V

def glue_op(U):
    V = ape(U); O = np.zeros(L)
    for i in (1, 2, 3):
        for j in range(i + 1, 4):
            P = qmul(qmul(V[i], sh(V[j], i, 1)), qmul(cj(sh(V[i], j, 1)), cj(V[j])))
            O += P[..., 0].sum(axis=(1, 2, 3))
    return O

t0 = time.time()
for s in range(THERM): sweep(U)
plaqs, Ws, Os = [], [], []
for s in range(MEAS):
    sweep(U)
    plaqs.append(plaq(U))
    if s % 2 == 0: Os.append(glue_op(U))
    if s % 5 == 0: Ws.append(wloops(U))
    if s % 500 == 0: print(group, 'sweep', s, 'plaq %.5f' % plaqs[-1], 'sec %d' % (time.time() - t0), flush=True)
np.savez('t177_%s.npz' % group, plaq=np.array(plaqs), W=np.array(Ws), O=np.array(Os))
print(group, 'done', 'sec %d' % (time.time() - t0))

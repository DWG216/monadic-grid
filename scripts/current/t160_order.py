"""t160: the record does not depend on how it is sliced. Pre-registration: PREDICTIONS_t160.md.
Events sprinkled in a 1+1 diamond; each event's monad state comes from its linked past by t134's rules."""
import numpy as np
Nev, Nt, will = 400, 16, 0.2
rng0 = np.random.default_rng(1600)
# sprinkle in the diamond |t| + |x| < 1 via null coordinates
u, v = rng0.random(Nev), rng0.random(Nev)
t, x = (u + v)/np.sqrt(2) - 1/np.sqrt(2), (v - u)/np.sqrt(2)
prec = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])          # i precedes j
C = prec.astype(int); between = C@C                                    # number of elements strictly between
link = prec & (between == 0)
p0 = rng0.uniform(0.5, 1.5, (Nev, Nt)); p0 /= p0.sum(1, keepdims=True)
phi0 = rng0.uniform(0, 2*np.pi, (Nev, Nt)); a0 = 10**rng0.uniform(-2, 0, Nev)

def update(j, P, PHI, A, src, eta, rng):
    if len(src) == 0: return P[j], PHI[j], A[j]
    c = np.sqrt(P[src])*np.exp(1j*PHI[src]); z = c.sum(0); den = P[src].sum(0)
    w = np.abs(z)**2/den
    phi = PHI[j] + np.minimum(will*A[j]*Nt*P[j], 1.0)*np.sin(np.angle(z) - PHI[j])
    if eta: phi = phi + eta*rng.standard_normal(Nt)
    e = (P[j]*w).sum()/w.mean(); a = np.clip(A[j]*e, 1/600, 1.0)
    p = P[j]*w**a; p = p/p.sum()
    return p, phi, a

def run_links(order, eta=0.0, seed=0):
    rng = np.random.default_rng(seed); P, PHI, A = p0.copy(), phi0.copy(), a0.copy()
    for j in order:
        P[j], PHI[j], A[j] = update(j, P, PHI, A, np.where(link[:, j])[0], eta, rng)
    return np.concatenate([P.ravel(), np.cos(PHI).ravel(), A])

def linear_extension(seed):
    rng = np.random.default_rng(seed); indeg = prec.sum(0).astype(int); ready = list(np.where(indeg == 0)[0]); order = []
    while ready:
        k = rng.integers(len(ready)); j = ready.pop(k); order.append(j)
        for m in np.where(prec[j])[0]:
            indeg[m] -= 1
            if indeg[m] == 0: ready.append(m)
    return order

def run_slices(rap, width=0.05):
    """Foliation update: in the frame of rapidity rap, slice by that frame's time; each event reads the previous slice's
    states of its causal past (not its links): the update depends on where the slices fall."""
    tt = np.cosh(rap)*t - np.sinh(rap)*x
    sl = np.floor((tt - tt.min())/width).astype(int)
    P, PHI, A = p0.copy(), phi0.copy(), a0.copy(); rng = np.random.default_rng(0)
    for s in range(sl.max() + 1):
        idx = np.where(sl == s)[0]; prevmask = sl == s - 1
        newP, newPHI, newA = {}, {}, {}
        for j in idx:
            src = np.where(prec[:, j] & prevmask)[0]
            newP[j], newPHI[j], newA[j] = update(j, P, PHI, A, src, 0.0, rng)
        for j in idx: P[j], PHI[j], A[j] = newP[j], newPHI[j], newA[j]
    return np.concatenate([P.ravel(), np.cos(PHI).ravel(), A])

out = {}
o1, o2 = linear_extension(1), linear_extension(2)
r1, r2 = run_links(o1), run_links(o2)
out['S1'] = dict(max_diff=float(np.max(np.abs(r1 - r2))), orders_differ=o1 != o2, links=int(link.sum()), pass_=float(np.max(np.abs(r1 - r2))) < 1e-12 and o1 != o2)
n1, n2 = run_links(o1, eta=0.3, seed=7), run_links(o2, eta=0.3, seed=7)
out['P1'] = dict(max_diff=float(np.max(np.abs(n1 - n2))), pass_=float(np.max(np.abs(n1 - n2))) > 0.1)
s0, s8 = run_slices(0.0), run_slices(0.8)
# link update in the two frames: the order is the same set of relations, so the frame enters only via the extension chosen
def frame_order(rap):
    tt = np.cosh(rap)*t - np.sinh(rap)*x; return list(np.argsort(tt, kind='stable'))
l0, l8 = run_links(frame_order(0.0)), run_links(frame_order(0.8))
out['P2'] = dict(slices_diff=float(np.max(np.abs(s0 - s8))), links_diff=float(np.max(np.abs(l0 - l8))),
                 pass_=float(np.max(np.abs(s0 - s8))) > 0.1 and float(np.max(np.abs(l0 - l8))) < 1e-12)
for k, v in out.items(): print(k, v)

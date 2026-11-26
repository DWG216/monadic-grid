"""t159: topology change while the record is written vs at a closing. Pre-registration: PREDICTIONS_t159.md.
Dynamics: t134's age() with eta = 0 (t143c), with an optional permutation of neighbourhoods at tick `swap`."""
import numpy as np
from t128_community import nsum
L, N, T, r, will = 12, 64, 600, 2, 0.2
M = L*L

def age(rng, a, p, phi, swap=None, track=False):
    eps = 1/T; rec, laws = [], []
    for t in range(T):
        if swap is not None and t == swap:
            perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        c = np.sqrt(p)*np.exp(1j*phi); z = nsum(c, L, r); den = nsum(p, L, r)
        w = np.abs(z)**2/den
        if track:
            top = p.argmax(1); rec.append(w[np.arange(M), top].copy())
            order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2
            laws.append(float((order[np.arange(M), top] > 0.8).mean()))
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2
    top = p.argmax(1); held = order[np.arange(M), top] > 0.8
    comp = float(((a >= 0.5) & ((p**2).sum(1) > 0.8) & held).mean())
    return a, p, phi, comp, np.array(rec), np.array(laws)

def init(seed):
    rng = np.random.default_rng(seed)
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    return rng, a, p, phi

out = {'P1_M': [], 'P1_ctrl': [], 'P2': [], 'P3': []}
for s in range(59000, 59010):
    for variant in ('M', '0'):
        rng, a, p, phi = init(s)
        _, _, _, _, rec, laws = age(rng, a, p, phi, swap=300 if variant == 'M' else None, track=True)
        jump = np.mean(np.abs(rec[300] - rec[299])); base = np.median(np.abs(np.diff(rec[250:300], axis=0)).mean(1))
        (out['P1_M'] if variant == 'M' else out['P1_ctrl']).append(jump/base)
        if variant == 'M': out['P2'].append((laws[299], laws[300]))
    rng, a, p, phi = init(s)
    a, p, phi, c1, _, _ = age(rng, a, p, phi)
    perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
    a, p, phi, c2, _, _ = age(rng, a, p, phi)
    out['P3'].append((c1, c2))
    print(s, 'M jump/base', round(out['P1_M'][-1], 2), 'ctrl', round(out['P1_ctrl'][-1], 2), 'laws', out['P2'][-1], 'closing comp', out['P3'][-1], flush=True)
p1 = sum(x > 10 for x in out['P1_M']) == 10 and all(x <= 2 for x in out['P1_ctrl'])
p2 = sum((b < 0.5*a_) for a_, b in out['P2']) >= 8
p3 = sum(c2 > 0.9 for _, c2 in out['P3']) >= 8
print('P1', dict(M=[round(x, 2) for x in out['P1_M']], ctrl=[round(x, 2) for x in out['P1_ctrl']], pass_=p1))
print('P2', dict(laws_before_after=out['P2'], pass_=p2))
print('P3', dict(completeness=out['P3'], pass_=p3))

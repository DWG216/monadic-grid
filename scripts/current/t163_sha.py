"""t163: a monad analogue of Sha and the rank. Pre-registration: PREDICTIONS_t163.md. Dynamics: t134's age() with eta = 0."""
import numpy as np
from t128_community import nsum
L, N, T, r, will = 24, 64, 600, 2, 0.2
M = L*L

def age(a, p, phi):
    eps = 1/T
    for t in range(T):
        c = np.sqrt(p)*np.exp(1j*phi); z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den; e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    return a, p, phi

def measure(p, phi):
    order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2
    top = p.argmax(1); held = order[np.arange(M), top] > 0.8
    rank = sha = 0; G = {}
    for k in np.unique(top[held]):
        h = np.where(held & (top == k))[0]
        if len(h) < 5: continue
        g = float(np.abs(np.exp(1j*phi[h, k]).mean())); G[int(k)] = round(g, 3)
        rank += g > 0.8; sha += g < 0.5
    return int(rank), int(sha), G

res = {}
for s in range(63000, 63006):
    for variant in ('B', 'A'):
        rng = np.random.default_rng(s)
        a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
        rows = []
        for g in range(4):
            if g > 0:
                if variant == 'A':
                    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
                else:
                    perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
            a, p, phi = age(a, p, phi)
            rank, sha, G = measure(p, phi); rows.append((rank, sha))
        res[s, variant] = rows
        print(s, variant, 'rank, sha per Age:', rows, 'final G:', G, flush=True)
p1 = sum(res[s, 'B'][0][1] >= 1 for s in range(63000, 63006)) >= 5
p2 = sum(res[s, 'B'][-1] == (1, 0) for s in range(63000, 63006)) >= 5
p3 = sum(res[s, 'A'][-1][1] >= 1 for s in range(63000, 63006)) >= 4
print('P1', dict(sha_age1=[res[s, 'B'][0][1] for s in range(63000, 63006)], pass_=p1))
print('P2', dict(final_B=[res[s, 'B'][-1] for s in range(63000, 63006)], pass_=p2))
print('P3', dict(final_A=[res[s, 'A'][-1] for s in range(63000, 63006)], pass_=p3))

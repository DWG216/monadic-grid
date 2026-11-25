"""t124: deriving the monads' rules from the record |O+R|^2 (identity checks, no fit).
Monad j at frequency k: c_jk = sqrt(p_jk) e^{i phi_jk}; record R_k = |sum_j c_jk|^2 = diagonal + cross terms.
(1) Without the meeting (phases unrelated) the cross terms average to zero: E[R_k] = sum_j p_jk. So
    w_k = R_k / sum_j p_jk = 1 + (cross terms)/(diagonal): what the meeting adds at k.
(2) Listening: an update p_k -> p_k g(w_k) / Z that (a) acts on each frequency alike (no frequency privileged) and (b) gives the
    same result whether a record is read at once or as independent parts (Born weights of independent parts multiply)
    needs g(w1 w2) = g(w1) g(w2), so g(w) = w^beta (Cauchy's multiplicative equation, g continuous). beta is the capacity.
(3) Turning: dR_k/dphi_jk = -2 sqrt(p_jk) |S_-j| sin(phi_jk - arg S_-j), S_-j = sum_{l != j} c_lk: the phase change that
    raises the record turns toward the others' phase; t116's rule is this ascent (with arg z for arg S_-j)."""
import numpy as np
rng = np.random.default_rng(124); M, N = 50, 16; out = {}
p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True)
R = np.array([np.abs((np.sqrt(p)*np.exp(1j*rng.uniform(0, 2*np.pi, (M, N)))).sum(0))**2 for _ in range(20000)]).mean(0)
out['1 E[R_k]/sum_j p_jk (random phases)'] = (float(np.min(R/p.sum(0))), float(np.max(R/p.sum(0))))
q = rng.dirichlet(np.ones(N)); w1, w2 = rng.uniform(0.2, 5, N), rng.uniform(0.2, 5, N); nz = lambda x: x/x.sum()
for name, g in (('power w^0.3', lambda w: w**0.3), ('exponential e^(0.3 w)', lambda w: np.exp(0.3*w)), ('additive 1 + 0.3 w', lambda w: 1 + 0.3*w)):
    out[f'2 split vs whole, {name}'] = float(np.abs(nz(nz(q*g(w1))*g(w2)) - nz(q*g(w1*w2))).max())
phi = rng.uniform(0, 2*np.pi, (M, N)); j, k, h = 3, 5, 1e-6
def Rk(ph): return np.abs((np.sqrt(p[:, k])*np.exp(1j*ph[:, k])).sum())**2
ph2 = phi.copy(); ph2[j, k] += h; ph1 = phi.copy(); ph1[j, k] -= h; fd = (Rk(ph2) - Rk(ph1))/(2*h)
S = (np.sqrt(p[:, k])*np.exp(1j*phi[:, k])).sum() - np.sqrt(p[j, k])*np.exp(1j*phi[j, k])
out['3 finite difference vs formula'] = (float(fd), float(-2*np.sqrt(p[j, k])*np.abs(S)*np.sin(phi[j, k] - np.angle(S))))
for a, b in out.items(): print(a, b)

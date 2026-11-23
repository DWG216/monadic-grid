import sys
import numpy as np
from core import *

Qm, A, B = find_Q()
print("Q det", np.linalg.det(Qm), "orth err", np.abs(Qm @ Qm.T - np.eye(3)).max())
orb = orbit(n_tau, R_phys)
print("orbit size", len(orb))
targets_bloch = (Qm @ orb.T).T
# sanity: logical class invariant under logical group
inv = max(min(np.linalg.norm(r @ t - s) for s in targets_bloch) for r in R_tw for t in targets_bloch[:5])
print("logical class invariant under logical rotations err", inv)
targets = [bloch_state(v) for v in targets_bloch]

Ux = bloch_unitary(n_tau)


def setup(N, rep=U_tw):
    C = Code(N, rep)
    Dx = Dmat(Ux, C.J)  # columns = Dicke states in x basis
    return C, Dx


def amps(C, V, Dx):
    return V.conj().T @ Dx  # 2 x (N+1): V^dag |D_k^x>


def out_err(amp, w, eps, N):
    wp = np.array([-np.conj(w[1]), np.conj(w[0])])
    k = np.arange(N + 1)
    wt = np.exp(k * np.log(eps) + (N - k) * np.log1p(-eps))
    p = np.sum(wt * np.sum(np.abs(amp) ** 2, 0))
    bad = np.sum(wt * np.abs(wp.conj() @ amp) ** 2)
    return bad / p, p


def design(C, Dx, r):
    """For each target, null space of order-r conditions, max acceptance at eps->0"""
    best = None
    z0 = Dx[:, 0]
    a = C.B0.conj().T @ z0
    b = C.B0.conj().T @ C.P[1, 0].conj().T @ z0
    for ti, w in enumerate(targets):
        wp = np.array([-np.conj(w[1]), np.conj(w[0])])
        U = []
        for k in range(r):
            psi = Dx[:, k]
            u = np.conj(wp[0]) * (C.B0.conj().T @ psi) + np.conj(wp[1]) * (C.B0.conj().T @ C.P[1, 0].conj().T @ psi)
            U.append(u)
        U = np.array(U).T  # m x r ; condition c^dag u_k = 0
        if r > 0:
            uu, ss, vh = np.linalg.svd(U, full_matrices=True)
            rank = int(np.sum(ss > 1e-10 * max(1, ss.max())))
            Nsp = uu[:, rank:]
        else:
            Nsp = np.eye(C.m)
        if Nsp.shape[1] == 0:
            continue
        M = np.outer(a, a.conj()) + np.outer(b, b.conj())
        Mr = Nsp.conj().T @ M @ Nsp
        ev, evec = np.linalg.eigh(Mr)
        c = Nsp @ evec[:, -1]
        p0 = ev[-1]
        if best is None or p0 > best[0] + 1e-12:
            best = (p0, ti, c, Nsp.shape[1])
    return best


def kl_resid(V, J, degree):
    Jx, Jy, Jz = J
    ops = [Jx, Jy, Jz]
    As = list(ops)
    if degree >= 2:
        As += [P @ Qo for P in ops for Qo in ops]
    res = 0
    for Aop in As:
        M = V.conj().T @ Aop @ V
        res = max(res, np.abs(M - np.trace(M) / 2 * np.eye(2)).max())
    return res


def cz_leak(V, N):
    f = cz_factor(N)
    worst = 0
    for i in range(2):
        for j in range(2):
            vi, vj = V[:, i], V[:, j]
            tot = 0
            for ip in range(2):
                for jp in range(2):
                    amp = V[:, ip].conj() @ (f * np.outer(vi, vj)) @ V[:, jp].conj()
                    tot += abs(amp) ** 2
            worst = max(worst, 1 - tot)
    return worst


def threshold(amp, w, N):
    es = np.linspace(1e-4, 0.499, 49891)
    ok = [out_err(amp, w, e, N)[0] < e for e in es]
    ok = np.array(ok)
    if not ok.any():
        return None
    return es[np.where(ok)[0].max()], ok


def report(N, r):
    C, Dx = setup(N)
    print(f"\n=== N={N}, m={C.m}, order r={r}")
    p0, ti, c, nd = design(C, Dx, r)
    V = C.V(c)
    print("cov err", C.cov_err(V), "orthonorm err", np.abs(V.conj().T @ V - np.eye(2)).max(), "nullspace dim", nd,
          "p(eps->0)", p0, "target idx", ti)
    amp = amps(C, V, Dx)
    w = targets[ti]
    wp = np.array([-np.conj(w[1]), np.conj(w[0])])
    print("|<w_perp|V^dag D_k>| k=0..4:", np.abs(wp.conj() @ amp)[:5])
    e3, p3 = out_err(amp, w, 1e-3, N)
    e4, _ = out_err(amp, w, 1e-4, N)
    print("err(1e-3)", e3, "err(1e-4)", e4, "exponent", np.log10(e3 / e4), "p(1e-3)", p3)
    print("err(0.5)", out_err(amp, w, 0.5, N)[0])
    th = threshold(amp, w, N)
    if th:
        t, ok = th
        print("threshold (largest eps<0.499 with err<eps)", t, "; contiguous from small eps?", ok[:np.where(ok)[0].max() + 1].all())
    print("KL deg1 resid", kl_resid(V, C.J, 1), "KL deg<=2 resid", kl_resid(V, C.J, 2))
    print("CZ leak", cz_leak(V, N))
    return C, V, Dx


if __name__ == "__main__":
    # Task 2: N=7
    C, Dx = setup(7)
    c = np.ones(C.m)
    V = C.V(c)
    print("N=7 m", C.m, "cov err", C.cov_err(V))
    amp = amps(C, V, Dx)
    for eps in (1e-3, 1e-4):
        errs = [out_err(amp, w, eps, 7)[0] for w in targets]
        print(f"N=7 eps={eps}: min err over class {min(errs)} (idx {int(np.argmin(errs))}), p {out_err(amp, targets[0], eps, 7)[1]}")
    e3 = min(out_err(amp, w, 1e-3, 7)[0] for w in targets)
    e4 = min(out_err(amp, w, 1e-4, 7)[0] for w in targets)
    print("N=7 exponent", np.log10(e3 / e4))
    # where is logical output at eps->0 ?
    v0 = amp[:, 0] / np.linalg.norm(amp[:, 0])
    rho = np.outer(v0, v0.conj())
    bl = np.real([np.trace(rho @ S) for S in (X, Y, Z)])
    print("N=7 eps->0 logical Bloch", bl, "max |dot| with class", np.max(np.abs(targets_bloch @ bl)))
    print("N=7 KL deg1", kl_resid(V, C.J, 1), "deg2", kl_resid(V, C.J, 2))

    report(67, 2)
    report(67, 1)
    # Task 5: untwisted control at N=11
    Cu = Code(11, U_phys)
    print("\nUntwisted N=11 m", Cu.m)
    rng = np.random.default_rng(0)
    for t in range(3):
        c = rng.normal(size=Cu.m) + 1j * rng.normal(size=Cu.m)
        Vu = Cu.V(c)
        print(" cov err", Cu.cov_err(Vu), "KL deg1 resid", kl_resid(Vu, Cu.J, 1))
    if len(sys.argv) > 1:
        report(97, 3)

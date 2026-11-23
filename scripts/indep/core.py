import numpy as np
from itertools import permutations, product
from scipy.stats import hypergeom

phi = (1 + 5 ** 0.5) / 2
phip = 1 - phi  # Galois conjugate

# coordinates as (a,b) meaning a + b*phi
HALF = (0.5, 0.0)
INVPHI_HALF = (-0.5, 0.5)   # (phi-1)/2 = 1/(2 phi)
PHI_HALF = (0.0, 0.5)
ZERO = (0.0, 0.0)


def neg(x):
    return (-x[0], -x[1])


def icosians():
    out = []
    for i in range(4):
        for s in (1, -1):
            q = [ZERO] * 4
            q[i] = (float(s), 0.0)
            out.append(q)
    for signs in product((1, -1), repeat=4):
        out.append([(0.5 * s, 0.0) for s in signs])
    base = [ZERO, HALF, INVPHI_HALF, PHI_HALF]
    even = [p for p in permutations(range(4))
            if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
    for p in even:
        for signs in product((1, -1), repeat=3):
            v = [base[0], base[1] if signs[0] > 0 else neg(base[1]),
                 base[2] if signs[1] > 0 else neg(base[2]),
                 base[3] if signs[2] > 0 else neg(base[3])]
            q = [v[p[i]] for i in range(4)]
            out.append(q)
    return out


Q = icosians()
assert len(Q) == 120
QN = np.array([[a + b * phi for a, b in q] for q in Q])
QT = np.array([[a + b * phip for a, b in q] for q in Q])
assert len({tuple(np.round(r, 9)) for r in QN}) == 120
assert np.allclose(np.sum(QN ** 2, 1), 1) and np.allclose(np.sum(QT ** 2, 1), 1)

X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def su2(q):
    a, b, c, d = q
    return a * I2 - 1j * (b * X + c * Y + d * Z)


U_phys = np.array([su2(q) for q in QN])
U_tw = np.array([su2(q) for q in QT])


def index_of(Ulist, U):
    d = np.abs(Ulist - U).reshape(len(Ulist), -1).max(1)
    i = int(np.argmin(d))
    assert d[i] < 1e-9
    return i


# multiplication table and twist homomorphism check
MT = np.zeros((120, 120), int)
for i in range(120):
    for k in range(120):
        MT[i, k] = index_of(U_phys, U_phys[i] @ U_phys[k])
hom_err = max(np.abs(U_tw[i] @ U_tw[k] - U_tw[MT[i, k]]).max() for i in range(120) for k in range(120))


def spin_ops(j2):
    """j2 = 2j = N. basis k=0..N, m=j-k."""
    j = j2 / 2
    m = j - np.arange(j2 + 1)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((j2 + 1, j2 + 1), complex)
    for k in range(1, j2 + 1):  # |m+1> <- |m>, index k-1 <- k
        mm = m[k]
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - mm * (mm + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return Jx, Jy, Jz


def Dmat(U, J):
    """D^j(U) for U in SU(2), via U = exp(-i theta/2 n.sigma) -> exp(-i theta n.J)."""
    a = np.real((U[0, 0] + U[1, 1]) / 2)
    # U = a I - i(b X + c Y + d Z)
    b = np.real(1j * (U[0, 1] + U[1, 0]) / 2)
    c = np.real((U[1, 0] - U[0, 1]) / 2)  # -i c (Y) : Y01=-i -> U01 has -c... compute robustly below
    # robust: coefficients via traces
    b = np.real(1j * np.trace(U @ X) / 2)
    c = np.real(1j * np.trace(U @ Y) / 2)
    d = np.real(1j * np.trace(U @ Z) / 2)
    s = np.sqrt(b * b + c * c + d * d)
    theta = 2 * np.arctan2(s, a)
    Jx, Jy, Jz = J
    dim = Jz.shape[0]
    if s < 1e-14:
        return np.eye(dim) * (1 if a > 0 else (-1) ** (dim - 1))
    n = np.array([b, c, d]) / s
    H = n[0] * Jx + n[1] * Jy + n[2] * Jz
    w, v = np.linalg.eigh(H)
    w = np.round(w * 2) / 2  # exact half-integers
    return (v * np.exp(-1j * theta * w)) @ v.conj().T


def rot(U):
    """SO(3) matrix of U: U sigma_k U^dag = sum_l R_lk sigma_l"""
    S = [X, Y, Z]
    return np.array([[np.real(np.trace(S[l] @ U @ S[k] @ U.conj().T)) / 2 for k in range(3)] for l in range(3)])


def mult(N, rep=U_tw):
    chi = np.real(np.trace(rep, axis1=1, axis2=2))
    a = QN[:, 0]
    th = 2 * np.arccos(np.clip(a, -1, 1))
    j2 = N
    chij = np.empty(120)
    for i, t in enumerate(th):
        if abs(np.sin(t / 2)) < 1e-12:
            chij[i] = (j2 + 1) * (1 if np.cos(t / 2) > 0 else (-1) ** j2)
        else:
            chij[i] = np.sin((j2 + 1) * t / 2) / np.sin(t / 2)
    return np.sum(chi * chij) / 120


class Code:
    def __init__(self, N, rep=U_tw):
        self.N = N
        self.J = spin_ops(N)
        self.D = np.array([Dmat(U, self.J) for U in U_phys])
        self.rep = rep
        self.P = {}
        for a in range(2):
            for b in range(2):
                self.P[a, b] = (2 / 120) * np.einsum('g,gij->ij', rep[:, a, b].conj(), self.D)
        w, v = np.linalg.eigh((self.P[0, 0] + self.P[0, 0].conj().T) / 2)
        self.B0 = v[:, w > 0.5]
        self.m = self.B0.shape[1]

    def V(self, c):
        c = c / np.linalg.norm(c)
        z = self.B0 @ c
        o = self.P[1, 0] @ z
        return np.stack([z, o], 1)

    def cov_err(self, V):
        return max(np.abs(self.D[g] @ V - V @ self.rep[g]).max() for g in range(120))


# tau60 physical state
n_tau = np.array([1, 1, 2 + phi]) / np.sqrt(7 + 5 * phi)
T60 = np.array([[2 + phi, 1 - 1j], [1 + 1j, -(2 + phi)]]) / np.sqrt(7 + 5 * phi)


def bloch_state(n):
    th = np.arccos(np.clip(n[2], -1, 1))
    ph = np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def bloch_unitary(n):
    x = bloch_state(n)
    xb = np.array([-np.conj(x[1]), np.conj(x[0])])
    return np.stack([x, xb], 1)


R_phys = np.array([rot(U) for U in U_phys])
R_tw = np.array([rot(U) for U in U_tw])


def fivefold_axes(R):
    axes = []
    for r in R:
        ang = np.arccos(np.clip((np.trace(r) - 1) / 2, -1, 1))
        if abs(ang - 2 * np.pi / 5) < 1e-8:
            w, v = np.linalg.eig(r)
            ax = np.real(v[:, np.argmin(np.abs(w - 1))])
            ax /= np.linalg.norm(ax)
            if not any(abs(abs(ax @ a) - 1) < 1e-8 for a in axes):
                axes.append(ax)
    return np.array(axes)


def frame(a, b):
    e1 = a / np.linalg.norm(a)
    e2 = b - (b @ e1) * e1
    e2 /= np.linalg.norm(e2)
    return np.stack([e1, e2, np.cross(e1, e2)], 1)


def find_Q():
    A = fivefold_axes(R_phys)
    B = fivefold_axes(R_tw)
    assert len(A) == 6 and len(B) == 6
    a1, a2 = A[0], A[1]
    dot = a1 @ a2
    for b1 in B:
        for b2 in B:
            for s1 in (1, -1):
                for s2 in (1, -1):
                    if abs((s1 * b1) @ (s2 * b2) - dot) > 1e-9:
                        continue
                    Qm = frame(s1 * b1, s2 * b2) @ frame(a1, a2).T
                    if all(any(abs(abs((Qm @ a) @ b) - 1) < 1e-9 for b in B) for a in A):
                        return Qm, A, B
    raise RuntimeError


def orbit(n, R):
    pts = []
    for r in R:
        for s in (1, -1):
            p = s * (r @ n)
            if not any(np.linalg.norm(p - q) < 1e-9 for q in pts):
                pts.append(p)
    return np.array(pts)


def cz_factor(N):
    f = np.zeros((N + 1, N + 1))
    for k in range(N + 1):
        for l in range(N + 1):
            o = np.arange(0, min(k, l) + 1)
            pm = hypergeom(N, k, l).pmf(o)
            f[k, l] = np.sum(pm * (-1.0) ** o)
    return f

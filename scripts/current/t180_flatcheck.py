"""t180: horizon molecules with the record's own past-count as 'now' (Milne sprinkling, null-plane horizon).
Pre-registration: PREDICTIONS_t180.md."""
import numpy as np
rng = np.random.default_rng(1802)
N0, C, W, RUNS = 170, 6.0, 2.0, 40
def prec(A, B):            # A[i] precedes B[j]
    dt = B[None, :, 0] - A[:, None, 0]; d2 = ((B[None, :, 1:] - A[:, None, 1:])**2).sum(-1)
    return (dt > 0) & (dt*dt > d2)
dens, s1 = [], []
for run in range(RUNS):
    n = rng.poisson(8*12**3)
    P = np.column_stack([8*rng.random(n), -6 + 12*rng.random((n, 3))])
    P = P[P[:, 0] > np.linalg.norm(P[:, 1:], axis=1)]
    u = P[:, 0] - P[:, 1]
    S = np.where((np.abs(u - C) < 2.5) & (np.abs(P[:, 2]) < 4) & (np.abs(P[:, 3]) < 4))[0]
    cnt = np.zeros(len(S), int)
    for a in range(0, len(S), 400):
        cnt[a:a + 400] = prec(P, P[S[a:a + 400]]).sum(0)
    tau = np.sqrt(np.clip(P[S, 0]**2 - (P[S, 1:]**2).sum(1), 0, None))
    s1.extend(cnt[np.abs(tau - 6) < 0.1].tolist())
    inD = P[S, 0] < 6.0   # code check: flat slice t = 6 (t166 geometry)
    SD = S[inD]; uD = u[SD]
    R = prec(P[SD], P[SD])                         # R[i, j]: SD[i] precedes SD[j]
    m = 0
    for i in np.where(uD < C)[0]:
        fut = np.where(R[i])[0]
        if len(fut) == 1:
            j = fut[0]
            if uD[j] > C and abs(P[SD[j], 2]) < W and abs(P[SD[j], 3]) < W: m += 1
    dens.append(m/(2*W)**2)
dens = np.array(dens); mean, se = dens.mean(), dens.std(ddof=1)/np.sqrt(len(dens))
print('S1', dict(mean_count_tau6=float(np.mean(s1)), expected=np.pi*6**4/24, rel=abs(np.mean(s1)/(np.pi*6**4/24) - 1), n=len(s1), pass_=abs(np.mean(s1)/(np.pi*6**4/24) - 1) < 0.05))
print('P1', dict(density=mean, se=se, target=np.sqrt(3)/10, z=(mean - np.sqrt(3)/10)/se, pass_=abs(mean - np.sqrt(3)/10) < 3*se))

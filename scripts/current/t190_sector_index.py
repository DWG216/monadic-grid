"""t190: one integer per sector fixes amplitude and phase? See PREDICTIONS_t190.md."""
import numpy as np

rng = np.random.default_rng(190)
N = 100_000
up = [(1.23e-3, 0.21e-3), (0.620, 0.017), (168.26, 0.75)]      # GeV, Huang-Zhou Table 2, M_Z
down = [(2.67e-3, 0.19e-3), (53.16e-3, 4.61e-3), (2.839, 0.026)]

def chord(ms):  # as t98: ms shape (3, ...) sorted light to heavy
    s = np.sqrt(np.asarray(ms, float)); A = s.mean(0); x = s / A - 1
    z = (2/3) * sum(x[k] * np.exp(-2j*np.pi*k/3) for k in range(3))
    c, d = np.abs(z), np.angle(z) % (2*np.pi/3)
    d = np.minimum(d, 2*np.pi/3 - d)
    return A, c, d

def masses(c, d):
    return np.sort([(1 + c*np.cos(d + 2*np.pi*k/3))**2 for k in range(3)])

def draw(sector):
    out = []
    for c0, s in sector:
        x = rng.normal(c0, s, 2*N); out.append(x[x > 0][:N])
    return np.array(out)

res = {}
for name, sector, n in [("down", down, 2), ("up", up, 3)]:
    A, c, d = chord(draw(sector))
    target = (2/9) * 2.0**(1 - n)
    z = (d.mean() - target) / d.std()
    print(f"{name}: c = {c.mean():.4f} +- {c.std():.4f} (sqrt(n+1/n) = {np.sqrt(n+1/n):.4f}); "
          f"delta = {d.mean():.4f} +- {d.std():.4f}, target {target:.4f}, z = {z:+.2f}")
    res[name + "_phase"] = abs(z) <= 2
    p = masses(np.sqrt(n + 1/n), target); p = p / p[2] * sector[2][0]
    for i, lab in enumerate(["light", "middle"]):
        c0, s = sector[i]
        zz = (p[i] - c0) / s
        print(f"  predicted {lab} mass {p[i]*1e3:.4g} MeV against {c0*1e3:.4g} +- {s*1e3:.2g} MeV, z = {zz:+.1f}")
        res[f"{name}_{lab}"] = abs(zz) <= 2

print()
print("P1 (delta_d ~ 1/9):", "PASS" if res["down_phase"] else "FAIL")
print("P2 (delta_u ~ 1/18):", "PASS" if res["up_phase"] else "FAIL")
p3 = res["down_light"] and res["down_middle"] and res["up_middle"]
print("P3 (m_d, m_s, m_c from n and the heaviest):", "PASS" if p3 else "FAIL", "(m_u reported, not scored)")

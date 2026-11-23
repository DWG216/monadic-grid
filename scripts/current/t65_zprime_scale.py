"""t65: the Z'_psi scale from the grid (pre-registration: PREDICTIONS_t65.md).

Rebuilt 2026-11-23 from the inline run that produced t65_run1.log; it reproduces that log.
D2 inputs (bridge): Dirac masses = up-type quark masses, pole and indicative high-scale values.
"""
import math

m1 = 0.365e-3                                  # eV, lightest neutrino (record section 125)
m2 = math.sqrt(m1**2 + 7.50e-5)                # eV
m3 = 59.16e-3 - m1 - m2                        # eV, from the sum 59.16 meV
print(f"m1 = {m1*1e3:.3f} meV, m2 = {m2*1e3:.2f} meV, m3 = {m3*1e3:.2f} meV")

pole = (2.16e-3, 1.27, 172.57)                 # GeV: u, c, t
high = (0.5e-3, 0.25, 80.0)                    # GeV: indicative running masses at a high scale
ev = 1e-9                                      # GeV per eV

def seesaw(mD):
    return [d**2 / (m * ev) for d, m in zip(mD, (m1, m2, m3))]

Rp, Rh = seesaw(pole), seesaw(high)
print("pole M_R1, M_R2, M_R3 (GeV): " + " ".join(f"{x:.2e}" for x in Rp))
print("high-scale M_R1, M_R2, M_R3 (GeV): " + " ".join(f"{x:.2e}" for x in Rh))
for g in (0.4, 0.5):
    print(f"g = {g}  M(Zpsi) ~ g*2*M_R3 = {g*2*Rp[2]:.1e} - {g*2*Rh[2]:.1e} GeV (with v_psi = M_R3)")

"""t123: the bridge from the Ages to the grid's physics. Numbers only (no fit, no free parameter).
Count: Lambda l_P^2 = 1/sqrt(N) (the grid's constant Lambda as the leftover of a fixed count of Planck 4-volumes, t72/t87).
Largest record: the de Sitter horizon entropy S_dS = 3 pi / (Lambda l_P^2) = 3 pi sqrt(N) (in k).
Written so far: S_obs = 3.1e104 k (Egan & Lineweaver 2010, ApJ 710, 1825); horizon today S_CEH = 2.6e122 k (same)."""
import numpy as np
c, G, hbar = 2.99792458e8, 6.67430e-11, 1.054571817e-34
H0 = 67.36e3/3.0856775814913673e22; OL = 0.6847                       # Planck 2018
Lam = 3*OL*H0**2/c**2; lp2 = hbar*G/c**3; x = Lam*lp2
N = x**-2; S_dS = 3*np.pi/x; S_obs, S_CEH = 3.1e104, 2.6e122
print(f'Lambda = {Lam:.4e} m^-2   Lambda l_P^2 = {x:.4e}')
print(f'count N = (Lambda l_P^2)^-2 = {N:.3e}   sqrt(N) = {np.sqrt(N):.3e}')
print(f'largest record S_dS = 3 pi sqrt(N) = {S_dS:.3e} k   (horizon today {S_CEH:.1e} k = {S_CEH/S_dS:.0%} of it)')
print(f'written inside so far S_obs = {S_obs:.1e} k = {S_obs/S_dS:.1e} of the largest record (log10 {np.log10(S_obs/S_dS):.1f})')
print(f'log10 S_dS / log10 N = {np.log10(S_dS)/np.log10(N):.4f}  (the root: 1/2 up to 3 pi)')

import numpy as np
# (1) grain size from Sakharov-Jacobson self-consistency: l_P^2 = G hbar/c^3 = pi a^2/(c_area N)
c_area=0.295   # t27, per real scalar degree of freedom (assumption: every dof contributes like a scalar)
dof_SM=4+2*12+2*45; dof_nuR=4+2*12+2*48
for name,N in [('SM, no nu_R',dof_SM),('SM + nu_R',dof_nuR)]:
    print(f'{name}: N = {N} dof  ->  a = l_P * sqrt(c N / pi) = {np.sqrt(c_area*N/np.pi):.2f} l_P')
# (2) Lambda from the count (Sorkin): Delta Lambda ~ 8 pi l_P^2 / (a^2 sqrt(V)), V = (c t0)^4 in l_P^4
lP=1.616e-35; t0=13.8e9*3.156e7; c=2.998e8
V=(c*t0/lP)**4
obs=1.1056e-52*lP**2
for a in [1.0,np.sqrt(c_area*dof_nuR/np.pi)]:
    print(f'a = {a:.2f} l_P: Lambda l_P^2 ~ 1/sqrt(V) = {1/np.sqrt(V):.2e};  with 8 pi/a^2: {8*np.pi/(a*a*np.sqrt(V)):.2e};  observed {obs:.2e}')
# (3) generations: CP-violating phases in an n-generation mixing matrix (Kobayashi-Maskawa counting)
for n in range(1,6):
    angles=n*(n-1)//2; phases=(n-1)*(n-2)//2
    print(f'n = {n}: mixing angles {angles}, irreducible CP phases {phases}')
# Weyl fermions per generation
print('Weyl fermions per generation: SM', 15, ' with nu_R', 16, ' (SO(10) spinor)')

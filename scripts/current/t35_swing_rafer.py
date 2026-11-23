import numpy as np
G=6.674e-11; c=2.998e8; hbar=1.0546e-34; eps0=8.854e-12
# geometric units G=c=1: Rafer(R)=sqrt(R^3/2M), Swing=sqrt(2R^3/M)=2 Rafer
M=1.0
Raf=lambda R: np.sqrt(R**3/(2*M)); Sw=lambda R: np.sqrt(2*R**3/M)
print('Swing/Rafer =',Sw(3.7)/Raf(3.7))
# exact radial free fall from rest at R in Schwarzschild: proper time tau = (pi/2) sqrt(R^3/2M); check by integrating dtau = dr / sqrt(2M/r - 2M/R)
for R in [3.0,10.0,50.0]:
    from scipy.integrate import quad
    tau=quad(lambda r: 1/np.sqrt(2*M/r-2*M/R),0,R,limit=200)[0]
    print(f'R={R}: integrated tau={tau:.6f}  (pi/2)Rafer={np.pi/2*Raf(R):.6f}')
print('R/v_esc at R=10:',10/np.sqrt(2*M/10),' Rafer(10)=',Raf(10))
# fixed point of R -> Rafer(R)
print('fixed point R=2M:',Raf(2*M),' slope there:',1.5*np.sqrt(2*M/(2*M)))
x=1.99; y=2.01
for i in range(6): x=Raf(x); y=Raf(y)
print('iterates from 1.99 ->',x,'  from 2.01 ->',y)
# impedances
mP=np.sqrt(hbar*c/G); tP=np.sqrt(hbar*G/c**5)
print('m_P/t_P =',mP/tP,' c^3/G =',c**3/G)
print('Planck electrical impedance 1/(4 pi eps0 c) =',1/(4*np.pi*eps0*c),' ohm; free space Z0 = 4pi x that =',1/(eps0*c))
Msun=1.989e30; Rs=2*G*Msun/c**2
print('black hole M/(Rs/c) =',Msun/(Rs/c),' c^3/(2G) =',c**3/(2*G))

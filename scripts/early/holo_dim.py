import numpy as np
from scipy.special import jv
from scipy.integrate import solve_ivp
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
# D1: radial solution of u_tt = Lap u in d dims, u(0)=0, u_t(0)=Gaussian width s, via Hankel transform
s=0.03; t=1.0
k=np.linspace(1e-6,400,200001); dk=k[1]-k[0]
def u(r,d):
    nu=d/2-1
    F=np.exp(-(k*s)**2/2)                      # Fourier transform of the Gaussian (up to constants)
    integrand=F*np.sin(k*t)/k * k**(d/2) * jv(nu,k*r)
    return (r**(1-d/2))*np.sum(integrand)*dk
print('D1 sharpness: tail inside the light cone relative to the peak on the cone (t = 1)')
res={}
for d in range(1,7):
    if d==1:
        # 1D: u = (1/2) * integral of initial velocity over [x-t, x+t]: exact
        from math import erf,sqrt
        g=lambda x: 0.5*(erf((x+t)/(sqrt(2)*s))-erf((x-t)/(sqrt(2)*s)))/2
        inside=[abs(g(r)) for r in np.linspace(0.05,t-6*s,40)]; peak=max(abs(g(r)) for r in np.linspace(t-6*s,t+6*s,200))
    else:
        rin=np.linspace(0.1,t-6*s,25); rpk=np.linspace(t-5*s,t+5*s,41)
        inside=[abs(u(r,d)) for r in rin]; peak=max(abs(u(r,d)) for r in rpk)
    ratio=max(inside)/peak; res[d]=ratio
    print('   d=%d: tail/peak = %.2e  -> %s'%(d,ratio,'sharp' if ratio<1e-3 else 'tail (blurred)'))
# D2: stability of perturbed circular orbits under F = -r^(1-d) (attractive), angular momentum fixed
print('D2 orbits: perturbed circular orbit (5% radial kick), 50 periods')
def orbit(d):
    r0=1.0; F=lambda r: -r**(1-d)
    L=np.sqrt(r0**3*(-F(r0)))       # circular: L^2/r^3 = |F|
    T=2*np.pi*r0**2/L
    def rhs(tt,y): r,v=y; return [v, L**2/r**3 + F(r)]
    sol=solve_ivp(rhs,[0,50*T],[r0,0.05],max_step=T/200,rtol=1e-9,atol=1e-12,events=lambda tt,y:y[0]-0.02)
    r=sol.y[0]; ok=(r.max()<2*r0) and (r.min()>r0/2) and sol.status==0
    return ok,r.min(),r.max()
for d in range(1,7):
    ok,a,b=orbit(d); print('   d=%d: radius range [%.3f, %.3f] -> %s'%(d,a,b,'stable' if ok else 'unstable'))
# D3: ground state of -1/2 Lap + V in d dims, l=0, V=-r^(2-d) (d!=2), log r (d=2); radial u = r^((d-1)/2) R
print('D3 quantum recorder: lowest energy as the grid is refined (falls without bound = no lasting atom)')
for d in range(1,7):
    Es=[]
    for N,rmin in ((2000,1e-2),(8000,2.5e-3),(32000,6e-4)):
        r=np.linspace(rmin,40,N); h=r[1]-r[0]
        if d==2: V=np.log(r)
        elif d==1: V=-np.abs(r)**1     # 1D Gauss law: V ~ -r^(1) grows... attractive linear confinement V=+r
        else: V=-r**(2.0-d)
        if d==1: V=np.abs(r)
        cent=((d-1)*(d-3)/8.0)/r**2
        main=1/h**2+V+cent; off=-0.5/h**2*np.ones(N-1)
        H=diags([off,main,off],[-1,0,1])
        E=eigsh(H,k=1,sigma=-1e6,which='LM',return_eigenvectors=False)[0] if d>=5 else eigsh(H,k=1,which='SA',return_eigenvectors=False)[0]
        Es.append(E)
    trend='bounded' if abs(Es[-1]-Es[-2])<0.05*max(1,abs(Es[-2])) else 'falls without bound'
    print('   d=%d: E0 = %s -> %s'%(d,', '.join('%.4g'%e for e in Es),trend))

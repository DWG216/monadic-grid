import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(1)
def psi(p,r,th):
    m,n,a=p; q=n+a*np.cos(th)
    return -(m+1j*n)/(r-1j*q)**3, -(m-1j*n)/(r+1j*q)**3
def F(x,pts):
    p=[x[0]+1j*x[1],x[2]+1j*x[3],x[4]+1j*x[5]]; out=[]
    for r,th in pts:
        P,Pt=psi(p,r,th); d=Pt-np.conj(P); out+= [d.real,d.imag]
    return np.array(out)
def rank_imag(pts,base=(1.0,0.4,0.7)):
    x0=np.array([base[0],0,base[1],0,base[2],0.]); J=np.zeros((2*len(pts),3)); e=1e-6
    for k,i in enumerate([1,3,5]):
        xp=x0.copy(); xp[i]+=e; xm=x0.copy(); xm[i]-=e; J[:,k]=(F(xp,pts)-F(xm,pts))/(2*e)
    s=np.linalg.svd(J,compute_uv=False); return int((s>1e-8*s[0]).sum()), s
def global_check(pts,trials=40):
    worst=0
    for _ in range(trials):
        x=rng.normal(size=6); x[[0,2,4]]=[1.0,0.4,0.7]   # fix real parts, start imag parts random
        f=lambda y: F(np.array([1.0,y[0],0.4,y[1],0.7,y[2]]),pts)
        sol=least_squares(f,x[[1,3,5]],xtol=1e-14,ftol=1e-14)
        if np.linalg.norm(sol.fun)<1e-9: worst=max(worst,np.abs(sol.x).max())
    return worst
rs=np.linspace(3,12,25)
sets={'P1 one null ray, th=1.0 (r sweeps)':[(r,1.0) for r in rs],
      'P2 null ray in equator, th=pi/2':[(r,np.pi/2) for r in rs],
      'P3 single event (r=5, th=1.0)':[(5.0,1.0)],
      'P4 radial timelike curve, th=1.0':[(r,1.0) for r in np.linspace(3,12,25)],
      'static observer worldline (r=5,th=1.0 fixed)':[(5.0,1.0)]*10}
print('Unknowns: imaginary parts of m, n, a (3). Rank 3 = reality forced.')
for name,pts in sets.items():
    rk,s=rank_imag(pts); w=global_check(pts)
    print('  %-45s rank %d/3 | largest leftover imaginary part over 40 random starts: %.1e'%(name,rk,w))
print('Note: P1 and P4 use the same (r, th) samples because the curvature depends only on r and th;')
print('a timelike curve that sweeps r at fixed th probes exactly the same values as the null ray.')
# P5 googly identity
for (m,n) in [(1j*0.5,0.5),(0,0)]:
    ok=all(abs(np.conj(psi([m,n,0.3],r,1.0)[0])-psi([m,n,0.3],r,1.0)[1])<1e-12 for r in rs)
    print('P5 self-dual member m=%s, n=%s: hand- = %.3g, |hand+| = %.3g at r=5 ; passes conjugate match: %s'%(m,n,abs(psi([m,n,0.3],5,1.0)[1]),abs(psi([m,n,0.3],5,1.0)[0]),ok))

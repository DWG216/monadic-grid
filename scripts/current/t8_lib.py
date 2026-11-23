import numpy as np
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
rho=0.5+1j*g; h=1e-5
Zp=np.array([(Z(t+h)-Z(t-h))/(2*h) for t in g]); zp=-1j*np.exp(-1j*theta(g))*Zp   # zeta'(rho)
taper=1-g/400.0
def S(u,wts): return np.array([2*np.real(np.sum(taper*wts*np.exp(1j*g*x))) for x in np.atleast_1d(u)])
def jumps(wts,ns,d=0.012): return np.array([S(np.log(n)+d,wts)[0]-S(np.log(n)-d,wts)[0] for n in ns])
def mu(n):
    r=1; m=n; p=2
    while p*p<=m:
        if m%p==0:
            m//=p
            if m%p==0: return 0
            r=-r
        p+=1
    return -r if m>1 else r
def lam(n):
    for p in range(2,n+1):
        if n%p==0:
            k=n
            while k%p==0: k//=p
            return np.log(p) if k==1 else 0.0

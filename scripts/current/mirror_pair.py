import numpy as np
from scipy.special import loggamma
def chi(s): return np.exp((-s/2)*np.log(np.pi)+loggamma(s/2)-(-(1-s)/2)*np.log(np.pi)-loggamma((1-s)/2))
for t in (14,100,400): print(f"M1 sigma=0.5 t={t}: |chi|-1 = {abs(chi(0.5+1j*t))-1:.2e}")
print(f"M1 sigma=0.6 t=100: ln|chi| = {np.log(abs(chi(0.6+100j))):.3f}")
def theta(t): return t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
def Z(t):
    a=np.sqrt(t/(2*np.pi)); N=int(np.floor(a)); p=a-N; n=np.arange(1,N+1)
    s=2*np.sum(np.cos(theta(t)-t*np.log(n))/np.sqrt(n))
    return s+(-1)**(N-1)*(t/(2*np.pi))**(-0.25)*np.cos(2*np.pi*(p*p-p-1/16))/np.cos(2*np.pi*p)
ts=np.arange(10,400,0.02); zs=np.array([Z(t) for t in ts]); zer=[]
for i in range(len(ts)-1):
    if zs[i]*zs[i+1]<0:
        a,b=ts[i],ts[i+1]
        for _ in range(45):
            m=(a+b)/2
            if Z(a)*Z(m)<=0: b=m
            else: a=m
        zer.append((a+b)/2)
g=np.array(zer); n=np.arange(1,len(g)+1); print("zeros:",len(g),"first",np.round(g[:3],4))
def lam(X):
    L=[]
    for m in range(2,X+1):
        for p in range(2,m+1):
            if m%p==0: break
        k=m; e=0
        while k%p==0: k//=p; e+=1
        if k==1: L.append((m,np.log(p)))
    return L
def S(T,X,fake=None,sign=1):
    if X<2: return 0*T
    out=0*T
    for idx,(m,lp) in enumerate(lam(X)):
        w=1-np.log(m)/np.log(X); ln=np.log(m) if fake is None else np.log(fake[idx])
        out+= w*lp*np.sin(T*ln)/(np.sqrt(m)*np.log(m))
    return -sign*out/np.pi
def res(Sv): return theta(g)/np.pi+Sv-(n-1.5)
r0=res(S(g,1)); rms0=np.sqrt(np.mean(r0**2))
out={}
for X in (1,10,100,1000):
    r=res(S(g,X)); out[X]=r; print(f"X={X}: RMS={np.sqrt(np.mean(r**2)):.4f}  frac|r|<0.5={np.mean(np.abs(r)<0.5):.4f}")
rng=np.random.default_rng(20261114); fake=rng.integers(2,1001,size=len(lam(1000)))
rN1=res(S(g,1000,fake=fake)); rN2=res(S(g,1000,sign=-1))
print(f"N1 fake primes: RMS={np.sqrt(np.mean(rN1**2)):.4f} ratio to smooth={np.sqrt(np.mean(rN1**2))/rms0:.3f}")
print(f"N2 sign flipped: RMS={np.sqrt(np.mean(rN2**2)):.4f}")
np.save("mp_resid.npy",np.vstack([g,out[1],out[1000]]))

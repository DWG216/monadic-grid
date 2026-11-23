# Round 6 library: zeros to height H with the same Riemann-Siegel Z as mirror_pair.py; operator tools from t10_lib.
import numpy as np
from scipy.special import jv
src=open('mirror_pair.py').read(); exec(src[src.index('def theta'):src.index('ts=np.arange')])
def zeros_to(H,lo=10,step=0.02):
    ts=np.arange(lo,H,step); zs=np.array([Z(t) for t in ts]); out=[]
    for i in np.where(zs[:-1]*zs[1:]<0)[0]:
        a,b=ts[i],ts[i+1]
        for _ in range(45):
            m=(a+b)/2
            if Z(a)*Z(m)<=0: b=m
            else: a=m
        out.append((a+b)/2)
    return np.array(out)
def zeta_prime(g,h=1e-5):
    Zp=np.array([(Z(t+h)-Z(t-h))/(2*h) for t in g]); return -1j*np.exp(-1j*theta(g))*Zp
_t10=open('t10_lib.py').read(); exec(_t10[_t10.index('def jacobi'):])   # jacobi, eigerr, tri, kpm, old_detector, peak
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
def op_jumps(g,c,ns,K=None,d=0.012):
    """jumps of S(u) = 2 Re <f, exp(iuJ) e1> at u = ln n; J from |c| (entries only), f carries the phases; K = keep top-left K x K block."""
    p=np.abs(c); a,b,Q=jacobi(g,p); f=Q@(np.conj(c)*np.sqrt(p.sum()/p))
    if K is not None: a,b,f=a[:K],b[:K-1],f[:K]
    Sx=lambda x: 2*np.real(kpm(a,b,f,np.array([x])))[0]
    return np.array([Sx(np.log(n)+d)-Sx(np.log(n)-d) for n in ns])
def shuffle_spacings(g,rng): return np.concatenate([[g[0]],g[0]+np.cumsum(rng.permutation(np.diff(g)))])
from math import factorial
_B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510]
def zeta_em(s,N=None,terms=8):
    """zeta(s) by Euler-Maclaurin (complex s != 1)."""
    if N is None: N=int(abs(s.imag)/np.pi)+200 if isinstance(s,complex) else 60
    n=np.arange(1,N); tot=np.sum(n**(-s))+N**(1-s)/(s-1)+0.5*N**(-s)
    fac=s; pw=N**(-s-1)
    for k in range(1,terms+1):
        tot+=_B[k-1]/factorial(2*k)*fac*pw
        fac*= (s+2*k-1)*(s+2*k); pw/=N*N
    return tot
def Dpeak(gg,w,u0):
    """plant detector: |S_w - S_uniform| at u0 over its window median; both read from operator entries (kpm). S_w = <e1,exp(iuJ_w)e1>."""
    e=np.zeros(len(gg)); e[0]=1
    a,b,_=jacobi(gg,w); a1,b1,_=jacobi(gg,np.ones(len(gg)))
    Df=lambda u: kpm(a,b,e,u).real-kpm(a1,b1,e,u).real
    return peak(Df,u0)

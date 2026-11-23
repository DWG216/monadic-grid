import numpy as np
from math import gamma
rng=np.random.default_rng(1)
def sprinkle(d,N):  # uniform points in the causal diamond between (0,0) and (1,0) in d-dim Minkowski
    pts=[]
    while len(pts)<N:
        t=rng.random(); x=rng.uniform(-0.5,0.5,d-1); r=np.linalg.norm(x)
        if r<t and r<1-t: pts.append(np.r_[t,x])
    return np.array(pts)
def relations(P):
    dt=P[:,0][None,:]-P[:,0][:,None]; dx=np.linalg.norm(P[None,:,1:]-P[:,None,1:],axis=2)
    return (dt>dx)   # i precedes j
def f_of_d(d): return gamma(d+1)*gamma(d/2)/(2*gamma(3*d/2))
def dim_from_f(f):
    ds=np.linspace(1.2,6,5000); return ds[np.argmin(abs(np.array([f_of_d(x) for x in ds])-f))]
def longest_chain(R,P):
    order=np.argsort(P[:,0]); L=np.zeros(len(P),int)
    Ro=R[np.ix_(order,order)]
    for j in range(len(P)):
        prev=np.nonzero(Ro[:j,j])[0]; L[j]=1+(L[prev].max() if len(prev) else 0)
    return L.max()
print(' d | N    | ordering fraction | predicted | dimension recovered | longest chain (time from counting)')
for d in (2,3,4):
    P=sprinkle(d,1500); R=relations(P); N=len(P)
    f=R.sum()/(N*(N-1)/2); print('%2d | %d | %.4f | %.4f | %.2f | %d'%(d,N,f,f_of_d(d),dim_from_f(f),longest_chain(R,P)))

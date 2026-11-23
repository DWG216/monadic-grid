import numpy as np
N=10**7; g=0.5772156649015329
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
Lam=np.zeros(N+1)
for p in np.nonzero(s)[0]:
    q=int(p)
    while q<=N: Lam[q]=np.log(p); q*=int(p)
def ratios(L):
    A=np.cumsum(L/np.maximum(np.arange(N+1),1)); P=np.cumsum(L)
    xs=np.unique(np.round(np.logspace(2,7,200)).astype(int))
    G=xs*A[xs]-P[xs]-xs*np.log(xs)+(1+g)*xs
    return xs,G,np.abs(G-np.log(2*np.pi))/np.sqrt(xs)
xs,G,r=ratios(Lam)
print(f"G1 max |G-log2pi|/sqrt x = {r.max():.4f} at x = {xs[r.argmax()]}; G2 >0.02: {r.max()>0.02}")
m=xs>=1000; print(f"G3 max G/sqrt x for x>=1e3 = {(G[m]/np.sqrt(xs[m])).max():.4f}; all G<=sqrt x: {np.all(G[m]<=np.sqrt(xs[m]))}")
print("sample:",[(int(x),round(float(v),3)) for x,v in zip(xs[::40],G[::40])])
rng=np.random.default_rng(20261120); n=np.arange(N+1); pr=np.zeros(N+1,bool); pr[3:]=rng.random(N-2)<1/np.log(n[3:]); pr[2]=True
Lr=np.where(pr,np.log(np.maximum(n,2)),0.0)
_,_,rr=ratios(Lr); print(f"N1 Cramer max ratio = {rr.max():.4f}")

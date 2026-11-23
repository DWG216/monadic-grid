import math, numpy as np
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]
# T2
g=np.diff(P); p=P[:-1]; m=p>3; ratio=g[m]/((22/25)*np.sqrt(p[m])*np.log(p[m]))
i=int(np.argmax(ratio)); print(f"T2 primes<1e8: {len(P)}; max gap/((22/25)sqrt(p)ln p) = {ratio[i]:.4f} at p={int(p[m][i])}, gap={int(g[m][i])}; largest gap {int(g.max())} at p={int(p[int(np.argmax(g))])}")
# T1
Q=P[(P>2)&(P<10**7)]; worst=0; tot=0; viol=0
for q in Q.tolist():
    a=2
    while pow(a,(q-1)//2,q)==1: a+=1
    tot+=a; r=a/(2*math.log(q)**2)
    if r>worst: worst,wq,wa=r,q,a
    if a>2*math.log(q)**2: viol+=1
print(f"T1 primes 3..1e7: {len(Q)}; violations of n(p)<=2(ln p)^2: {viol}; mean n(p) = {tot/len(Q):.4f}; max n(p)/(2 ln^2 p) = {worst:.4f} at p={wq} (n={wa})")
# T3
def sprp(n,a):
    d=n-1; s_=0
    while d%2==0: d//=2; s_+=1
    x=pow(a,d,n)
    if x in (1,n-1): return True
    for _ in range(s_-1):
        x=x*x%n
        if x==n-1: return True
    return False
fail=0; psp2=0
for n in range(9,10**6,2):
    if s[n]: continue
    if sprp(n,2): psp2+=1
    B=int(2*math.log(n)**2)
    if all(sprp(n,a) for a in range(2,min(B,n-2)+1)): fail+=1
print(f"T3 odd composites <1e6: Bach-bound Miller-Rabin failures = {fail}; strong pseudoprimes to base 2 = {psp2}")
# T4
mod=P%5; xs=np.arange(1000,10**7+1,1000)
nr=np.cumsum((mod==2)|(mod==3)); rr=np.cumsum((mod==1)|(mod==4))
idx=np.searchsorted(P,xs,side='right')-1; lead=(nr[idx]-rr[idx])>0
w=1/xs; print(f"T4 share of sampled x with non-residues ahead: {lead.mean():.4f}; log-density estimate on [1e3,1e7]: {(w*lead).sum()/w.sum():.4f}")
# post hoc (labelled): the T2 maximum comes from tiny primes; the same ratio for p > 1000
mm=p>1000; r2=g[mm]/((22/25)*np.sqrt(p[mm])*np.log(p[mm])); j=int(np.argmax(r2))
print(f"post hoc T2 p>1000: max ratio {r2[j]:.4f} at p={int(p[mm][j])}, gap={int(g[mm][j])}")

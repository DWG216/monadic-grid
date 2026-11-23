import numpy as np
N=10**7
mu=np.ones(N+1,dtype=np.int8); isp=np.ones(N+1,bool); isp[:2]=False
for p in range(2,N+1):
    if isp[p]:
        isp[p*p::p]=False if p*p<=N else isp[p*p::p]
        mu[p::p]*=-1
        if p*p<=N: mu[p*p::p*p]=0
mu[0]=0
# S1
M1=10**5; spf=np.zeros(M1+1,int)
for p in range(2,M1+1):
    if spf[p]==0: spf[p::p][spf[p::p]==0]=p
bad=0
divsum=np.zeros(M1+1,int)
for d in range(1,M1+1):
    if mu[d]: divsum[d::d]+=mu[d]
bad=int(np.count_nonzero(divsum[2:]))
# explicit pairing check on sample: toggling smallest prime p of n maps squarefree divisor d to d*p or d/p, flips sign, no fixed points
ok=True
for n in range(2,3001):
    p=spf[n]; ds=[d for d in range(1,n+1) if n%d==0 and mu[d]!=0]
    for d in ds:
        e=d//p if d%p==0 else d*p
        if e not in ds or mu[e]!=-mu[d] or e==d: ok=False
print("S1 nonzero divisor sums for 1<n<=1e5:",bad,"| pairing involution valid n<=3000:",ok,"| sum at n=1:",divsum[1])
# S2
n=np.arange(1,10**6+1,dtype=float); m=mu[1:10**6+1].astype(float)
for b in (2,3):
    z=np.sum(n**-b)+ (10**6)**(1-b)/(b-1); s=np.sum(m*n**-b)
    print(f"S2 b={b}: zeta*sum mu n^-b = {z*s:.8f}")
# S3
M=np.cumsum(mu[1:].astype(np.int64)); x=np.arange(1,N+1)
r=np.abs(M[99:])/np.sqrt(x[99:]); i=np.argmax(r)
print("S3 max |M|/sqrt x (100..1e7):",round(r[i],4),"at x =",i+100,"| M(1e7) =",M[-1])
# S4
rng=np.random.default_rng(20261114); sq=(mu[1:]!=0)
for pp,lab in ((0.5,"fair"),(0.51,"biased 0.51")):
    sg=np.where(rng.random(N)<pp,1,-1)*sq
    S=np.cumsum(sg); rr=np.abs(S[99:])/np.sqrt(x[99:])
    print(f"S4 {lab}: max|S|/sqrt x = {rr.max():.3f}, S(1e7)/sqrt(1e7) = {S[-1]/np.sqrt(N):.2f}")

import numpy as np
N=2_000_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
primes=np.nonzero(sieve)[0].tolist()
def U(n,P,Q,m):  # Lucas U_n(P,Q) mod m via matrix power of [[P,-Q],[1,0]]
    a,b,c,d=1,0,0,1; x,y,z,w=P%m,(-Q)%m,1,0
    while n:
        if n&1: a,b,c,d=(a*x+b*z)%m,(a*y+b*w)%m,(c*x+d*z)%m,(c*y+d*w)%m
        x,y,z,w=(x*x+y*z)%m,(x*y+y*w)%m,(z*x+w*z)%m,(z*y+w*w)%m
        n>>=1
    return c   # [[U_{n+1},..],[U_n,..]]
def leg(a,p): return 0 if a%p==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
out={}
for name,P,Q,D in [('golden phi (Fibonacci)',1,-1,5),('silver 1+sqrt2 (Pell)',2,-1,8),('2+sqrt3 (tetrahedral face)',4,1,12)]:
    hits=[]
    for p in primes:
        if p<=3 or D%p==0: continue
        e=p-leg(D,p); mm=p*p
        if U(e,P,Q,mm)%mm==0: hits.append(p)
    out[name]=hits; print('%-28s Wieferich-type primes below 2,000,000: %s'%(name,hits),flush=True)

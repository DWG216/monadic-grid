import numpy as np, math
N=2_000_000
sv=np.ones(N+1,bool); sv[:2]=False
for i in range(2,int(N**.5)+1):
    if sv[i]: sv[i*i::i]=False
primes=[p for p in np.nonzero(sv)[0].tolist() if p>5]
def U(n,P,Q,m):
    a,b,c,d=1,0,0,1; x,y,z,w=P%m,(-Q)%m,1,0
    while n:
        if n&1: a,b,c,d=(a*x+b*z)%m,(a*y+b*w)%m,(c*x+d*z)%m,(c*y+d*w)%m
        x,y,z,w=(x*x+y*z)%m,(x*y+y*w)%m,(z*x+w*z)%m,(z*y+w*w)%m
        n>>=1
    return c
def leg(a,p): return 1 if pow(a,(p-1)//2,p)==1 else -1
cases={'golden phi':(1,-1,5),'silver 1+sqrt2':(2,-1,8),'2+sqrt3':(4,1,12),'base 2 (control)':None}
res={}
for name,par in cases.items():
    qs=[]
    for p in primes:
        m=p*p
        if par is None: v=(pow(2,p-1,m)-1)%m
        else:
            P,Q,D=par; v=U(p-leg(D,p),P,Q,m)
        assert v%p==0
        q=(v//p)%p; qs.append(min(q,p-q))
    res[name]=np.array(qs); print(name,'done',flush=True)
P=np.array(primes,float)
def ks_uniform(u):
    u=np.sort(u); n=len(u); d=max(np.max(np.arange(1,n+1)/n-u),np.max(u-np.arange(0,n)/n))
    lam=(math.sqrt(n)+0.12+0.11/math.sqrt(n))*d
    return 2*sum((-1)**(j-1)*math.exp(-2*j*j*lam*lam) for j in range(1,100))
def pois_cdf(k,mu): return sum(math.exp(-mu)*mu**i/math.factorial(i) for i in range(k+1))
print('\n%-18s %8s | %-26s | %-26s'%('case','KS p','k=10 obs/exp (z, P<=obs)','k=1000 obs/exp (z, P<=obs)'))
for name,q in res.items():
    u=2*q/P; ks=ks_uniform(u); row=[]
    for k in (10,1000):
        mask=P>2*k+1; exp=np.sum((2*k+1)/P[mask]); obs=int(np.sum(q[mask]<=k))
        z=(obs-exp)/math.sqrt(exp); pl=pois_cdf(obs,exp) if obs<200 else 0.5*(1+math.erf(z/math.sqrt(2)))
        row.append('%d/%.1f (z=%+.2f, %.3f)'%(obs,exp,z,pl))
    exact=int(np.sum(q==0))
    print('%-18s %8.3f | %-26s | %-26s | exact hits %d'%(name,ks,row[0],row[1],exact))
np.savez('nearmiss.npz',P=P,**{k.split()[0]:v for k,v in res.items()})

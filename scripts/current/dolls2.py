import numpy as np
from scipy.stats import kstest
def primes(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return [int(x) for x in np.nonzero(s)[0]]
def mm(A,B,m): return ((A[0]*B[0]+A[1]*B[2])%m,(A[0]*B[1]+A[1]*B[3])%m,(A[2]*B[0]+A[3]*B[2])%m,(A[2]*B[1]+A[3]*B[3])%m)
def mp(e,m):
    R=(1,0,0,1); A=(1,1,1,0)
    while e:
        if e&1: R=mm(R,A,m)
        A=mm(A,A,m); e>>=1
    return R
def factor(n):
    f=set(); d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f
def is_period(e,m): return mp(e,m)==(1%m,0,0,1%m)
def exact_period(e,m): return is_period(e,m) and all(not is_period(e//q,m) for q in factor(e))
def pisano_p(p):
    a,b,k=0,1,0
    while True:
        a,b=b,(a+b)%p; k+=1
        if a==0 and b==1: return k
bad=[]; checked=0
for p in primes(500):
    pi=pisano_p(p)
    for k in (2,3,4):
        checked+=1
        if not exact_period(p**(k-1)*pi,p**k): bad.append((p,k))
print(f"D2: checked {checked} (p<500, k=2..4), failures {bad}")
P=[p for p in primes(20000) if p>=7]; c=[]
for p in P:
    a,b=1,1; m=p*p
    while a%p: a,b=b,(a+b)%m
    c.append(((a//p)%p)/p)
c=np.array(c)
print(f"D3 n={len(c)} KS p={kstest(c,'uniform').pvalue:.3f}  lag-1 r={np.corrcoef(c[:-1],c[1:])[0,1]:.4f}  WSS(zero comma)={int(np.sum(c==0))}")
ok=tot=0
for p in P:
    pi=pisano_p(p); circ=p%5 in (2,3); tot+=1
    ok += (2*(p+1))%pi==0 if circ else (p-1)%pi==0
print(f"C1: {ok}/{tot}")
def fib(n):
    a,b=0,1
    for _ in range(abs(n)): a,b=b,a+b
    return a if n>=0 else (-1)**(abs(n)+1)*a
print("D4 failures:",[n for n in range(1,61) if fib(n)*fib(-n)!=(-1)**(n+1)*fib(n)**2])

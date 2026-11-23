import numpy as np
from scipy.stats import kstest
def primes(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]
def pisano(m):
    a,b,k=0,1,0
    while True:
        a,b=b,(a+b)%m; k+=1
        if a==0 and b==1: return k
def first_zero_mult(m):
    a,b,k=1,1,1
    while a%m: a,b=b,(a+b)%m; k+=1
    return k,b%m
def order(x,m):
    y,k=x%m,1
    while y!=1: y=y*x%m; k+=1
    return k
for p,n in ((2,3),(3,4),(5,5),(13,7),(89,11),(233,13),(1597,17),(28657,23)):
    m=p*p; a,mu=first_zero_mult(m); print(f"D1 doll {m} (F({n})^2): first zero {a}, multiplier {mu}, order {order(mu,m)}")
bad=[(p,k) for p in primes(500) for k in (2,3,4) if pisano(p**k)!=p**(k-1)*pisano(p)] if True else []
print("D2 failures:",bad)
P=[p for p in primes(20000) if p>=7]; c=[]; ok=0
for p in P:
    a,b=1,1; k=1; m=p*p
    while a%p: a,b=b,(a+b)%m; k+=1
    c.append(((a//p)%p)/p)
    pi=pisano(p) if p<3000 else None
    if pi is not None:
        circ = p%5 in (2,3)
        ok += (2*(p+1))%pi==0 if circ else (p-1)%pi==0
c=np.array(c)
print(f"D3 n={len(c)} KS p={kstest(c,'uniform').pvalue:.3f}  lag-1 r={np.corrcoef(c[:-1],c[1:])[0,1]:.4f}  zeros(WSS)={np.sum(c==0)}")
print(f"C1 (primes 7..3000): {ok}/{sum(1 for p in P if p<3000)}")
F=lambda n: (lambda r:r)( [0,1][n] if n in (0,1) else None)
def fib(n):
    a,b=0,1
    for _ in range(abs(n)): a,b=b,a+b
    return a if n>=0 else (-1)**(abs(n)+1)*a
print("D4 failures:",[n for n in range(1,61) if fib(n)*fib(-n)!=(-1)**(n+1)*fib(n)**2])

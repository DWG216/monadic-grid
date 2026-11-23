import numpy as np
from math import prod
pr=[l for l in range(3,100000) if all(l%q for q in range(2,int(l**0.5)+1))]
inert=prod(1-1/(l*(l-1)) for l in pr if l!=5); split=0.75*0.9*inert
print(f"theory: inert {inert:.4f} split {split:.4f} all {(inert+split)/2:.4f}")
LO,HI=2*10**6,10**7; M=2*(HI+1)+2
spf=np.zeros(M+1,dtype=np.int32); spf[1]=1
for i in range(2,int(M**0.5)+1):
    if spf[i]==0:
        sl=spf[i*i::i]; sl[sl==0]=i
idx=np.nonzero(spf==0)[0]; spf[idx]=idx.astype(np.int32)
def pf(n):
    s=set()
    while n>1: q=int(spf[n]); s.add(q); n//=q
    return s
def fib(n,p):
    a,b=0,1
    for bit in bin(n)[2:]:
        c=a*((2*b-a)%p)%p; d=(a*a+b*b)%p
        a,b=(d,(c+d)%p) if bit=='1' else (c,d)
    return a,b
def is_id(n,p):
    a,b=fib(n,p); return a==0 and b==1
P=[int(q) for q in np.nonzero(spf[LO:HI]==np.arange(LO,HI))[0]+LO]
cnt={'split':[0,0],'inert':[0,0]}
for p in P:
    if p%5 in (1,4): k='split'; Mx=p-1
    else: k='inert'; Mx=2*(p+1)
    ok=is_id(Mx,p) and all(not is_id(Mx//q,p) for q in pf(Mx))
    cnt[k][0]+=ok; cnt[k][1]+=1
s=cnt['split'][0]/cnt['split'][1]; i=cnt['inert'][0]/cnt['inert'][1]; a=(cnt['split'][0]+cnt['inert'][0])/len(P)
print(f"primes in [2e6,1e7): {len(P)}; split {s:.4f} (pred 0.5314, diff {s-0.5314:+.4f}); inert {i:.4f} (pred 0.7873, diff {i-0.7873:+.4f}); all {a:.4f} (pred 0.6593, diff {a-0.6593:+.4f})")

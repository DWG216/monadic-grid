import numpy as np
L=2*10**6; M=2*(L+1)+2
spf=np.zeros(M+1,dtype=np.int64)
for i in range(2,M+1):
    if spf[i]==0: spf[i::i][spf[i::i]==0]=i
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
primes=[int(q) for q in np.nonzero(spf[:L]==np.arange(L))[0] if q>=7]
cnt={'split':[0,0],'inert':[0,0]}; half={0:[0,0],1:[0,0]}
for p in primes:
    if p%5 in (1,4): kind='split'; Mx=p-1
    else: kind='inert'; Mx=2*(p+1)
    ok=is_id(Mx,p) and all(not is_id(Mx//q,p) for q in pf(Mx))
    cnt[kind][0]+=ok; cnt[kind][1]+=1; h=0 if p<10**6 else 1; half[h][0]+=ok; half[h][1]+=1
tot=sum(c[0] for c in cnt.values())/sum(c[1] for c in cnt.values())
print(f"C1 share maximal (7<=p<2e6): {tot:.4f}; halves {half[0][0]/half[0][1]:.4f} / {half[1][0]/half[1][1]:.4f}")
for k,(a,b) in cnt.items(): print(f"C2 {k}: {a}/{b} = {a/b:.4f}")

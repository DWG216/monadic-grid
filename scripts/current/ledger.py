import itertools as it, random
def ledger(f,n):
    N=1<<n; d=[0]*N
    for x in sorted(range(N),key=lambda v:bin(v).count('1')):
        if x: d[x]=max(d[x^(1<<i)]+(f[x^(1<<i)]!=f[x]) for i in range(n) if x>>i&1)
    return d
def check(f,n):
    d=ledger(f,n); a=max(d); N=1<<n
    layers=[[int(d[x]>=i) for x in range(N)] for i in range(1,a+1)]
    mono=all(L[x]<=L[x|(1<<i)] for L in layers for x in range(N) for i in range(n))
    nested=all(layers[k][x]>=layers[k+1][x] for k in range(a-1) for x in range(N))
    exact=all((f[x]^f[0])==sum((-1)**i*layers[i][x] for i in range(a)) for x in range(N))
    return mono and nested and exact, a
ok=True; hist={}
for v in range(1<<16):
    f=[(v>>x)&1 for x in range(16)]; good,a=check(f,4); ok&=good; hist[a]=hist.get(a,0)+1
rnd=random.Random(20261122)
for n in range(5,9):
    for _ in range(2000):
        f=[rnd.randint(0,1) for _ in range(1<<n)]; ok&=check(f,n)[0]
print("L1 all 4-variable functions and 8000 random 5-8 variable functions:", "PASS" if ok else "FAIL")
# L2: minimal nested monotone XOR layers, brute force on 3 variables
N=8; monos=[m for m in it.product((0,1),repeat=N) if all(m[x]<=m[x|(1<<i)] for x in range(N) for i in range(3))]
best={}
from collections import deque
start=(0,)*N; best[start]=0; frontier=[(start,(1,)*N)]  # (value, last layer as upper bound)
reach={start:0}; layer_sets=[[(start,(1,)*N)]]
for k in range(1,9):
    nxt=[]
    for val,top in layer_sets[-1]:
        for m in monos:
            if all(m[x]<=top[x] for x in range(N)) and any(m):
                nv=tuple(val[x]^m[x] for x in range(N))
                if nv not in reach: reach[nv]=k
                nxt.append((nv,m))
    layer_sets.append(list({(v,t) for v,t in nxt}))
    if len(reach)==256: break
L2=all(reach[tuple(f)]==max(ledger(list(f),3)) for f in it.product((0,1),repeat=N) if f[0]==0)
print("L2 minimal layers = alternation for all 3-variable functions with f(0)=0:", "PASS" if L2 else "FAIL")
for n in (3,4,5,8):
    par=[bin(x).count('1')%2 for x in range(1<<n)]; maj=[int(bin(x).count('1')*2>n) for x in range(1<<n)]
    print(f"L3 n={n}: parity a={max(ledger(par,n))} (NOT gates {(max(ledger(par,n))).bit_length()}); majority a={max(ledger(maj,n))}")
print("L4 alternation histogram, all 4-variable functions:",dict(sorted(hist.items())))
# L5 (identity, added before saving; pre-registration amended below): paired layers m_(2j-1) AND NOT m_(2j) are disjoint bands whose OR is f (f(0) = 0)
ok5=True
for v in range(0,1<<16,2):
    f=[(v>>x)&1 for x in range(16)]; d=ledger(f,4); a=max(d)
    bands=[[int(d[x]>=2*j-1 and not d[x]>=2*j) for x in range(16)] for j in range(1,(a+1)//2+1)]
    ok5&=all(sum(b[x] for b in bands)==f[x] for x in range(16))
print("L5 bands: f = disjoint union of ceil(a/2) bands, each between an upward and a downward set:", "PASS" if ok5 else "FAIL")

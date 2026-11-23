import math, random, cmath
def chi_table(p):
    t=[0]*p
    for x in range(1,p): t[x*x%p]=1
    return [0]+[1 if t[v] else -1 for v in range(1,p)]
res={}
for p in (101,211):
    chi=chi_table(p); cubes=[(x*x*x)%p for x in range(p)]
    aps=[]
    for a in range(p):
        for b in range(p):
            if (4*a**3+27*b*b)%p==0: continue
            s=0
            for x in range(p): s+=chi[(cubes[x]+a*x+b)%p]
            aps.append(-s)
    m=max(abs(v) for v in aps)/(2*math.sqrt(p)); mean2=sum(v*v for v in aps)/len(aps)/p
    over=sum(1 for v in aps if abs(v)>2*math.sqrt(p))/len(aps)
    res[p]=aps
    print(f"p={p}: curves {len(aps)}, D1 max|a_p|/2sqrt p = {m:.4f}, D2 mean a_p^2/p = {mean2:.4f}, D3 frac over bound = {over}")
random.seed(20261122); p=211; N=200000; over=0; walks=[]
for _ in range(N):
    s=sum(random.choice((1,-1)) for _ in range(p)); walks.append(s)
    if abs(s)>2*math.sqrt(p): over+=1
print(f"D3 null random walks p={p}: frac over 2 sqrt p = {over/N:.4f}, mean S^2/p = {sum(w*w for w in walks)/N/p:.4f}")
ap=res[211][1000]; disc=ap*ap-4*211; al=(ap+cmath.sqrt(disc))/2; be=(ap-cmath.sqrt(disc))/2
print(f"D4 a_p={ap}: |alpha|={abs(al):.12f} sqrt p={math.sqrt(211):.12f}; max_k |a_(p^k)|/(2p^(k/2)) = {max(abs(al**k+be**k)/(2*211**(k/2)) for k in range(1,13)):.6f}")
bins=20; edges=[-1+2*i/bins for i in range(bins+1)]
h=[0]*bins; aps=res[211]
for v in aps:
    u=v/(2*math.sqrt(211)); i=min(int((u+1)/2*bins),bins-1); h[i]+=1
h=[c/len(aps)/(2/bins) for c in h]
mid=[(edges[i]+edges[i+1])/2 for i in range(bins)]
semi=[2/math.pi*math.sqrt(1-x*x) for x in mid]
sig=math.sqrt(211)/(2*math.sqrt(211)); norm=[math.exp(-x*x/(2*sig*sig))/(sig*math.sqrt(2*math.pi)) for x in mid]
L1s=sum(abs(a-b) for a,b in zip(h,semi))*2/bins; L1n=sum(abs(a-b) for a,b in zip(h,norm))*2/bins
print(f"D5 L1 to semicircle {L1s:.4f} vs to normal {L1n:.4f}")
print("HIST mid",[round(x,2) for x in mid]); print("HIST data",[round(x,3) for x in h]); print("HIST semi",[round(x,3) for x in semi]); print("HIST norm",[round(x,3) for x in norm])

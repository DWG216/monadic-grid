import itertools, numpy as np
dr=lambda x: 9 if x%9==0 else x%9
F=[0,1]
for i in range(200): F.append(F[-1]+F[-2])
cyc=[dr(F[n]) for n in range(1,25)]
print('digital roots F1..F24:',cyc)
print('repeats with period 24:',all(dr(F[n])==dr(F[n+24]) for n in range(1,150)))
print('n and n+12 sum to 9 (or both 9):',[ (cyc[i]+cyc[i+12])%9==0 for i in range(12)].count(True),'/12')
def pis(m):
    a,b,n=0,1,0
    while True:
        a,b=b,(a+b)%m;n+=1
        if (a,b)==(0,1): return n
print('last-digit cycle (mod 10):',pis(10),' mod 2:',pis(2),' mod 5:',pis(5))
V=[p for p in itertools.product([-1,0,1],repeat=4) if sorted(map(abs,p))==[0,0,1,1]]
print('24-cell vertices (perms of +-1,+-1,0,0):',len(V))
print('slice w=0:',sum(1 for v in V if v[3]==0),' w=+1:',sum(1 for v in V if v[3]==1),' w=-1:',sum(1 for v in V if v[3]==-1))
print('antipodal pairs:',len(V)//2,' each vertex neighbours at distance sqrt2:',sum(1 for u in V if np.isclose(np.sum((np.array(u)-np.array(V[0]))**2),2)))

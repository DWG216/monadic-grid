import itertools
def pis(m):
    a,b,n=0,1,0; z=None; anti=None
    while True:
        a,b=b,(a+b)%m;n+=1
        if z is None and a==0: z=n
        if anti is None and (a,b)==(0,m-1): anti=n
        if (a,b)==(0,1): return n,z,anti
for m in [3,9,27,81,216,6**3]: print('mod',m,'(period, first zero, sign flip):',pis(m))
def orbits(m):
    seen=set(); L=[]
    for p in itertools.product(range(m),repeat=2):
        if p in seen: continue
        o=[];q=p
        while q not in seen: seen.add(q);o.append(q);q=(q[1],(q[0]+q[1])%m)
        L.append(len(o))
    return sorted(L)
for m in [3,9,27]:
    L=orbits(m); from collections import Counter; print('orbits of Q on (Z/%d)^2:'%m,dict(Counter(L)),'total',sum(L))
# Hesse configuration: lines of the affine plane F3^2
pts=list(itertools.product(range(3),repeat=2)); lines=set()
for p,q in itertools.combinations(pts,2):
    d=((q[0]-p[0])%3,(q[1]-p[1])%3); lines.add(frozenset(((p[0]+t*d[0])%3,(p[1]+t*d[1])%3) for t in range(3)))
print('affine plane F3^2: points',len(pts),'lines',len(lines))
# |SL(2,3)| and |ASL(2,3)|
SL=[M for M in itertools.product(range(3),repeat=4) if (M[0]*M[3]-M[1]*M[2])%3==1]
print('|SL(2,3)| =',len(SL),' |ASL(2,3)| = 9*|SL| =',9*len(SL))
print('Millington coil passes per wire: 12 points x 18 =',12*18,'; 36 slots x 6 =',36*6)

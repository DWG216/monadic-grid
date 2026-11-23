import numpy as np, itertools
def pis(m):
    a,b,n=0,1,0; anti=None
    while True:
        a,b=b,(a+b)%m; n+=1
        if anti is None and (a,b)==(0,m-1): anti=n
        if (a,b)==(0,1): return n,anti
for m in [9,13,169]: print('mod',m,'period, antiperiod (F flips sign):',pis(m))
print('lines among 13 circles C(13,2)=',13*12//2)
# FCC: 12 nearest neighbours of origin = permutations of (+-1,+-1,0)
nb=[p for p in itertools.product([-1,0,1],repeat=3) if sorted(map(abs,p))==[0,1,1]]
print('FCC nearest neighbours:',len(nb),'+ centre =',len(nb)+1)
# tetrahedral-octahedral honeycomb vertices = FCC: check every unit cell's tets/octs have FCC vertices
pts=set(p for p in itertools.product(range(-2,3),repeat=3) if sum(p)%2==0)
tets=0;octs=0
for p in pts:
    x=np.array(p)
    # tetra: x, x+(1,1,0),x+(1,0,1),x+(0,1,1)
    T=[x,x+(1,1,0),x+(1,0,1),x+(0,1,1)]
    if all(tuple(t) in pts for t in T): tets+=1
    O=[x+d for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    if sum(p)%2==0 and all(tuple(o) not in pts for o in O): pass
# Cassini meeting of Binet hands
phi=(1+5**.5)/2; psi=-1/phi
print('phi*psi =',phi*psi,' F(n-1)F(n+1)-F(n)^2 for n=1..10:',[ (lambda F:F[n-1]*F[n+1]-F[n]**2)([0,1,1,2,3,5,8,13,21,34,55,89]) for n in range(1,11)])
# cut and project: Z^2 strip of slope 1/phi -> Fibonacci word
w=''.join('L' if int((n+2)/phi)-int((n+1)/phi)==1 else 'S' for n in range(20))
print('cut-and-project word:',w)

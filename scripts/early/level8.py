import numpy as np, itertools
from fractions import Fraction
exec(open('frozen_fluid.py').read().split('res={}')[0])
phi=(1+5**.5)/2
def npaths(k,n):
    v=[1]+[0]*k
    for _ in range(n): v=[(v[j-1] if j>0 else 0)+(v[j+1] if j<k else 0) for j in range(k+1)]
    return sum(v)
print('L1 two-step growth of path-space dimension (n=40 -> 42) vs d^2:')
for k in (2,4,8):
    D=[npaths(k,n) for n in (40,42)]; d=qn(2,k+2)
    print('   k=%d ratio %.4f | d^2 = %.4f'%(k,D[1]/D[0],d*d))
def rational(x,maxden=500,tol=1e-9):
    f=Fraction(x).limit_denominator(maxden); return abs(float(f)-x)<tol, f
def scan(k,n,L=6):
    g,_=rep(k,n); worst=None
    for l in range(1,L+1):
        for w in itertools.product(range(n-1),repeat=l):
            U=np.eye(g[0].shape[0],dtype=complex)
            for i in w: U=g[i]@U
            ph=np.angle(np.linalg.eigvals(U)); ph=(ph-ph[0])/(2*np.pi)
            for x in ph[1:]:
                ok,f=rational(x%1)
                if not ok: return 'INFINITE-ORDER word found: %s (phase ratio %.10f)'%(''.join('s%d'%(i+1) for i in w),x%1)
    return 'all words length<=%d have finite order'%L
print('L2:')
for k,n in [(8,3),(8,4),(8,5),(8,6),(4,5),(4,6),(2,6)]:
    print('   k=%d n=%d: %s'%(k,n,scan(k,n)),flush=True)
g,_=rep(8,4)
print('L3 level 8, 4 strands: <s1,s2> order',order(g[:2],30000),'| <s1,s2,s3> order',order(g,30000))

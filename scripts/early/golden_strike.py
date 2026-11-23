import numpy as np
def braid_count(r,L=9,cap=40000):
    q=np.exp(2j*np.pi/r); R=np.diag([1,q])                 # phase gate of order r
    # basis change chosen from the Jones-Wenzl (quantum-dimension) recipe: d = 2cos(pi/r)
    d=2*np.cos(np.pi/r); a=1/d; b=np.sqrt(max(1-a*a,0)); F=np.array([[a,b],[b,-a]])
    G=[R,R.conj().T,F@R@F,(F@R@F).conj().T]
    def key(U):
        k=np.argmax(abs(U.ravel())>1e-6); ph=np.conj(U.ravel()[k])/abs(U.ravel()[k]); return tuple(np.round((U*ph).ravel(),5))
    seen={key(np.eye(2))}; front=[np.eye(2)]; sizes=[]
    for l in range(L):
        nf=[]
        for U in front:
            for g in G:
                V=g@U; k=key(V)
                if k not in seen: seen.add(k); nf.append(V)
        front=nf; sizes.append(len(seen))
        if len(seen)>cap: break
    return sizes
print('G1. reachable gates (mod phase) by word length, Jones-type braid gates at order r:')
for r in [3,4,5,6,7,8,10,12]:
    s=braid_count(r); print('   r=%2d  %s  -> %s'%(r,s,'finite (saturates)' if s[-1]==s[-2]==s[-3] else 'keeps growing'))
def dynkin(name):
    edges={'E6':[(0,1),(1,2),(2,3),(3,4),(2,5)],'E7':[(0,1),(1,2),(2,3),(3,4),(4,5),(2,6)],'E8':[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(4,7)]}[name]
    n=max(max(e) for e in edges)+1; A=np.zeros((n,n))
    for i,j in edges: A[i,j]=A[j,i]=1
    w,v=np.linalg.eigh(A); m=np.abs(v[:,-1]); return np.sort(m/m.min())
phi=(1+5**.5)/2
print('\nG2. particle masses from the Dynkin diagrams (Perron-Frobenius vector), lightest = 1:')
for nm in ['E6','E7','E8']:
    m=dynkin(nm); print('   %s: %s'%(nm,np.round(m,4)))
m=dynkin('E8'); print('   E8: m2/m1 = %.10f ; golden ratio = %.10f ; equal: %s ; m3/m1 = %.6f vs 2cos(pi/30) = %.6f'%(m[1],phi,np.isclose(m[1],phi),m[2],2*np.cos(np.pi/30)))

import numpy as np
def jones_gens(r):
    A=1j*np.exp(-1j*np.pi/(2*r)); d=2*np.cos(np.pi/r)              # loop value d = -A^2 - A^-2 = 2cos(pi/r)
    P1=np.array([[1,0],[0,0]],complex)
    s=np.sqrt(max(1-1/d**2,0)); v=np.array([1/d,s]); P2=np.outer(v,v).astype(complex)
    I=np.eye(2); g1=A*(I-P1)-A**-3*P1; g2=A*(I-P2)-A**-3*P2
    assert np.allclose(g1.conj().T@g1,I) and np.allclose(g2.conj().T@g2,I)
    assert np.allclose(g1@g2@g1,g2@g1@g2)                            # braid relation
    return [g1,g1.conj().T,g2,g2.conj().T]
def count(r,L=10,cap=40000):
    G=jones_gens(r)
    def key(U):
        k=np.argmax(abs(U.ravel())>1e-6); ph=np.conj(U.ravel()[k])/abs(U.ravel()[k]); return tuple(np.round((U*ph).ravel(),5))
    seen={key(np.eye(2))}; front=[np.eye(2)]; out=[]
    for _ in range(L):
        nf=[]
        for U in front:
            for g in G:
                V=g@U; k=key(V)
                if k not in seen: seen.add(k); nf.append(V)
        front=nf; out.append(len(seen))
        if len(seen)>cap: break
    return out
print('Jones (Temperley-Lieb) braid representation, unitary and satisfying the braid relation:')
for r in [3,4,5,6,7,8,10,12]:
    s=count(r); print('   r=%2d  %s  -> %s'%(r,s,'FINITE' if len(s)>3 and s[-1]==s[-2]==s[-3] else 'keeps growing (dense)'))

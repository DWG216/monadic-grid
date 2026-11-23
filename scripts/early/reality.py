import numpy as np, itertools
phi=(1+5**.5)/2; psi=(1-5**.5)/2
eps=np.zeros((4,4,4,4))
for p in itertools.permutations(range(4)):
    s=1
    for i in range(4):
        for j in range(i+1,4):
            if p[i]>p[j]: s=-s
    eps[p]=s
pairs=list(itertools.combinations(range(4),2))
def vec(P): return np.array([P[i,j] for i,j in pairs])
def mat(v):
    P=np.zeros((4,4),complex)
    for k,(i,j) in enumerate(pairs): P[i,j]=v[k]; P[j,i]=-v[k]
    return P
def star(X): return 0.5*np.einsum('ijkl,kl->ij',eps,X)          # covariant -> contravariant bivector
def J(v,h,conj=True):                                           # semilinear map on bivectors induced by the form h
    P=mat(v); P=P.conj() if conj else P
    return vec(star(h@P@h.T))
def Q(v,w): return 0.125*np.einsum('ijkl,ij,kl->',eps,mat(v),mat(w))
def real_slice(h,label):
    # J is antilinear on C^6: J(v)=A conj(v). Find A, check A conj(A)=c I, fixed real subspace, Q signature there.
    A=np.array([J(e,h) for e in np.eye(6)]).T                   # J(e_k) with e_k real
    AA=A@A.conj(); c=AA[0,0]
    ok=np.allclose(AA,c*np.eye(6))
    hs=np.linalg.eigvalsh(h); hsig=(int(sum(hs>0)),int(sum(hs<0)))
    if not ok or abs(c.imag)>1e-9: print(f'{label}: Hermitian signature {hsig}: J^2 not scalar'); return
    c=c.real
    if c<0:
        print(f'{label}: Hermitian signature {hsig}: J^2 = {c:+.3f} < 0 -> quaternionic, no real points (Euclidean-type twistor structure)'); return
    A=A/np.sqrt(c)
    # real fixed space of v -> A conj(v): write v=x+iy, solve [[ReA-1, ImA],[ImA, -ReA-1]] (x,y)=0
    M=np.block([[A.real-np.eye(6), A.imag],[A.imag, -A.real-np.eye(6)]])
    u,s,vt=np.linalg.svd(M); N=vt[s.size-np.sum(s<1e-9):] if np.sum(s<1e-9) else np.zeros((0,12))
    ns=vt[-6:]; basis=[x[:6]+1j*x[6:] for x in ns]
    G=np.array([[Q(a,b) for b in basis] for a in basis])
    ev=np.linalg.eigvalsh((G+G.conj().T).real/2)
    sig=(int(sum(ev>1e-9)),int(sum(ev<-1e-9)))
    st={(4,2):'Lorentzian spacetime (3,1)',(2,4):'Lorentzian spacetime (3,1)',(3,3):'split spacetime (2,2), two times',(6,0):'no real null points',(0,6):'no real null points',(5,1):'Euclidean spacetime (4,0)',(1,5):'Euclidean spacetime (4,0)'}.get(sig,'?')
    print(f'{label}: Hermitian signature {hsig}: real 6D ambient signature {sig} -> {st}')
print('--- Computation 0: check the method on standard cases (complex conjugation) ---')
real_slice(np.diag([1,1,-1,-1]).astype(complex),'standard twistor form diag(1,1,-1,-1)')
real_slice(np.diag([1,1,1,-1]).astype(complex),'form diag(1,1,1,-1)')
real_slice(np.eye(4,dtype=complex),'definite form diag(1,1,1,1)')
print('--- Computation 2: complex conjugation with golden coefficients, at both real places of Q(sqrt5) ---')
hg=lambda r: np.diag([r,1,-1,-1]).astype(complex)               # entry phi, Galois-conjugate place gets psi
real_slice(hg(phi),'place sqrt5->+sqrt5, h=diag(phi,1,-1,-1)')
real_slice(hg(psi),'place sqrt5->-sqrt5, h=diag(psi,1,-1,-1)')
hg2=lambda r1,r2: np.array([[0,r1,0,0],[r1,0,0,0],[0,0,0,r2],[0,0,r2,0]],complex)
real_slice(hg2(phi,1),'place +, h=off-diagonal (phi,1)')
real_slice(hg2(psi,1),'place -, h=off-diagonal (psi,1)')
print('--- Computation 1: golden conjugation sigma alone (K=Q(sqrt5), fixed field Q) ---')
# over the reals K splits into R x R and sigma swaps the two copies; a sigma-Hermitian form is then a real
# bilinear pairing between the copies, and the induced map on bivectors is real-linear (no complex conjugation).
for name,h in [('generic real matrix',np.array([[2,1,0,1],[0,1,3,0],[1,0,1,2],[0,2,1,1]],float)),('golden matrix',np.array([[phi,1,0,0],[1,psi,0,0],[0,0,1,phi],[0,0,psi,1]],float))]:
    A=np.array([J(e,h.astype(complex),conj=False) for e in np.eye(6)]).T.real
    # fixed space of the swap on Lambda^2(V1)+Lambda^2(V2) is the graph of A: isomorphic to Lambda^2(R^4) with the wedge form
    G=np.array([[Q(a,b).real for b in np.eye(6)] for a in np.eye(6)]); ev=np.linalg.eigvalsh(G)
    print(f'sigma-Hermitian, {name}: real slice = Lambda^2(R^4), wedge-form signature {(int(sum(ev>0)),int(sum(ev<0)))} -> split spacetime (2,2)')
    # chirality check: in split signature alpha- and beta-planes are both real; the correlation sends a point z of
    # twistor space to the plane {w: w.(h z)=0}: count dimension of that plane
    z=np.random.default_rng(0).normal(size=4); cov=h.T@z
    print(f'   correlation maps a point to a plane of dimension {4-1-np.linalg.matrix_rank(cov[None,:])} in projective twistor space (point -> plane: swaps alpha and beta families)')

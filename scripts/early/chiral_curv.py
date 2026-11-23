# Step A: split curvature into hands (4D Euclidean, where self-dual/anti-self-dual 2-forms are real)
import numpy as np, itertools
rng=np.random.default_rng(7)
pairs=list(itertools.combinations(range(4),2))
def bivec(i,j):
    B=np.zeros((4,4)); B[i,j]=1; B[j,i]=-1; return B
E2=[bivec(i,j) for i,j in pairs]                       # basis of 2-forms
eps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)):
    eps[p]=np.linalg.det(np.eye(4)[list(p)])
def hodge(B): return 0.5*np.einsum('abcd,cd->ab',eps,B)
# self-dual / anti-self-dual bases
SD=[(E2[0]+hodge(E2[0])),(E2[1]+hodge(E2[1])),(E2[2]+hodge(E2[2]))]
ASD=[(E2[0]-hodge(E2[0])),(E2[1]-hodge(E2[1])),(E2[2]-hodge(E2[2]))]
def orth(L):
    V=np.array([b.ravel() for b in L]); Q,_=np.linalg.qr(V.T); return [Q[:,k].reshape(4,4) for k in range(Q.shape[1])]
SD,ASD=orth(SD),orth(ASD)
def riemann_from_operator(M,basis):     # R_abcd = sum M_kl B^k_ab B^l_cd
    return np.einsum('kl,kab,lcd->abcd',M,np.array(basis),np.array(basis))
def random_curvature(einstein=False):
    A=rng.normal(size=(3,3));A=A+A.T; Bm=rng.normal(size=(3,3));Bm=Bm+Bm.T
    C=np.zeros((3,3)) if einstein else rng.normal(size=(3,3))
    s=(np.trace(A)+np.trace(Bm))/2; A+= (s-np.trace(A))/3*np.eye(3); Bm+=(s-np.trace(Bm))/3*np.eye(3)  # equal traces = first Bianchi
    M=np.block([[A,C],[C.T,Bm]]); return riemann_from_operator(M,SD+ASD),A,Bm,C
for ein in (False,True):
    R,A,Bm,C=random_curvature(ein)
    bianchi=np.max(abs(R+np.einsum('abcd->acdb',R)+np.einsum('abcd->adbc',R)))
    Ric=np.einsum('acbc->ab',R); sc=np.trace(Ric); Ric0=Ric-sc/4*np.eye(4)
    print(f"{'Einstein (mixed block = 0)' if ein else 'generic curvature':28s}: first Bianchi violation {bianchi:.1e} | "
          f"|mixed SD-ASD block| = {np.linalg.norm(C):.3f} | |traceless Ricci| = {np.linalg.norm(Ric0):.3f} | "
          f"|Weyl+| = {np.linalg.norm(A-np.trace(A)/3*np.eye(3)):.3f}, |Weyl-| = {np.linalg.norm(Bm-np.trace(Bm)/3*np.eye(3)):.3f}")
# proportionality test across many samples
r=[]
for _ in range(200):
    R,A,Bm,C=random_curvature(); Ric=np.einsum('acbc->ab',R); Ric0=Ric-np.trace(Ric)/4*np.eye(4); r.append(np.linalg.norm(Ric0)/np.linalg.norm(C))
print('ratio |traceless Ricci| / |mixed block| over 200 random curvatures: min %.6f max %.6f'%(min(r),max(r)))

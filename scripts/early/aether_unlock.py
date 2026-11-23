import numpy as np, itertools
phi=(1+5**.5)/2
# ---- A1: compound of five cubes = dodecahedron
dod=[np.array(v,float) for v in itertools.product([1,-1],repeat=3)]
for a in [1,-1]:
    for b in [1,-1]: dod+= [np.array([0,a/phi,b*phi]),np.array([a/phi,b*phi,0]),np.array([b*phi,0,a/phi])]
dod=[v/np.linalg.norm(v) for v in dod]
def rot(axis,ang):
    a=axis/np.linalg.norm(axis); K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]]); return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*K@K
cube=[v/np.linalg.norm(v) for v in map(np.array,itertools.product([1.,-1],repeat=3))]
ax=np.array([0,1,phi])                                   # 5-fold axis through a dodecahedron face centre
cubes=[[rot(ax,2*np.pi*k/5)@c for c in cube] for k in range(5)]
allc=[c for cb in cubes for c in cb]
match=all(min(np.linalg.norm(c-d) for d in dod)<1e-9 for c in allc) and all(min(np.linalg.norm(c-d) for c in allc)<1e-9 for d in dod)
print('A1. five rotated cubes cover exactly the 20 dodecahedron vertices:',match,'| each vertex shared by',len(allc)//20,'cubes')
# ---- A2: magic
M2=lambda n:-np.log2((1+np.sum(np.array(n)**4))/2)
ico=[]
for a in [1,-1]:
    for b in [1,-1]: ico+=[np.array([0,a,b*phi]),np.array([a,b*phi,0]),np.array([b*phi,0,a])]
print('A2. magic M2: stabilizer (octahedron) %.3f | cube corner (T-type) %.3f | icosahedron vertex %.3f | other dodecahedron vertex %.3f'%(
      M2([0,0,1]),M2(np.ones(3)/3**.5),M2(ico[0]/np.linalg.norm(ico[0])),M2(dod[8])))
# ---- A3: Bravyi-Kitaev distillation with the 5-qubit (perfect-tensor) code
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1])
def kron(*m):
    r=np.array([[1.]]); 
    for a in m: r=np.kron(r,a)
    return r
Pm={'I':I,'X':X,'Z':Z}
stabs=[kron(*[Pm[c] for c in s]) for s in ['XZZXI','IXZZX','XIXZZ','ZXIXZ']]
P=np.eye(32)
for S in stabs: P=P@(np.eye(32)+S)/2
XL=kron(X,X,X,X,X); ZL=kron(Z,Z,Z,Z,Z); YL=1j*XL@ZL
w,v=np.linalg.eigh(P@ZL@P); L0=v[:,np.argmax(w)]; L1=XL@L0; V=np.column_stack([L0,L1])
def rho_from(n): return 0.5*(I+n[0]*X+n[1]*Y+n[2]*Z)
T=np.ones(3)/3**.5; corners=[np.array(s)/3**.5 for s in itertools.product([1,-1],repeat=3)]
def distill(eps):
    r=(1-eps)*rho_from(T)+eps*rho_from(-T); R=r
    for _ in range(4): R=np.kron(R,r)
    num=V.conj().T@P@R@P@V; p=np.real(np.trace(num)); rl=num/p
    n=np.real([np.trace(rl@X),np.trace(rl@Y),np.trace(rl@Z)])
    f=max((1+n@c)/2 for c in corners); return 1-f,p
print('A3. one round of distillation with our 5-qubit perfect code:')
for e in [0.02,0.05,0.10,0.15,0.17,0.18,0.25]:
    eo,p=distill(e); print('   input error %.3f -> output error %.4f  (%s)  success prob %.3f'%(e,eo,'better' if eo<e else 'worse',p))
lo,hi=0.05,0.3
for _ in range(50):
    m=(lo+hi)/2; lo,hi=(m,hi) if distill(m)[0]<m else (lo,m)
print('   threshold: input error %.4f'%lo)

import numpy as np, itertools
n=7; phi=(1+5**.5)/2
def dicke(k):
    v=np.zeros(2**n)
    for c in itertools.combinations(range(n),k): v[sum(1<<(n-1-i) for i in c)]=1
    return v/np.linalg.norm(v)
L0=np.sqrt(3)*dicke(0)+np.sqrt(7)*dicke(5); L1=np.sqrt(7)*dicke(2)-np.sqrt(3)*dicke(7)
L0/=np.linalg.norm(L0); L1/=np.linalg.norm(L1); V=np.column_stack([L0,L1]).astype(complex); P=V@V.conj().T
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1])
def op(single,i):
    m=np.array([[1.]])
    for q in range(n): m=np.kron(m,single if q==i else I)
    return m
errs=[np.eye(2**n)]+[op(p,i) for i in range(n) for p in (X,Y,Z)]
kl=max(np.linalg.norm(V.conj().T@E.conj().T@F@V-(V.conj().T@E.conj().T@F@V)[0,0]*np.eye(2)) for E in errs for F in errs)
print('B1a. Knill-Laflamme violation over all single-qubit error pairs: %.2e  (0 = corrects any single error)'%kl)
def q2u(q): a,b,c,d=q; return a*I-1j*(b*X+c*Y+d*Z)
gens=[np.array([1,1,1,1])/2, np.array([phi,1/phi,1,0])/2]
def tens(U):
    m=np.array([[1.]]); 
    for _ in range(n): m=np.kron(m,U)
    return m
ok=True; Llog=[]
for g in gens:
    U=q2u(g); T=tens(U); leak=np.linalg.norm(T@V-P@T@V); Llog.append(V.conj().T@T@V); ok&=leak<1e-9
    print('B1b. icosian generator',np.round(g,3),' leaks out of code space: %.1e'%leak)
print('     transversal icosahedral gates preserve the code:',ok)
def bloch(r): return np.real([np.trace(r@X),np.trace(r@Y),np.trace(r@Z)])
def rho(nv): return 0.5*(I+nv[0]*X+nv[1]*Y+nv[2]*Z)
ico=[]
for a in [1,-1]:
    for b in [1,-1]: ico+=[np.array([0,a,b*phi]),np.array([a,b*phi,0]),np.array([b*phi,0,a])]
ico=[v/np.linalg.norm(v) for v in ico]
dod=[np.array(v)/3**.5 for v in itertools.product([1,-1],repeat=3)]
for a in [1,-1]:
    for b in [1,-1]: dod+=[np.array([0,a/phi,b*phi])/3**.5,np.array([a/phi,b*phi,0])/3**.5,np.array([b*phi,0,a/phi])/3**.5]
def distill(Vc,Pc,nq,target,orbit,eps):
    r=(1-eps)*rho(target)+eps*rho(-target); R=r
    for _ in range(nq-1): R=np.kron(R,r)
    num=Vc.conj().T@Pc@R@Pc@Vc; p=np.real(np.trace(num)); b=bloch(num/p)
    return 1-max((1+b@o)/2 for o in orbit),p
def threshold(Vc,Pc,nq,target,orbit):
    es=np.linspace(0.005,0.3,60); d=[distill(Vc,Pc,nq,target,orbit,e)[0]-e for e in es]
    good=[e for e,x in zip(es,d) if x<0]; return (max(good) if good else 0.0), min(d)
# 5-qubit code
S5=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; Pm={'I':I,'X':X,'Z':Z}
def k5(s):
    m=np.array([[1.]])
    for c in s: m=np.kron(m,Pm[c])
    return m
P5=np.eye(32)
for s in S5: P5=P5@(np.eye(32)+k5(s))/2
XL=k5('XXXXX'); ZL=k5('ZZZZZ'); w,v=np.linalg.eigh(P5@ZL@P5); a0=v[:,np.argmax(w)]; V5=np.column_stack([a0,XL@a0]).astype(complex)
print('\nThresholds (largest input error that still improves; 0 = never improves):')
cubes=[np.array(c)/3**.5 for c in itertools.product([1,-1],repeat=3)]
print('   5-qubit code, cube-corner magic (check, expect ~0.173): %.3f'%threshold(V5,P5,5,cubes[0],cubes)[0])
print('   5-qubit code, icosahedron-vertex states:                %.3f'%threshold(V5,P5,5,ico[0],ico)[0])
print('   5-qubit code, dodecahedron (non-cube) vertex states:    %.3f'%threshold(V5,P5,5,dod[8],dod)[0])
for name,cls in [('icosahedron-vertex (5-fold) states',ico),('dodecahedron-vertex (3-fold) states',dod),('cube-corner states',cubes)]:
    best=max(threshold(V,P,7,t,cls)[0] for t in cls)
    print('   7-qubit icosahedral code, %-36s %.3f'%(name+':',best))

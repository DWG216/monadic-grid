import numpy as np, itertools
exec(open('icosa_code2.py').read().split("for name,cls in")[0])
m_ex=lambda b: max(0.0,np.sum(np.abs(b))-1)
def out7(t,eps):
    r=(1-eps)*rho(t)+eps*rho(-t); R=r
    for _ in range(6): R=np.kron(R,r)
    num=V.conj().T@P@R@P@V; p=np.real(np.trace(num)); return bloch(num/p),p
img=[out7(t,0.0)[0] for t in ico]
same=[min(np.linalg.norm(b-v) for v in ico)<1e-8 for b in img]
print('icosahedral code: perfect output of each vertex is again a vertex of the same icosahedron:',all(same))
magic_vtx=[k for k,t in enumerate(ico) if abs(abs(t[2])-1)>1e-6]            # the 10 non-pole (magic) vertices
k=magic_vtx[1]; t7=ico[k]; tgt7=img[k]
# 5-qubit code
S5=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; Pm={'I':I,'X':X,'Z':Z}
def k5(s):
    m=np.array([[1.]])
    for c in s: m=np.kron(m,Pm[c])
    return m
P5=np.eye(32)
for s in S5: P5=P5@(np.eye(32)+k5(s))/2
XL=k5('XXXXX'); ZL=k5('ZZZZZ'); w,v=np.linalg.eigh(P5@ZL@P5); a0=v[:,np.argmax(w)]; V5=np.column_stack([a0,XL@a0]).astype(complex)
cube=[np.array(c)/3**.5 for c in itertools.product([1,-1],repeat=3)]
def out5(eps):
    t=cube[0]; r=(1-eps)*rho(t)+eps*rho(-t); R=r
    for _ in range(4): R=np.kron(R,r)
    num=V5.conj().T@P5@R@P5@V5; p=np.real(np.trace(num)); b=bloch(num/p)
    c=max(cube,key=lambda c:b@c); return (1-b@c)/2,p,b
def step7(eps):
    b,p=out7(t7,eps); return (1-b@tgt7)/2,p,b
print('\nP1. magic delivered per raw noisy state (one round):')
print('   input err |  5-qubit: out err, magic/out, magic per raw  |  7-qubit: out err, magic/out, magic per raw')
for e in [0.02,0.05,0.10,0.15,0.20,0.25]:
    e5,p5,b5=out5(e); e7,p7,b7=step7(e)
    m5=m_ex(b5) if e5<e else 0.0; m7=m_ex(b7) if e7<e else 0.0
    print('     %.2f    |  %.4f  %.3f  %.4f                      |  %.4f  %.3f  %.4f'%(e,e5,m_ex(b5),m5*p5/5,e7,m_ex(b7),m7*p7/7))
print('   (magic of the pure targets: cube corner %.3f, this icosahedral output %.3f)'%(m_ex(cube[0]),m_ex(tgt7)))
def iterate(step,nq,e0,goal=1e-6,maxr=12):
    e=e0; cost=1.0; rounds=0
    while e>goal and rounds<maxr:
        eo,p,_=step(e)
        if eo>=e: return None
        cost*=nq/p; e=eo; rounds+=1
    return rounds,cost,e
print('\nP2. iterate to error 1e-6:')
for e0 in [0.05,0.10,0.15,0.20]:
    r5=iterate(lambda x:out5(x),5,e0); r7=iterate(step7,7,e0)
    f=lambda r:'cannot start' if r is None else '%d rounds, %.3g raw states per output, final err %.1e'%r
    print('   start %.2f | 5-qubit: %-52s | 7-qubit: %s'%(e0,f(r5),f(r7)))

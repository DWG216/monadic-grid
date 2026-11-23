import numpy as np, itertools
rng=np.random.default_rng(5); res={}
# N1 Nielsen-Ninomiya
shifts=[np.array(s) for s in itertools.product([-1,0,1],repeat=3) if sum(abs(np.array(s)))<=1]  # 0 and +-e_i
def model():
    a=rng.normal(size=(3,len(shifts))); b=rng.normal(size=(3,len(shifts)))
    a[:,0]+=rng.normal()*0.5
    def d(K):  # K shape (...,3)
        out=np.zeros(K.shape[:-1]+(3,))
        for j,s in enumerate(shifts):
            ph=K@s
            out+=np.cos(ph)[...,None]*a[:,j]+np.sin(ph)[...,None]*b[:,j]
        return out
    def J(K):
        out=np.zeros(K.shape[:-1]+(3,3))
        for j,s in enumerate(shifts):
            ph=K@s
            out+=(-np.sin(ph)[...,None]*a[:,j]+np.cos(ph)[...,None]*b[:,j])[...,:,None]*s[None,:]
        return out
    return d,J
tot=[];cnt=[]
g=np.linspace(0,2*np.pi,24,endpoint=False)
seeds=np.array(list(itertools.product(g,g,g)))
for m in range(20):
    d,J=model(); K=seeds.copy()
    for it in range(60):
        D=d(K); JJ=J(K)
        try: step=np.linalg.solve(JJ,D[...,None])[...,0]
        except np.linalg.LinAlgError: step=np.linalg.lstsq(JJ,D)[0]
        step=np.clip(step,-0.5,0.5); K=K-step
    ok=np.linalg.norm(d(K),axis=1)<1e-10
    Kz=np.mod(K[ok],2*np.pi); nodes=[]
    for kz in Kz:
        if not any(np.linalg.norm(np.angle(np.exp(1j*(kz-n))))<1e-6 for n in nodes): nodes.append(kz)
    ch=[int(np.sign(np.linalg.det(J(n[None,:])[0]))) for n in nodes]
    tot.append(sum(ch)); cnt.append(len(nodes))
res['N1 total chirality per model']=tot; res['N1 node counts']=cnt
res['N1 pass']=all(t==0 for t in tot) and all(c%2==0 for c in cnt)
# N2 naive 4D doublers
zs=list(itertools.product([0,np.pi],repeat=4))
chi=[int(np.prod(np.sign(np.cos(z)))) for z in zs]
res['N2 count, +, -']=(len(zs),chi.count(1),chi.count(-1))
# N3 Fidkowski-Kitaev
X=np.array([[0,1],[1,0]],dtype=complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1]).astype(complex); I2=np.eye(2)
def kron(*ms):
    out=np.array([[1.0+0j]])
    for m in ms: out=np.kron(out,m)
    return out
def majoranas(N):
    nf=N//2; gs=[]
    for j in range(nf):
        pre=[Z]*j; post=[I2]*(nf-j-1)
        gs.append(kron(*pre,X,*post)); gs.append(kron(*pre,Y,*post))
    return gs
out={}
for N in [2,4,6,8]:
    gs=majoranas(N); quads=list(itertools.combinations(range(N),4)); degs=0
    for s in range(200):
        H=np.zeros_like(gs[0])
        for q in quads: H=H+rng.normal()*gs[q[0]]@gs[q[1]]@gs[q[2]]@gs[q[3]]
        w=np.linalg.eigvalsh(H) if len(quads)>0 else np.zeros(gs[0].shape[0])
        if w[1]-w[0]<1e-10: degs+=1
    out[N]=degs/200
res['N3 fraction degenerate (N=2,4,6,8)']=out
for k,v in res.items(): print(k,v)

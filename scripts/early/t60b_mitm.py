import numpy as np, time, sys, io, contextlib
from scipy.spatial import cKDTree
src=open('tau60_braid.py').read().split("t=time.time()")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
Fa=np.array(F).astype(np.complex64); W1=np.array(P3).astype(np.complex64)
T3=lambda C: np.block([[C,np.zeros((2,1))],[np.zeros((1,2)),np.ones((1,1))]]).astype(np.complex64)
def canon(M,a,b):
    c2=M[:,a,2]; Bf=M[:,:,:2].reshape(len(M),6)[:,b]
    M=M.copy(); M[:,:,2]*=(np.abs(c2)/c2)[:,None]; M[:,:,:2]*=(np.abs(Bf)/Bf)[:,None,None]
    f=M.reshape(len(M),9); return np.hstack([f.real,f.imag]).astype(np.float32)
def err(U,C):  # exact error vs blockdiag(C)
    return np.sqrt(np.maximum(0,3-np.abs(np.einsum('nij,ij->n',U[:,:2,:2],C.conj()))-np.abs(U[:,2,2])))
def build(Ys,thr=0.45):
    trees={}
    B6=np.abs(Ys[:,:,:2].reshape(len(Ys),6)); C3=np.abs(Ys[:,:,2])
    for a in range(3):
        for b in range(6):
            idx=np.where((C3[:,a]>thr)&(B6[:,b]>thr))[0]
            if len(idx): trees[(a,b)]=(cKDTree(canon(Ys[idx],a,b),balanced_tree=False,compact_nodes=False),idx)
    return trees
def mitm(Xs,Ys,trees,C,k=4,chunk=200000):
    hs={}
    for g in Gb: hs.setdefault(pkey(C@g),C@g)
    best=(9,None)
    for Ch in hs.values():
        b=mitm1(Xs,Ys,trees,Ch,k,chunk)
        if b[0]<best[0]: best=b
    return best
def mitm1(Xs,Ys,trees,C,k=4,chunk=200000):
    T=T3(C); best=(9,None)
    for i in range(0,len(Xs),chunk):
        Z=np.einsum('nij,jk->nik',Xs[i:i+chunk],T)            # want Y ~ X T D
        a=np.abs(Z[:,:,2]).argmax(1); b=np.abs(Z[:,:,:2].reshape(len(Z),6)).argmax(1)
        for key,(tr,idx) in trees.items():
            sel=np.where((a==key[0])&(b==key[1]))[0]
            if not len(sel): continue
            d,j=tr.query(canon(Z[sel],*key),k=k,eps=0.5,workers=2)
            Yc=Ys[idx[j.reshape(-1)]]; Xc=np.repeat(Xs[i+sel],k,axis=0)
            U=np.einsum('nji,njk->nik',Xc.conj(),Yc)        # X^-1 Y
            e=err(U,C); m=e.argmin()
            if e[m]<best[0]: best=(e[m],(i+sel[m//k],idx[j.reshape(-1)[m]]))
    return best
def words(spec):   # spec like 'sf' : product left->right of s3-power and frame sets
    S=np.eye(3,dtype=np.complex64)[None]
    for ch in spec: S=np.einsum('aij,bjk->abik',S,W1 if ch=='s' else Fa).reshape(-1,3,3)
    return S
if __name__=='__main__':
    mode=sys.argv[1]
    rng=np.random.default_rng(7); q=rng.normal(size=4); q/=np.linalg.norm(q)
    targets={'tau60':tau_b,'rand1':W.conj().T@q2u(q)@W}
    if mode=='m3':   # validation vs exhaustive: X^-1 Y with X in {s f}, Y in {s f s f}
        Xs=words('sf'); Ys=words('fsfs'); t=time.time(); trees=build(Ys); print('tree built %.0fs, Y=%d'%(time.time()-t,len(Ys)),flush=True)
        for n,C in targets.items(): print('  m=3 MITM %s: %.4f (%.0fs)'%(n,mitm(Xs,Ys,trees,C)[0],time.time()-t),flush=True)
    if mode=='m4':
        nsub=int(sys.argv[2]); rs=np.random.default_rng(1); Ys=words('fsfs'); Om=words('sfsf'); Xs=Om[rs.choice(len(Om),nsub,replace=False)]; del Om
        t=time.time(); trees=build(Ys); print('tree built %.0fs, Y=%d X=%d'%(time.time()-t,len(Ys),len(Xs)),flush=True)
        out={}
        for n,C in targets.items():
            e,_=mitm(Xs,Ys,trees,C); out[n]=e; print('  m=4 MITM (%d of 5.76e6 left halves x all right halves) %s: %.4f (%.0fs)'%(nsub,n,e,time.time()-t),flush=True)
        np.save('t60b_m4_%d.npy'%nsub,out,allow_pickle=True)

import numpy as np, time, sys, io, contextlib
src=open('tau60_braid.py').read().split("t=time.time()")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
Fa=np.array(F); W1=np.array(P3)
A=np.einsum('aij,bjk->abik',W1,Fa).reshape(-1,3,3)            # s3^k g   (2400)
B=np.einsum('aij,bjk->abik',A,W1).reshape(-1,3,3)             # s3^k g s3^k (9600)
def m3(C,label):
    DC=dcoset(C); Cc=DC.reshape(len(DC),4).conj().T.astype(np.complex64); best=9; t=time.time(); arg=None
    for i,a in enumerate(A):
        Wm=np.einsum('ij,bjk->bik',a,B).astype(np.complex64)
        tr=np.abs(Wm[:,:2,:2].reshape(-1,4)@Cc).max(1)+np.abs(Wm[:,2,2]); j=np.argmax(tr)
        if 3-tr[j]<best: best=3-tr[j]; arg=(i,j)
    print('   %-12s m=3 exhaustive best error %.4f  (%.0fs)'%(label,np.sqrt(max(best,0)),time.time()-t),flush=True)
    return np.sqrt(max(best,0))
out={'tau':m3(tau_b,'tau60')}
rng=np.random.default_rng(7); qs=[]
for i in range(3):
    q=rng.normal(size=4); q/=np.linalg.norm(q); qs.append(q)
out['rand1']=m3(W.conj().T@q2u(qs[0])@W,'C2 random 1')
np.save('t60b_m3.npy',out,allow_pickle=True)

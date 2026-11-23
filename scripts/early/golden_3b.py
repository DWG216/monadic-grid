import numpy as np, io, contextlib
src=open('golden_janus.py').read().split("print('\\n=== TEST 1")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
E0,V0=np.linalg.eigh(H0); rng=np.random.default_rng(0)
psi0=V0[:,0]+0.6*V0[:,3]+0.5*np.linalg.qr(rng.normal(size=(D,1)))[0][:,0]; psi0/=np.linalg.norm(psi0)
# weight of psi0 on each degenerate pair of H0 and the first-order chiral shift of that pair
grp=[];k=0
while k<D:
    j=k
    while j+1<D and abs(E0[j+1]-E0[k])<1e-8: j+=1
    grp.append(list(range(k,j+1))); k=j+1
rows=[]
for g in grp:
    Vg=V0[:,g]; w=np.linalg.norm(Vg.T@psi0)**2
    if len(g)==2 and w>0.01:
        sh=np.linalg.eigvalsh(Vg.conj().T@C@Vg); rows.append((w,sh.max()))
for w,s in sorted(rows,reverse=True)[:4]: print('  degenerate pair, weight in start state %.3f: chiral shift +-%.4f*lam -> hand beat 2x shift = %.4f*lam'%(w,s,2*s))

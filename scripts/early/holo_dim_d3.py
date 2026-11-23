import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
# finite-volume radial operator H = -1/2 r^(1-d) d/dr(r^(d-1) d/dr) + V, Neumann at origin, symmetrised
def E0(d,N,R=60.0):
    h=R/N; rc=(np.arange(N)+0.5)*h; rf=np.arange(N+1)*h
    wc=rc**(d-1); wf=rf**(d-1)
    if d==1: V=np.abs(rc)
    elif d==2: V=np.log(rc)
    else: V=-rc**(2.0-d)
    a=wf[1:N]/(h*h)                    # coupling between cells i,i+1
    diag=np.zeros(N); diag[:-1]+=a; diag[1:]+=a; diag[-1]+=wf[N]/(h*h)  # Dirichlet at R
    diag=0.5*diag/wc + V
    off=-0.5*a/np.sqrt(wc[:-1]*wc[1:])
    H=diags([off,diag,off],[-1,0,1])
    return eigsh(H,k=1,which='SA',return_eigenvectors=False,tol=1e-8,maxiter=200000)[0]
for d in range(1,7):
    Es=[E0(d,N) for N in (1500,6000,24000)]
    grow=abs(Es[2]-Es[1])/max(1e-9,abs(Es[1]-Es[0]))
    trend='bounded (converging)' if abs(Es[2]-Es[1])<0.02*max(1,abs(Es[1])) else 'falls without bound'
    thr={1:'confining (no release)',2:'confining (no release)',3:'finite threshold 0 (bound + releasable)'}.get(d,'-')
    print('d=%d: E0 = %s -> %s | ionisation: %s'%(d,', '.join('%.5g'%e for e in Es),trend,thr),flush=True)

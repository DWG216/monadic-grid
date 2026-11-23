import numpy as np, itertools
from core import cz_factor
from distill import *
# brute force f(k,l) at N=4
N=4
f=cz_factor(N)
def dicke(N,k):
    v=np.zeros(2**N)
    for s in itertools.combinations(range(N),k):
        v[sum(1<<(N-1-i) for i in s)]=1
    return v/np.linalg.norm(v)
diag=np.array([(-1)**bin(((x>>N)&(2**N-1)) & (x&(2**N-1))).count('1') for x in range(4**N)])
err=0
for k in range(N+1):
  for l in range(N+1):
    psi=np.kron(dicke(N,k),dicke(N,l))
    err=max(err,abs(psi@(diag*psi)-f[k,l]))
print("f brute err",err)
# brute CZ leak N=7 code (2^14 dims)
C,Dx=setup(7); V=C.V(np.ones(1))
N=7
B=np.array([dicke(N,k) for k in range(N+1)]).T  # 2^N x (N+1)
L=B@V
diag=np.array([(-1)**bin(((x>>N)&(2**N-1)) & (x&(2**N-1))).count('1') for x in range(4**N)])
worst=0
for i in range(2):
  for j in range(2):
    out=diag*np.kron(L[:,i],L[:,j])
    tot=sum(abs(np.kron(L[:,a],L[:,b]).conj()@out)**2 for a in range(2) for b in range(2))
    worst=max(worst,1-tot)
print("N=7 brute leak",worst,"formula",cz_leak(V,7))
# threshold neighborhood N=67 r=2
C,Dx=setup(67); p0,ti,c,_=design(C,Dx,2); V=C.V(c); amp=amps(C,V,Dx)
for e in [0.48,0.486,0.4868,0.4869,0.487,0.49,0.495,0.499]:
    print(e, out_err(amp,targets[ti],e,67)[0]-e)

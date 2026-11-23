import numpy as np
def decompose(A):
    n=len(A); A=A-A.mean(0,keepdims=True)          # remove column constants (they do not change replicator dynamics)
    S=(A+A.T)/2; N=(A-A.T)/2
    # column-constant freedom can also absorb part of N: N_ij = b_j - b_i ; project it out
    b=N.mean(0); Nc=N-(b[None,:]-b[:,None])
    sS,sN=np.linalg.norm(S),np.linalg.norm(Nc)
    return sS**2/(sS**2+sN**2), sN**2/(sS**2+sN**2)
def hyper(n,c=10.0,base=2.0,par=False):
    m=n+1 if par else n; A=np.full((m,m),0.0)+base/m
    for i in range(n): A[i,(i-1)%n]+=c
    if par: A[n,0]+=1.2*c
    return A
mut=np.full((4,4),5.0); np.fill_diagonal(mut,0)
for name,A in [('mutual help (control)',mut),('hypercycle n=4',hyper(4)),('hypercycle n=6',hyper(6)),('hypercycle n=6 + free-rider',hyper(6,par=True))]:
    p,a=decompose(A); print('%-30s potential share %.2f | cycling share %.2f'%(name,p,a))
def simulate(A,T=40000,dt=0.002,seed=0):
    rng=np.random.default_rng(seed); x=rng.random(len(A)); x/=x.sum(); mf=[]
    for t in range(T):
        f=A@x; fb=x@f; x=x+dt*x*(f-fb); x=np.clip(x,1e-12,None); x/=x.sum()
        if t%20==0: mf.append(fb)
    mf=np.array(mf); tail=mf[len(mf)//2:]
    d=np.diff(tail); return tail.max()-tail.min(), (d<-1e-9).mean(), x
for name,A in [('mutual help (control)',mut),('hypercycle n=4',hyper(4)),('hypercycle n=6',hyper(6))]:
    amp,down,x=simulate(A)
    print('%-30s late mean-fitness swing %.4f | fraction of steps where it FALLS %.2f'%(name,amp,down))

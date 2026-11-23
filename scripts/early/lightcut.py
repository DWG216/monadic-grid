import numpy as np
N=400; lam=0.10; rng=np.random.default_rng(5)
def h(l):
    M=np.zeros((N,N),complex)
    for j in range(N):
        M[j,(j+1)%N]+=-1; M[(j+1)%N,j]+=-1
        M[j,(j+2)%N]+=1j*l; M[(j+2)%N,j]+=-1j*l
    return M
Ha=h(lam); eps,V=np.linalg.eigh(Ha)
def corr(beta):
    n=1/(1+np.exp(np.clip(beta*eps,-700,700)))
    U=np.vstack([V*np.sqrt(n),V*np.sqrt(1-n)])          # orbitals u_k = sqrt(n) e_k (+) sqrt(1-n) e_k  (shadow in particle-hole frame)
    return U@U.conj().T
c0=N//2; Rr=40; A=np.arange(c0-Rr,c0+Rr+1); x=A-c0; v=2.0
def weights(kind,beta):
    R=Rr+0.5
    if kind=='fixed-time (flat)': return np.ones_like(x,float)
    if kind=='light-cone (diamond)':
        L=beta*v/np.pi; return L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L)
    if kind=='control: random smooth':
        f=sum(rng.normal()*np.cos(k*np.pi*x/R+rng.uniform(0,6.3)) for k in range(1,5)); return 1.5+f/np.abs(f).max()
    if kind=='control: inverted':
        L=beta*v/np.pi; d=L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L); return d.max()-d+0.05*d.max()
def gen(hmat,w):
    sub=hmat[np.ix_(A,A)].copy(); W=np.sqrt(np.outer(w,w)) if False else (w[:,None]+w[None,:])/2   # weight each bond by its midpoint
    return sub*W
idx=np.concatenate([A,A+N])
kinds=['fixed-time (flat)','light-cone (diamond)','control: random smooth','control: inverted']
grid=np.linspace(-0.3,0.3,121)
print('aether chirality lam=%+.2f ; conjugate shadow = %+.2f ; region = %d sites (both sides)'%(lam,-lam,len(A)))
for beta in [1.0,2.0,5.0,10.0]:
    C=corr(beta)[np.ix_(idx,idx)]
    print('beta=%4.1f'%beta)
    for kind in kinds:
        w=weights(kind,beta); ga=gen(Ha,w); res=[]
        for lp in grid:
            gs=gen(h(-lp) if False else None,w) if False else None
            hs=h(-lp)  # shadow contributes h(-lam') in this frame; matched when lam'=-lam
            g=np.block([[ga,np.zeros_like(ga)],[np.zeros_like(ga),gen(hs,w)]])
            res.append(np.linalg.norm(g@C-C@g)/np.linalg.norm(g))
        res=np.array(res); k=np.argmin(res); s=slice(max(k-4,0),k+5)
        p=np.polyfit(grid[s],res[s]**2,2); xm=-p[1]/(2*p[0])
        same=res[np.argmin(abs(grid-lam))]
        print('   %-24s best shadow %+.4f  drift %.4f  | residual at best %.4f vs same-hand %.4f (contrast %.1fx)'%(kind,xm,abs(xm+lam),res[k],same,same/res[k]))

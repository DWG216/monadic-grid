import numpy as np, sys
Rr=int(sys.argv[1]); N=800; lam=0.10; beta=20.0; v=2.0
def h(l):
    M=np.zeros((N,N),complex)
    for j in range(N):
        M[j,(j+1)%N]+=-1; M[(j+1)%N,j]+=-1; M[j,(j+2)%N]+=1j*l; M[(j+2)%N,j]+=-1j*l
    return M
Ha=h(lam); eps,V=np.linalg.eigh(Ha); n=1/(1+np.exp(np.clip(beta*eps,-700,700)))
U=np.vstack([V*np.sqrt(n),V*np.sqrt(1-n)]); c0=N//2; A=np.arange(c0-Rr,c0+Rr+1); x=A-c0; idx=np.concatenate([A,A+N])
C=(U[idx]@U[idx].conj().T); R=Rr+0.5
def gen(hm,w): return hm[np.ix_(A,A)]*((w[:,None]+w[None,:])/2)
def wL(L): return L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L)
hs={lp:h(-lp) for lp in np.linspace(-0.13,-0.07,25)}
def drift(w):
    ga=gen(Ha,w); res=[]
    for lp,hm in hs.items():
        gs=gen(hm,w); Z=np.zeros_like(ga); g=np.block([[ga,Z],[Z,gs]]); res.append(np.linalg.norm(g@C-C@g)/np.linalg.norm(g))
    res=np.array(res); gr=np.array(list(hs)); k=np.argmin(res); s=slice(max(k-3,0),k+4); p=np.polyfit(gr[s],res[s]**2,2); return abs(-p[1]/(2*p[0])+lam)
S=np.exp(np.linspace(np.log(0.7),np.log(1.6),13)); L0=beta*v/np.pi; d=np.array([drift(wL(s*L0)) for s in S])
k=np.argmin(d); lo=max(k-2,0); hi=min(k+3,len(S)); pf=np.polyfit(np.log(S[lo:hi]),np.log(d[lo:hi]),2); sb=np.exp(-pf[1]/(2*pf[0]))
print('region %d sites (R/thermal length = %.1f): best stretch s = %.3f (grid %.3f), drift at best %.5f'%(2*Rr+1,R/L0,sb,S[k],d[k]),flush=True)

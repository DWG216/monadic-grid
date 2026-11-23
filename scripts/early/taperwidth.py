import numpy as np
src=open('lightcut.py').read().split("kinds=[")[0]; exec(src)
R=Rr+0.5
def wL(L): return L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L)
def drift(C,w,grid=np.linspace(-0.13,-0.07,61)):
    ga=gen(Ha,w); res=[]
    for lp in grid:
        g=np.block([[ga,np.zeros_like(ga)],[np.zeros_like(ga),gen(h(-lp),w)]]); res.append(np.linalg.norm(g@C-C@g)/np.linalg.norm(g))
    res=np.array(res); k=np.argmin(res); s=slice(max(k-4,0),k+5); p=np.polyfit(grid[s],res[s]**2,2); return abs(-p[1]/(2*p[0])+lam)
S=np.exp(np.linspace(np.log(0.2),np.log(5),17)); out={}
for beta in [5.0,10.0,20.0]:
    C=corr(beta)[np.ix_(idx,idx)]; L0=beta*v/np.pi
    d=np.array([drift(C,wL(s*L0)) for s in S]); out[beta]=d
    k=np.argmin(d); lo=max(k-2,0); hi=min(k+3,len(S)); pf=np.polyfit(np.log(S[lo:hi]),np.log(d[lo:hi]+1e-9),2); sb=np.exp(-pf[1]/(2*pf[0]))
    print('beta=%4.0f thermal length %.2f | best stretch s = %.2f (grid min %.2f) | drift at s=1: %.5f, at best: %.5f'%(beta,L0,sb,S[k],d[np.argmin(abs(S-1))],d[k]))
np.save('taperwidth.npy',np.vstack([S]+[out[b] for b in [5.0,10.0,20.0]]))
print('S=',np.round(S,3).tolist())
for b in out: print(b,np.round(out[b],5).tolist())

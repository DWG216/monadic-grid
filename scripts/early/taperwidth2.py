import numpy as np, sys
lamv=float(sys.argv[1])
src=open('lightcut.py').read().split("kinds=[")[0].replace("lam=0.10","lam=%r"%lamv); exec(src)
R=Rr+0.5
def wL(L): return L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L)
def drift(C,w):
    grid=np.linspace(-lam-0.03,-lam+0.03,61); ga=gen(Ha,w); res=[]
    for lp in grid:
        g=np.block([[ga,np.zeros_like(ga)],[np.zeros_like(ga),gen(h(-lp),w)]]); res.append(np.linalg.norm(g@C-C@g)/np.linalg.norm(g))
    res=np.array(res); k=np.argmin(res); s=slice(max(k-4,0),k+5); p=np.polyfit(grid[s],res[s]**2,2); return abs(-p[1]/(2*p[0])+lam), res[k]
S=np.exp(np.linspace(np.log(0.6),np.log(2.0),15)); beta=20.0
C=corr(beta)[np.ix_(idx,idx)]; L0=beta*v/np.pi
r=[drift(C,wL(s*L0)) for s in S]; d=np.array([a for a,b in r]); f=np.array([b for a,b in r])
k=np.argmin(f); lo=max(k-2,0); hi=min(k+3,len(S)); pf=np.polyfit(np.log(S[lo:hi]),f[lo:hi],2); sb=np.exp(-pf[1]/(2*pf[0]))
k2=np.argmin(d)
print('lam=%.2f speeds R/L = %.1f/%.1f | best s by residual floor = %.2f | by drift = %.2f (grid) | predicted faster/2 = %.2f'%(lamv,2+4*lamv,2-4*lamv,sb,S[k2],(2+4*lamv)/2))
print('   drift:',np.round(d,5).tolist())

import numpy as np
rng=np.random.default_rng(20261122); c=lambda *s: rng.normal(size=s)+1j*rng.normal(size=s)
def herm(): a=c(2,2); return (a+a.conj().T)/2
def pd(): a=c(2,2); return a@a.conj().T+0.1*np.eye(2)
Sig=lambda om,pi: 2*np.real(pi.conj()@om)
t1=max(abs(Sig(1j*x@p,p)) for x,p in ((herm(),c(2)) for _ in range(100))); print(f"T1 real points: max |Sigma| = {t1:.1e} ->",'PASS' if t1<1e-12 else 'FAIL')
neg=all(Sig(1j*(herm()+1j*pd())@p,p)<0 for p in (c(2) for _ in range(100))); pos=all(Sig(1j*(herm()-1j*pd())@p,p)>0 for p in (c(2) for _ in range(100)))
print("T2 forward tube Sigma < 0:",neg,"; backward tube Sigma > 0:",pos,"->",'PASS' if neg and pos else 'FAIL')
ok=True
for k in range(100):
    x=c(2,2)
    if k<50:
        u=c(2); v=c(2); d=np.outer(u,v)          # rank one = null separation
    else: d=c(2,2)
    y=x+d; s=np.linalg.svd(x-y,compute_uv=False); meet=s[-1]<1e-10*s[0]
    ok&=(meet==(k<50)) and (abs(np.linalg.det(x-y))<1e-10)==(k<50)
print("T3 lines meet iff x - y null:",'PASS' if ok else 'FAIL')
al=c(4); be=c(4); f=lambda Z: 1/((al@Z)**3*(be@Z)**3)
r=[]
for _ in range(20):
    Z=c(4); h=1e-6; Ups=sum(Z[a]*(f(Z+h*np.eye(4)[a])-f(Z-h*np.eye(4)[a]))/(2*h) for a in range(4)); r.append(abs(Ups/f(Z)+6))
print(f"T4 Upsilon f / f = -6 to {max(r):.1e}; helicity s = -(-6+2)/2 = +2 ->",'PASS' if max(r)<1e-6 else 'FAIL')

exec(open('g_lib.py').read()); rng=np.random.default_rng(20261122); C=lambda *s: rng.normal(size=s)+1j*rng.normal(size=s)
# path 2
a1=0; a1b=0
for _ in range(50):
    x=C(2,2); lam=C(2); pi=C(2); om,nu=amb(x,lam,pi); a1=max(a1,abs(om@lam+pi@nu))
    t=C(1)[0]; om2,nu2=amb(x+t*np.outer(lam,pi),lam,pi); a1b=max(a1b,abs(om2-om).max(),abs(nu2-nu).max())
print(f"A1 Z.W max {a1:.1e}; change along the null line {a1b:.1e} ->",'PASS' if a1<1e-12 and a1b<1e-12 else 'FAIL')
ok=True
for k in range(40):
    lam=C(2); pi=C(2); om=C(2); nu=C(2)
    if k<20: nu=nu-(om@lam+pi@nu)/(pi@pi)*pi   # project onto Z.W = 0 ... adjust nu so that Z.W = 0
    zw=om@lam+pi@nu
    # unknowns x (4 complex): i x pi = om ; -i x^T lam = nu
    A=np.zeros((4,4),complex); b=np.concatenate([om,nu])
    for i in range(2):
        for j in range(2):
            col=2*i+j; A[i,col]+=1j*pi[j]; A[2+j,col]+=-1j*lam[i]
    sol,res,rank,sv=np.linalg.lstsq(A,b,rcond=None); resid=np.linalg.norm(A@sol-b)/np.linalg.norm(b)
    if k<20:
        N=np.linalg.svd(A)[2][-1].conj().reshape(2,2)   # null direction of the solution line
        ok&=resid<1e-10 and rank==3 and abs(np.linalg.det(N))<1e-10*np.abs(N).max()**2
    else: ok&=resid>1e-3
print("A2 Z.W = 0: a null line of solutions; Z.W != 0: none ->",'PASS' if ok else 'FAIL')
# path 3
def pts(n,frw_=False):
    return [np.array([rng.uniform(0.8,1.5),*rng.normal(size=3)*0.3]) if frw_ else np.array([0.0,rng.uniform(3,8),rng.uniform(0.4,2.7),rng.uniform(0,6.28)]) for _ in range(n)]
P=pts(20); S=[Rkk(schw(1),x,rng)[0] for x in P]; print(f"T1 Schwarzschild max |R_kk| {max(S):.1e} ->",'PASS' if max(S)<1e-5 else 'FAIL')
P=[np.array([0.0,rng.uniform(1,6),rng.uniform(0.4,2.7),rng.uniform(0,6.28)]) for _ in range(20)]
D=[Rkk(dsit(10),x,rng) for x in P]; dk=max(v for v,_ in D); dr=min(abs(R).max() for _,R in D)
print(f"T2 de Sitter max |R_kk| {dk:.1e}; min over points of max |R_ab| {dr:.2f} ->",'PASS' if dk<1e-5 and dr>0.01 else 'FAIL')
P=pts(20); Q=[Rkk(rn(1,0.1),x,rng)[0] for x in P]; F=[Rkk(frw,x,rng)[0] for x in pts(20,True)]
print(f"T3 Reissner-Nordstrom min |R_kk| {min(Q):.1e}; FRW dust min {min(F):.2f} ->",'PASS' if min(Q)>1e-4 and min(F)>0.1 else 'FAIL')
# path 6
al=C(4); be=C(4); ga=C(4); de=C(4)
f=lambda Z: 1/(dot(al,Z)**3*dot(be,Z)**3)
cob=lambda Z: f(Z)+dot(ga,Z)**2/dot(al,Z)**8+dot(de,Z)**3/dot(be,Z)**9
bad=lambda Z: f(Z)+0.1/(dot(al,Z)**2*dot(be,Z)**4)
g1=0; g2=1e9
for _ in range(20):
    x=C(2,2); F0=field(f,al,be,x); s=np.abs(F0).max()
    g1=max(g1,np.abs(field(cob,al,be,x)-F0).max()/s); g2=min(g2,np.abs(field(bad,al,be,x)-F0).max()/s)
print(f"G1 coboundary: max relative change {g1:.1e} ->",'PASS' if g1<1e-9 else 'FAIL')
print(f"G2 non-coboundary: min relative change {g2:.1e} ->",'PASS' if g2>1e-3 else 'FAIL')

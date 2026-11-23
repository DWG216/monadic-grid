# SANITY RUN for round 6 (not a test): new zeros, sparse plant, pipeline control. Small nulls (30 draws, seed 1).
import time; t0=time.time()
exec(open('t11_lib.py').read())
G=zeros_to(600); NT=theta(600)/np.pi+1
print(f"zeros to 600: {len(G)} (Riemann-von Mangoldt main term {NT:.1f}); first {G[0]:.4f}; below 400: {np.sum(G<400)}; {time.time()-t0:.0f}s")
g=G[G<400]; e1=np.zeros(len(g)); e1[0]=1; rng=np.random.default_rng(1)
def pk(gg,w,u0):
    a,b,_=jacobi(gg,w); e=np.zeros(len(gg)); e[0]=1; return peak(lambda u: kpm(a,b,e,u).real,u0)
s=0.5+1j*g; wsp=np.abs(1+2**(-s)+3**(-s))**2; wfk=np.abs(1+2.37**(-s)+3.71**(-s))**2
for nm,w in (('sparse',wsp),('fake sparse',wfk)):
    for un,u0 in (('ln2',np.log(2)),('ln3',np.log(3)),('ln3/2',np.log(1.5))):
        v=pk(g,w,u0); q=np.quantile([pk(g,rng.permutation(w),u0) for _ in range(30)],0.95); print(f"{nm} {un}: {v:.2f} vs null95 {q:.2f}")
print(f"{time.time()-t0:.0f}s")
rhoG=0.5+1j*G; zpG=zeta_prime(G); ns=list(range(2,31))
cpsi=(1-G/600)/rhoG; J=op_jumps(G,cpsi,ns); pp=[n for n in ns if lam(n)>0]
print("pipeline control (1/rho, new zeros): prime-power jumps negative",np.mean([J[ns.index(n)]<0 for n in pp]),"ratio",np.median([abs(J[ns.index(n)]) for n in pp])/np.median([abs(J[ns.index(n)]) for n in ns if lam(n)==0]))
cm=(1-G/600)/(rhoG*zpG); Jm=op_jumps(G,cm,ns); sq=[n for n in ns if mu(n)]
print("Mobius on new zeros, full operator: signs",sum(np.sign(Jm[ns.index(n)])==mu(n) for n in sq),"/18")
for K in (len(G)//4,len(G)//2): Jk=op_jumps(G,cm,ns,K); print(f"  K={K}: signs",sum(np.sign(Jk[ns.index(n)])==mu(n) for n in sq))
print(f"{time.time()-t0:.0f}s")

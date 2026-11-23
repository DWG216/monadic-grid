# SANITY RUN (not a test): do the detectors behave? Run before predictions are frozen.
exec(open('t10_lib.py').read())
rng=np.random.default_rng(1)
# 1. entries-only spectral function = eigen sum (identity check)
w=np.ones(len(g)); a,b,Q=jacobi(g,w); us=np.array([0.3,0.69,1.5,3.4])
direct=np.array([np.sum(w/w.sum()*np.exp(1j*g*u)) for u in us]); e1=np.zeros(len(g)); e1[0]=1
print("1 eig err",f"{eigerr(a,b,g):.1e}","; kpm vs eigen sum max err",f"{np.abs(kpm(a,b,e1,us)-direct).max():.1e}")
# 2. old detector vs a huge planted ln2 modulation
wp=1+0.9*np.cos(g*np.log(2)); a,b,Q=jacobi(g,wp); P=old_detector(a,[np.log(2)])[0]
N=[old_detector(jacobi(g,rng.permutation(wp))[0],[np.log(2)])[0] for _ in range(50)]
print("2 old detector, planted ln2: percentile",np.mean(np.array(N)<P))
# 3. entries-only detector on the same plant
pk=peak(lambda u: kpm(a,b,e1,u).real,np.log(2))
N=[]
for _ in range(50):
    aa,bb,_=jacobi(g,rng.permutation(wp)); N.append(peak(lambda u: kpm(aa,bb,e1,u).real,np.log(2)))
print("3 kpm detector, planted ln2: peak",round(pk,2),"null 95th",round(np.quantile(N,0.95),2))
# 4. Mobius from entries: J carries |c|, readout vector f carries the phase
c=taper/(rho*zp); p=np.abs(c); a,b,Q=jacobi(g,p); f=Q@(np.conj(c)*np.sqrt(p.sum()/p))
ns=list(range(2,31)); d=0.012
Sx=lambda x: 2*np.real(kpm(a,b,f,np.atleast_1d(x)))
Jk=np.array([Sx(np.log(n)+d)[0]-Sx(np.log(n)-d)[0] for n in ns]); Jt=jumps(1/(rho*zp),ns)
print("4 eig err",f"{eigerr(a,b,g):.1e}","; max |jump(entries) - jump(t8)|",f"{np.abs(Jk-Jt).max():.1e}","; signs",sum(np.sign(Jk[i])==mu(n) for i,n in enumerate(ns) if mu(n)))

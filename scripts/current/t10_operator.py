# Round 5: can an operator's entries carry the Mobius information? Pre-registered: PREDICTIONS_round5_2026-11-22.md
exec(open('t10_lib.py').read())
L2=np.log(2); e1=np.zeros(len(g)); e1[0]=1; ND=200
def newpk(w,u0):
    a,b,_=jacobi(g,w); return peak(lambda u: kpm(a,b,e1,u).real,u0)
def nullq(w,fn,seed):
    r=np.random.default_rng(seed); return np.quantile([fn(r.permutation(w)) for _ in range(ND)],0.95)
# P1, P2
wp=1+0.9*np.cos(g*L2); a,b,_=jacobi(g,wp)
P=old_detector(a,[L2])[0]; r=np.random.default_rng(20261122)
pct=np.mean([old_detector(jacobi(g,r.permutation(wp))[0],[L2])[0]<P for _ in range(ND)])
print(f"P1 old detector, planted ln2: percentile {pct:.3f} -> {'blind (as predicted)' if pct<0.95 else 'SEES IT'}")
v=newpk(wp,L2); q=nullq(wp,lambda w: newpk(w,L2),20261122); print(f"P2 new detector, planted ln2: {v:.2f} vs null95 {q:.2f} {'PASS' if v>q else 'FAIL'}")
# P3, P4
PL=[(n,lam(n)) for n in range(2,51) if lam(n)>0]
wpr=np.abs(sum(l*n**(-0.5-1j*g) for n,l in PL))**2
xs=np.random.default_rng(20261122).uniform(2,50,len(PL)); wfk=np.abs(sum(l*x**(-0.5-1j*g) for x,(n,l) in zip(xs,PL)))**2
ok=True
for u0,nm in ((L2,'ln2'),(np.log(3),'ln3'),(np.log(1.5),'ln3/2')):
    v=newpk(wpr,u0); q=nullq(wpr,lambda w: newpk(w,u0),20261122); ok&=v>q; print(f"P3 primes planted, {nm}: {v:.2f} vs null95 {q:.2f} {'pass' if v>q else 'FAIL'}")
v=newpk(wfk,L2); q=nullq(wfk,lambda w: newpk(w,L2),20261122); print(f"P4 fake primes, ln2: {v:.2f} vs null95 {q:.2f} {'PASS (not above)' if v<=q else 'FAIL'}")
# R
ns=list(range(2,31)); sqf=[n for n in ns if mu(n)]; nsq=[n for n in ns if not mu(n)]; d=0.012
c=taper/(rho*zp); p=np.abs(c)
def jmp(a,b,f): 
    Sx=lambda x: 2*np.real(kpm(a,b,f,np.array([x])))[0]
    return np.array([Sx(np.log(n)+d)-Sx(np.log(n)-d) for n in ns])
cnt=lambda J: int(sum(np.sign(J[ns.index(n)])==mu(n) for n in sqf))
ratio=lambda J: np.median([abs(J[ns.index(n)]) for n in sqf])/np.median([abs(J[ns.index(n)]) for n in nsq])
a,b,Q=jacobi(g,p); J1=jmp(a,b,e1)
r=np.random.default_rng(20261122); N1=[cnt(jmp(*jacobi(g,r.permutation(p))[:2],e1)) for _ in range(ND)]
print(f"R1 magnitudes only: signs {cnt(J1)}/18, null95 {np.quantile(N1,0.95):.1f}, ratio {ratio(J1):.2f} -> {'PASS (not recovered)' if cnt(J1)<=np.quantile(N1,0.95) else 'FAIL (recovered)'}")
f=Q@(np.conj(c)*np.sqrt(p.sum()/p)); J2=jmp(a,b,f)
r=np.random.default_rng(20261122); N2=[]
for _ in range(ND):
    cc=r.permutation(c); pp=np.abs(cc); aa,bb,QQ=jacobi(g,pp); N2.append(cnt(jmp(aa,bb,QQ@(np.conj(cc)*np.sqrt(pp.sum()/pp)))))
print(f"R2 with phase vector: signs {cnt(J2)}/18, null95 {np.quantile(N2,0.95):.1f}, ratio {ratio(J2):.1f}; vs t8 max diff {np.abs(J2-jumps(1/(rho*zp),ns)).max():.1e}")
print("R3 locality (K: signs, median |J_K/J_full| at squarefree n):")
res=[]
for K in (25,50,100,150,175,201):
    JK=jmp(a[:K],b[:K-1],f[:K]); m=np.median([abs(JK[ns.index(n)]/J2[ns.index(n)]) for n in sqf])
    res.append((K,cnt(JK),m)); print(f"   K={K}: {cnt(JK)}/18, {m:.2f}")
np.save('t10_results.npy',np.array(res)); np.save('t10_J.npy',np.array([J1,J2]))

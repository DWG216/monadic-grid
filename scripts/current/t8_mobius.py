exec(open('t8_lib.py').read())
ns=list(range(2,31)); sqf=[n for n in ns if mu(n)!=0]; nsq=[n for n in ns if mu(n)==0]
wc=1/rho; Jc=jumps(wc,ns); pp=[n for n in ns if lam(n)>0]; npp=[n for n in ns if lam(n)==0]
print(f"M1 control: prime powers negative {np.mean([Jc[ns.index(n)]<0 for n in pp]):.2f}; ratio {np.median([abs(Jc[ns.index(n)]) for n in pp])/np.median([abs(Jc[ns.index(n)]) for n in npp]):.2f}")
wm=1/(rho*zp); J=jumps(wm,ns)
cnt=lambda JJ: sum(np.sign(JJ[ns.index(n)])==mu(n) for n in sqf)
c=cnt(J); ratio=np.median([abs(J[ns.index(n)]) for n in sqf])/np.median([abs(J[ns.index(n)]) for n in nsq])
print(f"M2 Mobius weights: correct signs {c}/18; ratio squarefree/non-squarefree {ratio:.2f}")
print("   n, mu, jump*sqrt(n):",[(n,mu(n),round(J[ns.index(n)]*np.sqrt(n),2)) for n in ns])
rng=np.random.default_rng(20261122); NA=[cnt(jumps(rng.permutation(wm),ns)) for _ in range(200)]
print(f"M3 null A (permuted weights): 95th pct {np.quantile(NA,0.95):.1f}, max {max(NA)}; real {c}")
rng=np.random.default_rng(20261123); sp=np.diff(g); NB=[]
for _ in range(200):
    gs=np.concatenate([[g[0]],g[0]+np.cumsum(rng.permutation(sp))])
    Sx=lambda x: 2*np.real(np.sum((1-gs/400)*wm*np.exp(1j*gs*x)))
    NB.append(sum(np.sign(Sx(np.log(n)+0.012)-Sx(np.log(n)-0.012))==mu(n) for n in sqf))
print(f"M4 null B (shuffled spacings): 95th pct {np.quantile(NB,0.95):.1f}, max {max(NB)}; real {c}")
print(f"M5 corr(|J|, 1/sqrt n) over squarefree: {np.corrcoef([abs(J[ns.index(n)]) for n in sqf],[1/np.sqrt(n) for n in sqf])[0,1]:.3f}")
# post hoc (labelled): magnitude statistic under the nulls (not pre-registered)
def stats(JJ): return np.median([abs(JJ[ns.index(n)]) for n in sqf])/np.median([abs(JJ[ns.index(n)]) for n in nsq]), np.corrcoef([abs(JJ[ns.index(n)]) for n in sqf],[1/np.sqrt(n) for n in sqf])[0,1]
rng=np.random.default_rng(7); RA=[stats(jumps(rng.permutation(wm),ns)) for _ in range(200)]
print(f"post hoc null A: ratio 95th {np.quantile([r[0] for r in RA],0.95):.2f} (real {ratio:.1f}); corr 95th {np.quantile([r[1] for r in RA],0.95):.3f}")

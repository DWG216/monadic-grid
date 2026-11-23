exec(open('t8_lib.py').read())
ns=list(range(2,31)); rng=np.random.default_rng(1)
for name,w in (("control 1/rho",1/rho),("control permuted",rng.permutation(1/rho))):
    J=jumps(w,ns); pp=[n for n in ns if lam(n)>0]; npp=[n for n in ns if lam(n)==0]
    neg=np.mean([J[ns.index(n)]<0 for n in pp]); ratio=np.median([abs(J[ns.index(n)]) for n in pp])/np.median([abs(J[ns.index(n)]) for n in npp])
    print(f"{name}: prime powers with negative jump {neg:.2f}; median |jump| prime powers / others = {ratio:.2f}")
# spacing-shuffle null for the control
g0=g.copy(); sp=np.diff(g0); rng=np.random.default_rng(2)
gs=np.concatenate([[g0[0]],g0[0]+np.cumsum(rng.permutation(sp))])
def S2(u,wts,gg): return np.array([2*np.real(np.sum((1-gg/400)*wts*np.exp(1j*gg*x))) for x in np.atleast_1d(u)])
J=np.array([S2(np.log(n)+0.012,1/(0.5+1j*gs),gs)[0]-S2(np.log(n)-0.012,1/(0.5+1j*gs),gs)[0] for n in ns])
pp=[n for n in ns if lam(n)>0]; npp=[n for n in ns if lam(n)==0]
print(f"control, shuffled spacings: prime powers negative {np.mean([J[ns.index(n)]<0 for n in pp]):.2f}; ratio {np.median([abs(J[ns.index(n)]) for n in pp])/np.median([abs(J[ns.index(n)]) for n in npp]):.2f}")

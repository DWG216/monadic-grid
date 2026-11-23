exec(open('t13_lib.py').read()); import json, time
out={}
for name,m,k,fn,ref,refname in (("triangle",6,7,lambda x,m,idx: has_clique(x,m,idx,3),lambda x,m,idx: degree_ge(x,m,idx,4),"degree>=4"),
                                ("4-clique",6,8,lambda x,m,idx: has_clique(x,m,idx,4),lambda x,m,idx: degree_ge(x,m,idx,5),"degree=5")):
    t0=time.time(); E,idx,n,pts,pos,A,lam=setup(m,k); lab=classes(m,E,idx,pts); nc=lab.max()+1
    f=np.array([fn(x,m,idx) for x in pts]); g=np.array([ref(x,m,idx) for x in pts]); cv=lambda h: np.array([h[lab==c][0] for c in range(nc)])
    rng=np.random.default_rng(20261122)
    t1=abs(boundary(f,A)-boundary_spectral(f,A,lam))<1e-6*boundary(f,A) and all(abs(boundary(h,A)-boundary_spectral(h,A,lam))<1e-6*boundary(h,A) for h in [(rng.random(len(pts))<0.5).astype(int) for _ in range(20)])
    H=hit_table(n,pts,lab,6)
    cf,cg=cv(f),cv(g); rng=np.random.default_rng(20261122); N=[]
    while len(N)<200:
        c=rng.permutation(cf)
        if 0<c.sum()<nc: N.append((witness(c,H,1),witness(c,H,0),int(sens(c[lab],A).max())))
    N=np.array(N); q5=np.quantile(N[:,0],0.05)
    w1f,w0f,w1g,w0g=witness(cf,H,1),witness(cf,H,0),witness(cg,H,1),witness(cg,H,0)
    print(f"{name} (k={k}): T1 boundary = spectral formula: {'PASS' if t1 else 'FAIL'}; boundary {boundary(f,A):.0f}")
    print(f"  null W1 counts by size {np.bincount(N[:,0],minlength=8).tolist()} (5th pct {q5:.0f}); null W0 counts {np.bincount(N[:,1],minlength=8).tolist()}")
    print(f"  R1 clique W1 = {w1f} -> {'PASS' if w1f<=q5 and w1f==(3 if name=='triangle' else 6) else 'FAIL'};  R2 {refname} W1 = {w1g} -> {'PASS' if w1g<=q5 else 'FAIL'}")
    print(f"  R3 clique W0 = {w0f}{'+' if w0f==7 else ''} > W1: {'PASS' if w0f>w1f else 'FAIL'}; {refname} W0 = {w0g}{'+' if w0g==7 else ''}")
    print(f"  E1 max sensitivity: clique {int(sens(f,A).max())}, {refname} {int(sens(g,A).max())}, null {N[:,2].min()}..{N[:,2].max()} (median {int(np.median(N[:,2]))}); densities {f.mean():.3f}, {g.mean():.3f}; {time.time()-t0:.0f}s",flush=True)
    out[name]=dict(nullW1=N[:,0].tolist(),w1=[w1f,w1g],w0=[w0f,w0g])
# E1 overlap of minimal witnesses (pairs of edges), m = 6
E=list(it.combinations(range(6),2))
def fam_clique(q): return [frozenset(it.combinations(T,2)) for T in it.combinations(range(6),q)]
def fam_star(d): return [frozenset(tuple(sorted((c,v))) for v in S) for c in range(6) for S in it.combinations([v for v in range(6) if v!=c],d)]
for nm,F in (("triangle",fam_clique(3)),("degree>=4 stars",fam_star(4)),("4-clique",fam_clique(4)),("degree=5 stars",fam_star(5))):
    sz=len(next(iter(F))); one=max(sum(e in W for W in F) for e in E)/len(F); two=max(sum(a in W and b in W for W in F) for a,b in it.combinations(E,2))/len(F)
    print(f"  E1 witnesses {nm}: {len(F)} of size {sz}; largest share through one edge {one:.3f} (size/15 = {sz/15:.3f}); through a pair {two:.3f}")
json.dump(out,open('t13_results.json','w'))

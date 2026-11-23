exec(open('t12_lib.py').read()); import json
res={}
for name,m,k,q in (("triangle",6,7,3),("4-clique",6,8,4)):
    E,idx,n,pts,pos,A,lam=setup(m,k); lab=classes(m,E,idx,pts); nc=lab.max()+1
    f=np.array([has_clique(x,m,idx,q) for x in pts]); cls_f=np.array([f[lab==c][0] for c in range(nc)])
    w=weights(f,A,lam); L=float(w@np.arange(1,len(w)+1))
    rng=np.random.default_rng(20261122); null=[]
    while len(null)<200:
        g=rng.permutation(cls_f)[lab]
        if 0<g.mean()<1: null.append(mean_level(g,A,lam))
    q5=np.quantile(null,0.05)
    print(f"{name} m={m} k={k}: slice {len(pts)}, classes {nc}, density {f.mean():.3f}")
    print(f"  E1 shares by level {np.round(w,4)}; highest nonzero level {int(np.max(np.nonzero(w>1e-9)))+1}")
    print(f"  mean level {L:.3f}; invariant null 5th {q5:.3f} median {np.median(null):.3f} 95th {np.quantile(null,0.95):.3f} -> {'PASS' if L<q5 else 'FAIL'} (percentile {np.mean(np.array(null)<L):.3f})")
    res[name]=dict(w=w.tolist(),L=L,null=null)
    if name=="triangle":
        mono=np.array([int(x&0b111==0b111) for x in pts]); wm=weights(mono,A,lam); print("  C1 monomial shares",np.round(wm,6),"->",'PASS' if wm[3:].sum()<1e-9 else 'FAIL')
        ind=np.array([(lab==c).astype(float) for c in range(nc)]); ranks=[]
        comps=[levels(v,A,lam) for v in ind]
        for j in range(len(lam)): ranks.append(int(np.linalg.matrix_rank(np.array([c[j] for c in comps]),tol=1e-6)))
        print("  I1 invariant tones per level",ranks,"->",'PASS' if ranks==[1,0,1,3,4,6,6,3] else 'FAIL')
json.dump(res,open('t12_results.json','w'))

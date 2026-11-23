exec(open('t14_lib.py').read()); import json
out={}
for name,m,k,fn,ref,refname in (("triangle",6,7,lambda x,m,idx: has_clique(x,m,idx,3),lambda x,m,idx: degree_ge(x,m,idx,4),"degree>=4"),
                                ("4-clique",6,8,lambda x,m,idx: has_clique(x,m,idx,4),lambda x,m,idx: degree_ge(x,m,idx,5),"degree=5")):
    E,idx,n,pts,pos,A,lam=setup(m,k); lab=classes(m,E,idx,pts); nc=lab.max()+1
    f=np.array([fn(x,m,idx) for x in pts]); g=np.array([ref(x,m,idx) for x in pts])
    one=np.array([x&1 for x in pts]); par=np.array([bin(x&0b11111).count('1')%2 for x in pts])
    Kf,Kg,K1,Kp=[pairing(h,A,pts)[0] for h in (f,g,one,par)]
    cf=np.array([f[lab==c][0] for c in range(nc)]); rng=np.random.default_rng(20261122); null=[]
    while len(null)<100:
        c=rng.permutation(cf)
        if 0<c.sum()<nc: null.append(pairing(c[lab],A,pts)[0])
    med=np.median(null)
    print(f"{name} slice (k={k}): P1 single edge K = {K1:.3f} {'PASS' if abs(K1-1)<1e-6 else 'FAIL'}; P2 parity K = {Kp:.2f} {'PASS' if Kp>15 else 'FAIL'}")
    print(f"  R1 K({name}) = {Kf:.2f} vs K({refname}) = {Kg:.2f} -> {'PASS' if Kf>Kg else 'FAIL'}")
    print(f"  R2 null: min {min(null):.2f}, median {med:.2f}, max {max(null):.2f}; clique percentile {np.mean(np.array(null)<Kf):.2f} -> {'PASS' if Kf<med else 'FAIL'}; K/15 = {Kf/15:.2f}",flush=True)
    out[name]=dict(K=[Kf,Kg,K1,Kp],null=null,ref=refname)
json.dump(out,open('t14_results.json','w'))

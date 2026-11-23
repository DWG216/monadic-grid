exec(open('t14_lib.py').read()); rng=np.random.default_rng(1)
m,k=5,5; E,idx,n,pts,pos,A,lam=setup(m,k); lab=classes(m,E,idx,pts); nc=lab.max()+1
f=np.array([has_clique(x,m,idx,3) for x in pts]); g=np.array([degree_ge(x,m,idx,3) for x in pts])
par=np.array([bin(x&0b11111).count('1')%2 for x in pts])   # parity of 5 fixed edges: a known formula-hard shape (control)
one=np.array([x&1 for x in pts])                            # a single edge: formula size 1 (control)
for nm,h in (("single edge (control, true size 1)",one),("parity of 5 edges (control)",par),("triangle",f),("degree>=3",g)): print(nm,"K, B, sigma =",np.round(pairing(h,A,pts),3))
cf=np.array([f[lab==c][0] for c in range(nc)]); K=[]
for _ in range(60):
    c=rng.permutation(cf)
    if 0<c.sum()<nc: K.append(pairing(c[lab],A,pts)[0])
print("invariant null K: min",round(min(K),2),"median",round(np.median(K),2),"max",round(max(K),2))

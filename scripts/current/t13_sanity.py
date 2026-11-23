# SANITY RUN (not a test), m = 5, k = 5.
exec(open('t13_lib.py').read()); rng=np.random.default_rng(1)
m,k=5,5; E,idx,n,pts,pos,A,lam=setup(m,k); lab=classes(m,E,idx,pts); nc=lab.max()+1
f=np.array([has_clique(x,m,idx,3) for x in pts]); g=np.array([degree_ge(x,m,idx,3) for x in pts])
print("boundary direct vs spectral:",boundary(f,A),round(boundary_spectral(f,A,lam),6))
H=hit_table(n,pts,lab,5); print("partial assignments by size:",[len(T) for T in H])
cv=lambda h: np.array([h[lab==c][0] for c in range(nc)])
for nm,h in (("triangle",f),("degree>=3",g)):
    c=cv(h); print(nm,"density",round(h.mean(),3),"W1",witness(c,H,1),"W0",witness(c,H,0),"max sens",int(sens(h,A).max()))
cf=cv(f); W=[]
for _ in range(60):
    c=rng.permutation(cf)
    if 0<c.sum()<nc: W.append((witness(c,H,1),witness(c,H,0),int(sens(c[lab],A).max())))
W=np.array(W); print("null W1 values",np.bincount(W[:,0]),"W0",np.bincount(W[:,1]),"max sens range",W[:,2].min(),W[:,2].max())

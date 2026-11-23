# SANITY RUN (not a test), m = 5 only: positive control, null spread.
exec(open('t12_lib.py').read()); rng=np.random.default_rng(1)
m,k=5,5; E,idx,n,pts,pos,A,lam=setup(m,k); print("slice points",len(pts),"levels",len(lam)-1)
mono=np.array([int(x&0b111==0b111) for x in pts]); w=weights(mono,A,lam); print("control: degree-3 monomial, variance share by level:",np.round(w,6))
f=np.array([has_clique(x,m,idx,3) for x in pts]); lab=classes(m,E,idx,pts); nc=lab.max()+1
print("triangle slice: density",f.mean(),"iso classes",nc,"weights",np.round(weights(f,A,lam),4),"mean level",round(mean_level(f,A,lam),3))
cls_f=np.array([f[lab==c][0] for c in range(nc)]); ok=all((f[lab==c]==cls_f[c]).all() for c in range(nc)); print("triangle is class-invariant:",ok)
sizes=np.bincount(lab); null=[]
for _ in range(100):
    g=rng.permutation(cls_f)[lab]
    if 0<g.mean()<1: null.append(mean_level(g,A,lam))
print("invariant null mean level: 5th",round(np.quantile(null,0.05),3),"median",round(np.median(null),3),"95th",round(np.quantile(null,0.95),3))
r=[mean_level((rng.random(len(pts))<f.mean()).astype(int),A,lam) for _ in range(30)]; print("unstructured random: median",round(np.median(r),3))

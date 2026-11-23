import numpy as np, time
exec(open('t45_coil_sweep.py').read().split("rows=[]")[0])
exec("def _x():pass")
src=open('t45_coil_sweep.py').read()
exec(src[src.index('def wire_order'):src.index('lam=Ltot*best')])
def ratios(o,xfrac):
    Ac=wire_order(o,a); L=np.sum(np.linalg.norm(np.diff(Ac,axis=0),axis=1))
    M=[abs(mutual_c(Ac,wire_order(o[k:]+o[:k],a+0.0005),L*xfrac)) for k in range(3)]
    return M[1]/M[0],M[2]/M[0]
def dist(r): return np.hypot(r[0]-0.5,r[1]-0.25)
t=time.time(); xs=[0.45,0.5,0.55]
dbl=[ratios(list(order),x) for x in xs]
print('doubling',[tuple(round(v,3) for v in r) for r in dbl], 'dist',[round(dist(r),3) for r in dbl], round(time.time()-t,1),'s')
rng=np.random.default_rng(1); D=[]
for i in range(40):
    o=list(rng.permutation(order)); D.append([dist(ratios(o,x)) for x in xs])
D=np.array(D); dd=np.array([dist(r) for r in dbl])
for j,x in enumerate(xs):
    print(f'lambda/L={x}: doubling dist {dd[j]:.3f}; random orders median {np.median(D[:,j]):.3f}, fraction closer than doubling {np.mean(D[:,j]<dd[j]):.2f}')

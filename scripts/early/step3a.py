import numpy as np
exec(open('radiation2.py').read().split("print('light-cone")[0])
cone=[(sg*(1-np.linalg.norm(x)),x) for sg in (1,-1) for x in circ(60,72)]
Rw=rows(cone); u,s,vt=np.linalg.svd(Rw); null=vt[(s>1e-9*s[0]).sum():]
w=(abs(null)**2).sum(0).reshape(K,M)        # weight of null space on each (wave, u-sample)
print('cone rank',rk(Rw),'/168; null-space weight by u-sample (summed over waves):'); print('  u =',np.round(ug,2).tolist()); print('  w =',np.round(w.sum(0),2).tolist())
keep=np.array([abs(ug[j])<=0.9 for k in range(K) for j in range(M)])
print('cone, unknowns restricted to |u|<=0.9: rank %d / %d'%(rk(Rw[:,keep]),keep.sum()))
sl=rows([(0.0,x) for x in circ(60,72)],deriv=True); print('slice+rate, restricted: rank %d / %d'%(rk(sl[:,keep]),keep.sum()))

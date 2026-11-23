import numpy as np
exec(open('radiation.py').read().split("e=np.array")[0])
h=1e-4
def rows(points,deriv=False):
    R=[]
    for t,x in points:
        r=np.zeros(K*M); d=np.zeros(K*M)
        for k in range(K):
            u=t-n[k]@x; r[k*M:(k+1)*M]=interp_row(u)
            d[k*M:(k+1)*M]=(interp_row(u+h)-interp_row(u-h))/(2*h)
        R.append(r); 
        if deriv: R.append(d)
    return np.array(R)
def rk(A): s=np.linalg.svd(A,compute_uv=False); return int((s>1e-9*s[0]).sum())
circ=lambda R,P:[r*np.array([np.cos(p),np.sin(p)]) for r in np.linspace(0,1,R) for p in np.linspace(0,2*np.pi,P,endpoint=False)]
cone=lambda R,P:[(sg*(1-np.linalg.norm(x)),x) for sg in (1,-1) for x in circ(R,P)]
print('light-cone boundary, field only:   coarse %d, fine %d, finer %d  / 168'%(rk(rows(cone(30,36))),rk(rows(cone(60,72))),rk(rows(cone(90,96)))))
print('future light cone ONLY (one sheet): fine %d / 168'%rk(rows([(1-np.linalg.norm(x),x) for x in circ(60,72)])))
print('spacelike slice, field only:        fine %d / 168'%rk(rows([(0.0,x) for x in circ(60,72)])))
print('spacelike slice, field + rate:      fine %d / 168'%rk(rows([(0.0,x) for x in circ(60,72)],deriv=True)))

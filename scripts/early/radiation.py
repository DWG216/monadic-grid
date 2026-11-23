import numpy as np
K=8; M=21; ug=np.linspace(-1,1,M); ang=np.arange(K)*np.pi/K*2; n=np.stack([np.cos(ang),np.sin(ang)],1)
def interp_row(u):  # linear interpolation weights onto grid
    w=np.zeros(M); 
    if u<ug[0] or u>ug[-1]: return w
    j=min(np.searchsorted(ug,u)-1,M-2); j=max(j,0); f=(u-ug[j])/(ug[j+1]-ug[j]); w[j]=1-f; w[j+1]=f; return w
def rank(points):
    rows=[]
    for t,x in points:
        r=np.zeros(K*M)
        for k in range(K): r[k*M:(k+1)*M]=interp_row(t-n[k]@x)
        rows.append(r)
    s=np.linalg.svd(np.array(rows),compute_uv=False); return int((s>1e-9*s[0]).sum())
e=np.array([1.0,0.3]); e/=np.linalg.norm(e)
sets={
 'static worldline (x=0)':[(t,np.zeros(2)) for t in np.linspace(-1,1,120)],
 'moving timelike geodesic (v=0.6)':[(s,0.6*s*e) for s in np.linspace(-1/1.6,1/1.6,120)],
 'single light ray':[(s,s*e) for s in np.linspace(-0.5,0.5,120)],
 'light-cone boundary of diamond':[(sg*(1-r),r*np.array([np.cos(p),np.sin(p)])) for sg in (1,-1) for r in np.linspace(0,1,30) for p in np.linspace(0,2*np.pi,36,endpoint=False)],
 'spacelike slice t=0 (disk)':[(0.0,r*np.array([np.cos(p),np.sin(p)])) for r in np.linspace(0,1,30) for p in np.linspace(0,2*np.pi,36,endpoint=False)],
}
print('unknowns: %d complex numbers (8 waves x 21 samples of hand -). Full rank = reality forced for every wave.'%(K*M))
for k,v in sets.items(): print('  %-34s rank %3d / %d'%(k,rank(v),K*M))

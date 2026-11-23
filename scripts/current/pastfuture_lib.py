exec(open('cone_lib.py').read())
def cone2(g,x0,a,b,lams,sign,h=0.01,eps=1e-4):
    """sign = +1 future cone, -1 past cone along the same ray; screen made right-handed relative to the direction of travel."""
    k,s1,s2=frame(g,x0,a,b); c,sn=np.cos(0.6),np.sin(0.6); s1,s2=c*s1+sn*s2,-sn*s1+c*s2; s2=sign*s2; K=sign*k
    X0=geod(g,x0,K,lams,h); dX=[]
    for s in (s1,s2):
        p=geod(g,x0,K+eps*s,lams,h); m=geod(g,x0,K-eps*s,lams,h); dX.append((p-m)/(2*eps))
    area=[]; shape=[]; ang=[]
    for i,L in enumerate(lams):
        gx=g(X0[i]); Gm=np.array([[dX[p][i]@gx@dX[q][i] for q in (0,1)] for p in (0,1)])/L**2; Gm=(Gm+Gm.T)/2
        mu,V=np.linalg.eigh(Gm); area.append(1-np.sqrt(mu[0]*mu[1])); shape.append(mu[1]-mu[0])
        v=V[:,1]; ang.append(np.mod(np.arctan2(v[1],v[0]),np.pi))           # major axis angle in the right-handed screen, mod pi
    return np.array(area),np.array(shape),np.array(ang)
def angdiff(a,b): d=np.mod(a-b,np.pi); return min(d,np.pi-d)

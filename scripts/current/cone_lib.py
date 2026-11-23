# Order-by-order obstruction along light rays: shoot a thin cone of null geodesics from a vertex, measure area (Ricci) and shape (Weyl).
exec(open('g_lib.py').read())
def riemann(g,x,h=1e-3):
    G=christoffel(g,x); dG=np.zeros((4,4,4,4))
    for e_ in range(4):
        e=np.zeros(4); e[e_]=h; dG[e_]=(christoffel(g,x+e)-christoffel(g,x-e))/(2*h)
    R=np.zeros((4,4,4,4))   # R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce}G^e_{db} - G^a_{de}G^e_{cb}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    R[a,b,c,d]=dG[c][a,d,b]-dG[d][a,c,b]+sum(G[a,c,e]*G[e,d,b]-G[a,d,e]*G[e,c,b] for e in range(4))
    return R
def frame(g,x,a,b):
    gx=g(x); s=np.sqrt(np.abs(np.diag(gx))); E=np.diag(1/s)            # orthonormal e_t, e_r, e_theta, e_phi (diagonal metrics)
    n=np.cos(a)*E[1]+np.sin(a)*(np.cos(b)*E[2]+np.sin(b)*E[3])
    s1=-np.sin(a)*E[1]+np.cos(a)*(np.cos(b)*E[2]+np.sin(b)*E[3]); s2=-np.sin(b)*E[2]+np.cos(b)*E[3]
    return E[0]+n, s1, s2
def direct(g,x,a,b):
    k,s1,s2=frame(g,x,a,b); R=riemann(g,x); gx=g(x)
    T=np.einsum('abcd,b,d->ac',R,k,k)                                 # tidal operator R^a_{bcd} k^b k^d
    O=np.array([[s@gx@T@u for u in (s1,s2)] for s in (s1,s2)]); O=(O+O.T)/2
    ev=np.linalg.eigvalsh(O); return ev.sum(), (ev[1]-ev[0])/2         # trace (= R_kk), Weyl part w
def geod(g,x0,v0,lams,h):
    def acc(x,v): G=christoffel(g,x); return -np.einsum('abc,b,c->a',G,v,v)
    out=[]; x=x0.copy(); v=v0.copy(); lam=0.0
    for L in lams:
        while lam<L-1e-12:
            st=min(h,L-lam)
            k1x=v; k1v=acc(x,v); k2x=v+st/2*k1v; k2v=acc(x+st/2*k1x,v+st/2*k1v)
            k3x=v+st/2*k2v; k3v=acc(x+st/2*k2x,v+st/2*k2v); k4x=v+st*k3v; k4v=acc(x+st*k3x,v+st*k3v)
            x=x+st/6*(k1x+2*k2x+2*k3x+k4x); v=v+st/6*(k1v+2*k2v+2*k3v+k4v); lam+=st
        out.append(x.copy())
    return np.array(out)
def cone(g,x0,a,b,lams,h=0.01,eps=1e-4):
    k,s1,s2=frame(g,x0,a,b); X0=geod(g,x0,k,lams,h); dX=[]
    for s in (s1,s2):
        p=geod(g,x0,k+eps*s,lams,h); m=geod(g,x0,k-eps*s,lams,h); dX.append((p-m)/(2*eps))
    area=[]; shape=[]
    for i,L in enumerate(lams):
        gx=g(X0[i]); Gm=np.array([[dX[p][i]@gx@dX[q][i] for q in (0,1)] for p in (0,1)])/L**2
        mu=np.linalg.eigvalsh((Gm+Gm.T)/2); area.append(1-np.sqrt(mu[0]*mu[1])); shape.append(mu[1]-mu[0])
    return np.array(area),np.array(shape)
def fit(lams,y):
    A=np.vstack([lams**p for p in (1,2,3,4)]).T; c=np.linalg.lstsq(A,y,rcond=None)[0]; return c   # c[0]: order 1, c[1]: order 2

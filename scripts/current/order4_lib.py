exec(open('kerr_lib.py').read())
def transport(g,x0,k0,e1,e2,lams,h=0.01):
    """RK4 for the central null geodesic with two parallel-transported screen vectors; returns states at lams."""
    def rhs(S):
        x,k,a,b=S[:4],S[4:8],S[8:12],S[12:]; G=christoffel(g,x)
        return np.concatenate([k,-np.einsum('abc,b,c->a',G,k,k),-np.einsum('abc,b,c->a',G,k,a),-np.einsum('abc,b,c->a',G,k,b)])
    S=np.concatenate([x0,k0,e1,e2]); lam=0.0; out=[]
    for L in lams:
        while lam<L-1e-12:
            st=min(h,L-lam); a1=rhs(S); a2=rhs(S+st/2*a1); a3=rhs(S+st/2*a2); a4=rhs(S+st*a3); S=S+st/6*(a1+2*a2+2*a3+a4); lam+=st
        out.append(S.copy())
    return out
def tidal_series(g,x0,a,b):
    k,s1,s2=frame(g,x0,a,b); c,sn=np.cos(0.6),np.sin(0.6); s1,s2=c*s1+sn*s2,-sn*s1+c*s2
    lt=np.linspace(0,0.4,9); Ts=[]
    for S in transport(g,x0,k,s1,s2,lt):
        x,kk,e1,e2=S[:4],S[4:8],S[8:12],S[12:]; R=riemann(g,x); gx=g(x); Tm=np.einsum('abcd,b,d->ac',R,kk,kk)
        T=np.array([[u@gx@Tm@v for v in (e1,e2)] for u in (e1,e2)]); Ts.append((T+T.T)/2)
    Ts=np.array(Ts); co=np.polynomial.polynomial.polyfit(lt,Ts.reshape(len(lt),4),4)
    T0=co[0].reshape(2,2); T1=co[1].reshape(2,2); T2=2*co[2].reshape(2,2)
    return T0,T1,T2
def cone_matrix(g,x0,a,b,lams,h=0.01,eps=1e-4):
    k,s1,s2=frame(g,x0,a,b); c,sn=np.cos(0.6),np.sin(0.6); s1,s2=c*s1+sn*s2,-sn*s1+c*s2
    X0=geod(g,x0,k,lams,h); dX=[]
    for s in (s1,s2):
        p=geod(g,x0,k+eps*s,lams,h); m=geod(g,x0,k-eps*s,lams,h); dX.append((p-m)/(2*eps))
    Ms=[]
    for i,L in enumerate(lams):
        gx=g(X0[i]); Gm=np.array([[dX[p][i]@gx@dX[q][i] for q in (0,1)] for p in (0,1)])/L**2; Ms.append((Gm+Gm.T)/2-np.eye(2))
    Ms=np.array(Ms).reshape(len(lams),4); A=np.vstack([lams**p for p in range(2,8)]).T; co=np.linalg.lstsq(A,Ms,rcond=None)[0]
    return co[0].reshape(2,2),co[1].reshape(2,2),co[2].reshape(2,2)
def predicted(T0,T1,T2): return -T0/3, -T1/6, 2/45*T0@T0 - T2/20
rel=lambda X,Y: np.linalg.norm(X-Y)/np.linalg.norm(Y)

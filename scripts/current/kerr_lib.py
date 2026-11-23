exec(open('pastfuture_lib.py').read())
def kerr(M,a):
    def g(x):
        r,th=x[1],x[2]; S=r*r+a*a*np.cos(th)**2; D=r*r-2*M*r+a*a; s2=np.sin(th)**2
        G=np.zeros((4,4)); G[0,0]=-(1-2*M*r/S); G[0,3]=G[3,0]=-2*M*a*r*s2/S; G[1,1]=S/D; G[2,2]=S; G[3,3]=(r*r+a*a+2*M*a*a*r*s2/S)*s2
        return G
    return g
def frame(g,x,a,b):   # general: static observer + Gram-Schmidt (overrides the diagonal version)
    gx=g(x); ip=lambda p,q: p@gx@q; E=np.eye(4)
    u=E[0]/np.sqrt(-ip(E[0],E[0])); es=[]
    for v in (E[1],E[2],E[3]):
        w=v+ip(v,u)*u
        for e in es: w=w-ip(w,e)*e
        es.append(w/np.sqrt(ip(w,w)))
    er,et,ep=es
    n=np.cos(a)*er+np.sin(a)*(np.cos(b)*et+np.sin(b)*ep)
    s1=-np.sin(a)*er+np.cos(a)*(np.cos(b)*et+np.sin(b)*ep); s2=-np.sin(b)*et+np.cos(b)*ep
    return u+n, s1, s2
def fitd(lams,y,deg=6):
    A=np.vstack([lams**p for p in range(1,deg+1)]).T; return np.linalg.lstsq(A,y,rcond=None)[0]
def angle_fit(lams,ang,ref):
    # unwrap near ref, fit theta = t0 + t1 lambda on lambda <= 0.4
    d=np.array([np.mod(a_-ref+np.pi/2,np.pi)-np.pi/2 for a_ in ang])+ref; m=lams<=0.4+1e-9
    return np.polyfit(lams[m],d[m],1)[::-1]

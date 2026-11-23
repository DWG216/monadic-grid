exec(open('undermine.py').read().split('hits=[]')[0])
exec(open('frozen_fluid.py').read().split('def rep')[0].split('import')[0]) if False else None
def key(U):
    f=U.reshape(-1); i=np.argmax(abs(f)>1e-6); U=U*abs(f[i])/f[i]; return tuple(np.round(U.reshape(-1),6))
def grp(gs,cap=20000):
    gs=gs+[np.linalg.inv(x) for x in gs]; I=np.eye(len(gs[0])); seen={key(I)}; fr=[I]
    while fr:
        nw=[]
        for U in fr:
            for x in gs:
                V=x@U; kk=key(V)
                if kk not in seen:
                    seen.add(kk); nw.append(V)
                    if len(seen)>cap: return '>%d'%cap
        fr=nw
    return len(seen)
def block(k,j,Y):
    qn,adm,F,R=mk(k); E,Fs,M=F(j,j,j,Y)
    s1=np.diag([R(j,e) for e in E]); s2=M@np.diag([R(j,f) for f in Fs])@M.T
    return [s1.astype(complex),s2.astype(complex)],E
qn,adm,F,R=mk(6)
for Y in range(0,13):
    if not adm(2,2,0) : pass
    g,E=block(6,2,Y)
    if len(E)==0: continue
    print('SU(2)_6 spin-1, 3 strands, target Y=%g: window dim %d, projective image order %s'%(Y/2,len(E),grp(g)))

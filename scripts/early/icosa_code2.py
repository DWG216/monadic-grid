import numpy as np, itertools
exec(open('icosa_code.py').read().split("def q2u")[0])
def q2u(q): a,b,c,d=q; return a*I-1j*(b*X+c*Y+d*Z)
def tens(U):
    m=np.array([[1.]])
    for _ in range(n): m=np.kron(m,U)
    return m
def quat(axis,ang): u=np.array(axis)/np.linalg.norm(axis); return np.r_[np.cos(ang/2),u*np.sin(ang/2)]
def leak(q): T=tens(q2u(q)); return np.linalg.norm(T@V-P@T@V)
best=None
for az in np.linspace(0,2*np.pi/5,721):
    v1=[2/5**.5*np.cos(az),2/5**.5*np.sin(az),1/5**.5]
    L=leak(quat([0,0,1],2*np.pi/5))+leak(quat(v1,2*np.pi/5))
    if best is None or L<best[0]: best=(L,az)
L,az=best; print('code frame search: 5-fold axis z; second 5-fold axis at azimuth %.2f deg -> total leak %.1e'%(np.degrees(az),L))
v1=np.array([2/5**.5*np.cos(az),2/5**.5*np.sin(az),1/5**.5])
ico=[np.array([0,0,1.]),np.array([0,0,-1.])]
for k in range(5):
    a=az+2*np.pi*k/5; ico+=[np.array([2/5**.5*np.cos(a),2/5**.5*np.sin(a),1/5**.5]),np.array([2/5**.5*np.cos(a+np.pi/5),2/5**.5*np.sin(a+np.pi/5),-1/5**.5])]
faces=[]
for i,j,k in itertools.combinations(range(12),3):
    if all(abs(np.dot(ico[x],ico[y])-1/5**.5)<1e-6 for x,y in [(i,j),(j,k),(i,k)]): c=ico[i]+ico[j]+ico[k]; faces.append(c/np.linalg.norm(c))
print('icosahedron in code frame: %d vertices, %d face centres (dodecahedron vertices)'%(len(ico),len(faces)))
src=open('icosa_code.py').read()
exec(src.split("def bloch")[1].join(["def bloch",""]) if False else "def bloch(r): return np.real([np.trace(r@X),np.trace(r@Y),np.trace(r@Z)])\ndef rho(nv): return 0.5*(I+nv[0]*X+nv[1]*Y+nv[2]*Z)")
def distill(target,orbit,eps):
    r=(1-eps)*rho(target)+eps*rho(-target); R=r
    for _ in range(n-1): R=np.kron(R,r)
    num=V.conj().T@P@R@P@V; p=np.real(np.trace(num)); b=bloch(num/p)
    return 1-max((1+b@o)/2 for o in orbit),p,np.linalg.norm(b)
for name,cls in [('5-fold (icosahedron vertex)',ico),('3-fold (dodecahedron vertex)',faces)]:
    t=cls[0] if name.startswith('5') else cls[0]
    rows=[(e,)+distill(t,cls,e) for e in [0.05,0.1,0.2,0.3,0.4,0.5]]
    print('\n%s target, 7-qubit icosahedral code:'%name)
    for e,eo,p,blen in rows: print('   input error %.2f -> output error %.4f (%s) | output purity |b| = %.3f | success %.3f'%(e,eo,'better' if eo<e else 'worse',blen,p))
    es=np.linspace(0.005,0.499,200); good=[e for e in es if distill(t,cls,e)[0]<e]
    print('   improves for input error up to %.3f'%(max(good) if good else 0))

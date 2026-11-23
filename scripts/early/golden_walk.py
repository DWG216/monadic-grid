import numpy as np, itertools
src=open('fib_aether.py').read(); exec(src.split('# ---------------- F1')[0]); exec('def spin_mats'+src.split('def spin_mats')[1].split('ram=')[0])
phi=(1+5**.5)/2
def q2u(q): a,b,c,d=q; return a*I-1j*(b*X+c*Y+d*Z)
ic=[]
for k in range(4):
    for s in [1,-1]: e=np.zeros(4); e[k]=s; ic.append(e)
ic+=[np.array(s)/2 for s in itertools.product([1,-1],repeat=4)]
base=[0,1,1/phi,phi]; ev=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[i]<p[j])%2==0]
for p in ev:
    for sg in itertools.product([1,-1],repeat=3):
        q=np.zeros(4); vals=[0]+[sg[i]*base[i+1] for i in range(3)]
        for i in range(4): q[p[i]]=vals[i]
        ic.append(q/2)
ic=np.unique(np.round(ic,12),axis=0); C60=[q2u(q) for q in ic]
tau=np.array([[1j*(2+phi),1+1j],[-1+1j,-1j*(2+phi)]])/np.sqrt(5*phi+7)
# Clifford group (projective) from H,S
Hd=np.array([[1,1],[1,-1]])/2**.5; S=np.diag([1,1j])
def proj_close(gens):
    out={}; fr=[I.astype(complex)]
    def key(U):
        U=U/np.sqrt(np.linalg.det(U)); k=np.argmax(abs(U.reshape(-1))>1e-6); U=U*abs(U.reshape(-1)[k])/U.reshape(-1)[k]; return tuple(np.round(U.reshape(-1),7))
    out[key(fr[0])]=fr[0]
    while fr:
        new=[]
        for U in fr:
            for g in gens:
                V=g@U; k=key(V)
                if k not in out: out[k]=V; new.append(V)
        fr=new
    return list(out.values())
C24=proj_close([Hd,S]); print('Clifford group size (projective):',len(C24))
T=np.diag([1,np.exp(1j*np.pi/4)])
def walk(Cg,g,J=60):
    lam=[]; allv=[]
    for j in range(1,J+1):
        Jm=spin_mats(j); P=sum(Dj(c,Jm) for c in Cg)/len(Cg)
        w,V=np.linalg.eigh((P+P.conj().T)/2); B=V[:,w>0.5]
        if B.shape[1]==0: continue
        M=B.conj().T@Dj(g,Jm)@B; e=np.abs(np.linalg.eigvals(M)); lam.append((j,e.max())); allv+=list(e)
    return lam,np.array(allv)
li,ai=walk(C60,tau); print('G1 icosahedral+tau60: j with invariants:',[j for j,_ in li][:12],'... max |lambda| = %.6f'%max(v for _,v in li))
print('   distinct |lambda| values (rounded 1e-6):',sorted(set(np.round(ai,6)))[:10],' targets 1/sqrt59=%.6f, 1/59=%.6f'%(1/59**.5,1/59))
lc,ac=walk(C24,T); print('G2 Clifford+T: max |lambda| = %.6f (1/sqrt2 = %.6f)'%(max(v for _,v in lc),1/2**.5),' distinct:',sorted(set(np.round(ac,6)))[:8])
lt,_=walk(C60,C60[37]); print('Control tau inside C: max |lambda| = %.6f'%max(v for _,v in lt))
li_=max(v for _,v in li); lc_=max(v for _,v in lc)
print('G3 expensive-gate ratio ln(1/lam_CT)^-1 / ln(1/lam_ico)^-1 = %.3f  (log2 59 = %.3f)'%(np.log(1/li_)/np.log(1/lc_),np.log2(59)))
for eps in [1e-3,1e-6,1e-10]:
    print('   to shrink every j<=60 component by %.0e: icosahedral %d tau60, Clifford+T %d T, Fibonacci %d braids (0.964 each)'%(eps,np.ceil(np.log(eps)/np.log(li_)),np.ceil(np.log(eps)/np.log(lc_)),np.ceil(np.log(eps)/np.log(0.964))))

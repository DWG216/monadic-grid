import numpy as np
mu0=4e-7*np.pi; eps0=8.854e-12
R=0.040; a=0.015; S=36; rw=0.0002; m=40
def pas(n,step,rad):
    t=np.linspace(0,1,m+1); ph=2*np.pi*(n+step*t)/S; th=2*np.pi*t
    rr=R+rad*np.cos(th); return np.stack([rr*np.cos(ph),rr*np.sin(ph),rad*np.sin(th)],1)
def build(step):
    g=[(1+step*k)%S for k in range(12)]; b=[(2+step*k)%S for k in range(12)]
    paths=[pas(n,step,a) for n in g]+[pas(n,step,a+0.0006) for n in b]
    seg=[];own=[]
    for i,p in enumerate(paths):
        for j in range(m): seg.append((p[j],p[j+1])); own.append(i)
    A=np.array([s[0] for s in seg]); B=np.array([s[1] for s in seg]); own=np.array(own)
    mid=(A+B)/2; dl=B-A; l=np.linalg.norm(dl,axis=1)
    d=np.linalg.norm(mid[:,None]-mid[None],axis=2); np.fill_diagonal(d,1)
    K=(dl@dl.T)/np.sqrt(d**2+rw**2); np.fill_diagonal(K,l*(2*np.log(2*l/rw)-2))
    Ls=mu0/(4*np.pi)*K
    pk=1/np.sqrt(d**2+rw**2); np.fill_diagonal(pk,2*np.log(l/rw)/l)
    Ps=pk/(4*np.pi*eps0)
    nb=24; Lp=np.zeros((nb,nb))
    for i in range(nb):
        for j in range(nb): Lp[i,j]=Ls[np.ix_(own==i,own==j)].sum()
    # node cells: wire w (0 grey,1 brown), node k: half of pass k-1 (second half) + half of pass k (first half)
    cells=[]
    for w in range(2):
        for k in range(13):
            idx=[]
            if k>0: idx+=list(np.where(own==w*12+k-1)[0][m//2:])
            if k<12: idx+=list(np.where(own==w*12+k)[0][:m//2])
            cells.append(np.array(idx))
    nn=26; P=np.zeros((nn,nn))
    for I in range(nn):
        wI=l[cells[I]]/l[cells[I]].sum()
        for J in range(nn):
            wJ=l[cells[J]]/l[cells[J]].sum(); P[I,J]=wI@Ps[np.ix_(cells[I],cells[J])]@wJ
    C=np.linalg.inv(P); return Lp,C
def node(w,k): return w*13+k
inc=np.zeros((26,24))
for w in range(2):
    for k in range(12): inc[node(w,k),w*12+k]=1; inc[node(w,k+1),w*12+k]=-1
def solve(Lp,C,f,fixed):
    w=2*np.pi*f; nn,nb=26,24
    M=np.zeros((nn+nb,nn+nb),complex); M[:nn,:nn]=1j*w*C; M[:nn,nn:]=inc
    M[nn:,:nn]=inc.T; M[nn:,nn:]=-1j*w*Lp
    # unknowns V,I ; KCL: jwC V + inc I = Iinj ; branch: inc^T V - jwL I = 0
    fx=list(fixed); free=[i for i in range(nn+nb) if i not in fx]
    x=np.zeros(nn+nb,complex)
    for k,v in fixed.items(): x[k]=v
    rows=[i for i in range(nn+nb) if i not in fx]   # drop KCL rows of fixed nodes
    rhs=-M[np.ix_(rows,fx)]@np.array(list(fixed.values()))
    x[free]=np.linalg.solve(M[np.ix_(rows,free)],rhs)
    Iinj=M[:nn]@x
    return x,Iinj
def powers(Lp,C,f,s):
    fixed={node(0,0):1.0,node(0,12-s):1j}
    x,Ii=solve(Lp,C,f,fixed)
    PA=np.real(1.0*np.conj(Ii[node(0,0)])); PB=np.real(1j*np.conj(Ii[node(0,12-s)]))
    return PA,PB
def zin(Lp,C,f):
    x,Ii=solve(Lp,C,f,{node(0,0):1.0}); return 1/Ii[node(0,0)]
def analyse(step,label):
    Lp,C=build(step)
    s1=dict(Lsym=np.abs(Lp-Lp.T).max()/np.abs(Lp).max(),Csym=np.abs(C-C.T).max()/np.abs(C).max(),
            Lpd=np.linalg.eigvalsh((Lp+Lp.T)/2).min()>0,Cpd=np.linalg.eigvalsh((C+C.T)/2).min()>0)
    fs=np.logspace(7,10.5,3000); X=np.array([zin(Lp,C,f).imag for f in fs])
    sr=[fs[i] for i in range(len(fs)-1) if X[i]>0 and X[i+1]<0]; fsr=sr[0] if sr else np.nan
    rows=[];s2=0
    for f in fs[::3]:
        P=[powers(Lp,C,f,s) for s in range(3)]
        s2=max(s2,max(abs(pa+pb)/max(abs(pa),1e-300) for pa,pb in P))
        rows.append((f,P[1][0]/P[0][0],P[2][0]/P[0][0]))
    rows=np.array(rows)
    cost=np.abs(rows[:,1]+2)+np.abs(rows[:,2]-4)/4; i=np.argmin(cost); f2,r1,r2=rows[i]
    print(f'--- {label}: Ltot grey={Lp[:12,:12].sum()*1e6:.3f} uH, f_sr={fsr/1e6:.1f} MHz, S1={s1}, S2 max={s2:.2e}')
    print(f'best match to (-2,4): f={f2/1e6:.1f} MHz, r1={r1:.3f}, r2={r2:.3f}, f/f_sr={f2/fsr:.3f}')
    hits=rows[(np.abs(rows[:,1]+2)<0.1)&(np.abs(rows[:,2]-4)<0.4)]
    print('frequencies meeting Q1 (MHz):',np.round(hits[:,0]/1e6,1))
    return s1,s2,f2,r1,r2,fsr,hits
s1,s2,f2,r1,r2,fsr,hits=analyse(15,'p.204 winding')
ok={'S1':s1['Lsym']<1e-12 and s1['Csym']<1e-12 and s1['Lpd'] and s1['Cpd'],'S2':s2<1e-9,
    'Q1':len(hits)>0,'Q2':len(hits)>0 and abs(r2-r1**2)<0.2*abs(r1)**2,'Q3':len(hits)>0 and abs(f2/fsr-1.06)<0.10}
print(ok)
analyse(3,'control plain toroid')

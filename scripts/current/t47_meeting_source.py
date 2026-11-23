import numpy as np
def solve(Z1,Z2,N,Va,Vb=None,Zend=None):
    # nodes 0..N; node0=Va fixed; node N = Vb fixed, or loaded by Zend
    n=N+1; Y=np.zeros((n,n),complex); I=np.zeros(n,complex)
    for k in range(N):
        y=1/Z1; Y[k,k]+=y; Y[k+1,k+1]+=y; Y[k,k+1]-=y; Y[k+1,k]-=y
    for k in range(1,N): Y[k,k]+=1/Z2
    if Zend is not None: Y[N,N]+=1/Zend
    fixed={0:Va}; 
    if Vb is not None: fixed[N]=Vb
    free=[k for k in range(n) if k not in fixed]
    V=np.zeros(n,complex)
    for k,v in fixed.items(): V[k]=v
    A=Y[np.ix_(free,free)]; b=-Y[np.ix_(free,list(fixed))]@np.array(list(fixed.values()))
    V[free]=np.linalg.solve(A,b)
    Iser=[(V[k]-V[k+1])/Z1 for k in range(N)]
    Pser=[np.real(V[k]*np.conj(Iser[k])) for k in range(N)]
    return V,np.array(Pser)
w=1.0; L=1.0; N=12; res={}
Z1=1j*w*L; Z2=1j*w*2*L
g=np.arccosh(1+Z1/(2*Z2)); res['H1']=abs(np.exp(g).real-2)
Va=1.0; Vb=1j  # quadrature
_,P=solve(Z1,Z2,N,Va,0.0); Z0=np.sqrt(Z1*Z2+Z1**2/4)
_,P2=solve(Z1,Z2,N,Va,None,Z0)
res['H2']=max(abs(P[0]),abs(P2[0]))
_,P=solve(Z1,Z2,N,Va,Vb); res['H3']=np.ptp(P)/abs(P.mean())
Ps=[solve(Z1,Z2,N-s,Va,Vb)[1][0] for s in range(3)]
r=np.array(Ps)/Ps[0]; ex=np.array([np.sinh(N*np.log(2))/np.sinh((N-s)*np.log(2)) for s in range(3)])
res['H4_exact']=max(abs(r/ex-1)); res['H4_124']=max(abs(r-[1,2,4])/[1,2,4]); res['ratios']=r
th=np.linspace(0.1,np.pi-0.1,9); Pt=np.array([solve(Z1,Z2,N,Va,np.exp(1j*t))[1][0] for t in th])
res['H5']=max(abs(Pt/Pt.max()-np.sin(th)/np.sin(th).max()))
# control: passband
Zc1=1j*w*L; Zc2=1/(1j*w*0.7); Zc0=np.sqrt(Zc1*Zc2+Zc1**2/4)
_,Pc=solve(Zc1,Zc2,N,Va,None,Zc0); res['C1']=Pc[0]/(abs(Va)**2/abs(Zc0))
Pcs=[solve(Zc1,Zc2,N-s,Va,Vb)[1][0] for s in range(3)]; rc=np.array(Pcs)/Pcs[0]
res['C2']=max(abs(rc[1]-2),abs(rc[2]-4)); res['ctrl_ratios']=rc
for k,v in res.items(): print(k,v)
ok={'H1':res['H1']<1e-9,'H2':res['H2']<1e-12,'H3':res['H3']<1e-9,'H4':res['H4_exact']<1e-6 and res['H4_124']<1e-3,
    'H5':res['H5']<1e-9,'C1':res['C1']>0.01,'C2':res['C2']>0.1}
print(ok, 'ALL PASS' if all(ok.values()) else 'FAIL')

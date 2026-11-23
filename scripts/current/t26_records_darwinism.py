import numpy as np, itertools
def S(r):
    w=np.linalg.eigvalsh(r); w=w[w>1e-14]; return float(-(w*np.log2(w)).sum())
def build(a,b,N,copy=True):
    # state over S + N env qubits, all env |0>, apply CNOTs
    psi=np.zeros(2**(N+1),dtype=complex)
    psi[0]=a  # |0>|0...0>
    idx1=int('1'+('1'*N if copy else '0'*N),2) if N>0 else 1
    psi[idx1]=b
    return psi
def red(psi,keep,n):
    T=psi.reshape((2,)*n); rest=[k for k in range(n) if k not in keep]
    T=np.transpose(T,keep+rest).reshape(2**len(keep),-1); return T@T.conj().T
p=0.3; a=np.sqrt(p); b=np.sqrt(1-p)*np.exp(0.4j); N=8; n=N+1
psi=build(a,b,N)
res={}
rS=red(psi,[0],n); res['D1 |rho01|']=float(abs(rS[0,1]))
H=lambda q:-(q*np.log2(q)+(1-q)*np.log2(1-q))
I=[]
for f in range(1,N+1):
    F=list(range(1,f+1)); I.append(S(red(psi,[0],n))+S(red(psi,F,n))-S(red(psi,[0]+F,n)))
res['D2 I(S:F) f=1..N']=[round(x,6) for x in I]
res['D2 plateau err']=float(max(abs(x-H(p)) for x in I[:-1])); res['D2 full']=float(I[-1]); res['H(p)']=float(H(p))
psi0=build(a,b,N,copy=False); I0=[]
for f in range(1,N+1):
    F=list(range(1,f+1)); I0.append(S(red(psi0,[0],n))+S(red(psi0,F,n))-S(red(psi0,[0]+F,n)))
res['C1 max I no copy']=float(max(abs(x) for x in I0))
rp=red(build(1/np.sqrt(2),1/np.sqrt(2),N),[1],n); rm=red(build(1/np.sqrt(2),-1/np.sqrt(2),N),[1],n)
res['C2 env qubit |+> vs |->']=float(0.5*np.abs(np.linalg.eigvalsh(rp-rm)).sum())
for k,v in res.items(): print(k,v)

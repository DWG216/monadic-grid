# STEP 1: local equilibrium, region by region, bond by bond
import numpy as np, io, contextlib
src=open('golden_janus.py').read().split("print('\\n=== TEST 1")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
rng=np.random.default_rng(11); lam=rng.uniform(-0.5,0.5,L)          # aether chirality, different on every bond
Ci=[1j*(P[i]@P[(i+1)%L]-P[(i+1)%L]@P[i]) for i in range(L)]
Haeth=H0+sum(lam[i]*Ci[i] for i in range(L))
# local qubit-form operators (golden constraint embedded) for region A = sites 2..6, aether + shadow (10 qubits)
Ploc=np.zeros((8,8))
for a_ in (0,1):
    for b_ in (0,1):
        if a_==1 and b_==1:
            blk=np.array([[phi**-2,phi**-1.5],[phi**-1.5,phi**-1]])
            for x in (0,1):
                for y in (0,1): Ploc[a_*4+x*2+b_, a_*4+y*2+b_]=blk[x,y]
        elif a_==0 and b_==0: Ploc[0*4+1*2+0,0*4+1*2+0]=1
def onq(op,first,k,n):  # op on k consecutive qubits starting at 'first' among n
    return np.kron(np.kron(np.eye(2**first),op),np.eye(2**(n-first-k)))
reg=list(range(2,7)); nA=len(reg)
def H_reg(lams):    # terms fully inside the region, written on the region's 5 qubits
    Pq={i:onq(Ploc,i-1-reg[0],3,nA) for i in range(reg[0]+1,reg[-1])}
    Hh=-sum(Pq.values())
    for i in range(reg[0]+1,reg[-1]-1): Hh=Hh+lams[i]*1j*(Pq[i]@Pq[i+1]-Pq[i+1]@Pq[i])
    return Hh
def rho_reg(T2):
    big=np.zeros(2**(2*L),complex); big[(emb[:,None]*2**L+emb[None,:]).ravel()]=T2.reshape(-1)
    A=reg+[L+r for r in reg]; Bq=[k for k in range(2*L) if k not in A]
    M=np.transpose(big.reshape([2]*(2*L)),A+Bq).reshape(2**len(A),-1); return M@M.conj().T
inner=[i for i in range(reg[0]+1,reg[-1]-1)]
print('aether bond chiralities inside region (bonds %s): %s'%(inner,np.round(lam[inner],3)))
for beta in [0.0,1.0,3.0]:
    E_,V_=np.linalg.eigh(Haeth); w=np.exp(-beta*(E_-E_.min())/2); w/=np.linalg.norm(w)
    T2=(V_*w)@V_.T.conj().T if False else sum(w[k]*np.outer(V_[:,k],V_[:,k].conj()) for k in range(D))
    r=rho_reg(T2); HA=H_reg(lam)
    print('beta=%.0f'%beta)
    for b in inner:
        res=[]; grid=np.linspace(-1,1,81)
        for x in grid:
            lp=-lam.copy(); lp[b]=x
            G=np.kron(HA,np.eye(2**nA))-np.kron(np.eye(2**nA),H_reg(lp)); res.append(np.linalg.norm(G@r-r@G))
        res=np.array(res); k=np.argmin(res)
        # refine with quadratic fit near min
        c=np.polyfit(grid[max(k-3,0):k+4],res[max(k-3,0):k+4]**2,2); xm=-c[1]/(2*c[0])
        print('   bond %d: shadow value that minimises the regional imbalance = %+.4f   (conjugate = %+.4f)   residual at min %.2e, at same-hand %.3f'%(
            b,xm,-lam[b],res[k],res[np.argmin(abs(grid-lam[b]))]))

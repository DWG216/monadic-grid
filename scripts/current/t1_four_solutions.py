import numpy as np
rng=np.random.default_rng(20261122)
def F(v,t,Q):
    a,b,c=v
    if Q==-1: return np.array([b*b+a*a-a, c*c+b*b-c, c*c-a*a-t*b])
    return np.array([b*b-a*a-a, c*c-b*b-c, c*c-a*a-t*b])
def J(v,t,Q):
    a,b,c=v
    if Q==-1: return np.array([[2*a-1,2*b,0],[0,2*b,2*c-1],[-2*a,-t,2*c]])
    return np.array([[-2*a-1,2*b,0],[0,-2*b,2*c-1],[-2*a,-t,2*c]])
def solve(t,Q):
    sols=[]
    for _ in range(4000):
        v=(rng.normal(size=3)+1j*rng.normal(size=3))*1.5
        for _ in range(80):
            try: dv=np.linalg.solve(J(v,t,Q),-F(v,t,Q))
            except np.linalg.LinAlgError: break
            v=v+dv
            if np.abs(dv).max()<1e-14: break
        if np.abs(F(v,t,Q)).max()<1e-10 and not any(np.abs(v-s).max()<1e-7 for s in sols): sols.append(v)
    return sols
for Q,ts in ((-1,(1,2,3,4)),(1,(1,3))):
    for t in ts:
        S=solve(t,Q); real=[s.real for s in S if np.abs(s.imag).max()<1e-9]
        lam=(t+np.sqrt(t*t-4*Q+0j))/2; mu=(t-np.sqrt(t*t-4*Q+0j))/2
        g=np.array([lam**n/(lam-mu) for n in (-1,0,1)]); h=np.array([-mu**n/(lam-mu) for n in (-1,0,1)])
        has=lambda x: any(np.abs(s-x).max()<1e-8 for s in S)
        mirror=[tuple(np.round(r,6)) for r in real if abs(r[0]-r[2])<1e-9]; anti=[tuple(np.round(r,6)) for r in real if abs(r[0]+r[2])<1e-9]
        print(f"Q={Q:+d} t={t}: {len(S)} solutions, {len(real)} real; pure modes found {has(g)},{has(h)}; sum found {has(g+h)}; a=c keeps {mirror}; a=-c keeps {anti}")

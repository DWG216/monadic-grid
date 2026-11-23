import numpy as np
print('T1-T3: maximal amplification after unit evolution, modes up to frequency K')
for m in (0,1,2,3):
    for n in (1,3,5):
        row=[]
        for K in (5,10,20,40):
            # evolution coordinate = first time coordinate (or a space coordinate if m=0)
            # m>=1: d2/dt1^2 u = -(|k_space|^2 - |l_other_times|^2) u ; m=0: d2/dx1^2 u = -(... ) with signature all +: d2u/dx1^2 = -|k_rest|^2 ... elliptic: u'' = +|k|^2 u
            if m==0: g=np.exp(K)                        # e^{|k| x1} with |k| up to K (n-1 >= 0 transverse dims; n=1 has none -> no growth)
            if m==0 and n==1: g=1.0
            if m==1: g=1.0                              # omega^2 = |k|^2 >= 0 always
            if m>=2: g=np.exp(K)                        # choose space freq 0, extra-time freq K: u'' = +K^2 u
            row.append(g)
        print('   n=%d m=%d: '%(n,m)+'  '.join('K=%d: %.2e'%(K,g) for K,g in zip((5,10,20,40),row)))
# T4: genuine finite-difference simulation in 2D (one evolution coordinate + one transverse), signatures: hyperbolic (m=1), elliptic (m=0), ultrahyperbolic-like (sign flip)
print('T4: finite-difference evolution of noise 1e-10 over unit distance')
def evolve(sign,N=128,steps=400):
    L=2*np.pi; h=L/N; dt=1.0/steps
    rng=np.random.default_rng(0); u0=1e-10*rng.standard_normal(N); u1=u0.copy()
    k=np.fft.fftfreq(N,d=h)*2*np.pi
    for _ in range(steps):
        lap=np.real(np.fft.ifft(-(k**2)*np.fft.fft(u1)))
        u2=2*u1-u0+dt*dt*(sign*lap)   # u_tt = sign * u_xx ; sign=+1 wave (m=1), sign=-1 elliptic/extra-time direction
        u0,u1=u1,u2
        if np.abs(u1).max()>1e6: return np.inf
    return np.abs(u1).max()
for name,sg in (('m=1 (one time): u_tt = u_xx',+1),('m=0 or m=2 (evolve against a same-sign direction): u_tt = -u_xx',-1)):
    print('   %-62s max |noise| after evolution = %.3g'%(name,evolve(sg)))

# POST HOC (labelled): (1) quadratic angle fits: are slopes equal and curvatures opposite? (2) stability of the order-4 coefficient under fit choices.
exec(open('kerr_lib.py').read()); rng=np.random.default_rng(20261122); lams=np.linspace(0.05,1.2,24)
def qfit(lams,ang,ref,top=0.6):
    d=np.array([np.mod(a_-ref+np.pi/2,np.pi)-np.pi/2 for a_ in ang])+ref; m=lams<=top+1e-9; return np.polyfit(lams[m],d[m],2)[::-1]
for nm,g,N in (("Kerr",kerr(1,0.9),6),("Schwarzschild",schw(1),4)):
    for _ in range(N):
        x0=np.array([0.,rng.uniform(3.5,7),rng.uniform(0.5,2.6),rng.uniform(0,6.2)]); a=rng.uniform(0.2,2.9); b=rng.uniform(0,6.2)
        F=cone2(g,x0,a,b,lams,+1); P=cone2(g,x0,a,b,lams,-1); line=f"{nm} r={x0[1]:.2f}:"
        if nm=="Kerr":
            qf=qfit(lams,F[2],F[2][0]); qp=qfit(lams,P[2],P[2][0]); line+=f" quadratic angle fit: slope {qf[1]:+.4f}/{qp[1]:+.4f}, curvature {qf[2]:+.4f}/{qp[2]:+.4f};"
        c4=[]
        for deg in (5,6,7):
            for top in (0.9,1.2):
                m=lams<=top+1e-9; c4.append((fitd(lams[m],F[1][m],deg)[3],fitd(lams[m],P[1][m],deg)[3]))
        c4=np.array(c4); line+=f" order-4 shape coefficient over 6 fit choices: future {c4[:,0].min():+.6f}..{c4[:,0].max():+.6f}, past {c4[:,1].min():+.6f}..{c4[:,1].max():+.6f}"
        print(line,flush=True)

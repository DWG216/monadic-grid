import numpy as np
exec(open('t47_meeting_source.py').read().split('w=1.0')[0])
g=[1,16,31,10,25,4,19,34,13,28,7,22]; b=[2,17,32,11,26,5,20,35,14,29,8,23]
def chk(seq,m):
    out=[]
    for k in range(len(seq)):
        x=seq[k]%9; y=seq[(k+1)%len(seq)]%9; out.append((x*m)%9==y)
    return out
W1=sum(chk(g,7))+sum(chk(b,4)); print('W1',W1,'/24'); print('W2',(7*4)%9)
def run(x,N=12):
    Z1=1j*1.0; Z2=1/(1j*x)   # w=1, L=1, C=x  -> w^2LC=x
    ga=np.arccosh(complex(1+Z1/(2*Z2))); f=np.exp(ga)
    f=f if abs(f)>=1 else 1/f
    _,P1=solve(Z1,Z2,N,1.0,0.0)
    _,P=solve(Z1,Z2,N,1.0,1j)
    Ps=np.array([solve(Z1,Z2,N-s,1.0,1j)[1][0] for s in range(3)])
    return f,P1[0],np.ptp(P)/abs(P.mean()),Ps/Ps[0]
f,p1,spr,r=run(4.5)
print('L1 cell factor',f); print('L2',p1); print('L3 ratios',r); print('L4',spr)
fc,_,_,rc=run(1.4); print('control ratios',rc)
ok={'W1':W1==24,'W2':(7*4)%9==1,'L1':abs(f+2)<1e-9,'L2':abs(p1)<1e-12,
 'L3':max(abs(abs(r)-[1,2,4])/[1,2,4])<1e-3 and list(np.sign(r.real))==[1,-1,1],
 'L4':spr<1e-9,'C':max(abs(abs(rc[1])-2),abs(abs(rc[2])-4))>0.1}
print(ok,'ALL PASS' if all(ok.values()) else 'FAIL')

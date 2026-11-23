import numpy as np
exec(open('t47_meeting_source.py').read().split('Va=1.0')[0])
th=np.linspace(0.1,np.pi-0.1,9)
Pt=np.array([solve(Z1,Z2,N,1.0,np.exp(1j*t))[1][0] for t in th])
q=Pt/np.sin(th)
print('P(theta)=',Pt)
print('P/sin(theta) rel spread:',np.ptp(q)/abs(q.mean()),' constant =',q.mean())
print('expected -1/(|X| sinh(N ln2)) with X=Im Z0:', -1/(abs(np.sqrt(Z1*Z2+Z1**2/4))*np.sinh(N*np.log(2))))

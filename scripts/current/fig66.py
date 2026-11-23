import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
ns=np.arange(2,31); J=np.load('t11_J1.npy')
def liou(n):
    k=0; m=n; p=2
    while p*p<=m:
        while m%p==0: m//=p; k+=1
        p+=1
    return (-1)**(k+(m>1))
L=np.array([liou(n) for n in ns])
fig,ax=plt.subplots(1,2,figsize=(12,4.6))
ax[0].bar(ns-0.2,L,0.4,color='#bbb',label='λ(n) = (−1)^Ω(n)'); ax[0].bar(ns+0.2,J*np.sqrt(ns),0.4,color=['#2a7' if np.sign(j)==l else '#c44' for j,l in zip(J,L)],label='jump × √n, from the operator')
for n in (4,9,16,25): ax[0].annotate('square',(n,1.18),ha='center',fontsize=7,color='#555')
ax[0].axhline(0,color='k',lw=0.6); ax[0].set_ylim(-1.35,1.35); ax[0].set_xlabel('n'); ax[0].legend(fontsize=8,loc='lower left')
ax[0].set_title('Liouville from the operator: 29/29 signs, squares included',fontsize=10)
r=np.load('t11_locality.npy'); r5=np.load('t10_results.npy')
ax[1].plot(r[:,0]/341,r[:,1]/29,'o-',color='#36c',label='Liouville signs, 341 zeros (test)')
ax[1].plot(r[:,0]/341,r[:,2],'s--',color='#36c',alpha=0.6,label='Liouville |J_K/J|, 341 zeros')
ax[1].plot(r5[:,0]/201,r5[:,1]/18,'o-',color='#c63',label='Möbius signs, 201 zeros (round 5, exploratory)')
ax[1].axhline(1,color='#ccc',lw=0.8); ax[1].set_xlabel('K / N: share of the operator\'s rows kept'); ax[1].set_ylim(0,1.15)
ax[1].set_title('Signs return from about a quarter of the rows',fontsize=10); ax[1].legend(fontsize=8,loc='lower right')
fig.suptitle('Round 6 (§64): controls passed; Liouville λ(n) read from the operator, sign held by the reading vector',fontsize=11)
plt.tight_layout(); plt.savefig('/home/claude/visuals/fig66_round6.png',dpi=110)

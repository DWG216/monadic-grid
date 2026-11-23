import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(12,4.6))
lab=['P1 old\nplanted ln2','P2 new\nplanted ln2','P3 primes\nln2','P3 primes\nln3','P3 primes\nln3/2','P4 fake\nln2']
val=[None,34.70,6.85,8.99,0.04,4.48]; q=[None,8.84,8.55,10.29,2.58,6.18]
col=['#999','#2a7','#c44','#c44','#c44','#2a7']
x=np.arange(1,6); ax[0].bar(x-0.18,val[1:],0.36,color=col[1:],label='measured'); ax[0].bar(x+0.18,q[1:],0.36,color='#bbb',label='null 95th')
ax[0].set_xticks(np.arange(0,6)); ax[0].set_xticklabels(lab,fontsize=8); ax[0].text(0.05,12,'old detector:\n71st percentile\n(blind)',ha='center',fontsize=8)
ax[0].set_ylabel('peak / window median'); ax[0].set_title('Positive controls first: P3 failed, so R1–R3 are exploratory',fontsize=10); ax[0].legend(fontsize=8)
r=np.load('t10_results.npy'); ax[1].plot(r[:,0],r[:,1]/18,'o-',color='#36c',label='Möbius signs correct (of 18)'); ax[1].plot(r[:,0],r[:,2],'s--',color='#c63',label='median |jump_K / jump_full|')
ax[1].axhline(1,color='#ccc',lw=0.8); ax[1].set_xlabel('K: rows of the operator kept (of 201)'); ax[1].set_ylim(0,1.1)
ax[1].set_title('Exploratory: signs from half the rows; magnitudes need ~3/4',fontsize=10); ax[1].legend(fontsize=8,loc='lower right')
fig.suptitle('Round 5 (§63): operator entries. |1/ζ′| in the matrix, the sign in the readout vector',fontsize=11)
plt.tight_layout(); plt.savefig('/home/claude/visuals/fig65_round5.png',dpi=110)

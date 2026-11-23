import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
r=json.load(open('t13_results.json')); fig,ax=plt.subplots(1,2,figsize=(11,4.2))
for a,(nm,ref) in zip(ax,(("triangle","degree ≥ 4"),("4-clique","degree = 5"))):
    c=np.bincount(r[nm]['nullW1'],minlength=8); a.bar(range(8),c,color='#bbb',label='200 random graph properties')
    a.axvline(r[nm]['w1'][0],color='#c63',lw=3,label=f'{nm}'); a.axvline(r[nm]['w1'][1],color='#36c',lw=3,ls='--',label=f'{ref} (easy)')
    a.set_xticks(range(8)); a.set_xticklabels(['0','1','2','3','4','5','6','>6']); a.set_xlabel('shortest witness for "yes" (edges fixed)'); a.legend(fontsize=8,loc='upper left'); a.set_title(f'{nm} slice',fontsize=10)
fig.suptitle('Step 4 (§71): short witnesses mark checkable properties, hard and easy alike',fontsize=11); plt.tight_layout(); plt.savefig('/home/claude/visuals/fig69_witness.png',dpi=110)

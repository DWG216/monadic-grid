import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
r=json.load(open('t14_results.json')); fig,ax=plt.subplots(1,2,figsize=(11,4.2))
for a,nm in zip(ax,("triangle","4-clique")):
    d=r[nm]; a.hist(d['null'],bins=20,color='#bbb',label='100 random graph properties')
    a.axvline(d['K'][0],color='#c63',lw=3,label=nm); a.axvline(d['K'][1],color='#36c',lw=3,ls='--',label=d['ref']+' (easy)'); a.axvline(d['K'][2],color='#2a7',lw=2,ls=':',label='single edge (control, exact)'); a.axvline(d['K'][3],color='#555',lw=2,ls=':',label='parity of 5 edges (control)')
    a.set_xlabel('pairing bound K (leaves any monotone formula needs)'); a.legend(fontsize=7); a.set_title(nm+' slice',fontsize=10)
fig.suptitle('Step 5 (§73): the yes-against-no pairing by Cauchy–Schwarz also sees clique as simple on 6 vertices',fontsize=11); plt.tight_layout(); plt.savefig('/home/claude/visuals/fig70_pairing.png',dpi=110)

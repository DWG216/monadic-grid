import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
r=json.load(open('cone_results.json')); fig,ax=plt.subplots(1,2,figsize=(11,4.4))
for nm,c in (("Schwarzschild",'#36c'),("Reissner-Nordstrom",'#c63'),("de Sitter",'#2a7'),("flat",'#999')):
    R=np.array(r[nm]); ax[0].scatter(R[:,0],R[:,2],color=c,label=nm,s=30); ax[1].scatter(R[:,1],R[:,3],color=c,label=nm,s=30)
for a,t in zip(ax,('Area of the light cone measures Ricci (Einstein\'s equations)','Shape of the light cone measures Weyl (free field)')):
    lim=a.get_xlim(); a.plot([0,max(lim[1],0.003)],[0,max(lim[1],0.003)],color='#aaa',ls=':'); a.set_title(t,fontsize=10); a.legend(fontsize=8)
ax[0].set_xlabel('R_ab k^a k^b from the metric'); ax[0].set_ylabel('from the cone of rays'); ax[1].set_xlabel('Weyl part w from the metric'); ax[1].set_ylabel('from the cone of rays')
fig.suptitle('§81: the tower along light rays, measured on real geodesics (order 1 free; order 2 = Ricci + Weyl)',fontsize=11); plt.tight_layout(); plt.savefig('/home/claude/visuals/fig73_cone.png',dpi=110)

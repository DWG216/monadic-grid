import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
r=json.load(open('t12_results.json')); fig,ax=plt.subplots(1,2,figsize=(12,4.4))
j=np.arange(1,8); ax[0].bar(j-0.2,r['triangle']['w'],0.4,color='#c63',label='triangle, 7 edges'); ax[0].bar(j+0.2,r['4-clique']['w'],0.4,color='#36c',label='4-clique, 8 edges')
ax[0].plot(j,[0,1,3,4,6,6,3],'k.--',alpha=0.0); ax[0].set_xlabel('level j (tones = counts of subgraphs with j edges)'); ax[0].set_ylabel('share of variance'); ax[0].legend(fontsize=8); ax[0].set_title('Clique on a slice of 6-vertex graphs: where its variance sits',fontsize=10)
for name,c,y in (('triangle','#c63',1),('4-clique','#36c',0)):
    ax[1].hist(r[name]['null'],bins=25,color=c,alpha=0.35,label=f'{name}: 200 random graph properties'); ax[1].axvline(r[name]['L'],color=c,lw=2.5)
ax[1].set_xlabel('mean spectral level'); ax[1].legend(fontsize=8,loc='upper left'); ax[1].set_title('Solid lines: clique. It sits below typical graph properties',fontsize=10)
fig.suptitle('Step 3 (§70): the slice\'s Fourier side sees clique as simple, so level cannot be the measure of hardness',fontsize=11)
plt.tight_layout(); plt.savefig('/home/claude/visuals/fig68_slice_levels.png',dpi=110)

import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
by=json.load(open('bands_tri.json')); w=np.arange(11); free=[by[str(k)][0] for k in w]; tri=[by[str(k)][1] for k in w]
fig,ax=plt.subplots(figsize=(9,4.6))
ax.bar(w,free,color='#9aa',label='triangle-free graphs'); ax.bar(w,tri,bottom=free,color='#c63',label='graphs with a triangle')
ax.axvspan(4.5,5.5,color='#36c',alpha=0.12); ax.text(5,262,'central slice:\nboth kinds, no two comparable',ha='center',fontsize=8,color='#135')
ax.annotate('positive tests\n(single triangles)',(3,125),(1.2,190),arrowprops=dict(arrowstyle='->'),fontsize=8)
ax.annotate('negative tests\n(complete bipartite)',(6,212),(7.6,235),arrowprops=dict(arrowstyle='->'),fontsize=8); ax.annotate('',(4,212),(7.6,240),arrowprops=dict(arrowstyle='->'))
ax.set_xticks(w); ax.set_xlabel('slice = number of edges present (5 vertices, 10 possible edges)'); ax.set_ylabel('graphs'); ax.set_ylim(0,290); ax.legend(fontsize=8,loc='upper left')
ax.set_title('Step 2 (§69): slices are cheap bands. Razborov\'s tests never share one; the hardness sits inside a slice',fontsize=10)
plt.tight_layout(); plt.savefig('/home/claude/visuals/fig67_bands.png',dpi=110)

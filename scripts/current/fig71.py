import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
pub=np.array([48.005151,49.773832,52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,69.546402,72.067158,75.704691,77.144840,79.337375]); rv=np.load('t15_ritz.npy')
fake=np.array([46.074,48.009,49.758,51.401,52.895,54.364,55.965,57.588,59.059,60.49,62.096,63.741,65.172,66.5,68.069,69.695,71.175,72.583,74.102,75.662,77.246,78.956,80.913])
fig,ax=plt.subplots(figsize=(11,3.4))
ax.vlines(pub,2.1,2.9,color='#333',lw=2); ax.vlines(rv,1.1,1.9,color='#c63',lw=2); ax.vlines(fake,0.1,0.9,color='#99a',lw=2)
ax.set_yticks([0.5,1.5,2.5]); ax.set_yticklabels(['fake primes','operator from the primes','published zeros']); ax.set_xlim(42,84); ax.set_xlabel('height on the critical line')
ax.set_title('§75: the scaling generator with the Weil inner product, built from the primes alone, returns the zeros (window 47–80)',fontsize=10)
plt.tight_layout(); plt.savefig('/home/claude/visuals/fig71_operator.png',dpi=110)

"""t192: Koide meeting shares at six scales (Huang-Zhou Tables 2, 3, full SM). See PREDICTIONS_t192.md."""
import numpy as np
rng = np.random.default_rng(192); N = 100_000
# scale: up (u,c,t), down (d,s,b), leptons (e,mu,tau); GeV, (central, sigma)
T = {
 "M_Z":  ([(1.23e-3,.21e-3),(.620,.017),(168.26,.75)], [(2.67e-3,.19e-3),(53.16e-3,4.61e-3),(2.839,.026)], [(.48307e-3,.00045e-3),(.101766,.000023),(1.72856,.00028)]),
 "M_h":  ([(1.20e-3,.21e-3),(.607,.017),(165.05,.75)], [(2.61e-3,.18e-3),(52.00e-3,4.51e-3),(2.768,.026)], [(.48449e-3,.00045e-3),(.102065,.000020),(1.73369,.00020)]),
 "M_t":  ([(1.18e-3,.20e-3),(.594,.017),(161.98,.75)], [(2.56e-3,.18e-3),(50.90e-3,4.41e-3),(2.702,.025)], [(.48583e-3,.00045e-3),(.102347,.000019),(1.73850,.00014)]),
 "1e5":  ([(.86e-3,.15e-3),(.435,.013),(123.77,.85)], [(1.88e-3,.13e-3),(37.47e-3,3.26e-3),(1.908,.021)], [(.49850e-3,.00064e-3),(.105015,.000095),(1.78412,.00158)]),
 "1e8":  ([(.69e-3,.12e-3),(.350,.011),(102.49,.89)], [(1.52e-3,.11e-3),(30.34e-3,2.65e-3),(1.502,.018)], [(.49691e-3,.00098e-3),(.104681,.000183),(1.77852,.00308)]),
 "1e12": ([(.56e-3,.10e-3),(.283,.009),(85.07,.89)],  [(1.24e-3,.09e-3),(24.76e-3,2.17e-3),(1.194,.015)], [(.48388e-3,.00139e-3),(.101936,.000277),(1.73194,.00466)]),
}
def Q(m): return m.sum(0)/np.sqrt(m).sum(0)**2
def draw(sec):
    out=[]
    for c,s in sec:
        x=rng.normal(c,s,2*N); out.append(x[x>0][:N])
    return np.array(out)
ok={"d":True,"u":True,"l":True}
for k,(u,d,l) in T.items():
    qu,qd,ql=Q(draw(u)),Q(draw(d)),Q(draw(l))
    zu=(qu.mean()-8/9)/qu.std(); zd=(qd.mean()-3/4)/qd.std(); dl=ql.mean()-2/3
    ok["u"]&=abs(zu)<=2; ok["d"]&=abs(zd)<=2; ok["l"]&=abs(dl)<0.003
    print(f"{k:>5}: Q_u {qu.mean():.5f}+-{qu.std():.5f} (z {zu:+.2f})  Q_d {qd.mean():.5f}+-{qd.std():.5f} (z {zd:+.2f})  Q_l {ql.mean():.6f} (Q_l - 2/3 = {dl:+.6f})")
print()
print("P1 (Q_d ~ 3/4 at all scales):","PASS" if ok["d"] else "FAIL")
print("P2 (Q_u ~ 8/9 at all scales):","PASS" if ok["u"] else "FAIL")
print("P3 (Q_l within 0.003 of 2/3):","PASS" if ok["l"] else "FAIL")

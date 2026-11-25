// t84: degree-4 restricted closure (Grigoriev/Schoenebeck pseudo-expectation) for the XOR system derived from random 3-SAT.
// Same combination rule as t82 (combine equations sharing at least one variable while the degree stays <= 4), indexed by variable and by pair.
// Usage: closure4 n m seed mode(0 random,1 planted,2 random+cover) nballs ballsize nprod
#include <bits/stdc++.h>
using namespace std; typedef uint64_t u64;
static inline u64 pack(const vector<int>& v){u64 k=0;for(int x:v)k=(k<<16)|(u64)x;return k|((u64)v.size()<<62)*0+0;}
struct Mono{int d;int v[4];};
static u64 key(const Mono&m){u64 k=0;for(int i=0;i<m.d;i++)k=(k<<16)|(u64)m.v[i];return k;}
static Mono symd(const Mono&a,const Mono&b){Mono c;c.d=0;int i=0,j=0;while(i<a.d||j<b.d){if(j>=b.d||(i<a.d&&a.v[i]<b.v[j])){if(c.d<5)c.v[min(c.d,3)]=a.v[i];c.d++;i++;}else if(i>=a.d||b.v[j]<a.v[i]){if(c.d<5)c.v[min(c.d,3)]=b.v[j];c.d++;j++;}else{i++;j++;}if(c.d>4)return c;}return c;}
int main(int argc,char**argv){
 int n=atoi(argv[1]); long m=atol(argv[2]); u64 seed=strtoull(argv[3],0,10); int mode=atoi(argv[4]); int nballs=atoi(argv[5]); int bsz=atoi(argv[6]); int nprod=atoi(argv[7]);
 mt19937_64 rng(seed); vector<array<int,3>> T; vector<array<int,3>> F; vector<int> hid(n+1);
 for(int i=1;i<=n;i++)hid[i]=rng()&1;
 while((long)T.size()<m){array<int,3>t;do{for(auto&x:t)x=1+rng()%n;}while(t[0]==t[1]||t[0]==t[2]||t[1]==t[2]);array<int,3>f;for(auto&x:f)x=rng()&1;
  if(mode==1&&((f[0]+f[1]+f[2])%2)==((hid[t[0]]+hid[t[1]]+hid[t[2]])%2))continue; T.push_back(t);F.push_back(f);}
 if(mode==2){int cv[4][3]={{1,2,3},{1,2,4},{3,5,6},{4,5,6}};int cf[4][3]={{1,0,0},{1,0,0},{1,0,0},{0,0,0}};for(int q=0;q<4;q++){T.push_back({cv[q][0],cv[q][1],cv[q][2]});F.push_back({cf[q][0],cf[q][1],cf[q][2]});}}
 vector<Mono> eq; vector<int8_t> sg; unordered_map<u64,int> idx; idx.reserve(1<<24);
 vector<vector<int>> varAll(n+1),varLow(n+1); unordered_map<u64,vector<int>> pairIdx; pairIdx.reserve(1<<24);
 deque<int> q; string status="ok"; const size_t CAP=40000000;
 auto add=[&](Mono c,int s)->bool{ if(c.d==0)return s==1; u64 k=key(c)|((u64)c.d<<60); auto it=idx.find(k); if(it!=idx.end())return sg[it->second]==s; int id=eq.size(); eq.push_back(c); sg.push_back(s); idx[k]=id; q.push_back(id); return true;};
 for(size_t i=0;i<T.size();i++){Mono c;c.d=3;int a[3]={T[i][0],T[i][1],T[i][2]};sort(a,a+3);for(int j=0;j<3;j++)c.v[j]=a[j];int par=(F[i][0]+F[i][1]+F[i][2])%2;int s=par?1:-1; if(!add(c,s)){status="conflict";break;}}
 auto combine=[&](int a,int b)->bool{Mono c=symd(eq[a],eq[b]); if(c.d>4)return true; return add(c,sg[a]*sg[b]);};
 while(status=="ok"&&!q.empty()){int a=q.front();q.pop_front();const Mono A=eq[a];unordered_set<int> seen;
  auto probe=[&](int b)->bool{if(b==a||!seen.insert(b).second)return true;return combine(a,b);};
  bool ok=true;
  if(A.d<=2){for(int i=0;i<A.d&&ok;i++)for(int b:varAll[A.v[i]]){if(!probe(b)){ok=false;break;}}}
  else{ for(int i=0;i<A.d&&ok;i++)for(int b:varLow[A.v[i]]){if(A.d==4&&eq[b].d>2)continue;if(!probe(b)){ok=false;break;}}
        for(int i=0;i<A.d&&ok;i++)for(int j=i+1;j<A.d&&ok;j++){auto it=pairIdx.find(((u64)A.v[i]<<16)|A.v[j]);if(it==pairIdx.end())continue;for(int b:it->second){if(!probe(b)){ok=false;break;}}}}
  if(!ok){status="conflict";break;}
  for(int i=0;i<A.d;i++){varAll[A.v[i]].push_back(a);if(A.d<=3)varLow[A.v[i]].push_back(a);}
  for(int i=0;i<A.d;i++)for(int j=i+1;j<A.d;j++)pairIdx[((u64)A.v[i]<<16)|A.v[j]].push_back(a);
  if(eq.size()>CAP){status="cap";break;}}
 if(getenv("DUMP")){FILE*fd=fopen(getenv("DUMP"),"w");for(size_t i=0;i<T.size();i++)fprintf(fd,"%d %d %d %d %d %d\n",T[i][0],T[i][1],T[i][2],F[i][0],F[i][1],F[i][2]);fclose(fd);}
 printf("{\"status\":\"%s\",\"size\":%zu",status.c_str(),eq.size());
 if(status!="ok"){printf("}\n");return 0;}
 auto E=[&](vector<int> v)->int{ if(v.empty())return 1; sort(v.begin(),v.end()); Mono c;c.d=v.size();if(c.d>4)return 0;for(int i=0;i<c.d;i++)c.v[i]=v[i]; auto it=idx.find(key(c)|((u64)c.d<<60)); return it==idx.end()?0:sg[it->second];};
 auto viol=[&](size_t i,int extra)->double{double tot=0;for(int mask=0;mask<8;mask++){int s=1;set<int> mono;for(int j=0;j<3;j++)if(mask>>j&1){if(F[i][j])s=-s;mono.insert(T[i][j]);}
   if(extra){if(mono.count(extra))mono.erase(extra);else mono.insert(extra);} tot+=s*E(vector<int>(mono.begin(),mono.end()));}return tot/8;};
 long bad=0; for(size_t i=0;i<T.size();i++)if(fabs(viol(i,0))>1e-12)bad++;
 long badp=0; for(int r=0;r<nprod;r++){size_t i=rng()%T.size();vector<int> vs(T[i].begin(),T[i].end());for(int k=0;k<5;k++)vs.push_back(1+rng()%n);for(int v:vs)if(fabs(viol(i,v))>1e-12)badp++;}
 long hidok=-1; if(mode==1){hidok=0;for(size_t i=0;i<T.size();i++){int p=(hid[T[i][0]]+hid[T[i][1]]+hid[T[i][2]])%2;int fp=(F[i][0]+F[i][1]+F[i][2])%2;if(p!=fp)hidok++;}}
 printf(",\"clauses\":%zu,\"clause_viol\":%ld,\"prod_viol\":%ld,\"hidden_sat\":%ld,\"balls\":[",T.size(),bad,badp,hidok);
 vector<vector<int>> occ(n+1); for(size_t i=0;i<T.size();i++)for(int v:T[i])occ[v].push_back(i);
 for(int bnum=0;bnum<nballs;bnum++){size_t i0=rng()%T.size();vector<int> order;set<int> seen;deque<int> dq;for(int v:T[i0]){seen.insert(v);dq.push_back(v);}
  while(!dq.empty()&&(int)order.size()<bsz){int v=dq.front();dq.pop_front();order.push_back(v);for(int c:occ[v])for(int w:T[c])if(seen.insert(w).second)dq.push_back(w);}
  printf("%s{\"vars\":[",bnum?",":"");for(size_t k=0;k<order.size();k++)printf("%s%d",k?",":"",order[k]);printf("],\"eqs\":[");bool first=true;
  int B=order.size();
  // subsets of size 1..4
  for(int a=0;a<B;a++){ {int e=E({order[a]});if(e){printf("%s[[%d],%d]",first?"":",",order[a],e);first=false;}}
   for(int b=a+1;b<B;b++){ {int e=E({order[a],order[b]});if(e){printf("%s[[%d,%d],%d]",first?"":",",order[a],order[b],e);first=false;}}
    for(int c=b+1;c<B;c++){ {int e=E({order[a],order[b],order[c]});if(e){printf("%s[[%d,%d,%d],%d]",first?"":",",order[a],order[b],order[c],e);first=false;}}
     for(int d=c+1;d<B;d++){int e=E({order[a],order[b],order[c],order[d]});if(e){printf("%s[[%d,%d,%d,%d],%d]",first?"":",",order[a],order[b],order[c],order[d],e);first=false;}}}}}
  printf("]}");}
 printf("]}\n"); return 0;}

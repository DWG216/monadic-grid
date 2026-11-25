// t88: does a small connected set of clauses carry an F2 law (its solutions lie in a proper affine subspace)?
// Usage: f2law family(0 = 3-SAT density 4.5, 1 = 3-XOR density 1 as 4 clauses each) n s count seed
// Output: one line per subset: nvars nclauses status(0 no law, 1 law, 2 unsatisfiable)
#include <bits/stdc++.h>
using namespace std;
typedef bitset<192> BS;
mt19937_64 rng;
struct F { int v; vector<array<int,3>> cl; }; // literals: +-(var+1)
static bool dpll(const F& f, const vector<int>* xv, int xb, vector<int8_t>& a, bool rnd) {
  // propagate
  for (bool ch = true; ch;) { ch = false;
    for (auto& c : f.cl) { int un = 0, ul = 0; bool sat = false;
      for (int l : c) { int x = abs(l) - 1; if (a[x] < 0) { un++; ul = l; } else if ((a[x] == 1) == (l > 0)) { sat = true; break; } }
      if (sat) continue; if (un == 0) return false; if (un == 1) { a[abs(ul) - 1] = ul > 0; ch = true; } }
    if (xv) { int un = 0, ux = -1, p = 0; for (int x : *xv) { if (a[x] < 0) { un++; ux = x; } else p ^= a[x]; }
      if (un == 0 && p != xb) return false; if (un == 1) { a[ux] = p ^ xb; ch = true; } } }
  vector<int> free; for (int i = 0; i < f.v; i++) if (a[i] < 0) free.push_back(i);
  if (free.empty()) return true;
  int x = rnd ? free[rng() % free.size()] : free[0]; int first = rnd ? (int)(rng() & 1) : 0;
  for (int t = 0; t < 2; t++) { vector<int8_t> b = a; b[x] = t ? !first : first; if (dpll(f, xv, xb, b, rnd)) { a = b; return true; } }
  return false;
}
static BS tobs(const vector<int8_t>& a) { BS b; for (size_t i = 0; i < a.size(); i++) if (a[i] == 1) b[i] = 1; return b; }
struct Basis { vector<BS> rows; vector<int> piv; bool add(BS x) { for (size_t i = 0; i < rows.size(); i++) if (x[piv[i]]) x ^= rows[i];
    if (x.none()) return false; int p = 0; while (!x[p]) p++; for (auto& r : rows) if (r[p]) r ^= x; rows.push_back(x); piv.push_back(p); return true; } };
static vector<BS> nullspace(const Basis& B, int v) { // vectors c with <c, row> = 0 for all rows (rows are reduced: each pivot appears in one row)
  vector<char> isp(v, 0); for (int p : B.piv) isp[p] = 1; vector<BS> out;
  for (int j = 0; j < v; j++) if (!isp[j]) { BS c; c[j] = 1; for (size_t i = 0; i < B.rows.size(); i++) if (B.rows[i][j]) c[B.piv[i]] = 1; out.push_back(c); }
  return out; }
static int status(const F& f) { // 0 no law, 1 law, 2 unsat
  vector<int8_t> a(f.v, -1); if (!dpll(f, nullptr, 0, a, true)) return 2;
  BS x0 = tobs(a); Basis B;
  for (int k = 0; k < 4 * f.v + 20 && (int)B.rows.size() < f.v; k++) { vector<int8_t> b(f.v, -1); dpll(f, nullptr, 0, b, true); B.add(tobs(b) ^ x0); }
  while ((int)B.rows.size() < f.v) {
    auto ns = nullspace(B, f.v); bool grew = false;
    for (auto& c : ns) { vector<int> xv; for (int j = 0; j < f.v; j++) if (c[j]) xv.push_back(j); int b0 = (c & x0).count() & 1;
      vector<int8_t> b(f.v, -1); if (dpll(f, &xv, b0 ^ 1, b, false)) { B.add(tobs(b) ^ x0); grew = true; break; } else return 1; }
    if (!grew) return 1; }
  return 0; }
int main(int argc, char** argv) {
  int fam = atoi(argv[1]), n = atoi(argv[2]), s = atoi(argv[3]), cnt = atoi(argv[4]); rng.seed(strtoull(argv[5], 0, 10));
  if (fam < 0) { // sanity: S1
    F f; f.v = 3; f.cl = {{1, 2, 3}, {1, 2, -3}, {1, -2, 3}, {1, -2, -3}}; F g; g.v = 3; g.cl = {{1, 2, 3}};
    printf("S1 four=%d single=%d\n", status(f), status(g)); return 0; }
  long m = fam == 0 ? (long)(4.5 * n) : n; vector<array<int,3>> T(m); vector<array<int,3>> S(m);
  for (long i = 0; i < m; i++) { array<int,3> t; do { for (auto& x : t) x = rng() % n; } while (t[0] == t[1] || t[0] == t[2] || t[1] == t[2]); T[i] = t; for (auto& x : S[i]) x = rng() & 1; }
  vector<vector<int>> occ(n); for (long i = 0; i < m; i++) for (int x : T[i]) occ[x].push_back(i);
  for (int r = 0; r < cnt; r++) {
    set<long> chosen; vector<long> order; long c0 = rng() % m; chosen.insert(c0); order.push_back(c0);
    while ((int)order.size() < s) { vector<long> cand; for (long c : order) for (int x : T[c]) for (long d : occ[x]) if (!chosen.count(d)) cand.push_back(d);
      if (cand.empty()) break; long d = cand[rng() % cand.size()]; chosen.insert(d); order.push_back(d); }
    map<int,int> loc; for (long c : order) for (int x : T[c]) if (!loc.count(x)) { int k = loc.size(); loc[x] = k; }
    F f; f.v = loc.size();
    for (long c : order) { int a = loc[T[c][0]] + 1, b = loc[T[c][1]] + 1, d = loc[T[c][2]] + 1;
      if (fam == 0) f.cl.push_back({S[c][0] ? a : -a, S[c][1] ? b : -b, S[c][2] ? d : -d});
      else { int par = (S[c][0] + S[c][1] + S[c][2]) & 1; // XOR x_a+x_b+x_c = par: forbid tuples of the other parity
        for (int u = 0; u < 8; u++) { int bits[3] = {u & 1, (u >> 1) & 1, (u >> 2) & 1}; if (((bits[0] + bits[1] + bits[2]) & 1) == par) continue;
          f.cl.push_back({bits[0] ? -a : a, bits[1] ? -b : b, bits[2] ? -d : d}); } } }
    printf("%d %zu %d\n", f.v, order.size(), status(f)); }
  return 0; }

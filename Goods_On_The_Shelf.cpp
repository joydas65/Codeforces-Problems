#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
static int bufpos = 0, buflen = 0;

static inline int gc() {
    if (bufpos == buflen) {
        buflen = (int)fread(buf, 1, sizeof(buf), stdin);
        bufpos = 0;
        if (buflen == 0) return -1;
    }
    return buf[bufpos++];
}

static inline long long readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    int sign = 1;
    if (c == '-') { sign = -1; c = gc(); }
    long long x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x * sign;
}

int main() {
    int t = (int)readInt();
    string out;
    out.reserve(1 << 20);
    while (t--) {
        int n = (int)readInt();
        vector<int> a(n), vals(n);
        for (int i = 0; i < n; i++) { a[i] = (int)readInt(); vals[i] = a[i]; }
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int m = (int)vals.size();
        vector<int> id(n);
        for (int i = 0; i < n; i++)
            id[i] = (int)(lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin());
        vector<int> cnt(m, 0), fst(m, -1), lst(m, -1);
        vector<vector<int>> pos(m);
        for (int i = 0; i < n; i++) {
            int v = id[i];
            cnt[v]++;
            if (fst[v] < 0) fst[v] = i;
            lst[v] = i;
            pos[v].push_back(i);
        }
        vector<int> broken;
        for (int v = 0; v < m; v++)
            if (lst[v] - fst[v] + 1 != cnt[v]) broken.push_back(v);
        bool ans;
        if (broken.empty()) ans = true;
        else if ((int)broken.size() > 2) ans = false;
        else {
            vector<pair<int,int>> cand;
            for (int bi = 0; bi < (int)broken.size(); bi++) {
                vector<int> &p = pos[broken[bi]];
                int mm = (int)p.size();
                for (int excl = 0; excl < 2; excl++) {
                    int ki0, ki1, ii;
                    if (excl == 0) { ki0 = 1; ki1 = mm - 1; ii = p[0]; }
                    else { ki0 = 0; ki1 = mm - 2; ii = p[mm - 1]; }
                    if (ki1 < ki0) continue;
                    int keptFirst = p[ki0], keptLast = p[ki1];
                    int spanK = keptLast - keptFirst + 1;
                    if (spanK == mm - 1) {
                        cand.push_back({ii, keptFirst - 1});
                        cand.push_back({ii, keptLast + 1});
                    } else if (spanK == mm) {
                        int hole = -1; bool okh = true;
                        for (int idx = ki0 + 1; idx <= ki1; idx++) {
                            int d = p[idx] - p[idx - 1];
                            if (d == 2 && hole < 0) hole = p[idx - 1] + 1;
                            else if (d != 1) { okh = false; break; }
                        }
                        if (okh && hole >= 0) cand.push_back({ii, hole});
                    }
                }
            }
            ans = false;
            for (auto &pr : cand) {
                int i = pr.first, j = pr.second;
                if (i < 0 || j < 0 || i >= n || j >= n || i == j) continue;
                int x = id[i], y = id[j];
                if (x == y) continue;
                bool sub = true;
                for (int b : broken) if (b != x && b != y) { sub = false; break; }
                if (!sub) continue;
                long long dx;
                vector<int> &px = pos[x];
                if ((int)px.size() == 1) dx = 0;
                else {
                    int lo = (i != px.front()) ? px.front() : px[1];
                    int hi = (i != px.back()) ? px.back() : px[(int)px.size() - 2];
                    int nmin = min(lo, j), nmax = max(hi, j);
                    dx = (long long)nmax - nmin + 1 - cnt[x];
                }
                if (dx != 0) continue;
                long long dy;
                vector<int> &py = pos[y];
                if ((int)py.size() == 1) dy = 0;
                else {
                    int lo = (j != py.front()) ? py.front() : py[1];
                    int hi = (j != py.back()) ? py.back() : py[(int)py.size() - 2];
                    int nmin = min(lo, i), nmax = max(hi, i);
                    dy = (long long)nmax - nmin + 1 - cnt[y];
                }
                if (dy == 0) { ans = true; break; }
            }
        }
        out += ans ? "YES\n" : "NO\n";
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}

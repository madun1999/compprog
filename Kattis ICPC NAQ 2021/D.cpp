// template from https://ncduy0303.github.io/Competitive-Programming/Contest%20Template/main.cpp
#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
ll MOD = 1e9 + 7;
const ll INF = 1e9;



void solve() {
    vector<ll> mem;
    map<int, int> m;
    map<int, int> m2;
    ll n = 0;
    cin >> n;
    cin >> MOD;
    ll sum  = 1;
    mem.push_back(1);
    for (int i  = 2; i <= n; i++) {
        ll now = sum;
        int k = 0;
        

        for (int j = 2; j <= i; j++) {
            int k1 = i / j;
            int k2 = i / (j + 1);
            if (k1 == k2) {
                k = k1;
                break;
            }
            m[k1-1] = 1;
        }

        for (int j = 1; j <= k; j++) {
            int high = i / j;
            int low = i / (j+1);
            m[j-1] = high - low;
        }

        
        if 
        for ( auto item : m) {
            now = (now + mem[item.first] * item.second) % MOD;
        }
        
        mem.push_back(now);
        sum = (sum + now) % MOD;

        
    }
    cout << mem.back() << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}

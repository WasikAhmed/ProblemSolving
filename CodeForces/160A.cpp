// Twins

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <utility>
using namespace std;

#define vi vector<int>
#define pii pair<int,int>
#define vii vector<pii>
#define rep(i,a,b) for(int i=a; i<b; i++)
#define rrep(i,a,b) for(int i=a-1; i>=b; i--)
#define for_each(x,y) for(auto &x : y)
#define pb push_back
#define ff first
#define ss second

int main()
{
    int n; cin>> n;
    vi v(n);
    int total = 0;
    rep(i, 0, n) {
        cin>> v[i];
        total += v[i];
    }

    int ans = 0, pick = 0;
    sort(v.rbegin(), v.rend());
    int i=0;
    while(pick <= total && i < n) {
        pick += v[i];
        total -= v[i];
        ans++;
        i++;
    }
    cout<< ans<< endl;

    return 0;
}
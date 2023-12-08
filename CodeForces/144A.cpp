// Arrival of the General

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
    rep(i, 0, n) {
        cin>> v[i];
    }
    int ans = 0;
    auto max = max_element(v.begin(), v.end());
    auto min = min_element(v.rbegin(), v.rend());
    int maxElementDistance = distance(v.begin(), max);
    int minElementDistance = n - distance(v.rbegin(), min) - 1;

    if(maxElementDistance >= minElementDistance) {
        ans = ans + maxElementDistance + (n-1-minElementDistance) - 1;
    } else {
        ans = ans + maxElementDistance + (n-1-minElementDistance);
    }
    cout<< ans<< endl;

    return 0;
}
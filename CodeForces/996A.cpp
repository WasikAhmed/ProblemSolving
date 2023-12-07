// Hit the Lottery

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
#define ll long long

int main()
{
    ll n; cin>> n;

    vi denominators;
    denominators.pb(100);
    denominators.pb(20);
    denominators.pb(10);
    denominators.pb(5);
    denominators.pb(1);

    int ans = 0;
    for_each(denominator, denominators) {
        while(n >= denominator) {
            n -= denominator;
            ans++;
        }
    }
    cout<< ans<< endl;

    return 0;
}
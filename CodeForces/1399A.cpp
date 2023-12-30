// Remove Smallest

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
    int t; cin>> t;
    int n; 
    while (t--)
    {
        cin>> n;
        vi v(n);
        rep(i, 0, n) cin>> v[i];

        sort(v.begin(), v.end());
        bool result = true;

        rep(i, 0, n-1) {
            if(v[i+1] - v[i] > 1) {
                result = false;
                break;
            }
        }
        if(result) cout<< "YES"<< endl;
        else cout<< "NO"<< endl;
    } 
    return 0;
}
// Helpful Maths

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <utility>
#include <string>
using namespace std;

#define vi vector<int>
#define vs vector<string>
#define vc vector<char>
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
    string s; cin>> s;

    vc v;
    for_each(ch, s) {
        if(ch != '+') {
            v.pb(ch);
        }
    }

    sort(v.begin(), v.end());
    rep(i, 0, v.size()) {
        cout<< v[i];
        if(i != v.size() - 1) {
            cout<< "+";
        }
    }
    cout<< endl;

    return 0;
}
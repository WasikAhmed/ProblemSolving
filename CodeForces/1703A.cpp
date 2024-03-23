// YES or YES?

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
    vector<string> v(t);

    rep(i, 0, t) {
        cin>> v[i];
        transform(v[i].begin(), v[i].end(), v[i].begin(), ::tolower);

        if(v[i] == "yes") cout<< "YES"<< endl;
        else cout<< "NO"<< endl;
    }

    return 0;
}
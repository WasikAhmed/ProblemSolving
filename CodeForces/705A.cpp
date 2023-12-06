// Hulk

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <utility>
#include <string>
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

    string ans = "";
    for(int i=1; i<=n; i++) {
        if(i%2 != 0) ans+="I hate";
        else ans+="I love";

        if(i != n) ans+=" that ";
        else ans+=" it";
    }
    cout<< ans<< endl;

    return 0;
}
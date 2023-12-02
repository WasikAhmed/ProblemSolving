// Soldier and Bananas

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
    int k, n, w; cin>> k>> n>> w;

    int totalCost = 0;
    rep(i, 1, w+1) {
        totalCost += (i * k);
    }

    int ans = totalCost - n;
    if(ans <= 0) {
        cout<< 0<< endl;
    } else {
        cout<< ans<< endl;       
    }


    return 0;
}
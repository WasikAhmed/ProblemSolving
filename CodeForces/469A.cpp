// I Wanna Be the Guy
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
    int p1; cin>> p1;
    vi v1(p1);
    rep(i, 0, v1.size()) {
        cin>> v1[i];
    }
    int p2; cin>> p2;
    vi v2(p2);
    rep(i, 0, v2.size()) {
        cin>> v2[i];
    }

    vi allLevels;
    allLevels.insert(allLevels.end(), v1.begin(), v1.end());
    allLevels.insert(allLevels.end(), v2.begin(), v2.end());

    sort(allLevels.begin(), allLevels.end());
    auto it = unique(allLevels.begin(), allLevels.end());
    allLevels.erase(it, allLevels.end());

    if(allLevels.size() == n) {
        cout<< "I become the guy."<< endl;
    } else {
        cout<< "Oh, my keyboard!"<< endl;
    }

    return 0;
}

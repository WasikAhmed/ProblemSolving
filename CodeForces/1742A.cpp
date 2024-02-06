// Sum

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <utility>
#include <string>
#include <numeric>
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

    while (t--)
    {
        vi v(3);
        for_each(x, v) cin>> x;

        auto largest = max_element(v.begin(), v.end());
        int sum = accumulate(v.begin(), v.end(), 0);

        if(sum == *largest * 2) cout<< "YES"<< endl;
        else cout<< "NO"<< endl;
    }   
    
    return 0;
}
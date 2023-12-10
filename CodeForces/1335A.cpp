// Candies and Two Sisters

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
    while(t >= 1) {
        int n; cin>>n;
        if(n>2) {
            n%2==0 ? cout<< n/2-1<< endl : cout<< n/2<<endl;      
        } else {
            cout<< 0<< endl;
        }
        t--;
    }

    return 0;
}
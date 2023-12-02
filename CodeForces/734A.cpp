// Anton and Danik

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
    string s; cin>> s;

    int A=0, D=0;
    for_each(ch, s) {
        if(ch == 'A') A++;
        else D++;
    }

    if(A > D) {
        cout<< "Anton"<< endl;
    } else if(D > A) {
        cout<< "Danik"<< endl;
    } else {
        cout<< "Friendship"<< endl;
    }

    return 0;
}
// A. Quintomania

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
    int t; cin >> t;
    while (t--)
    {
        int n; cin >> n;
        vi notes(n);
        rep(i, 0, n)
        {
            cin >> notes[i];
        }

        string result = "YES";
        rep(i, 1, n) 
        {
            int interval = abs(notes[i] - notes[i - 1]);
            if(interval != 5 && interval != 7) {
                result = "NO";
                break;
            }
        }
        cout<< result<< endl;
    }

    return 0;
}
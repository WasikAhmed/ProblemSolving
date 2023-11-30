// Calculating Function

#include <iostream>
using namespace std;

#define ll long long

int main()
{
    int n; cin>> n;

    ll ans = 0;
    for(int i=1; i<=n; i++) {
        if(i % 2 == 0) {
            ans += i;
        } else {
            ans -= i;
        }
    }
    cout<< ans<< endl;

    return 0;
}
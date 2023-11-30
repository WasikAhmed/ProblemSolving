// Calculating Function

#include <iostream>
using namespace std;

#define ll long long

int main()
{
    ll n; cin>> n;

    ll ans = 0;
    if(n % 2 == 0) {
        ans = n / 2;
    } else {
        ans = ((n+1)/2) * (-1);
    }
    cout<< ans<< endl;

    return 0;
}
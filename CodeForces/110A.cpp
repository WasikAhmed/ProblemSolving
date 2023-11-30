// Nearly Lucky Number

#include <iostream>
using namespace std;

#define ll long long

int main()
{
    ll n; cin>> n;

    int ans = 0;
    while (n != 0) {
        int digit = n % 10;

        if (digit == 4 || digit == 7) {
            ans++;
        }
        n = n / 10;
    }

    if (ans == 4 || ans == 7) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}

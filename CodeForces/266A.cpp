// Stones on the table

#include <iostream>
using namespace std;

int main()
{
    int n; cin>> n;
    string s; cin>> s;

    char c = s[0];
    int ans = 0;
    for(int i=1; i<n; i++) {
        if(s[i] == c) {
            ans++;
        } else {
            c = s[i];
        }
    }
    cout<< ans<< endl;

    return 0;
}
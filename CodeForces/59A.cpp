// Word

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string s; cin>> s;

    int u=0, l=0;
    for(auto c : s) {
        if(isupper(c)) {
            u++;
        } else {
            l++;
        }
    }

    if(l >= u) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
    } else {
        transform(s.begin(), s.end(), s.begin(), ::toupper);
    }
    cout<< s<< endl;

    return 0;
}

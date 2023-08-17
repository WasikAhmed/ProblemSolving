
#include <iostream>
using namespace std;

bool isPalindrome(int x) {
        string num = to_string(x);
        string reverseNum = "";
        for(int i=num.length()-1; i>=0; i--) {
            reverseNum += num[i];
        }

        return (num == reverseNum);
}

// 
bool isPalindrome2(int x) {
    if (x<0 || (x!=0 && x%10==0)) 
        return false;
    int back = 0;
    while (x>back){
        back = back*10 + x%10;
        x = x/10;
    }
    return (x==back || x==back/10);
}

int main() {


    cout<< isPalindrome(-101)<<endl;


    return 0;
}
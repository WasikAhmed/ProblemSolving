// Longest Common Prefix

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        for(int i=0; i<strs[0].size(); i++) {
            char ch = strs[0][i];

            for(int j=0; j<strs.size(); j++) {
                if(ch != strs[j][i] || i >= strs[j].size()) {
                    return prefix;
                }
            }
            prefix += strs[0][i];
        }
        return prefix;
    }
};
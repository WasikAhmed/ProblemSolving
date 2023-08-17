#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        vector<int> r;

        for(auto i=nums.begin(); i!=nums.end(); ++i) {
            for(auto j=i+1; j!=nums.end(); ++j) {
                if( *i + *j == target) {
                    // int position = std::distance(nums.begin(), it);
                    r.push_back(distance(nums.begin(), i));
                    r.push_back(distance(nums.begin(), j));
                }
            }
        }

        return r;
    }
};
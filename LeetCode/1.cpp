// Two Sum

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0; i<nums.size()-1; i++) {
            for(int j=i+1; j<nums.size(); j++) {
                if(nums[i] + nums[j] == target) {
                    return vector<int>{i, j};
                }
            }
        }
        return vector<int>{};
    }
};


int main() {

    Solution s;
    vector<int> nums = {2,7,11,15};
    vector<int> ans = s.twoSum(nums, 9);
    for(int i=0; i<ans.size(); i++) {
        cout<< ans[i]<< endl;
    }

    return 0;
}
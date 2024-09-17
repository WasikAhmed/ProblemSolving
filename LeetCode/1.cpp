// Two Sum

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         for(int i=0; i<nums.size()-1; i++) {
//             for(int j=i+1; j<nums.size(); j++) {
//                 if(nums[i] + nums[j] == target) {
//                     return vector<int>{i, j};
//                 }
//             }
//         }
//         return vector<int>{};
//     }
// };

// using hashmap
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> num_map;
        for(int i=0; i<nums.size(); i++) {
            int complement = target - nums[i];
            if(num_map.find(complement) != num_map.end()) {
                return {num_map[complement], i};
            }
            num_map[nums[i]] = i;
        }
        return {};
    }
};


int main() {

    Solution s;
    // vector<int> nums = {2,7,11,15};
    vector<int> nums = {3,2,4};
    vector<int> ans = s.twoSum(nums, 6);
    for(int i=0; i<ans.size(); i++) {
        cout<< ans[i]<< endl;
    }

    return 0;
}
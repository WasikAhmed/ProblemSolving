class Solution:
    def findDuplicates(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] not in ans:
                ans.append(nums[i])
        
        return ans

nums = [4,3,2,7,8,2,3,1]

solution = Solution()
solution.findDuplicates(nums)
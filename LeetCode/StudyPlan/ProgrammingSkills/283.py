# Move Zeroes

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1


nums_1 = [0, 1, 0, 3, 12]
nums_2 = [0]

s = Solution()
s.moveZeroes(nums_1)
print(nums_1)
s.moveZeroes(nums_2)
print(nums_2)

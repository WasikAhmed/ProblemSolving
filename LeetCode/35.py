# Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))
    print(s.searchInsert([1, 3], 2))

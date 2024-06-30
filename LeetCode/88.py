# Merge Sorted Array
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        end_idx = len(nums1) - 1
        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[end_idx] = nums2[n - 1]
                n -= 1
            else:
                nums1[end_idx] = nums1[m - 1]
                m -= 1
            end_idx -= 1
        while n > 0:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
            end_idx -= 1


s = Solution()
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))

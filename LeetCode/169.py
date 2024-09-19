# Majority Element
from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using nested loops
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count >= n // 2:
        #         return nums[i]
        # return -1

        # using hashmap
        n = len(nums)
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

            if count_map[num] > n / 2:
                return num
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))

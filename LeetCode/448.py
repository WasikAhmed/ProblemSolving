# Find All Numbers Disappeared in an Array

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

        # using hash
        # result = []
        # hashset = set(nums)
        # for i in range(1, len(nums) + 1):
        #     if i not in hashset:
        #         result.append(i)
        # return result

        # without extra space
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     if nums[index] > 0:
        #         nums[index] = -nums[index]
        #
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         result.append(i + 1)
        #
        # return result


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([1, 1]))

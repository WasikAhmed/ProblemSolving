# Sign of the Product of an Array
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        negatives = [x for x in nums if x < 0]
        if len(negatives) % 2 != 0:
            return -1
        return 1


s = Solution()
print(s.arraySign([-1,-2,-3,-4,3,2,1]))
print(s.arraySign([1,5,0,2,-3]))
print(s.arraySign([-1,1,-1,1,-1]))
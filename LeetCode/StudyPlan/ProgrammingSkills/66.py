# Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        for digit in digits:
            integer = (integer * 10) + digit
        integer += 1

        ans = []
        while integer > 0:
            ans.insert(0, integer % 10)
            integer = integer // 10

        return ans


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))

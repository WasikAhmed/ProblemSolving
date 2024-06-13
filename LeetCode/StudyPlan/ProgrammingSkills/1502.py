# Can Make Arithmetic Progression From Sequence
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
        return True


s = Solution()
print(s.canMakeArithmeticProgression([3, 5, 1]))
print(s.canMakeArithmeticProgression([1, 2, 4]))

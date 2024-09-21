# Power of Three
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        # wrong ans for n=243
        # base = 3
        # p = math.log(n) / math.log(base)
        # return p.is_integer()

        while n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(-1))
    print(s.isPowerOfThree(243))

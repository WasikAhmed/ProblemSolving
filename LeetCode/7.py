# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        max_int32 = 2 ** 31 - 1
        output = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            digit = x % 10
            x = x // 10
            output = output * 10 + digit
            if output > max_int32:
                return 0

        return output * sign

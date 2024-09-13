# Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # count = 1
        # while count <= n:
        #     if count == n:
        #         return True
        #     count *= 2
        # return False

        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2

        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(3))

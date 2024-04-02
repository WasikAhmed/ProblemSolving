class Solution:
    def largestAltitude(self, gain):
        max = 0
        a = 0

        for i in gain:
            a+=i
            if a > max:
                max = a
        return max


s = Solution()

nums = [-5, 1, 5, 0, -7]

print(s.largestAltitude(nums))

class Solution:
    def largestAltitude(self, gain):
        n = len(gain)

        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + gain[i]

        return max(prefix_sum)


s = Solution()

nums = [-5, 1, 5, 0, -7]

print(s.largestAltitude(nums))

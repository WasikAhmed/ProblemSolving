# Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]


s = Solution()
print(s.findTheDifference('abcd', 'abcde'))
print(s.findTheDifference('', 'y'))

# Longest Palindromic Substring

class Solution:
    def check_pal(self, s, low, high) -> bool:
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        max_len = 1
        start = 0

        for i in range(n):
            for j in range(i, n):
                if self.check_pal(s, i, j) and (j - i + 1) > max_len:
                    start = i
                    max_len = j - i + 1
        return s[start:start + max_len]

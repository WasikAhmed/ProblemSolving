# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(char.lower() for char in s if char.isalnum())
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        return s == s[::-1]


soln = Solution()
print(soln.isPalindrome("A man, a plan, a canal: Panama"))
print(soln.isPalindrome("race a car"))
print(soln.isPalindrome(" "))

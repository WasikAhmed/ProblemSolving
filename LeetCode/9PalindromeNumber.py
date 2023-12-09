# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(0, int(len(s)/2)):
            if(s[i] != s[len(s)-i-1]):
                return False
        return True

if __name__ == "__main__":
    x: int = int(input("Please enter an integer to check palindrome: "))
    print(type(x))
    s = Solution()
    print(s.isPalindrome(x))

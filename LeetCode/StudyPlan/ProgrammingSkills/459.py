# Repeated Substring Pattern

class Solution:
    # When we concatenate s with itself and then remove the first and last characters,
    # any repeating pattern in s will still appear as a substring in the modified string.
    def repeatedSubstringPattern(self, s: str) -> bool:
        modified_string = (s + s)[1:-1]
        return s in modified_string


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('abab'))
    print(s.repeatedSubstringPattern('aba'))
    print(s.repeatedSubstringPattern('abcabcabcabc'))
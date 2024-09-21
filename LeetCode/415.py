# Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]

        result, carry = '', 0
        for i in range(max(len(num1), len(num2))):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result += str(total % 10)

        if carry:
            result += str(carry)

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('11', '123'))
    print(s.addStrings('456', '77'))
    print(s.addStrings('0', '0'))

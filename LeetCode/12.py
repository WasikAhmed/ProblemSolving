# Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        sym_val = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
                   4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        values = [1, 4, 5, 9, 10, 40, 50, 90,
                  100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]

        roman = ''
        i = 12
        while num > 0:
            div = num // values[i]
            num = num % values[i]

            while div:
                roman += sym[i]
                div -= 1
            i -= 1
        return roman


if __name__ == "__main__":
    s = Solution()

    number = 3749
    print("Roman value is:", end=" ")
    print(s.intToRoman(number))

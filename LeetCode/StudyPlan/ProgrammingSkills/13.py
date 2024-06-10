# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]

        value_table = dict(zip(symbols, values))

        integer = 0
        # for i in range(len(s)):
        #     if i < len(s) - 1 and s[i] in ['I', 'X', 'C']:
        #         if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
        #             integer -= value_table.get(s[i])
        #         elif s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
        #             integer -= value_table.get(s[i])
        #         elif s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
        #             integer -= value_table.get(s[i])
        #         else:
        #             integer += value_table.get(s[i])
        #     else:
        #         integer += value_table.get(s[i])
        # return integer

        integer = 0
        for i in range(len(s)):
            if i < len(s) - 1 and value_table[s[i]] < value_table[s[i+1]]:
                integer -= value_table[s[i]]
            else:
                integer += value_table[s[i]]

        return integer


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))

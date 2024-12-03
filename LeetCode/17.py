# Letter Combinations of a Phone Number

from typing import List
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
                   6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        if not digits:
            return []
        
        strings = [mapping[int(digit)] for digit in digits if int(digit) in mapping]
        
        combinations = itertools.product(*strings)
        return [''.join(combination) for combination in combinations]
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('2'))
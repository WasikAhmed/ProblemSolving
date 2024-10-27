# Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_rows = 1
        while n >= complete_rows:
            n -= complete_rows
            complete_rows += 1
        return complete_rows - 1
        

if __name__ == "__main__":
    s = Solution()
    print(s.arrangeCoins(5))
    print(s.arrangeCoins(8))
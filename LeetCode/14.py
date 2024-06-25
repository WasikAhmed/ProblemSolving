# Longest Common Prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = sorted(strs)
        # ans = ''
        # for i in range(len(strs[0])):
        #     if strs[0][i] == strs[-1][i]:
        #         ans += strs[0][i]
        #     else:
        #         break
        # return ans

        mini, maxi = min(strs), max(strs)

        for i in range(len(mini)):
            if mini[i] != maxi[i]:
                return mini[:i]
        return mini


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

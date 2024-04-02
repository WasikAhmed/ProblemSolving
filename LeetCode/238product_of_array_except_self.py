class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)

            prefix_product = [1] * n
            suffix_product = [1] * n

            for i in range(1, n):
                prefix_product[i] = prefix_product[i-1] * nums[i-1]
            
            for i in range(n-2, -1, -1):
                suffix_product[i] = suffix_product[i+1] * nums[i+1]

            return [prefix_product[i] * suffix_product[i] for i in range(n)]
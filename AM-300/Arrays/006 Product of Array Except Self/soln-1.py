class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Compute prefix products directly in res
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
            
        # Step 2: Compute suffix products on the fly
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res

# Prefix-Suffix Accumulator Space-Optimized
# time -> O(n)
# space -> O(1)
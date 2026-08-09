class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_subarrays = 0
        current_run = 0
        
        for num in nums:
            if num == 0:
                current_run += 1
                total_subarrays += current_run
            else:
                current_run = 0
                
        return total_subarrays

# Linear Scan with Running Sum
# time -> O(n)
# space -> O(1)
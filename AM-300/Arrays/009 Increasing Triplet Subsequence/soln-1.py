class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
                
        return False

# Linear Scan Greedy Elimination
# time -> O(n)
# space -> O(1)
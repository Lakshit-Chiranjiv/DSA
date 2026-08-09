# My approach
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        bkw_ptr = 0
        frw_ptr = 1
        while frw_ptr < len(nums):
            if nums[bkw_ptr] != nums[frw_ptr]:
                bkw_ptr += 1
                nums[bkw_ptr] = nums[frw_ptr]
            frw_ptr += 1
        
        return bkw_ptr+1
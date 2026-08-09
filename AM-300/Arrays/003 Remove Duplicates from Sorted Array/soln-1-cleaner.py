class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        bkw_ptr = 0
        for frw_ptr in range(1, len(nums)):
            if nums[bkw_ptr] != nums[frw_ptr]:
                bkw_ptr += 1
                nums[bkw_ptr] = nums[frw_ptr]
                
        return bkw_ptr + 1
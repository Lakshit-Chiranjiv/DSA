class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_of_zeroes = 0
        for i in nums:
            if i == 0:
                num_of_zeroes += 1
        
        total_non_zeroes = len(nums) - num_of_zeroes
        non_zero_ptr = 0
        non_zeroes_till_now = 0
        for i in range(len(nums)):
            if nums[i] != 0 and non_zeroes_till_now < total_non_zeroes:
                nums[non_zero_ptr] = nums[i]
                non_zero_ptr += 1
                non_zeroes_till_now += 1
                if i >= total_non_zeroes:
                    nums[i] = 0

        return nums
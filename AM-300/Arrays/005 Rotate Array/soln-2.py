class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        count = 0
        start = 0
        
        while count < n:
            current = start
            prev = nums[start]
            
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

# Cyclic Replacements
# time -> O(n)
# space -> O(1)
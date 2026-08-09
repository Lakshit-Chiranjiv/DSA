class Solution:

  def firstMissingPositive(self, nums: list[int]) -> int:
    nums.sort()
    target = 1
    for num in nums:
      if num == target:
        target += 1
      elif num > target:
        break
    return target

# sorting solution
# time -> O(n log n)
# space -> O(1)
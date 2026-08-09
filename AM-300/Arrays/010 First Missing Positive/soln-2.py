class Solution:

  def firstMissingPositive(self, nums: list[int]) -> int:
    num_set = set(nums)
    target = 1
    while target in num_set:
      target += 1
    return target

# hash set solution
# time -> O(n)
# space -> O(n)
class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
      count += n & 1
      n >>= 1
    return count

# Bitwise Shift Solution
# time -> O(1)
# space -> O(1)
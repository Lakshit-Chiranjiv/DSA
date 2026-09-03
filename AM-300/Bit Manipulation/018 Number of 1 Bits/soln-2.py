class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
      n &= n - 1
      count += 1
    return count

# Brian Kernighan's Algorithm
# time -> O(1)
# space -> O(1)
class Solution:

  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    while right > left:
      right &= right - 1
    return right

# Brian Kernighan Range Mask
# time -> O(1)
# space -> O(1)
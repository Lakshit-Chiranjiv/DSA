class Solution:

  def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF

    def add(x: int, y: int) -> int:
      if y == 0:
        return x
      # x ^ y computes partial sum, (x & y) << 1 computes shifted carry
      return add((x ^ y) & mask, ((x & y) << 1) & mask)

    res = add(a, b)
    # Reconstruct 32-bit signed integer if MSB is 1
    return res if res <= 0x7FFFFFFF else ~(res ^ mask)

# Bitwise Recursive Full Adder
# time -> O(1) (at most 32 recursion frames)
# space -> O(1) (tail-call overhead bounded by 32 call frames)
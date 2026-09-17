class Solution:

  def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF  # 32-bit mask to handle infinite precision in Python

    while b != 0:
      carry = (a & b) << 1
      a = (a ^ b) & mask  # Keep 'a' within 32-bit range
      b = carry & mask  # Keep 'b' within 32-bit range

    # If 'a' is a positive 32-bit signed integer, return it directly.
    # If 'a' is negative (most significant bit is 1), convert it back to Python's signed int.
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

# Bitwise Full Adder Simulation
# time -> O(1) (at most 32 iterations)
# space -> O(1)
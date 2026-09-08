class Solution:

  def singleNumber(self, nums: list[int]) -> list[int]:
    xor_all = 0
    for num in nums:
      xor_all ^= num

    # Clear lowest set bit, then XOR with original to isolate that single bit
    diff_bit = (xor_all & (xor_all - 1)) ^ xor_all

    a, b = 0, 0
    for num in nums:
      if num & diff_bit:
        a ^= num
      else:
        b ^= num

    return [a, b]

# Kernighan Bit-Difference Isolation
# time -> O(n)
# space -> O(1)
class Solution:

  def singleNumber(self, nums: list[int]) -> list[int]:
    # Step 1: XOR all numbers to get (a ^ b)
    xor_all = 0
    for num in nums:
      xor_all ^= num

    # Step 2: Isolate the lowest set bit (where a and b differ)
    diff_bit = xor_all & -xor_all

    # Step 3: Divide numbers into two groups based on diff_bit
    a = 0
    b = 0
    for num in nums:
      if num & diff_bit:
        a ^= num
      else:
        b ^= num

    return [a, b]

# Partitioning via Lowest Set Bit
# time -> O(n)
# space -> O(1)
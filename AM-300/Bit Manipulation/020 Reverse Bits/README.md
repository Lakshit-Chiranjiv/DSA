# 190. Reverse Bits

## Problem Summary
Reverse the bits of a given 32-bit unsigned integer `n`.

## My Approach
Extract the rightmost bit of `n` using bitwise shift operations, append it to a running result variable, and right-shift `n` until all bits are reversed. Avoid string conversions to maintain constant space complexity.

## Final Accepted Approach
Bit Reversal via Bitwise Shift and Masking (`res = (res << 1) | (n & 1)`).

## All Solutions Explanation
- **Bit Reversal Shift Solution**: Iterates exactly 32 times (for a 32-bit integer). In each iteration, it shifts the accumulated result `res` left by 1 bit to make space, extracts the lowest bit of `n` using `n & 1`, appends it to `res` using bitwise OR (`|`), and shifts `n` right by 1 bit (`n >>= 1`). This constructs the reversed bit sequence from left to right in $O(1)$ time and $O(1)$ space.

## How to Think Toward This Pattern Next Time
When required to process or construct binary digits in reverse order without extra memory, treat the integer like a stream of bits: use `n & 1` to peek at the tail, `res << 1` to push elements onto the head of the new sequence, and `n >>= 1` to pop elements from the old sequence.

## Key Observation That Unlocks the Problem
Bits can be moved into position using shifting operators (`<<` and `>>`). Left-shifting `res` by 1 makes room at the least significant bit position (`0`), allowing us to attach the rightmost bit of `n` (`n & 1`) seamlessly using bitwise OR (`|`). Repeating this exactly 32 times guarantees a full reversal of fixed-width binary numbers.

## Complexity Comparison
- Bit Reversal Shift Solution: Time $O(1)$ (exactly 32 iterations for a 32-bit integer), Space $O(1)$ extra space.

## Similar Problems / Pattern Keywords
- Number of 1 Bits
- Single Number
- Reverse Integer
- Pattern Keywords: Bit Manipulation, Bit Shift, Bitwise OR, Bitwise AND, Fixed-width Binary

## Detailed Explanation and Walkthrough

### Solution: Bit Reversal Shift Solution

#### Mechanism
1. Initialize `res = 0`.
2. Loop 32 times (for a 32-bit integer):
   - Shift `res` to the left by 1 position: `res = res << 1`.
   - Extract the rightmost bit of `n`: `bit = n & 1`.
   - Combine the extracted bit with `res`: `res = res | bit`.
   - Shift `n` to the right by 1 position: `n = n >> 1`.
3. Return `res`.

#### Walkthrough for a 4-Bit Example
Consider reversing 4 bits for `n = 11` (binary `1011`). Initialize `res = 0000`.

- **Iteration 1**:
  - `bit = 1011 & 0001 = 1`
  - `res = (0000 << 1) | 1 = 0001`
  - `n = 1011 >> 1 = 0101` (5)
- **Iteration 2**:
  - `bit = 0101 & 0001 = 1`
  - `res = (0001 << 1) | 1 = 0011`
  - `n = 0101 >> 1 = 0010` (2)
- **Iteration 3**:
  - `bit = 0010 & 0001 = 0`
  - `res = (0011 << 1) | 0 = 0110`
  - `n = 0010 >> 1 = 0001` (1)
- **Iteration 4**:
  - `bit = 0001 & 0001 = 1`
  - `res = (0110 << 1) | 1 = 1101`
  - `n = 0001 >> 1 = 0000` (0)

Final Output: `res = 1101` (binary representation of `1011` reversed).
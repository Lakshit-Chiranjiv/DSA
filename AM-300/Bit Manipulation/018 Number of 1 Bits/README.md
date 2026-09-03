# 191. Number of 1 Bits

## Problem Summary
Given a positive integer `n`, write a function to return the number of set bits (1s) it has (also known as Hamming Weight).

## My Approach
Convert the number to a binary string and iterate through the string to count '1's.

## Final Accepted Approach
Brian Kernighan’s Bitwise Algorithm (`n & (n - 1)`).

## All Solutions Explanation
- **Bitwise Shift Solution**: Loop through all bits by using bitwise AND with 1 (`n & 1`) to check the lowest bit, then shift right (`n >>= 1`) until `n` is 0.
- **Brian Kernighan's Algorithm**: Perform `n = n & (n - 1)` in a loop until `n` becomes 0. Each operation clears the rightmost set bit, running iterations equal only to the count of set bits.

## How to Think Toward This Pattern Next Time
When dealing with set bit counting or bit manipulation where you want to jump directly between set bits without processing zero bits, use `n & (n - 1)`.

## Key Observation That Unlocks the Problem
Subtracting 1 flips the rightmost set bit to 0 and all trailing bits to 1. Performing `n & (n - 1)` systematically removes the lowest set bit in $O(1)$ without inspecting 0 bits.

## Complexity Comparison
- Bitwise Shift Solution: Time $O(1)$ (up to 32 shifts for a 32-bit int), Space $O(1)$
- Brian Kernighan's Algorithm: Time $O(1)$ (bounded by number of set bits $\le 32$), Space $O(1)$

## Similar Problems / Pattern Keywords
- Counting Bits
- Reverse Bits
- Power of Two
- Keywords: Bit Manipulation, Set Bits, Hamming Weight, Brian Kernighan

## Detailed Explanation and Walkthrough

### Bitwise Shift Solution
- Check the least significant bit using `n & 1`.
- Add the result to a running counter.
- Shift `n` right by 1 bit using `n >>= 1`.
- Repeat until `n == 0`.

### Brian Kernighan's Algorithm
- Loop `while n > 0`, clear the rightmost set bit using `n &= (n - 1)` and increment `count`.
- Example: `n = 11` (`1011` in binary)
  - Iteration 1: `n = 11 & 10` (`1011 & 1010`) -> `1010` (10), `count = 1`
  - Iteration 2: `n = 10 & 9` (`1010 & 1001`) -> `1000` (8), `count = 2`
  - Iteration 3: `n = 8 & 7` (`1000 & 0111`) -> `0000` (0), `count = 3`
- Loop terminates. Result: `3`
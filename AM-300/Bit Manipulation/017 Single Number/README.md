# 136. Single Number

## Problem Summary
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. The solution must run in linear runtime complexity and use only constant extra space.

## My Approach
Bitwise XOR Bit Manipulation

## Final Accepted Approach
Bitwise XOR Bit Manipulation

## Solution Explanation
- **Bitwise XOR Solution**: Initialize an accumulator with the first element (or 0) and compute the bitwise XOR across all elements in the array. Since $A \oplus A = 0$ and $A \oplus 0 = A$, all duplicate numbers cancel out, leaving only the unique element.

## How to Think Toward This Pattern Next Time
When a problem asks for an $O(n)$ time and $O(1)$ space solution involving finding unique or missing elements where pairs cancel out, think of bitwise XOR ($\oplus$).

## Key Observation That Unlocks the Problem
XOR is commutative and associative ($A \oplus B \oplus A = A \oplus A \oplus B = 0 \oplus B = B$). XORing identical numbers results in 0, effectively removing all paired duplicates.

## Complexity Comparison
- Bitwise XOR Solution: Time $O(n)$, Space $O(1)$

## Similar Problems / Pattern Keywords
- Single Number II
- Single Number III
- Missing Number
- Find the Duplicate Number
- Keywords: Bit Manipulation, XOR, Cancel Pairs, In-Place Constant Space

## Detailed Explanation and Walkthrough

### Bitwise XOR Solution
- Iterate through every integer in the array while maintaining a running XOR total.
- For example, with `nums = [4, 1, 2, 1, 2]`:
  - Step 1: Start with `4`.
  - Step 2: `4 ^ 1` = `5`.
  - Step 3: `5 ^ 2` = `7`.
  - Step 4: `7 ^ 1` = `6` (cancels out `1`).
  - Step 5: `6 ^ 2` = `4` (cancels out `2`).
- The final result is `4`, which is the single element that appears only once.
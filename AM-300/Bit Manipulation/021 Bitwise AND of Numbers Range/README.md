# 201. Bitwise AND of Numbers Range

## Problem Summary
Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

## My Approach
Initially consider iterating from `left` to `right` and applying the bitwise AND operation sequentially (`left & (left + 1) & ... & right`). However, this linear scan results in a Time Limit Exceeded (TLE) error when the range size $right - left$ is large (up to $2^{31} - 1$).

## Final Accepted Approach
Identify the **Common Binary Prefix** between `left` and `right`. Any bit position that flips between `0` and `1` across the range $[left, right]$ evaluates to `0` under bitwise AND. The problem reduces to finding the longest common prefix of `left` and `right` and padding the trailing bits with zeros.

## All Solutions Explanation
- **Solution 1: Common Prefix Bit Shift**: Repeatedly right-shift both `left` and `right` simultaneously until they become equal (`left == right`). Track the number of shifts performed in a variable `shifts`. Once `left` and `right` match, the common prefix is isolated. Left-shift the matching prefix back by `shifts` positions (`left << shifts`) to append trailing zeros and restore the original bit positions.
- **Solution 2: Brian Kernighan Range Masking**: Continuously clear the lowest set bit (`1`) of `right` using `right &= right - 1` as long as `right > left`. Since any `1` bit in `right` that makes `right` strictly greater than `left` is guaranteed to flip to `0` at least once in the range $[left, right]$, clearing it directly skips irrelevant non-prefix bits. When `right <= left`, all changing lower bits have been cleared to `0`, leaving `right` as the exact common prefix.

## How to Think Toward This Pattern Next Time
When tasked with computing bitwise operations across a contiguous integer range $[left, right]$:
1. Recognize that positional bit transitions follow a strict binary hierarchy. Lower-order bits cycle rapidly between `0` and `1`, while higher-order bits (prefix) remain unchanged unless a carry-over spans across the entire range.
2. Realize that any bit position that changes value at least once in the range will evaluate to `0` in a cumulative bitwise AND.
3. Shift both bounds or systematically clear trailing set bits of the upper bound until the non-common changing bits are eliminated.

## Key Observation That Unlocks the Problem
If `left` and `right` share a common binary prefix, no integer $x$ in the range $[left, right]$ can ever change those prefix bits, because changing a prefix bit requires a value overflow strictly greater than `right`. Consequently, the result of the range bitwise AND is simply the shared prefix of `left` and `right` followed by zeros in all non-matching rightmost bit positions.

## Complexity Comparison
- **Solution 1 (Common Prefix Bit Shift)**: Time Complexity $O(1)$ (at most 32 shift operations for 32-bit integers), Space Complexity $O(1)$ auxiliary space.
- **Solution 2 (Brian Kernighan Range Masking)**: Time Complexity $O(1)$ (at most 32 bit-clearing operations), Space Complexity $O(1)$ auxiliary space.

## Similar Problems / Pattern Keywords
- Number of 1 Bits
- Counting Bits
- Reverse Bits
- Single Number
- Pattern Keywords: Bit Manipulation, Common Binary Prefix, Bit Shift, Range Operations, Brian Kernighan Algorithm

## Detailed Explanation and Walkthrough

### Solution 1: Common Prefix Bit Shift

#### Mechanism
1. Initialize a counter `shifts = 0`.
2. Enter a loop that continues while `left != right`:
   - Right-shift `left` by 1 bit (`left >>= 1`).
   - Right-shift `right` by 1 bit (`right >>= 1`).
   - Increment `shifts` by 1.
3. Left-shift `left` back by `shifts` bits (`left << shifts`) and return it.

#### Walkthrough for `left = 9` (`1001`) and `right = 12` (`1100`)
- **Initial State**: `left = 1001` (9), `right = 1100` (12), `shifts = 0`.
- **Iteration 1**:
  - `left` becomes `0100` (4), `right` becomes `0110` (6).
  - `shifts = 1`. (`left != right`)
- **Iteration 2**:
  - `left` becomes `0010` (2), `right` becomes `0011` (3).
  - `shifts = 2`. (`left != right`)
- **Iteration 3**:
  - `left` becomes `0001` (1), `right` becomes `0001` (1).
  - `shifts = 3`.
- **Loop Termination**: `left == right` (`0001`).
- **Reconstruction**: `left << shifts` $
ightarrow$ `0001 << 3` = `1000` (8).
- **Result**: `8`.

---

### Solution 2: Brian Kernighan Range Masking

#### Mechanism
1. Enter a loop that runs while `right > left`.
2. Clear the rightmost set bit of `right` using `right = right & (right - 1)`.
3. When `right <= left`, the loop terminates. Return `right`.

#### Why Stopping at `right <= left` Works
- While `right > left`, `right` contains at least one set bit (`1`) at a lower position that makes its numeric value strictly exceed `left`.
- Because $left \le right$, this set bit is guaranteed to flip to `0` somewhere in the range $[left, right]$, making it impossible for that bit position to survive bitwise AND.
- `right &= right - 1` clears this doomed bit in $O(1)$ time.
- Once `right` drops to or below `left`, all non-common trailing bits have been zeroed out, and `right` holds the common binary prefix.

#### Walkthrough for `left = 9` (`1001`) and `right = 12` (`1100`)
- **Initial State**: `left = 1001` (9), `right = 1100` (12).
- **Iteration 1**:
  - Is `right > left`? ($12 > 9$) $
ightarrow$ **True**.
  - `right = 12 & (12 - 1)` = `1100 & 1011` = `1000` (8).
- **Loop Check**:
  - Is `right > left`? ($8 > 9$) $
ightarrow$ **False**.
- **Loop Termination**: Returns `right = 8` (`1000`).
- **Result**: `8`.
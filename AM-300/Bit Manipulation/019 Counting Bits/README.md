# 338. Counting Bits

## Problem Summary
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`s in the binary representation of `i`.

## My Approach
Iterate through every integer from `0` to `n`. For each individual integer, execute Brian Kernighan's bit-clearing algorithm (`i & (i - 1)`) in a nested loop to count how many set bits it contains, storing each result independently in an array.

## Final Accepted Approach
Bitwise Dynamic Programming utilizing the subproblem relationship `ans[i] = ans[i & (i - 1)] + 1`.

## All Solutions Explanation
- **Brian Kernighan Iteration Solution**: Loops through every integer `i` from `1` to `n`. In an inner loop, it clears the lowest set bit of `i` using `curr &= curr - 1` while incrementing a counter until `curr` becomes `0`. The count is then assigned to `ans[i]`. While correct and running in linear time overall, it processes each number independently without leveraging work already done for earlier numbers.
- **Bitwise Dynamic Programming Solution**: Leverages overlapping subproblems. Clearing the lowest set bit of any number `i` using `i & (i - 1)` always yields a smaller integer whose binary representation is identical to `i` except for that one dropped bit. Since `i & (i - 1) < i`, its set bit count has already been calculated and stored in `ans[i & (i - 1)]`. Therefore, `ans[i]` can be computed in constant $O(1)$ time by taking `ans[i & (i - 1)]` and adding `1` for the bit that was removed.

## How to Think Toward This Pattern Next Time
When tasked with calculating a bitwise property across a continuous sequence of integers $[0, n]$, ask whether a larger number's binary representation can be derived from a smaller, previously processed number. Instead of evaluating each integer independently, map the target integer to a smaller subproblem via bit manipulation (such as bit-shifting or dropping the lowest set bit) and build a Dynamic Programming table sequentially.

## Key Observation That Unlocks the Problem
The bitwise expression `i & (i - 1)` drops the rightmost `1` bit from `i`. Because removing a bit strictly decreases the numeric value, `i & (i - 1)` points to an index prior to `i`. Thus, the set bit count of `i` is always exactly equal to $1 + 	ext{set bits in } (i 	ext{ \& } (i - 1))$, which is already precomputed in `ans`.

## Complexity Comparison
- Brian Kernighan Iteration Solution: Time $O(n)$ (since each integer has at most 32 bits, requiring $\le 32$ iterations per element), Space $O(1)$ extra auxiliary space (excluding the required output array of size $n + 1$).
- Bitwise Dynamic Programming Solution: Time $O(n)$ (exactly 1 constant-time step per element), Space $O(1)$ extra auxiliary space (excluding the required output array of size $n + 1$).

## Similar Problems / Pattern Keywords
- Number of 1 Bits
- Reverse Bits
- Single Number
- Power of Two
- Pattern Keywords: Bit Manipulation, Dynamic Programming, Subproblem Reuse, Bitwise DP, State Transition

## Detailed Explanation and Walkthrough

### Solution 1: Brian Kernighan Iteration Solution
#### Mechanism
1. Construct an answer array `ans` of size `n + 1` initialized with `0`s.
2. For each number `i` from `1` to `n`:
   - Assign `curr = i` and `count = 0`.
   - Enter a loop that continues while `curr > 0`:
     - Perform `curr = curr & (curr - 1)` to clear the lowest set bit.
     - Increment `count` by `1`.
   - Assign `ans[i] = count`.

#### Walkthrough for $n = 3$
- `i = 0`: `0` set bits $
ightarrow$ `ans[0] = 0`
- `i = 1` (`01`):
  - `curr = 1 & 0 = 0`, `count = 1`
  - Loop terminates $
ightarrow$ `ans[1] = 1`
- `i = 2` (`10`):
  - `curr = 2 & 1 = 0`, `count = 1`
  - Loop terminates $
ightarrow$ `ans[2] = 1`
- `i = 3` (`11`):
  - Iteration 1: `curr = 3 & 2 = 2` (`10`), `count = 1`
  - Iteration 2: `curr = 2 & 1 = 0` (`00`), `count = 2`
  - Loop terminates $
ightarrow$ `ans[3] = 2`
- Final Array: `[0, 1, 1, 2]`

---

### Solution 2: Bitwise Dynamic Programming Solution
#### Mechanism
1. Initialize an array `ans` of size `n + 1` with all zeros (`ans[0] = 0` acts as the base case).
2. Iterate `i` sequentially from `1` to `n`.
3. Compute `prev_index = i & (i - 1)`.
4. Look up `ans[prev_index]` from memory.
5. Set `ans[i] = ans[prev_index] + 1`.

#### Step-by-Step State Execution for $n = 5$
- Base Case: `ans[0] = 0`
- `i = 1` (`001` in binary):
  - `i & (i - 1)` = `1 & 0` = `0`
  - `ans[1] = ans[0] + 1` = $0 + 1 = 1$
- `i = 2` (`010` in binary):
  - `i & (i - 1)` = `2 & 1` = `0`
  - `ans[2] = ans[0] + 1` = $0 + 1 = 1$
- `i = 3` (`011` in binary):
  - `i & (i - 1)` = `3 & 2` = `2` (`010`)
  - `ans[3] = ans[2] + 1` = $1 + 1 = 2$
- `i = 4` (`100` in binary):
  - `i & (i - 1)` = `4 & 3` = `0`
  - `ans[4] = ans[0] + 1` = $0 + 1 = 1$
- `i = 5` (`101` in binary):
  - `i & (i - 1)` = `5 & 4` = `4` (`100`)
  - `ans[5] = ans[4] + 1` = $1 + 1 = 2$

#### Final Output
`ans = [0, 1, 1, 2, 1, 2]`
# Single Number III

## Problem Summary
Given an integer array `nums` where exactly two elements appear only once, and all other elements appear exactly twice, find the two elements that appear only once. The algorithm must run in $O(n)$ time complexity and use $O(1)$ auxiliary space.

## My Approach
A single XOR pass across all elements yields `xor_all = a ^ b`. Since $a \neq b$, `xor_all` contains at least one set bit (`1`), which indicates a bit position where $a$ and $b$ differ. Using this bit as a partition mask splits the array into two groups such that $a$ and $b$ fall into separate groups, while identical duplicate pairs fall into the same group and cancel out.

## Final Accepted Approach
Isolate a single differentiating set bit from `xor_all` (using low-bit extraction) and use bitwise AND with this mask to partition the array elements into two buckets, finding $a$ and $b$ independently via XOR accumulators.

## All Solutions Explanation
- **Solution 1: Two's Complement Low-Bit Extraction (`diff_bit = xor_all & -xor_all`)**: Computes `-xor_all` using two's complement arithmetic (`~xor_all + 1`). Bitwise ANDing `xor_all & -xor_all` isolates the rightmost `1` bit because the carry-over during negation preserves only the lowest set bit while inverting all higher bits.
- **Solution 2: Kernighan Bit-Difference Isolation (`diff_bit = (xor_all & (xor_all - 1)) ^ xor_all`)**: Uses `xor_all & (xor_all - 1)` to turn off the lowest set bit of `xor_all`. XORing this modified value back with `xor_all` cancels all remaining set bits, leaving only the isolated rightmost set bit.

## How to Think Toward This Pattern Next Time
When required to isolate two unique values from a paired collection in $O(n)$ time and $O(1)$ space:
1. Apply XOR across the dataset to reduce duplicate pairs to `0`.
2. Realize that the non-zero XOR sum represents $a \oplus b$.
3. Pick any set bit in $a \oplus b$ as a binary divider (since $a$ and $b$ must have opposing bits at this position).
4. Filter the entire array into two sub-problems using this bit mask.

## Key Observation That Unlocks the Problem
In XOR arithmetic, a bit evaluates to `1` if and only if the corresponding bits of the two operands are different (`1 ^ 0 = 1`). Isolating any set bit in `xor_all = a ^ b` gives a deterministic criterion to separate $a$ and $b$ into different groups while guaranteeing that paired duplicates land in the same group.

## Complexity Comparison
- **Solution 1 (Two's Complement Low-Bit)**: Time Complexity $O(n)$ (two passes over `nums`), Space Complexity $O(1)$ auxiliary space.
- **Solution 2 (Kernighan Bit-Difference)**: Time Complexity $O(n)$ (two passes over `nums`), Space Complexity $O(1)$ auxiliary space.

## Similar Problems / Pattern Keywords
- Single Number
- Single Number II
- Missing Number
- Pattern Keywords: Bit Manipulation, XOR Partitioning, Low-Bit Extraction, Two's Complement, Brian Kernighan Algorithm

---

## Detailed Explanation and Walkthrough

### Solution 1: Two's Complement Low-Bit Extraction

#### Theoretical Mechanics
To separate $a$ and $b$ from `xor_all = a ^ b`, we extract its lowest set bit using `diff_bit = xor_all & -xor_all`. 

In two's complement representation:
$$\text{-xor\_all} = \sim\text{xor\_all} + 1$$

When adding `1` to `~xor_all`, the binary addition carries over across all trailing inverted `1`s (converting them to `0`s) until it reaches the first inverted `0` (which was the original lowest set bit `1`), turning it back into `1`. 

All bits to the left remain inverted. Performing bitwise AND between `xor_all` (original prefix + lowest `1` + trailing zeros) and `-xor_all` (inverted prefix + lowest `1` + trailing zeros) results in `0` for the prefix, `0` for trailing zeros, and `1` strictly at the lowest set bit position.

#### Algorithm Steps
1. Compute `xor_all` by XORing all integers in `nums`.
2. Extract the rightmost set bit: `diff_bit = xor_all & -xor_all`.
3. Initialize `a = 0` and `b = 0`.
4. Iterate over `nums`:
   - If `num & diff_bit` is non-zero, update `a ^= num`.
   - Otherwise, update `b ^= num`.
5. Return `[a, b]`.

#### Step-by-Step Execution Trace (`nums = [1, 2, 1, 3, 2, 5]`)
- **Step 1 (XOR Pass)**:
  $$\text{xor\_all} = 1 \oplus 2 \oplus 1 \oplus 3 \oplus 2 \oplus 5 = (1 \oplus 1) \oplus (2 \oplus 2) \oplus (3 \oplus 5) = 0 \oplus 0 \oplus 6 = 6 \quad (\text{binary: } 0110_2)$$
- **Step 2 (Low-Bit Extraction)**:
  $$\text{xor\_all} = 6 \rightarrow 0110_2$$
  $$\text{-xor\_all} = -6 \rightarrow 1010_2$$
  $$\text{diff\_bit} = 0110_2 \text{ \& } 1010_2 = 0010_2 \quad (\text{decimal: } 2)$$
- **Step 3 (Group Partitioning)**:
  Mask = `0010_2` (testing bit position 1).
  - `1` (`0001_2`): `1 & 2 == 0` $\rightarrow$ Group B (`b ^= 1`)
  - `2` (`0010_2`): `2 & 2 == 2` $\rightarrow$ Group A (`a ^= 2`)
  - `1` (`0001_2`): `1 & 2 == 0` $\rightarrow$ Group B (`b ^= 1`)
  - `3` (`0011_2`): `3 & 2 == 2` $\rightarrow$ Group A (`a ^= 3`)
  - `2` (`0010_2`): `2 & 2 == 2` $\rightarrow$ Group A (`a ^= 2`)
  - `5` (`0101_2`): `5 & 2 == 0` $\rightarrow$ Group B (`b ^= 5`)
- **Step 4 (Accumulation)**:
  - **Group A Accumulation**: $a = 2 \oplus 3 \oplus 2 = 3$
  - **Group B Accumulation**: $b = 1 \oplus 1 \oplus 5 = 5$
- **Result**: `[3, 5]`

---

### Solution 2: Kernighan Bit-Difference Isolation

#### Theoretical Mechanics
Instead of relying on negative integer representation (`-x`), Solution 2 extracts the lowest set bit using Brian Kernighan's bit-clearing mechanism paired with XOR.

1. **Bit Clearing**: `cleared = xor_all & (xor_all - 1)`
   Subtracting `1` from `xor_all` flips its lowest set bit from `1` to `0`, and flips all trailing `0`s to `1`s. Performing `xor_all & (xor_all - 1)` clears the lowest set bit while leaving all higher bits unchanged.
2. **Bit Isolation**: `diff_bit = cleared ^ xor_all`
   `cleared` and `xor_all` are completely identical across all bit positions except for the single lowest set bit that was just erased. XORing `cleared` with `xor_all` cancels all identical higher bits (`1 ^ 1 = 0`, `0 ^ 0 = 0`) and isolates the erased bit (`0 ^ 1 = 1`).

#### Algorithm Steps
1. Compute `xor_all` by XORing all integers in `nums`.
2. Clear the lowest set bit: `cleared = xor_all & (xor_all - 1)`.
3. Isolate the difference bit: `diff_bit = cleared ^ xor_all`.
4. Initialize `a = 0` and `b = 0`.
5. Iterate over `nums` and partition into `a` and `b` using `num & diff_bit`.
6. Return `[a, b]`.

#### Step-by-Step Execution Trace (`xor_all = 6`, binary `0110_2`)
- **Step 1 (Kernighan Clear)**:
  $$\text{xor\_all} = 6 \rightarrow 0110_2$$
  $$\text{xor\_all} - 1 = 5 \rightarrow 0101_2$$
  $$\text{cleared} = 0110_2 \text{ \& } 0101_2 = 0100_2 \quad (\text{decimal: } 4)$$
- **Step 2 (Isolation via XOR)**:
  $$\text{diff\_bit} = \text{cleared} \oplus \text{xor\_all} = 0100_2 \oplus 0110_2 = 0010_2 \quad (\text{decimal: } 2)$$
- **Step 3 (Partitioning)**:
  Applies mask `diff_bit = 2` across `nums` to separate $a$ and $b$ identically to Solution 1.
- **Result**: `[3, 5]`
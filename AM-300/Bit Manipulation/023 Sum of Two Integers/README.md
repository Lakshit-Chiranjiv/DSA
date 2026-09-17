# 371. Sum of Two Integers

## Problem Summary
Calculate the sum of two integers `a` and `b` without using the operators `+` and `-`. The solution must handle signed 32-bit integers, including negative numbers, using bitwise operations.

## My Approach
Simulate binary addition at the bit level just like a hardware Arithmetic Logic Unit (ALU). Split addition into two parallel bitwise operations:
1. **Sum without Carry**: Use XOR (`a ^ b`) to add bits where $1 \oplus 0 = 1$ and $1 \oplus 1 = 0$.
2. **Shifted Carry**: Use AND (`a & b`) to identify where both bits are `1`, and left-shift by 1 (`<< 1`) to carry the overflow over to the next bit position.

Iteratively add the partial sum and the shifted carry until no carries remain (`b == 0`).

## Final Accepted Approach
Use an iterative loop (or tail recursion) maintaining a 32-bit bitmask (`0xFFFFFFFF`) to clamp intermediate states and emulate fixed-width 32-bit signed integer overflow in languages with arbitrary precision like Python.

## All Solutions Explanation
- **Solution 1: Iterative Bitwise ALU Simulation (`while` loop)**: Computes `carry = (a & b) << 1` and `a = a ^ b` inside a loop. Applies a bitmask `0xFFFFFFFF` at each step to drop bits beyond position 31. Terminates when `b == 0` and restores negative values using two's complement decoding if the 31st bit (sign bit) is set.
- **Solution 2: Recursive Bitwise Full Adder**: Replaces the explicit state loop with a recursive call frame, passing `(a ^ b) & mask` as the new partial sum and `((a & b) << 1) & mask` as the new carry until the base case `y == 0` is reached.

## How to Think Toward This Pattern Next Time
When tasked with performing arithmetic without arithmetic operators:
1. Break down grade-school column addition into truth tables.
2. Recognize that $1 + 1 = 0 \text{ (carry 1)}$ maps directly to XOR (`^`) for the partial sum.
3. Recognize that a carry occurs strictly when both bits are $1$, mapping directly to AND (`&`).
4. Shift the carry left by $1$ (`<< 1`) to position it for the next bit column.
5. In dynamically-typed/arbitrary-precision languages (like Python), always clamp operations with a 32-bit mask (`0xFFFFFFFF`) to prevent infinite left-shift on negative numbers.

## Key Observation That Unlocks the Problem
Binary addition is mathematically equivalent to:
$$\text{Sum} = (a \oplus b) + ((a \ \& \ b) \ll 1)$$
By substituting the outer addition `+` with another iteration of the same formula, the process converges in at most 32 steps because the carry mask shifts left on every iteration until `carry == 0`.

## Complexity Comparison
- **Solution 1 (Iterative)**: Time Complexity $O(1)$ (bounded by 32 iterations for 32-bit integers), Space Complexity $O(1)$ auxiliary space.
- **Solution 2 (Recursive)**: Time Complexity $O(1)$ (bounded by 32 recursion steps), Space Complexity $O(1)$ auxiliary space (max 32 call stack frames).

## Similar Problems / Pattern Keywords
- Add Binary
- Add Two Numbers
- Multiply Strings
- Pattern Keywords: Bit Manipulation, Bitwise Full Adder, XOR Partial Sum, Shifted Carry, Two's Complement, 32-Bit Masking

---

## Detailed Explanation and Walkthrough

### Solution 1: Iterative Bitwise ALU Simulation

#### Theoretical Mechanics
A hardware full adder splits bitwise addition into two components:
* **XOR (`^`)**: Computes the sum bit at each column without propagation ($0 \oplus 0 = 0$, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$).
* **AND + Left Shift (`(&) << 1`)**: Computes carries. A carry is generated only when $1 \ \& \ 1 = 1$. The left-shift (`<< 1`) moves the carry bit to the next higher significance column (tens place equivalent in decimal).

In Python, integers have arbitrary precision (infinite width). Negative numbers are represented with infinite leading `1`s in two's complement. Truncating values with `0xFFFFFFFF` enforces 32-bit hardware boundary constraints and prevents infinite loop bit-extension.

#### Algorithm Steps
1. Define mask `0xFFFFFFFF`.
2. While carry `b != 0`:
   - Compute `carry = (a & b) << 1`.
   - Update `a = (a ^ b) & mask` (partial sum clamped to 32 bits).
   - Update `b = carry & mask` (carry clamped to 32 bits).
3. If `a <= 0x7FFFFFFF`, return `a` (positive integer).
4. Otherwise, return `~(a ^ mask)` to decode the 32-bit signed two's complement representation back to Python's negative integer format.

#### Step-by-Step Execution Trace (`a = 5` [`0101_2`], `b = 7` [`0111_2`])
- **Iteration 1**:
  $$\text{carry} = (0101_2 \text{ \& } 0111_2) \ll 1 = 0101_2 \ll 1 = 1010_2 \quad (\text{decimal: } 10)$$
  $$a = 0101_2 \oplus 0111_2 = 0010_2 \quad (\text{decimal: } 2)$$
  $$b = 1010_2 \quad (\text{decimal: } 10)$$
- **Iteration 2**:
  $$\text{carry} = (0010_2 \text{ \& } 1010_2) \ll 1 = 0010_2 \ll 1 = 0100_2 \quad (\text{decimal: } 4)$$
  $$a = 0010_2 \oplus 1010_2 = 1000_2 \quad (\text{decimal: } 8)$$
  $$b = 0100_2 \quad (\text{decimal: } 4)$$
- **Iteration 3**:
  $$\text{carry} = (1000_2 \text{ \& } 0100_2) \ll 1 = 0000_2 \ll 1 = 0000_2 \quad (\text{decimal: } 0)$$
  $$a = 1000_2 \oplus 0100_2 = 1100_2 \quad (\text{decimal: } 12)$$
  $$b = 0000_2$$
- **Loop Terminated** (`b == 0`). `a = 12 <= 0x7FFFFFFF`, returns `12`.

---

### Solution 2: Recursive Bitwise Full Adder

#### Theoretical Mechanics
Solution 2 expresses the iterative ALU state transitions using functional tail-recursion. The base case occurs when the carry argument evaluates to `0`.

#### Algorithm Steps
1. Define mask `0xFFFFFFFF`.
2. Define helper `add(x, y)`:
   - Base Case: If `y == 0`, return `x`.
   - Recursive Case: Call `add((x ^ y) & mask, ((x & y) << 1) & mask)`.
3. Process result through sign bit checker: `res if res <= 0x7FFFFFFF else ~(res ^ mask)`.

#### Step-by-Step Execution Trace (`a = 2` [`0010_2`], `b = 3` [`0011_2`])
- **Frame 1**: `add(x = 2 [0010_2], y = 3 [0011_2])`
  - Next `x` = `0010 ^ 0011` = `0001_2` ($1$)
  - Next `y` = `(0010 & 0011) << 1` = `0010 << 1` = `0100_2` ($4$)
- **Frame 2**: `add(x = 1 [0001_2], y = 4 [0100_2])`
  - Next `x` = `0001 ^ 0100` = `0101_2` ($5$)
  - Next `y` = `(0001 & 0100) << 1` = `0000 << 1` = `0000_2` ($0$)
- **Frame 3**: `add(x = 5 [0101_2], y = 0)`
  - Base case reached (`y == 0`). Returns `x = 5`.
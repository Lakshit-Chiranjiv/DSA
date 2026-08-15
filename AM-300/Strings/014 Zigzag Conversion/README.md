# LeetCode 6: Zigzag Conversion

## Problem Summary
Given a string `s` and a number of rows `numRows`, arrange the characters of `s` in a zigzag pattern across `numRows` and then read the characters line by line (row by row) to form a new string.

---

## My Approach
Identify the fixed cycle period in the zigzag shape. The outer rows (first and last) follow a constant stride jump, while the middle rows contain an extra intermediate "climbing" character coming from the diagonal stroke of the zigzag pattern.

---

## Final Accepted Approach
Both **Row Simulation (Direction Toggle)** and **Direct Index Math** achieve optimal performance. The **Row Simulation** approach is preferred in interview settings due to its intuitive design and low bug surface area, while **Direct Index Math** achieves the result via pure index arithmetic without auxiliary row buckets.

---

## All Solutions Explanation

### 1. Direct Index Math
This approach calculates the exact index of every character row by row. Each full "V" cycle consists of `cycle = 2 * numRows - 2` steps.
- **First & Last Rows:** Every character in row `r` is separated by exactly `cycle` indices (`i`, `i + cycle`, `i + 2 * cycle`, ...).
- **Middle Rows:** Contains main characters at `i` and intermediate diagonal characters at `i + cycle - 2 * row`.

### 2. Row Simulation (Direction Toggle)
Simulate placing characters into `numRows` separate string buckets, traversing down and up like a bouncing ball.
- Maintain a `curr_row` index initialized to `0` and a `step` variable set to `1` (downward).
- Append each character of `s` to `rows[curr_row]`.
- Reverse the `step` direction (`step = -1` or `step = 1`) whenever `curr_row` reaches the top (`0`) or bottom (`numRows - 1`) boundary.
- Concatenate all row strings at the end.

---

## How to Think Toward This Pattern Next Time
When a problem asks to reorganize a sequence based on visual positions, geometric paths, or multi-row layouts:
1. **Try Simulation First:** Determine if tracking state variables (like index, row, direction flag) simplifies boundary handling.
2. **Look for Modulo / Stride Patterns:** If simulation works, examine whether positions repeat at fixed intervals. If indices repeat every $k$ steps, direct mathematical indexing can skip simulation steps entirely.

---

## Key Observation That Unlocks the Problem
The full cycle of moving down $numRows - 1$ steps and back up $numRows - 1$ steps takes exactly **$2 	imes numRows - 2$** characters. Every row's character placement is strictly periodic based on this cycle length.

---

## Complexity Comparison

| Solution | Time Complexity | Space Complexity | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| **Row Simulation** | $O(N)$ | $O(N)$ | Highly intuitive, zero index math, bug-resistant | Minor overhead creating row strings |
| **Direct Index Math** | $O(N)$ | $O(N)$ | Direct layout, minimal memory allocations | Requires precise formula derivation |

---

## Similar Problems / Pattern Keywords
- **Keywords:** Simulation, String Manipulation, Index Arithmetic, Matrix Traversal
- **Similar Problems:**
  - LeetCode 498: Diagonal Traverse
  - LeetCode 54: Spiral Matrix
  - LeetCode 68: Text Justification

---

## Detailed Explanation & Example Walkthrough of Each Solution

### Detailed Walkthrough: Direct Index Math
Consider `s = "PAYPALISHIRING"` and `numRows = 4`.
- **Cycle size:** $2 	imes 4 - 2 = 6$.

Visual Index Map:
```text
Row 0: P(0)             I(6)             N(12)
Row 1: A(1)       L(5)  S(7)       I(11) G(13)
Row 2: Y(2) A(4)       H(8) R(10)
Row 3: P(3)             I(9)
```

1. **Row 0:** Select indices $0, 6, 12 
ightarrow$ `"PIN"`
2. **Row 1:** Main indices $1, 7, 13$. Diagonal indices at $i + 6 - 2(1) 
ightarrow$ $5, 11$. Combined sequence: $1, 5, 7, 11, 13 
ightarrow$ `"ALSIG"`
3. **Row 2:** Main indices $2, 8$. Diagonal indices at $i + 6 - 2(2) 
ightarrow$ $4, 10$. Combined sequence: $2, 4, 8, 10 
ightarrow$ `"YAHR"`
4. **Row 3:** Select indices $3, 9 
ightarrow$ `"PI"`

Result concatenation: `"PIN" + "ALSIG" + "YAHR" + "PI" = "PAHNAPLSIIGYIR"`

---

### Detailed Walkthrough: Row Simulation
Consider `s = "PAYPALISHIRING"` and `numRows = 3`.
- Initialize `rows = ["", "", ""]`, `curr_row = 0`, `step = 1`.

Step-by-step trace:
1. `'P'` $
ightarrow$ `rows[0] = "P"`, `curr_row` reaches top boundary $0 
ightarrow$ `step = 1`, `curr_row = 1`
2. `'A'` $
ightarrow$ `rows[1] = "A"`, `curr_row = 2`
3. `'Y'` $
ightarrow$ `rows[2] = "Y"`, `curr_row` reaches bottom boundary $2 
ightarrow$ `step = -1`, `curr_row = 1`
4. `'P'` $
ightarrow$ `rows[1] = "AP"`, `curr_row = 0`
5. `'A'` $
ightarrow$ `rows[0] = "PA"`, `curr_row` reaches top boundary $0 
ightarrow$ `step = 1`, `curr_row = 1`
6. `'L'` $
ightarrow$ `rows[1] = "APL"`, `curr_row = 2`
... and so on.

Final row buckets:
- `rows[0]` = `"PAHN"`
- `rows[1]` = `"APLSIIG"`
- `rows[2]` = `"YIR"`

Concatenation result: `"PAHNAPLSIIGYIR"`
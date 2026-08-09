# First Missing Positive

## Problem Summary
Given an unsorted integer array `nums`, find the smallest missing positive integer. The solution must run in O(n) time and use O(1) auxiliary space.

---

## My Approach
1. **Sorting**: Sort the array and iterate from 1 upwards to find the first missing integer.
2. **Marker Array (Hash Set)**: Store all numbers in a Hash Set/Marker array, then check presence starting from 1.

---

## Final Accepted Approach
**Cyclic Sort (In-Place Hashing)**: Map numbers to their corresponding array indices. Place each number `x` (where 1 <= x <= n) at index `x - 1` using in-place swaps.

---

## Key Observation That Unlocks the Problem
For an array of length `n`, the smallest missing positive integer **must** lie in the range `[1, n + 1]`. Thus, the array itself can be repurposed as a hash table where index `i` stores value `i + 1`.

---

## How to Think Toward This Pattern Next Time
- When asked for O(n) time and O(1) space on an array of numbers in range `[1, n]`, think **Cyclic Sort / Index Mapping**.
- Ask: "Can I use the array indices as bucket keys to avoid extra auxiliary space?"

---

## Detailed Solution Explanations & Example Walkthroughs

### Solution 1: Sorting Solution
Sort the input array. Maintain a target pointer starting at 1. Traverse through the sorted elements: if the element equals the target, increment target; if greater, break.

Walkthrough on `[3, 4, -1, 1]`:
- Sorted array: `[-1, 1, 3, 4]`
- `num = -1`: skip
- `num = 1`: target becomes 2
- `num = 3`: 3 > 2, break loop
- Output: 2

sorting solution
time -> O(n log n)
space -> O(1)

---

### Solution 2: Hash Set Solution
Store all array elements in a hash set for O(1) lookups. Increment target counter starting from 1 until target is not present in the set.

Walkthrough on `[3, 4, -1, 1]`:
- Hash set: `{3, 4, -1, 1}`
- Target `1`: present in set
- Target `2`: missing from set -> return 2

hash set solution
time -> O(n)
space -> O(n)

---

### Solution 3: Cyclic Sort Solution
Iterate through the array. While `nums[i]` is in `[1, n]` and `nums[i] != nums[nums[i] - 1]`, swap `nums[i]` with the element at index `nums[i] - 1`. Finally, do a linear scan: the first index `i` where `nums[i] != i + 1` yields answer `i + 1`. If all match, return `n + 1`.

Walkthrough on `[3, 4, -1, 1]` (n = 4):
- `i = 0`: `nums[0] = 3` belongs at index 2 -> swap with `nums[2]` -> array: `[-1, 4, 3, 1]`
- `i = 1`: `nums[1] = 4` belongs at index 3 -> swap with `nums[3]` -> array: `[-1, 1, 3, 4]`
- `nums[1] = 1` belongs at index 0 -> swap with `nums[0]` -> array: `[1, -1, 3, 4]`
- `nums[1] = -1` (invalid, stop swapping)
- `i = 2, 3`: elements already in correct places
- Final Scan: Index 0 has 1 (OK), Index 1 has -1 != 2 -> Answer is 2.

cyclic sort solution
time -> O(n)
space -> O(1)

---

## Complexity Comparison

| Solution | Time Complexity | Space Complexity |
|---|---|---|
| Sorting | O(n log n) | O(1) |
| Hash Set | O(n) | O(n) |
| Cyclic Sort | O(n) | O(1) |

---

## Similar Problems & Pattern Keywords
- **Keywords**: Cyclic Sort, In-Place Hashing, Index Mapping, Array Manipulation
- **Similar Problems**:
  - Find the Duplicate Number (LeetCode 287)
  - Find All Numbers Disappeared in an Array (LeetCode 448)
  - Missing Number (LeetCode 268)
  - Set Mismatch (LeetCode 645)
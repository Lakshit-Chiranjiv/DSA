# LeetCode 189: Rotate Array

## Problem Summary
Rotate an array of `n` elements to the right by `k` steps, where `k` is non-negative. The rotation must be done in-place where possible.

## My Approach
1. **Extra Space:** Slice or loop to move elements from `len(nums) - k` to the end, then `0` to `len(nums) - k`. Correct but takes $O(n)$ space.
2. **Two Pointers:** Place one pointer at start and one at `length - k` and swap until the second pointer reaches the end. *Incorrect: overwrites/misplaces intermediate elements.*

## Final Accepted Approach
The optimal approaches achieve $O(n)$ time and $O(1)$ space. Two standard techniques are the **Reversal Algorithm** and **Cyclic Replacements**.

## Key Observation that Unlocks the Problem
Rotation shifts everything uniformly. Instead of moving elements one by one across boundaries, we can exploit structural symmetries:
* Rotating by `k` means the last `k` elements move to the front, and the first `n - k` move to the back.
* An element at index `i` always lands exactly at `(i + k) % n`.

## All Solutions Explanation

### 1. Reversal Algorithm
* **Core Logic:** Reversing an entire array reverses the global order. If we then reverse the first `k` elements and the remaining `n - k` elements individually, their internal relative order is restored while maintaining the shifted positions.
* **Steps:** 1. Normalize `k = k % n`.
  2. Reverse the entire array.
  3. Reverse the first `k` elements.
  4. Reverse the remaining `n - k` elements.

### 2. Cyclic Replacements
* **Core Logic:** Every element tracks exactly to its target destination index `(i + k) % n`. By displacing the element at the destination and processing the displaced element next, we form a closed cycle.
* **Steps:**
  1. Move the current element to its destination, saving the displaced element.
  2. Follow the chain of displacements until returning to the start index.
  3. If the cycle terminates before all `n` elements are moved, advance the start index by 1 to begin a new cycle. Stop when total elements moved equals `n`.

## Detailed Example Walkthroughs

### Example: `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`

#### Reversal Algorithm Walkthrough
1. **Initial:** `[1, 2, 3, 4, 5, 6, 7]`
2. **Reverse entire array:** `[7, 6, 5, 4, 3, 2, 1]`
3. **Reverse first k (3) elements:** `[5, 6, 7, 4, 3, 2, 1]`
4. **Reverse remaining n-k (4) elements:** `[5, 6, 7, 1, 2, 3, 4]` (Result)

#### Cyclic Replacements Walkthrough
1. **Start at idx 0 (val 1):** Target is `(0+3)%7 = 3`. Put `1` at idx 3, hold displaced `4`.
2. **Process displaced val 4 (from idx 3):** Target is `(3+3)%7 = 6`. Put `4` at idx 6, hold displaced `7`.
3. **Process displaced val 7 (from idx 6):** Target is `(6+3)%7 = 2`. Put `7` at idx 2, hold displaced `3`.
4. **Process displaced val 3 (from idx 2):** Target is `(2+3)%7 = 5`. Put `3` at idx 5, hold displaced `6`.
5. **Process displaced val 6 (from idx 5):** Target is `(5+3)%7 = 1`. Put `6` at idx 1, hold displaced `2`.
6. **Process displaced val 2 (from idx 1):** Target is `(1+3)%7 = 4`. Put `2` at idx 4, hold displaced `5`.
7. **Process displaced val 5 (from idx 4):** Target is `(4+3)%7 = 0`. Put `5` at idx 0. 
8. **Cycle complete:** Returns to idx 0. Total elements moved = 7. (Result: `[5, 6, 7, 1, 2, 3, 4]`)

## Complexity Comparison
* **Reversal Algorithm:** Time: $O(n)$ | Space: $O(1)$
* **Cyclic Replacements:** Time: $O(n)$ | Space: $O(1)$

## How to Think Toward This Pattern Next Time
When asked to shift or rotate elements in linear structures within $O(1)$ space constraints, think of global structural operations like **reversal** or graph-like **cyclic transitions** instead of sequential adjacent swapping.

## Similar Problems / Pattern Keywords
* Rotate String
* Reverse Words in a String
* In-place Array Manipulation
* Cycle-Finding Algorithms
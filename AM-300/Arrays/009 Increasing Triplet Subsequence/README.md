# Increasing Triplet Subsequence

## Problem Summary
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

## My Approach
Iterate through the array, find the absolute smallest element as the first element, and then make subsequent passes to find the second and third elements forward.
* **Why it breaks:** The valid increasing triplet does not necessarily include the global minimum of the entire array.

## Final Accepted Approach
Maintain two variables, `first` and `second`, initialized to infinity. Iterate through the array once:
1. Update `first` if the current number is smaller than or equal to `first`.
2. Update `second` if the current number is greater than `first` but smaller than or equal to `second`.
3. If a number is greater than both, a valid triplet `first < second < num` is found.

Even if `first` is updated to a smaller value *after* `second` is set, `second` still implicitly preserves the knowledge that a valid smaller element existed before it historically.

## Solutions Explanation
* **Linear Scan Greedy Elimination:** A single-pass approach that dynamically narrows down the boundaries for the first two elements of a potential triplet. If any element exceeds both boundaries, the triplet condition is instantly satisfied.

## How to Think Toward This Pattern Next Time
When asked to find an increasing subsequence of a fixed length (like 3) in linear time, avoid checking all combinations or fixing global extrema. Think about tracking the minimal thresholds needed to satisfy the prefix of the subsequence.

## Key Observation That Unlocks the Problem
You do not need to track the exact indices or the exact historical `first` element that paired with `second`. As long as a valid `second` exists, it acts as a gatekeeper: any number greater than `second` completes the triplet because `second` could only have been set if a smaller number appeared before it.

## Complexity Comparison
* **Initial Idea:** O(n^3) or O(n) multiple passes (incorrect tracking) -> Space: O(1)
* **Optimal Linear Scan:** O(n) Time -> Space: O(1)

## Similar Problems / Pattern Keywords
* Longest Increasing Subsequence (LIS)
* Greedy Algorithm
* Single-pass Optimization

## Detailed Explanation and Example Walkthrough

### Linear Scan Greedy Elimination

#### Detailed Explanation
We maintain the smallest (`first`) and second-smallest (`second`) elements found so far that can form the start of an increasing triplet. We greedily keep both values as small as possible to maximize our chances of finding a third, larger element later. 

If we encounter a number smaller than `first`, we update `first`. If we find a number larger than `first` but smaller than `second`, we update `second`. Crucially, if we later find a new `first` that is even smaller than the original one, we can safely update it without clearing `second`. This is because `second` still represents a valid second element anchored to the *old* `first` that appeared before it in the array. If a number arrives that is greater than `second`, it is automatically greater than the old `first` too, validating the triplet condition.

#### Example Walkthrough
Let's trace the array: `nums = [2, 5, 1, 6]`

1. **Initialization:**
   * `first` = infinity
   * `second` = infinity

2. **Processing `num = 2`:**
   * Is `2 <= first` (infinity)? Yes.
   * Update `first = 2`.
   * State: `first = 2`, `second = infinity`.

3. **Processing `num = 5`:**
   * Is `5 <= first` (2)? No.
   * Is `5 <= second` (infinity)? Yes.
   * Update `second = 5`.
   * State: `first = 2`, `second = 5`. 
   * *Meaning:* We have a valid pair `[2, 5]`.

4. **Processing `num = 1`:**
   * Is `1 <= first` (2)? Yes.
   * Update `first = 1`.
   * State: `first = 1`, `second = 5`.
   * *Meaning:* `second` remains 5 because 5 still has the historical `2` before it. The new `first = 1` prepares us for an even better potential triplet later.

5. **Processing `num = 6`:**
   * Is `6 <= first` (1)? No.
   * Is `6 <= second` (5)? No.
   * Since `6` is greater than both `first` and `second`, we have found our third element. 
   * Return `True`. (The historical triplet was `2 -> 5 -> 6`).
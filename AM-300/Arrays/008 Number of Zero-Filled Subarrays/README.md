# Number of Zero-Filled Subarrays

### Problem Summary
Given an integer array `nums`, return the third-party number of subarrays filled with `0`. A subarray is a contiguous non-empty sequence of elements within an array.

### My Approach
Iterate through the array to find contiguous groups of zeros, count their lengths, and calculate the sum of natural numbers up to that length for each group. Add these values to a global tracker.

### Final Accepted Approach
A highly optimized single-pass linear scan that maintains a running count of current consecutive zeros (`current_run`). For every zero encountered, increment `current_run` and immediately add its value to `total_subarrays`. Reset `current_run` to zero whenever a non-zero element is encountered.

### All Solutions Explanation
- **Linear Scan with Running Sum**: Instead of waiting for a contiguous run of zeros to end and applying the formula `n * (n + 1) // 2`, we incrementally add the size of the expanding run at each step. If a zero is appended to a run of length `k`, it creates exactly `k + 1` new zero-filled subarrays ending at that position.

### How to Think Toward This Pattern Next Time
When asked to count contiguous subarrays satisfying a condition, think about how the total count changes as you extend the window or list by one element. If the current element maintains the valid property, the number of new valid subarrays ending at the current index is exactly equal to the length of the current valid window.

### Key Observation That Unlocks the Problem
Adding a valid element to a valid window of size `k` introduces exactly `k + 1` new valid subarrays. This eliminates the need for post-processing mathematical formulas or multi-pass checks.

### Complexity Comparison
- **Linear Scan with Running Sum**: Time complexity is O(n), space complexity is O(1).

### Similar Problems / Pattern Keywords
- **Keywords**: Contiguous subarrays, linear scan, sliding window, math progression.
- **Similar Problems**:
  - LeetCode 413: Arithmetic Slices
  - LeetCode 1513: Number of Substrings With Only 1s
  - LeetCode 2750: Ways to Split Array Into Good Subarrays

### Detailed Explanation and Example Walkthrough
Consider the input `nums = [0, 0, 1, 0, 0, 0]`.

1. `nums[0] = 0`: `current_run` becomes 1. `total_subarrays` increases by 1 (Total = 1).
2. `nums[1] = 0`: `current_run` becomes 2. `total_subarrays` increases by 2 (Total = 3).
3. `nums[2] = 1`: Non-zero found. `current_run` resets to 0.
4. `nums[3] = 0`: `current_run` becomes 1. `total_subarrays` increases by 1 (Total = 4).
5. `nums[4] = 0`: `current_run` becomes 2. `total_subarrays` increases by 2 (Total = 6).
6. `nums[5] = 0`: `current_run` becomes 3. `total_subarrays` increases by 3 (Total = 9).

The algorithm returns 9 without any extra storage or division operations.
# Product of Array Except Self

## Problem Summary
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The solution must run in O(n) time and without using the division operation.

## My Approach
The initial approach uses two separate arrays to store prefix products (cumulative product of elements to the left) and suffix products (cumulative product of elements to the right). The final value for each index is computed by multiplying the corresponding prefix and suffix values.

## Final Accepted Approach
The final approach optimizes space to O(1) by reusing the output array. It first fills the output array with the prefix products. Then, it traverses backward, maintaining a single rolling variable to calculate and multiply the suffix products on the fly directly into the output array.

## All Solutions Explanation
- **Two-Pass Prefix-Suffix Array:** Allocates two auxiliary arrays of size n. One tracks left-to-right cumulative products, and the other tracks right-to-left cumulative products. The result is the element-wise multiplication of these two arrays.
- **Space-Optimized Accumulator:** Eliminates auxiliary storage. The output array acts as the prefix tracker. A single integer variable updates cumulative suffix products from right to left, multiplying into the output array inline.

## How to Think Toward This Pattern Next Time
When a problem requires combining information from all elements except the current one, and division is prohibited or dangerous (due to zeros), look to isolate the left and right halves. Splitting a global property into two independent directional accumulations (Prefix and Suffix) resolves the item exclusion.

## Key Observation That Unlocks the Problem
Any element's total product except itself is exactly `(Product of all elements to its left) * (Product of all elements to its right)`.

## Complexity Comparison
- **Two-Pass Prefix-Suffix Array:** Time O(n), Space O(n)
- **Space-Optimized Accumulator:** Time O(n), Space O(1) (excluding output array)

## Similar Problems / Pattern Keywords
- Prefix Sum / Prefix Product
- Trapping Rain Water
- Left and Right Passes
- Subarray/Window Accumulation

## Detailed Explanation and Example Walkthrough

### Two-Pass Prefix-Suffix Array Walkthrough
For `nums = [1, 2, 3, 4]`:
1. Build Prefix: `[1, 1, 2, 6]` (prefix of index i is product up to i-1).
2. Build Suffix: `[24, 12, 4, 1]` (suffix of index i is product from i+1 to end).
3. Combine: `res[i] = prefix[i] * suffix[i]` giving `[24, 12, 8, 6]`.

### Space-Optimized Accumulator Walkthrough
For `nums = [1, 2, 3, 4]`:
1. Fill output array with prefix products: `res = [1, 1, 2, 6]`.
2. Iterate backward maintaining `suffix = 1`:
   - i = 3: `res[3] *= 1 -> 6`, update `suffix = 1 * 4 = 4`.
   - i = 2: `res[2] *= 4 -> 8`, update `suffix = 4 * 3 = 12`.
   - i = 1: `res[1] *= 12 -> 12`, update `suffix = 12 * 2 = 24`.
   - i = 0: `res[0] *= 24 -> 24`, update `suffix = 24 * 1 = 24`.
3. Final `res = [24, 12, 8, 6]`.
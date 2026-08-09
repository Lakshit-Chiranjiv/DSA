# LeetCode 26: Remove Duplicates from Sorted Array

### Problem Summary
Given an integer array sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return the number of unique elements.

### Final Accepted Approach
The problem requires modifying the array in-place with O(1) extra space. The standard and optimal pattern for this requirement is the Two-Pointer Overwrite technique. A slow pointer tracks the position of the last confirmed unique element, while a fast pointer scans the array to find new unique elements. When a new unique element is found, the slow pointer advances and the value is overwritten.

### All Solutions Explanation
1. Two-Pointer Overwrite: Initialize a slow pointer at index 0 and iterate a fast pointer from index 1 to the end of the array. At each step, compare the element at the fast pointer with the element at the slow pointer. If they are different, it means a new unique element has been discovered. Increment the slow pointer and copy the fast pointer's value to this new position. Once the iteration completes, the number of unique elements is the slow pointer index plus one.

### How to Think Toward This Pattern Next Time
When a problem asks for in-place modifications or filtering of a sorted linear structure under strict space constraints, think of a two-pointer read-write layout. One pointer acts as a scanner (reader) and the other acts as a boundary marker for the valid prefix (writer).

### Key Observation That Unlocks the Problem
Because the input array is already sorted, all duplicate elements are guaranteed to be adjacent. This means you only ever need to compare the current scanning element with the last placed unique element to determine if it is a duplicate.

### Complexity Comparison
- Two-Pointer Overwrite: Time complexity is O(n) because it requires a single linear scan through the array. Space complexity is O(1) because the modifications are performed entirely in-place without allocating extra data structures.

### Similar Problems and Pattern Keywords
- Keywords: Two-pointer, in-place modification, fast and slow runners, array deduplication.
- Similar Problems: LeetCode 27 (Remove Element), LeetCode 80 (Remove Duplicates from Sorted Array II), LeetCode 283 (Move Zeroes).

### Detailed Explanation and Example Walkthrough
Consider the input array: nums = [1, 1, 2]

1. Initialization:
   - Slow pointer starts at index 0 (value 1).
   - Fast pointer starts at index 1 (value 1).

2. Step 1:
   - Compare nums[slow] (1) and nums[fast] (1).
   - They are equal, so it is a duplicate.
   - Move fast pointer to index 2. Slow pointer remains at index 0.

3. Step 2:
   - Compare nums[slow] (1) and nums[fast] (2).
   - They are not equal, so a new unique element is found.
   - Increment slow pointer to index 1.
   - Copy nums[fast] to nums[slow]. The array becomes [1, 2, 2].
   - Move fast pointer to index 3 (ends the loop).

4. Termination:
   - The loop finishes because the fast pointer reaches the end of the array.
   - Return slow pointer + 1, which equals 2. The first two elements of the array contain the unique values [1, 2].
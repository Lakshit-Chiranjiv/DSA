# LeetCode 283: Move Zeroes

## Problem Summary

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. The operation must be done in-place without making a copy of the array.

## My Approach

Name: Two-Pass Overwrite with Boundary Tracking
Counted the total number of zeros first to compute the total number of non-zero elements. Used a write pointer to overwrite non-zero elements from the beginning, and kept track of the non-zeros written so far. Zeros were written back into the array using a boundary check condition based on the computed counts.

## Final Accepted Approach

Name: Single-Pass Two-Pointer Swap
Maintained a write pointer starting at index 0. Iterated through the array with a read pointer. Whenever a non-zero element was found, swapped the elements at the write pointer and read pointer, then moved the write pointer forward. This automatically pushes all zeros to the right without needing a second pass or extra count variables.

## All Solutions Explanation

1. Two-Pass Overwrite with Boundary Tracking: Counts zeros first to know exactly how many non-zeros exist. Iterates again to shift non-zeros forward and overwrites trailing positions with zero based on index boundaries.
2. Single-Pass Two-Pointer Swap: Processes elements in a single scan. Non-zero elements are swapped with the element at the current write position, which is guaranteed to be a zero or the element itself, collecting all zeros naturally behind the write pointer.

## How to Think Toward This Pattern Next Time

When asked to modify an array in-place while retaining the relative order of a specific subset of elements (like non-zeros), think of it as a partitioning problem. Instead of managing multiple counting variables or figuring out when to overwrite values, use two pointers moving at different speeds: one to scan the elements (read pointer) and one to mark the destination for valid elements (write pointer).

## Key Observation That Unlocks the Problem

Instead of finding where the zeros should go, focus entirely on where the non-zero elements belong. Swapping a non-zero element with the first available zero slot guarantees that zeros naturally accumulate on the right side while preserving the relative sequence of all other numbers.

## Complexity Comparison

Two-Pass Overwrite with Boundary Tracking:
Time: O(N)
Space: O(1)

Single-Pass Two-Pointer Swap:
Time: O(N)
Space: O(1)

## Similar Problems / Pattern Keywords

* Two-Pointer Technique
* Array Partitioning
* Remove Element (LeetCode 27)
* Apply Operations to an Array (LeetCode 2460)

---

## Detailed Breakdown: Two-Pass Overwrite with Boundary Tracking

### 1. Core Logic & Algorithm

This approach solves the problem in two distinct sequential phases:

1. Counting Phase: Scan the entire array to count the number of zeroes. This allows us to calculate exactly how many non-zero elements are in the array (total_non_zeroes = len(nums) - num_of_zeroes).
2. Placement & Overwrite Phase: Loop through the array a second time. Use a non_zero_ptr to copy non-zero elements forward. To handle the remaining zeroes, check if the current loop index i has passed the total_non_zeroes boundary. If it has, overwrite that index with 0.

### 2. Comprehensive Example Walkthrough

Input: nums = [0, 1, 0, 3, 12]

Phase 1: Counting

* Scan through nums:
* nums[0] = 0 -> num_of_zeroes = 1
* nums[1] = 1
* nums[2] = 0 -> num_of_zeroes = 2
* nums[3] = 3
* nums[4] = 12


* Calculations: num_of_zeroes = 2, total_non_zeroes = 5 - 2 = 3

Phase 2: Execution Loop
Initialize non_zero_ptr = 0, non_zeroes_till_now = 0. Loop variable i goes from 0 to 4.

* i = 0: nums[0] = 0
* Condition nums[i] != 0 is False. No placement happens.
* State: [0, 1, 0, 3, 12], non_zero_ptr = 0


* i = 1: nums[1] = 1
* Condition nums[1] != 0 and 0 < 3 is True.
* Action: nums[non_zero_ptr] = nums[1] -> nums[0] = 1
* Increment: non_zero_ptr = 1, non_zeroes_till_now = 1
* Check boundary: i >= total_non_zeroes (1 >= 3) is False.
* State: [1, 1, 0, 3, 12], non_zero_ptr = 1


* i = 2: nums[2] = 0
* Condition nums[i] != 0 is False.
* State: [1, 1, 0, 3, 12], non_zero_ptr = 1


* i = 3: nums[3] = 3
* Condition nums[3] != 0 and 1 < 3 is True.
* Action: nums[non_zero_ptr] = nums[3] -> nums[1] = 3
* Increment: non_zero_ptr = 2, non_zeroes_till_now = 2
* Check boundary: i >= total_non_zeroes (3 >= 3) is True. Overwrite nums[3] = 0.
* State: [1, 3, 0, 0, 12], non_zero_ptr = 2


* i = 4: nums[4] = 12
* Condition nums[4] != 0 and 2 < 3 is True.
* Action: nums[non_zero_ptr] = nums[4] -> nums[2] = 12
* Increment: non_zero_ptr = 3, non_zeroes_till_now = 3
* Check boundary: i >= total_non_zeroes (4 >= 3) is True. Overwrite nums[4] = 0.
* State: [1, 3, 12, 0, 0], non_zero_ptr = 3



Final output: [1, 3, 12, 0, 0]

### 3. Edge Cases Covered

* All Zeroes ([0, 0, 0]): total_non_zeroes becomes 0. The write conditions are never triggered, and the boundary condition i >= 0 fills everything correctly back to 0.
* No Zeroes ([1, 2, 3]): total_non_zeroes matches array length. Elements copy over onto themselves, and the boundary zero overwrite condition is never met because i never equals or exceeds the length.
* Single Element ([0] or [1]): Handled smoothly as boundary checks match exact lengths.

Two-Pass Overwrite with Boundary Tracking
time -> O(N)
space -> O(1)

---

## Detailed Breakdown: Single-Pass Two-Pointer Swap

### 1. Core Logic & Algorithm

This approach processes the array using the Partitioning pattern in a single continuous scan.
Two pointers are maintained:

1. write_ptr: Points to the location where the next non-zero element must be placed.
2. read_ptr: Scans the array sequentially from left to right.

Whenever nums[read_ptr] encounters a non-zero element, it is immediately swapped with nums[write_ptr].

* If write_ptr and read_ptr are at the same index, the element swaps with itself (no operational change).
* If write_ptr lags behind, it is always guaranteed to be sitting on a zero element. Swapping pushes the non-zero forward and automatically bubbles the zero backward to the read_ptr position.

### 2. Comprehensive Example Walkthrough

Input: nums = [0, 1, 0, 3, 12]

Initialize write_ptr = 0. Loop variable read_ptr ranges from 0 to 4.

* read_ptr = 0: nums[0] = 0
* Element is zero, do nothing.
* State: [0, 1, 0, 3, 12], write_ptr = 0


* read_ptr = 1: nums[1] = 1
* Element is non-zero. Swap nums[write_ptr] and nums[read_ptr] (nums[0] and nums[1]).
* Action: Swap 0 and 1.
* Increment: write_ptr = 1
* State: [1, 0, 0, 3, 12], write_ptr = 1


* read_ptr = 2: nums[2] = 0
* Element is zero, do nothing.
* State: [1, 0, 0, 3, 12], write_ptr = 1


* read_ptr = 3: nums[3] = 3
* Element is non-zero. Swap nums[write_ptr] and nums[read_ptr] (nums[1] and nums[3]).
* Action: Swap 0 and 3.
* Increment: write_ptr = 2
* State: [1, 3, 0, 0, 12], write_ptr = 2


* read_ptr = 4: nums[4] = 12
* Element is non-zero. Swap nums[write_ptr] and nums[read_ptr] (nums[2] and nums[4]).
* Action: Swap 0 and 12.
* Increment: write_ptr = 3
* State: [1, 3, 12, 0, 0], write_ptr = 3



Final output: [1, 3, 12, 0, 0]

### 3. Edge Cases Covered

* All Zeroes ([0, 0, 0]): read_ptr never finds a non-zero element. write_ptr stays at 0. No swaps occur. Array remains [0, 0, 0].
* No Zeroes ([1, 2, 3]): Every element is non-zero. write_ptr and read_ptr increment together at every step, swapping elements with themselves. No zeros are introduced.
* Single Element ([0]): Code safely completes the single iteration loop without throwing pointer exceptions.

Single-Pass Two-Pointer Swap
time -> O(N)
space -> O(1)
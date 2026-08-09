# LeetCode 169: Majority Element

### Problem Summary

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### My Approach

Implemented the Boyer-Moore Voting Algorithm using `res` and `majority` tracking variables to find the element that remains after canceling out opposing choices.

### Final Accepted Approach

The Boyer-Moore Voting Algorithm. It maintains a candidate and a counter, incrementing when the current number matches the candidate and decrementing otherwise. If the counter hits zero, a new candidate is selected.

### All Solutions Explanation

* **Boyer-Moore Voting Algorithm**: Uses a single pass to cancel out pairs of distinct elements. The majority element always survives because it occupies more than half of the array positions.
* **Hash Map Counter (Alternative)**: Counts frequencies of all elements using a hash map and returns the one with a count > ⌊n / 2⌋.
* **Sorting (Alternative)**: Sorts the array and returns the element at index `n // 2`, as the majority element must occupy the middle position.

### How to Think Toward This Pattern Next Time

When a problem asks for an element that dominates a collection by a strict majority (> 50%), think of a pairing/canceling mechanism instead of counting everything. Visualizing the problem as an elimination game where opposing elements destroy each other helps identify that the majority item will always be the last one standing.

### Key Observation That Unlocks the Problem

The majority element appears more times than all other elements combined. Therefore, if you pair up different elements and remove them, the majority element will always be part of the remaining unpaired elements.

### Complexity Comparison

* **Boyer-Moore Voting Algorithm**: Time O(n), Space O(1)
* **Hash Map Counter**: Time O(n), Space O(n)
* **Sorting**: Time O(n log n), Space O(1) or O(n) depending on the sorting algorithm

### Similar Problems / Pattern Keywords

* LeetCode 229: Majority Element II (Boyer-Moore with multiple candidates)
* Keywords: Boyer-Moore, Voting Algorithm, Streaming Majority, Frequency Cancellation

---

### Detailed Walkthrough & Core Logic Deep Dive

#### Core Intuition

Imagine an arena where each distinct number represents a different army faction. If two soldiers from different factions clash, they both eliminate each other. Because the majority faction has more soldiers than **all other factions combined**, even if every single minority soldier teams up against the majority faction, the minority armies will completely run out of soldiers first. The lone faction standing at the end is guaranteed to be the majority.

#### Step-by-Step Code Traversal

* **Empty Throne (`count == 0`)**: If `count` drops to 0, it means all previous elements have completely neutralized each other. The current element `num` instantly becomes the new leading `candidate`.
* **Reinforcement**: If `num == candidate`, the current faction gets stronger (`count += 1`).
* **Elimination**: If `num != candidate`, a clash occurs and both drop out (`count -= 1`).

#### Detailed Edge Case Walkthroughs

**Case 1: Minority Elements Clumped Early (`nums = [1, 1, 1, 2, 2, 2, 2]`)**

* `num = 1`: `count` drops to 0 initially, so `candidate` becomes 1. After three `1`s, `candidate = 1, count = 3`.
* `num = 2`: The incoming `2`s systematically fight the existing `1`s. `count` steadily decrements: $3 \rightarrow 2 \rightarrow 1 \rightarrow 0$.
* Final `num = 2`: At index 6, `count` hits 0. The final `2` claims the empty throne (`candidate = 2, count = 1`).
* **Result**: `2` wins.

**Case 2: Interleaved Alternating Array (`nums = [2, 1, 2, 1, 2]`)**

* `num = 2` $\rightarrow$ `candidate = 2, count = 1`
* `num = 1` $\rightarrow$ Clashes! `count` drops to 0. (Throne is cleared)
* `num = 2` $\rightarrow$ Throne is empty, so `candidate = 2, count = 1`
* `num = 1` $\rightarrow$ Clashes! `count` drops to 0. (Throne is cleared)
* `num = 2` $\rightarrow$ Throne is empty, so `candidate = 2, count = 1`
* **Result**: `2` wins.
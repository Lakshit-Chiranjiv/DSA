# LeetCode 392: Is Subsequence

## Problem Summary
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

## My Approach
Two-pointer scan where one pointer tracks progress in `s` and the other iterates through `t`. If a character matches, advance the pointer in `s`. If `s`'s pointer reaches the end of `s`, return true.

## Final Accepted Approach
Two Pointers approach. Since we only need to preserve relative ordering, matching greedily from left to right using two pointers guarantees correctness in a single pass.

## Solutions Explanation

### Two Pointers (Greedy Matching)
Initialize pointer `i` at index 0 of `s` and pointer `j` at index 0 of `t`. Iterate `j` across all characters in `t`. Whenever `s[i] == t[j]`, increment `i` to move to the next target character in `s`. The loop terminates early if `i` reaches `len(s)` or when `j` exhausts `t`. Return `true` if `i == len(s)`, else `false`.

#### Example Walkthrough:
s = "abc", t = "ahbgdc"
- Step 1: i=0 ('a'), j=0 ('a') -> Match! Advance i to 1, j to 1.
- Step 2: i=1 ('b'), j=1 ('h') -> No match. Advance j to 2.
- Step 3: i=1 ('b'), j=2 ('b') -> Match! Advance i to 2, j to 3.
- Step 4: i=2 ('c'), j=3 ('g') -> No match. Advance j to 4.
- Step 5: i=2 ('c'), j=4 ('d') -> No match. Advance j to 5.
- Step 6: i=2 ('c'), j=5 ('c') -> Match! Advance i to 3, j to 6.
- i == len(s) (3 == 3) -> Return True.

### Follow-up Variant: Binary Search (Precomputed Hash Map)
If there are multiple incoming `s` strings to check against a fixed large string `t`, precompute a hash map storing the indices of each character in `t` in ascending order. For each character in `s`, use binary search (`bisect_right`) on the stored index list to find the next valid index in `t` strictly greater than the previously matched index.

#### Example Walkthrough:
t = "ahbgdc" -> map = {'a': [0], 'h': [1], 'b': [2], 'g': [3], 'd': [4], 'c': [5]}
s = "abc"
- Target 'a': smallest index > -1 is 0. Current position = 0.
- Target 'b': smallest index > 0 in [2] is 2. Current position = 2.
- Target 'c': smallest index > 2 in [5] is 5. Current position = 5.
- All characters matched in increasing order -> Return True.

## How to Think Toward This Pattern Next Time
When checking order-preserving properties between two linear sequences where element deletion is allowed, think **Greedy Matching with Two Pointers**. The earliest valid match for a character never restricts future matches compared to a later match.

## Key Observation That Unlocks the Problem
Greedy selection works: matching the earliest possible occurrence of `s[i]` in `t` leaves the maximum remaining prefix of `t` to match the rest of `s`.

## Complexity Comparison
- Two Pointers: Time O(N), Space O(1) [N = length of t]
- Precomputed Binary Search (Follow-up): Time O(N + M log N), Space O(N) [N = len(t), M = len(s)]

## Similar Problems / Pattern Keywords
- Two Pointers
- Greedy
- Binary Search
- String Matching
- LC 1055: Shortest Way to Form String
- LC 792: Number of Matching Subsequences
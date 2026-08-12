# Longest Common Prefix

## Problem Summary
Find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

## My Approach
Vertical scanning: matching characters column-wise across all strings simultaneously until a mismatch occurs.

## Final Accepted Approach
Vertical Scanning (or Python Zip Character Match). Both operate in O(S) time where S is the total number of characters across all strings.

## All Solutions Explanation
1. Vertical Scanning: Compare characters index by index using the first string as benchmark. Stop at the first mismatch or length boundary.
2. Python Zip Character Match: Transpose strings into tuples of corresponding index characters using `zip(*strs)` and check uniformity using sets.

## How to Think Toward This Pattern Next Time
When searching for aligned prefix properties across multiple strings, scan vertically (character by character across strings) rather than horizontally (string by string) to terminate early at the first mismatch.

## Key Observation that Unlocks the Problem
A prefix fails as soon as a single string differs at index `i`. Vertical scanning allows immediate termination without processing remaining strings or characters.

## Complexity Comparison
| Solution | Time Complexity | Space Complexity |
| --- | --- | --- |
| Vertical Scanning | O(S) | O(1) |
| Python Zip Character Match | O(S) | O(1) |

*(where S is the total number of characters in all strings)*

## Similar Problems / Pattern Keywords
- Vertical Scanning
- String Alignment
- Trie
- Longest Common Subsequence / Prefix

## Detailed Explanation and Example Walkthrough

### Solution 1: Vertical Scanning
- **Explanation:** Loop through each character index of the first string. For each index, iterate through all other strings to check if they match the character. Return the prefix immediately upon any mismatch or boundary overflow.
- **Example Walkthrough:** `strs = ["flower", "flow", "flight"]`
  - Index 0: 'f', 'f', 'f' -> Match
  - Index 1: 'l', 'l', 'l' -> Match
  - Index 2: 'o' ("flower"), 'o' ("flow"), 'i' ("flight") -> Mismatch at 'i'
  - Return prefix: "fl"

### Solution 2: Python Zip Character Match
- **Explanation:** Use `zip(*strs)` to tuple-wise inspect characters at matching positions across all strings. Convert each tuple to a set; if set size is 1, all strings share the character at that position.
- **Example Walkthrough:** `strs = ["flower", "flow", "flight"]`
  - Tuple 1: ('f', 'f', 'f') -> Set size 1 -> Keep 'f'
  - Tuple 2: ('l', 'l', 'l') -> Set size 1 -> Keep 'l'
  - Tuple 3: ('o', 'o', 'i') -> Set size 2 -> Stop
  - Result: "fl"
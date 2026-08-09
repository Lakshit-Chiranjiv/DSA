# Valid Palindrome - LeetCode 125

## Problem Summary
Determine if a given string is a valid palindrome, considering only alphanumeric characters and ignoring cases.

## My Approach
Convert string to lowercase and remove spaces using join, then check if string equals its reverse. 
*Status:* Incorrect because it fails to strip non-alphanumeric punctuation/symbols.

## Final Accepted Approach
Two-pointer approach traversing from both ends inward, skipping non-alphanumeric characters and comparing characters case-insensitively in O(1) extra space.

## All Solutions Explanation
1. Filter & Reverse: Extract all alphanumeric characters into a list/string in lowercase, then compare with its reverse. Uses O(N) extra space.
2. Two Pointers In-Place: Use left and right pointers starting at opposite ends. Skip non-alphanumeric characters dynamically and compare matching characters. Uses O(1) extra space.

## Detailed Explanation & Example Walkthrough

### Filter & Reverse Section
- Explanation: Iterate through the string, filtering out any character where `isalnum()` is False, converting valid characters to lower case into a new array. Check if the array equals its reverse.
- Walkthrough: `s = "A man, a plan, a canal: Panama!"`
  1. Filter & Lowercase -> `['a','m','a','n','a','p','l','a','n','a','c','a','n','a','l','p','a','n','a','m','a']`
  2. Reversed array is identical.
  3. Return `True`.

### Two Pointer In-Place Section
- Explanation: Maintain `left = 0` and `right = len(s) - 1`. Increment `left` while `s[left]` is not alphanumeric. Decrement `right` while `s[right]` is not alphanumeric. Compare `s[left].lower()` with `s[right].lower()`. If unequal, return `False`. Move both pointers inward and repeat until `left >= right`.
- Walkthrough: `s = "A man, a plan, a canal: Panama!"`
  1. `left` starts at 'A', `right` starts at '!'
  2. Move `right` back past '!' to 'a'
  3. Compare 'a' and 'a' -> Match. Increment `left`, decrement `right`.
  4. Continue skipping non-alphanumeric characters (spaces, commas, colons) and matching valid letters.
  5. Pointers cross without mismatch -> Return `True`.

## Key Observation That Unlocks the Problem
Palindromes are symmetric around their center. By filtering out noise (non-alphanumeric characters) on the fly, we can validate symmetry in a single pass without extra memory.

## How to Think Toward This Pattern Next Time
When checking symmetric properties or pairs in a linear data structure (strings/arrays) where skipping invalid elements is allowed, immediately think of the Two-Pointer pattern (converging from opposite ends).

## Complexity Comparison
- Filter & Reverse: Time O(N), Space O(N)
- Two Pointer In-Place: Time O(N), Space O(1)

## Similar Problems / Pattern Keywords
- Two Pointers, String Manipulation, In-Place Traversal
- Valid Palindrome II
- Palindrome Linked List
- Reverse String
# LeetCode 151: Reverse Words in a String

## Problem Summary

Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space, with no leading or trailing spaces.

## My Approach

Use Python's built-in string manipulation functions to split the string into words, reverse the list of words, and join them back with a single space.

## Final Accepted Approach

The built-in split and join approach is already optimal for Python ($O(N)$ time and space). For low-level or strict space-constraint requirements, the two-pointer string inversion pattern achieves the result manually without using high-level string split built-ins.

---

## Solutions Detailed Breakdown

### 1. Built-in Split and Join (`reverseWords_split_and_join`)

#### Explanation

1. `s.split()` automatically trims leading/trailing whitespace and splits the string by sequences of multiple spaces into a list of words.
2. `reversed(...)` reverses the list of extracted word tokens.
3. `" ".join(...)` joins the reversed list of words back into a single string separated by a single space.

#### Example Walkthrough

Input: `s = "  the sky  is blue  "`

1. `s.split()` $\rightarrow$ `['the', 'sky', 'is', 'blue']`
2. `reversed(...)` $\rightarrow$ `['blue', 'is', 'sky', 'the']`
3. `" ".join(...)` $\rightarrow$ `"blue is sky the"`

---

### 2. Manual Two-Pointer Inversion (`reverseWords_manual_two_pointer_inversion`)

#### Explanation

1. **Clean Whitespace:** Iterate through the string using a index pointer and build a clean character array with single spaces between words, skipping leading, trailing, and duplicate spaces.
2. **Global Reversal:** Reverse the entire character array in-place using two pointers (`left` and `right`). This puts the words in their correct relative positions but leaves individual words spelled backwards.
3. **Local Reversal:** Iterate through the array to locate word boundaries (space or end of array), then reverse each word back to restore proper character order.
4. **Output:** Join the character array into a final string.

#### Example Walkthrough

Input: `s = "  the sky  is blue  "`

1. Clean Whitespace: `chars = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']`
2. Reverse Entire Array: `chars = ['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']`
3. Reverse Each Word:
* Word 1 (`"eulb"`): $\rightarrow$ `"blue"`
* Word 2 (`"si"`): $\rightarrow$ `"is"`
* Word 3 (`"yks"`): $\rightarrow$ `"sky"`
* Word 4 (`"eht"`): $\rightarrow$ `"the"`
* Result: `chars = ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']`


4. Join: `"blue is sky the"`

---

## Pattern & Key Observations

### Key Observation That Unlocks The Problem

Reversing a sequence of words in-place without splitting can be achieved via **Double Reversal**: Reversing the full sequence places all words in the target order, but flips individual word spellings. A second pass reversing each word independently fixes the individual spellings.

### How to Think Toward This Pattern Next Time

* When asked to reverse order at a macro level (words in sentence) while preserving order at a micro level (characters in word), think **Global Flip + Local Flip**.
* When asked to manipulate string tokens without using library helpers, use a **Two-Pointer Scan** to identify token boundaries.

---

## Complexity Comparison

| Solution | Time Complexity | Auxiliary Space |
| --- | --- | --- |
| Built-in Split & Join | $O(N)$ | $O(N)$ |
| Manual Two-Pointer Inversion | $O(N)$ | $O(N)$ ($O(1)$ in mutable-string languages) |

---

## Keywords & Similar Problems

* **Keywords:** Two-Pointer, String Manipulation, In-Place Reversal, Word Boundaries
* **Similar Problems:**
* Reverse String (LeetCode 344)
* Reverse String II (LeetCode 541)
* Rotate Array (LeetCode 189)
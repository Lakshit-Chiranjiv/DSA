# 843. Guess the Word

## Problem Summary
You are given a list of unique words of length 6 and a hidden secret word from the list. You are provided with a helper API `master.guess(word)` that returns an integer:
- `6` if the guessed word is the secret word.
- `0` to `5` indicating how many characters match the secret word at the exact same position (index).

You have a limited number of guess attempts (typically 10). The goal is to find the secret word within the allowed guesses by strategically selecting candidate words and eliminating invalid options based on API feedback.

## My Approach
Attempt to guess words from the list sequentially or pick candidate words based on feedback. The core realization is that if `master.guess(guessed_word)` returns $k$ matches, any word in the candidate list that does not share **exactly** $k$ character-by-character position matches with `guessed_word` cannot be the secret word and must be filtered out.

## Final Accepted Approach
Both Randomized Match Filtering and Minimax Elimination are valid accepted strategies:
1. **Randomized Match Filtering:** Pick a candidate word randomly from the remaining valid pool, query `master.guess`, and keep only the words that share exactly $k$ matches with the guessed word. Repeat until the secret word ($k = 6$) is found.
2. **Minimax Elimination:** Instead of picking randomly, compute the worst-case remaining candidate pool size for every candidate word across all potential feedback scores ($0$ to $5$). Pick the candidate word that minimizes this maximum remaining pool size.

## All Solutions Explanation

### Solution 1: Randomized Match Filtering
Pick a random word from the active pool of candidates and submit it to `master.guess`. If it returns $k = 6$, the secret is found. Otherwise, iterate through all remaining candidate words in the list and compare each with the guessed word using a helper function that counts exact-position character matches. Filter the candidate pool to retain only those words that yield a match score strictly equal to $k$. Because each non-6 feedback score eliminates a large portion of the candidate pool, random selection converges rapidly to the secret word well within the 10-guess limit.

### Solution 2: Minimax Elimination
For each candidate word $w_1$ in the current pool, simulate what would happen for every possible score $i \in [0, 5]$ by counting how many other candidate words $w_2$ would yield exactly $i$ matches with $w_1$. Find the maximum count across all $i$ for $w_1$, representing the worst-case size of the candidate pool remaining after guessing $w_1$. Choose the word $w_1$ that minimizes this worst-case candidate pool size. Guess this optimal word, receive the actual feedback $k$ from `master.guess`, filter the candidate pool to keep only words matching $w_1$ at exactly $k$ positions, and repeat.

## How to Think Toward This Pattern Next Time
When given an interactive API problem with limited query attempts and exact-match feedback:
- Reframe the feedback as a distance constraint relative to the hidden target.
- Use feedback from each query to aggressively shrink the search space by retaining only candidates consistent with all prior constraints.
- If deterministic guarantees are required, evaluate choices by their capacity to minimize the worst-case set of remaining candidates (Minimax principle).

## Key Observation That Unlocks the Problem
If `master.guess(guessed_word)` returns $k$, the secret word shares **exactly $k$ index matches** with `guessed_word`. Therefore, any candidate word $C$ where `count_matches(guessed_word, C) != k` **cannot** be the secret word, regardless of whether its match count is lower or higher than $k$.

## Complexity Comparison
- **Randomized Match Filtering:**
  - Time Complexity: O(N * L) per step, where N is candidate count and L is word length (6)
  - Space Complexity: O(N)
- **Minimax Elimination:**
  - Time Complexity: O(N^2 * L) per step, where N is candidate count and L is word length (6)
  - Space Complexity: O(N)

## Similar Problems / Pattern Keywords
- Interactive Problems
- Minimax Algorithm
- Candidate Pool Elimination
- String Pair Matching / Hamming Distance

## Detailed Explanation and Example Walkthrough of Each Solution

### Section 1: Randomized Match Filtering Walkthrough
Consider a candidate pool `["acckzz", "ccbazz", "eiowzz", "abcczz"]` with secret `"acckzz"`.

1. **Step 1:** Randomly pick `"ccbazz"`. Call `master.guess("ccbazz")`.
   - Character comparisons between `"ccbazz"` and secret `"acckzz"`:
     - Index 1 (`'c'`), Index 4 (`'z'`), Index 5 (`'z'`) match. Total = 3.
   - `master.guess` returns `3`.

2. **Step 2:** Filter candidate pool using match target `3`:
   - Compare `"acckzz"` with `"ccbazz"` -> 3 matches -> **Keep**.
   - Compare `"eiowzz"` with `"ccbazz"` -> 2 matches -> 2 != 3 -> **Discard**.
   - Compare `"abcczz"` with `"ccbazz"` -> 4 matches -> 4 != 3 -> **Discard**.
   - Updated pool: `["acckzz"]`.

3. **Step 3:** Pick `"acckzz"`. `master.guess` returns `6`. Solved.

### Section 2: Minimax Elimination Walkthrough
Consider a candidate pool `["ABLE", "BEACH", "CHAIR", "DANCE"]`.

1. **Evaluate Candidate 1 (`"ABLE"`):**
   - Count candidates matching at score 0: 3 words (`"BEACH"`, `"CHAIR"`, `"DANCE"`).
   - Worst-case group size for `"ABLE"` = 3.

2. **Evaluate Candidate 2 (`"BEACH"`):**
   - Count candidates matching at score 0: 1 word (`"CHAIR"`).
   - Count candidates matching at score 1: 2 words (`"ABLE"`, `"DANCE"`).
   - Worst-case group size for `"BEACH"` = max(1, 2) = 2.

3. **Minimax Decision:**
   - Compare worst cases: `"ABLE"` (3) vs `"BEACH"` (2).
   - Choose `"BEACH"` because it minimizes the worst-case remaining pool size to 2.

4. **Execute & Filter:** Guess `"BEACH"`, get score $k$, filter candidate list to candidates having exactly $k$ matches with `"BEACH"`, and repeat.
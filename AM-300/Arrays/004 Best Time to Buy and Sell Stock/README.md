# Best Time to Buy and Sell Stock

## Problem Summary
Given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day, maximize profit by choosing a single day to buy one stock and choosing a different day in the future to sell it. Return the maximum profit possible. If no profit can be achieved, return 0.

## My Approach
Assume buying at index 0. If a subsequent index has a higher price, calculate the potential profit and track the maximum. If a lower price than the current buying price is found, update the buying price to this new minimum and continue the evaluation.

## Final Accepted Approach
The optimal strategy uses a single-pass greedy technique. We maintain two tracking states as we iterate through the price sequence: the minimum price observed up to the current step, and the maximum profit achievable by selling at the current price.

## All Solutions Explanation
The solution initializes `min_price` to infinity and `max_profit` to zero. For each price encountered, it performs an updated check: if the price is lower than `min_price`, it updates `min_price`. Otherwise, it calculates the difference between the current price and `min_price` to determine if it exceeds the current `max_profit`.

## How to Think Toward This Pattern Next Time
When required to find an optimal pair of elements preserving a relative order constraint (e.g., index `j > i`), avoid nested loops. Look for ways to track a running state (like a minimum, maximum, or prefix sum) dynamically during a single traversal to evaluate potential solutions instantly.

## Key Observation that Unlocks the Problem
You do not need to know all future prices to make an optimal decision; you only need to know the lowest price seen in the past relative to your current position.

## Complexity Comparison
- One-pass Greedy Solution: Time O(N), Space O(1)

## Similar Problems / Pattern Keywords
- Maximum Subarray (Kadane's Algorithm)
- Best Time to Buy and Sell Stock II
- Two Pointers / Slidng Window
- Greedy Running State

## Detailed Explanation and Example Walkthrough
Consider the input array: `prices = [7, 1, 5, 3, 6, 4]`

1. **Day 1 (Price = 7):** `min_price` becomes 7. `max_profit` remains 0.
2. **Day 2 (Price = 1):** 1 is less than 7. `min_price` updates to 1. `max_profit` remains 0.
3. **Day 3 (Price = 5):** 5 is greater than 1. Potential profit = 5 - 1 = 4. `max_profit` updates to 4.
4. **Day 4 (Price = 3):** 3 is greater than 1. Potential profit = 3 - 1 = 2. `max_profit` remains 4.
5. **Day 5 (Price = 6):** 6 is greater than 1. Potential profit = 6 - 1 = 5. `max_profit` updates to 5.
6. **Day 6 (Price = 4):** 4 is greater than 1. Potential profit = 4 - 1 = 3. `max_profit` remains 5.

Final returned `max_profit` is 5.
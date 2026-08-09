# README.md

## Problem Summary

Given an integer array `prices` where `prices[i]` is the price of a given stock on the $i$-th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and then immediately sell it on the same day. Find and return the maximum profit you can achieve.

## My Approach

A Dynamic Programming approach using a top-down state machine with `@cache`. For each day, we maintain a state of whether we are currently `holding` a stock or not. At each step, we explore two decisions: doing nothing, or executing a transaction (buying if not holding, or selling if holding), to exhaustively discover the maximum possible profit.

## Final Accepted Approach

The optimal approach is a Greedy Algorithm that captures every single consecutive price increment. Instead of tracking complex transaction states over multiple days, we realize that a long-term profit from day $A$ to day $B$ is identical to the sum of daily positive price differences between $A$ and $B$.

## All Solutions Explanation

1. **Top-down Memoization DP**: Tracks the current day index and a boolean flag `holding`. It recursively branches into either holding/selling or waiting, storing results in a memoization table to avoid redundant state calculations.
2. **Greedy Peak-Valley Accumulation**: Iterates through the prices array starting from the second day. If the current day's price is strictly greater than the previous day's price, the profit difference is added directly to the running total.

## How to Think Toward This Pattern Next Time

When a problem allows an arbitrary number of concurrent or consecutive actions, and actions can happen instantly (e.g., buying and selling on the same day), look for a way to decompose a global path into local, independent steps. If local optimal choices (capturing every micro-gain) perfectly aggregate into the global optimal choice, the problem possesses the greedy choice property.

## Key Observation that Unlocks the Problem

Continuous price increases can be broken down into daily increments.
Mathematically, if $P[3] > P[2] > P[1]$, then the profit of buying at Day 1 and selling at Day 3 is $(P[3] - P[1])$, which is exactly equivalent to $(P[2] - P[1]) + (P[3] - P[2])$. Thus, we only need to collect every positive delta between adjacent days.

## Complexity Comparison

* **Top-down Memoization DP**: Time complexity is $O(N)$ because there are $2N$ states to explore. Space complexity is $O(N)$ due to the recursion stack and memoization storage.
* **Greedy Peak-Valley Accumulation**: Time complexity remains $O(N)$ but optimized with a single pass and minimal overhead. Space complexity drops to $O(1)$ because no extra tracking states or call stacks are maintained.

## Similar Problems / Pattern Keywords

* Best Time to Buy and Sell Stock (with variations I, III, IV, Cooldown, Fee)
* Greedy Algorithms
* Peak-Valley Approach
* State Machine DP

## Detailed Explanation and Example Walkthrough

### Section 1: Top-down Memoization DP

#### Explanation

This approach explores the decision tree of the problem at each day. We use two state variables: `i` (the current day index) and `holding` (a boolean indicating whether we currently own a stock).

* If `holding` is False, we can either choose to skip the day (moving to day `i+1` with `holding=False`) or buy the stock (paying `prices[i]` and moving to day `i+1` with `holding=True`).
* If `holding` is True, we can either choose to skip the day (moving to day `i+1` with `holding=True`) or sell the stock (receiving `prices[i]` and moving to day `i+1` with `holding=False`).

The `@cache` decorator ensures that if we reach the same day with the same holding status via different paths, we reuse the precomputed max profit instead of recalculating.

#### Example Walkthrough

Input: `prices = [7, 1, 5, 3, 6, 4]`

* `solve(0, False)`: Day 0 (Price 7). Max of skipping `solve(1, False)` or buying `-7 + solve(1, True)`.
* `solve(1, False)`: Day 1 (Price 1). Max of skipping `solve(2, False)` or buying `-1 + solve(2, True)`.
* `solve(2, True)`: Day 2 (Price 5). Max of skipping `solve(3, True)` or selling `5 + solve(3, False)`.
* ... This branches out. If we decide to buy at Day 1 (-1) and sell at Day 2 (+5), our net profit becomes +4, and we move to `solve(3, False)`.
* At Day 3 (Price 3), we buy (-3) and move to `solve(4, True)`.
* At Day 4 (Price 6), we sell (+6) and move to `solve(5, False)`. Net profit from this transaction is +3.
* Total accumulated profit returning up the recursion tree is 4 + 3 = 7.

### Section 2: Greedy Peak-Valley Accumulation

#### Explanation

Instead of searching for complex combinations of buying and selling across distant days, this approach makes a local decision at every single step. Since you can sell and buy on the same day, any multi-day upward price movement is equal to the sum of its daily increases. We simply loop through the array starting from index 1. If today's price is greater than yesterday's price, we act as if we bought yesterday and sold today, adding that instant profit to our total. If the price drops or stays the same, we ignore it.

#### Example Walkthrough

Input: `prices = [7, 1, 5, 3, 6, 4]`
Initial Profit = 0

* `i = 1`: Price changes from 7 to 1. No increase. Profit = 0.
* `i = 2`: Price changes from 1 to 5. Increase found! Profit += (5 - 1) -> Profit = 4.
* `i = 3`: Price changes from 5 to 3. No increase. Profit = 4.
* `i = 4`: Price changes from 3 to 6. Increase found! Profit += (6 - 3) -> Profit = 4 + 3 = 7.
* `i = 5`: Price changes from 6 to 4. No increase. Profit = 7.

End of loop. Final Return Value = 7.
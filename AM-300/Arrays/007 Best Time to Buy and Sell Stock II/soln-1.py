from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def solve(i: int, holding: bool) -> int:
            if i == len(prices):
                return 0
            
            # Option 1: Do nothing on this day
            profit = solve(i + 1, holding)
            
            if holding:
                # Option 2: Sell the stock
                profit = max(profit, prices[i] + solve(i + 1, False))
            else:
                # Option 2: Buy the stock
                profit = max(profit, -prices[i] + solve(i + 1, True))
                
            return profit
            
        return solve(0, False)

# Top-down Memoization DP
# time -> O(N)
# space -> O(N)
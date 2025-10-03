class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,holding):
            if i >= len(prices):
                return 0
            if (i,holding) in memo:
                return memo[(i,holding)]
            memo[(i,holding)] = max(-prices[i] + dp(i+1,1),dp(i+1,0)) if holding == 0 else max(prices[i] + dp(i+2,0),dp(i+1,1))         
            return memo[(i,holding)]
        return dp(0,0)
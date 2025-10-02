class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i,rem):
            if rem == 0:
                return 0
            if i >= len(coins) or rem < 0:
                return float('inf')
            if (i,rem) in memo:
                return memo[(i,rem)]
            include = 1 + dp(i,rem-coins[i])
            exclude = dp(i+1,rem)
            memo[(i,rem)]= min(include,exclude)
            return memo[(i,rem)]
        res = dp(0,amount)
        return -1 if res == float('inf') else res
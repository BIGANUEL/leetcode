class Solution:
    def __init__(self):
            self.memo = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i >= len(cost):
                return 0
            if i not in self.memo:
                self.memo[i] = cost[i] + min(dp(i+1),dp(i+2))
            return self.memo[i]
        return min(dp(0),dp(1))
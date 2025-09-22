class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(dp(i+1),dp(i+2) + nums[i])
            return memo[i]
        return dp(0)


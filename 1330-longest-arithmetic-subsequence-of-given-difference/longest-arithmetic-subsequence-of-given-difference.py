class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_val = 0

        for num in arr:
            dp[num] = dp.get(num-difference,0) + 1
            max_val = max(max_val,dp[num])
        return max_val
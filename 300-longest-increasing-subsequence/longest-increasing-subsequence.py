class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # dp[i] = length of LIS ending at index i
        dp = [-1] * n
        
        def solve(i):
            if dp[i] != -1:
                return dp[i]
            
            max_len = 1  # Minimum length is 1 (the element itself)
            
            # Check all previous elements that can extend the sequence
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, 1 + solve(j))
            
            dp[i] = max_len
            return dp[i]
        
        # Find maximum LIS ending at each position
        result = 0
        for i in range(n):
            result = max(result, solve(i))
        
        return result
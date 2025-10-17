class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1][:]
        print(dp)
        for i in range(n-2,-1,-1):
            row = triangle[i]
            for j in range(len(row)):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1]) 
        return dp[0]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[]*(m+1) for _ in range(n)]
        memo = {}
        def dp(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if i == m or j == n:
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
            left = dp(i+1,j)
            right = dp(i,j+1)
            memo[(i,j)] = left + right
            return memo[(i,j)]
        return dp(0,0)
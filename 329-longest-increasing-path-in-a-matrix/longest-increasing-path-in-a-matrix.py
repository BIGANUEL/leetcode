class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            
            max_len = 1  # path length at least 1 (itself)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(ni, nj))
            memo[i][j] = max_len
            return max_len
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res

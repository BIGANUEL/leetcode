class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dp(row,col):
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            right = grid[row][col] + dp(row,col + 1)
            down = grid[row][col] + dp(row+1,col)
            memo[(row,col)] = min(right,down)
            return memo[(row,col)]
        return dp(0,0)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(101)]
        dp[0][0] = poured

        for r in range(100):
            for c in range(len(dp[r])):
                if dp[r][c] > 1:
                    overflow = (dp[r][c] - 1) / 2.0
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow
                    dp[r][c] = 1  

        return min(1, dp[query_row][query_glass])

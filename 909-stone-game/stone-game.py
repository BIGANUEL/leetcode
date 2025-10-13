class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = [[-1]*(len(piles)+1) for _ in range(len(piles))]
        def dp(i,j):
            if i == j:
                return piles[i]
            if memo[i][j] == -1:
                left = piles[i] - dp(i+1,j)
                right = piles[j] - dp(i,j-1)
                memo[i][j] = max(left,right)
            return memo[i][j]
        return dp(0,len(piles)-1) > 0
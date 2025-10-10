class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(i):
            if i >= len(questions):
                return 0
            if i not in memo:
                p,b = questions[i]
                include = 0
                include = p + dp(i+b+1)
                exclude = dp(i+1)
                memo[i] = max(include,exclude)
            return memo[i]
        return dp(0)
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            if i not in memo:
                memo[i]= dp(i+1)
                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    memo[i]+= dp(i+2)
            return memo[i]
        return dp(0)
        

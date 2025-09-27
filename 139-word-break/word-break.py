class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def validator(start,end):
            temp = s[start:end+1]
            if temp in wordDict:
                return True
            return False

        def checker(l,r):
            if r >= len(s):
                return False
            res = False
            if (l,r) not in memo:
                if validator(l,r):
                    if r == len(s) - 1:
                        res = True
                    memo[(l,r)] =  res or checker(r+1,r+1) or checker(l,r+1)
                else:
                    memo[(l,r)] = res or checker(l,r+1)
            return memo[(l,r)]
            
        
        res =checker(0,0)
        return res
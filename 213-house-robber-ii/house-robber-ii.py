class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_s(start,end):
            memo = {}
            def dp(i):
                if i>end:
                    return 0
                if i in memo:
                    return memo[i]
                include = 0
                include = nums[i] + dp(i+2)
                exclude = dp(i+1)
                memo[i] = max(include,exclude)
                return memo[i]
            return dp(start)
        case1 = rob_s(0,n-2)
        case2 = rob_s(1,n-1)
        return max(case1,case2)
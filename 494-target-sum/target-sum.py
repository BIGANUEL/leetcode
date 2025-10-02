class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,cur_sum):
            if i == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            if (i,cur_sum) in memo:
                return memo[(i,cur_sum)]
            pos = dp(i+1,cur_sum + nums[i])
            neg = dp(i+1,cur_sum - nums[i])
            memo[(i,cur_sum)] = pos + neg
            return memo[(i,cur_sum)]
        return dp(0,0)

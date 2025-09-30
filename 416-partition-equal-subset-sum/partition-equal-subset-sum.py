class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total= sum(nums)
        half= total // 2
        memo = {}
        if total % 2 != 0:
            return False
        def dp(i,cur_sum):
            if i >= n or cur_sum > half:
                return False
            if nums[i] == half or cur_sum == half:
                return True
            if (i,cur_sum) in memo:
                return memo[(i,cur_sum)]
            memo[(i,cur_sum)] = dp(i+1,cur_sum+nums[i]) or dp(i+1,cur_sum)
            return memo[(i,cur_sum)]
        return dp(0,0)
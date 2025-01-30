class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        left, right =0,len(nums) - 1
        res = []
        while len(nums) != len(res):
            res.append(nums[left])
            left+=1

            if left <= right:
                res.append(nums[right])
                right-=1
        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for i in range(len(nums)):
            candidates = [nums[i],curMax*nums[i],curMin*nums[i]]
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(curMax,res)
        return res
        
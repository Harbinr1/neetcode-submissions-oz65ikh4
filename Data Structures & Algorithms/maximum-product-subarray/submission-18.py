class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            candidates = [nums[i],currMax*nums[i],currMin*nums[i]]
            currMax = max(candidates)
            currMin = min(candidates)
            res = max(res,currMax)
        
        return res
        
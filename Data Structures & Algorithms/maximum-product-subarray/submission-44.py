class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for num in nums:
            candidates = [num,curMax*num,curMin*num]
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(curMax,res)
        
        return res
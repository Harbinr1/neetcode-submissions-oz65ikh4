class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            tmp = currMax
            currMax = max(n,n*currMax,n*currMin)
            currMin = min(n,n*tmp,n*currMin)
            res = max(res,currMax)
        
        return res

        
        
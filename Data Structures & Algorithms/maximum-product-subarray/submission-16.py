class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            tmp = currMax
            currMax = max(n,currMax*n,n*currMin)
            currMin = min(n,tmp*n,n*currMin)
            res = max(res,currMax)
        return res

        
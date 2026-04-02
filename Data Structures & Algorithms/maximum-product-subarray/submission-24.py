class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = max(nums)

        for num in nums:
            tmp = currMax
            currMax = max(num,currMax*num,currMin*num)
            currMin = min(num,tmp*num,currMin*num)
            res = max(res,currMax)
        return res
        
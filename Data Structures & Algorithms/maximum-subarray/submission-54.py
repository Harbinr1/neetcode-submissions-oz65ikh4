class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = max(nums[i],nums[i] + curSum)
            maxSum = max(curSum,maxSum)
        return maxSum
        
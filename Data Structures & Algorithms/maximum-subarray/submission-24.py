class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for i in range(len(nums)):
            curSum = max(nums[i],curSum + nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        bestSum = nums[0]

        for i in range(1,len(nums)):
            currSum = max(nums[i],currSum + nums[i])
            bestSum = max(currSum,bestSum)
        return bestSum
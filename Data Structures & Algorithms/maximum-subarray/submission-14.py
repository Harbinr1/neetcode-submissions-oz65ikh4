class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        bestSoFar = nums[0]
        
        

        for i in range(1,len(nums)):
            bestSoFar = max(nums[i],bestSoFar + nums[i])
            currSum = max(bestSoFar,currSum)
        return currSum
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        
        for i in range(1,len(nums)):
            num = nums[i]
            candidates = [num,num* curr_max,num*curr_min]

            curr_max = max(candidates)
            curr_min = min(candidates)

            result = max(result,curr_max)

        return result    
        
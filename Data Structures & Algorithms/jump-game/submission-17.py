class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range(1,len(nums)):
            if i <= farthest:
                farthest = max(farthest,nums[i] + i)
            else:
                return False
        return True
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
            else:
                return False
        return True
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farthest = 0
        jumps = 0
        for i in range(len(nums)-1):
            farthest = max(i + nums[i],farthest)
            if i == end:
                end = farthest
                jumps += 1
        return jumps
        
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0
        l = 0
        r = len(height) - 1
        total = 0


        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax,height[l])
                total += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax,height[r])
                total += rightMax - height[r]
                r -= 1
        
        return total
        
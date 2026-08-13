class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0 
        l = 0
        r = len(height)-1
        water = 0
        while l < r:
            if height[l] > leftMax:
                leftMax = height[l]
            if height[r] > rightMax:
                rightMax = height[r]
            
            if height[l] < height[r]:
                water += leftMax - height[l]
                l += 1
            else:
                water += rightMax - height[r]
                r -= 1
        return water

        
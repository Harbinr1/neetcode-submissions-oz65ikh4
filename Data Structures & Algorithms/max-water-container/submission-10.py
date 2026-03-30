class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = (right - left)
            height = min(heights[right],heights[left])
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
            area = (width * height)
            max_area = max(max_area,area)
        return max_area
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        q = []

        for index,val in enumerate(heights):
            while q and val < q[-1][1]:
                prev_index,prev_val = q.pop()
                if q:
                    L = q[-1][0]
                    width = index - L - 1
                else:
                    width = index
                max_area = max(max_area,width * prev_val)
            q.append((index,val))
        
        while q :
            prev_index,prev_val = q.pop()
            if q:
                L = q[-1][0]
                width = len(heights) - L - 1
            else:
                width = len(heights)
            max_area = max(max_area,width * prev_val)
        return max_area
        
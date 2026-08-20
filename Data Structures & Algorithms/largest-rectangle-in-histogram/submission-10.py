class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        q = []

        for  i,v in enumerate(heights):
            while q and v < q[-1][1]:
                prev_i,prev_v = q.pop()
                if q:
                    L = q[-1][0]
                    width = i - L - 1
                else:
                    width = i
                
                max_area = max(max_area,width*prev_v)
            
            q.append((i,v))
        
        while q:
            prev_i,prev_v = q.pop()
            if q:
                L = q[-1][0]
                width = len(heights) - L - 1
            else:
                width = len(heights)
            
            max_area = max(max_area,width *prev_v)
        return max_area
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        visited = set()
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for r in range(ROWS):
            pacific_reachable.add((r,0))
        
        for c in range(COLS):
            pacific_reachable.add((0,c))
        
        for r in range(ROWS):
            atlantic_reachable.add((r,COLS-1))
        
        for c in range(COLS):
            atlantic_reachable.add((ROWS-1,c))
        
        pacific_q = deque(pacific_reachable)
        atlantic_q = deque(atlantic_reachable)


        while pacific_q:
            i,j = pacific_q.popleft()
            for dr,dc in directions:
                nr,nc = dr+i,dc+j
                if 0 <= nr <ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] >= heights[i][j] and (nr,nc) not in pacific_reachable:
                        pacific_reachable.add((nr,nc))
                        pacific_q.append((nr,nc))
        

        while atlantic_q:
            i,j = atlantic_q.popleft()
            for dr,dc in directions:
                nr,nc = dr+i,dc +j
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] >= heights[i][j] and (nr,nc) not in atlantic_reachable:
                        atlantic_reachable.add((nr,nc))
                        atlantic_q.append((nr,nc))
        

        result = atlantic_reachable & pacific_reachable

        return [list(coord) for coord in result]

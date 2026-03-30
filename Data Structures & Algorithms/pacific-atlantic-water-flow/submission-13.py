class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        for r in range(ROWS):
            pacific_set.add((r,0))
        
        for c in range(COLS):
            pacific_set.add((0,c))
        
        for r in range(ROWS):
            atlantic_set.add((r,COLS-1))
        
        for c in range(COLS):
            atlantic_set.add((ROWS-1,c))
        
        pacific_reachable = set()
        pacific_q = deque(pacific_set)
        for (r,c) in pacific_set:
            pacific_reachable.add((r,c))
            pacific_q.append((r,c))

        atlantic_reachable = set()
        atlantic_q = deque(atlantic_set)

        for (r,c) in atlantic_set:
            atlantic_reachable.add((r,c))
            atlantic_q.append((r,c))
        

        while pacific_q:
            r,c = pacific_q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] >= heights[r][c] and (nr,nc) not in pacific_reachable:
                        pacific_reachable.add((nr,nc))
                        pacific_q.append((nr,nc))
        
        while atlantic_q:
            r,c = atlantic_q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] >= heights[r][c] and (nr,nc) not in atlantic_reachable:
                        atlantic_reachable.add((nr,nc))
                        atlantic_q.append((nr,nc))
        

        result = atlantic_reachable & pacific_reachable

        return [list(cell) for cell in result]


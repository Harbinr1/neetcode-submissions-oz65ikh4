class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r,c,reachable_set):
            if (r,c) in reachable_set:
                return
            
            reachable_set.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,reachable_set)
            

        for r in range(ROWS):
            dfs(r,0,pacific_reachable)
        for c in range(COLS):
            dfs(0,c,pacific_reachable)
            
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic_reachable)
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic_reachable)





        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                    res.append([r,c])
        
        return res
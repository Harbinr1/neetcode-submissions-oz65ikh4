class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        def dfs(r,c,reachable_set):
            if (r,c) in reachable_set:
                return
            reachable_set.add((r,c))
            for dr,dc in directions:
                nr,nc =dr+r,dc+c
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,reachable_set)

        for r in range(ROWS):
            dfs(r,0,pacific_set)
        for c in range(COLS):
            dfs(0,c,pacific_set)
        
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic_set)
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic_set)




        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    res.append([r,c])

        return res 
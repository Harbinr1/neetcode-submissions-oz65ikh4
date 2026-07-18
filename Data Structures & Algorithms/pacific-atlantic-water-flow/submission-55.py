class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,reachable_set):
            reachable_set.add((r,c))

            for dr,dc in directions:
                ni,nj = dr+r,dc+c
                if 0 <= ni < ROWS and 0 <= nj < COLS and (ni,nj) not in reachable_set:
                    if heights[ni][nj] >= heights[r][c]:
                        dfs(ni,nj,reachable_set)
        

        pacific_reachable = set()
        atlantic_reachable = set()

        for r,c in pacific_set:
            dfs(r,c,pacific_reachable)
        
        for r,c in atlantic_set:
            dfs(r,c,atlantic_reachable)
        

        return list(atlantic_reachable.intersection(pacific_reachable))

        
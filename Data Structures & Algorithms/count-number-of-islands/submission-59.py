class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0

        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                ni,nj = dr + r,dc + c
                if 0 <= ni < ROWS and 0 <= nj < COLS:
                    if grid[ni][nj] == '1' and (ni,nj) not in visited:
                        
                        dfs(ni,nj)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    dfs(r,c)
        
        return count



        
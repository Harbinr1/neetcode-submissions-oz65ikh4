class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        self.max_area = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        ROWS = len(grid)
        COLS = len(grid[0])
    
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            visited.add((r,c))
            area = 1

            for dr,dc in directions:
                ni,nj = dr + r,dc +c
                area += dfs(ni,nj)
            return area

        
        for r in range(ROWS):
            for c in range(COLS):
                self.max_area = max(self.max_area,dfs(r,c))
        return self.max_area
        
        
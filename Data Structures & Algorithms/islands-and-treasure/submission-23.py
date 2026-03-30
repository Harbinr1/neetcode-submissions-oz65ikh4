class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        
        distance = 0
        while q:
            
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr,dc in directions:
                    ni,nj = dr +i,dc+j
                    if 0 <= ni < ROWS and 0 <= nj < COLS:
                        if grid[ni][nj] == 2147483647:
                            grid[ni][nj] = distance +1
                            q.append((ni,nj))
            distance += 1
            

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_count = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                
                if grid[r][c] == 1:
                    fresh_count += 1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                row,col = q.popleft()

                for dr,dc in directions:
                    ni,nj = dr+row,dc+col
                    if 0<= ni < ROWS and 0 <= nj < COLS:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            q.append((ni,nj))
                            fresh_count -= 1
            
            minutes += 1
        
        return minutes if fresh_count == 0 else - 1



        
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        minutes = -1
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+i,dc+j
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr,nc))
            minutes += 1
        
        return minutes if fresh == 0 else - 1
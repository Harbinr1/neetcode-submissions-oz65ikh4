class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
        

        minutes = -1
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr,dc in directions:
                    ni,nj = dr+i,dc +j
                    if 0 <= ni <ROWS and 0 <= nj < COLS:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            fresh -= 1
                            q.append((ni,nj))
            
            minutes += 1
            
                
        return minutes if fresh == 0 else -1
        
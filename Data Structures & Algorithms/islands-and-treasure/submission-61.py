class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

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
                    nr,nc = dr+i,dc+j
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 2147483647:
                            grid[nr][nc] = distance + 1
                            q.append((nr,nc))
            distance += 1
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        visited = set()

        q = deque()
        distance = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                
                for dr,dc in directions:
                    nr,nc = dr+i,dc+j

                    if 0<= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 2147483647 and (nr,nc) not in visited:
                            grid[nr][nc] = distance + 1

                            visited.add((nr,nc))
                            q.append((nr,nc))
            distance += 1    


        
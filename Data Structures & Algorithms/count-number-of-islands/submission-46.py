class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        count = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def bfs(r,c):
            visited.add((r,c))
            q.append((r,c))
            

            while q:
                i,j = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+i,dc+j
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == '0' or (nr,nc) in visited:
                            continue
                        visited.add((nr,nc))
                        q.append((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count +=1
                    bfs(r,c)
        
        return count


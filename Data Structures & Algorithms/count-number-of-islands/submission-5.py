class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(r,c):
            visited.add((r,c))
            q.append((r,c))

            while q:
                i,j = q.popleft()
                for dr,dc in directions:
                    ni,nj = dr +i,dc + j

                    if 0 <= ni < ROWS and 0 <= nj < COLS:
                        if grid[ni][nj] == '0' or (ni,nj) in visited:
                            continue
                        visited.add((ni,nj))
                        q.append((ni,nj))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0':
                    continue
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    bfs(r,c)
        return count




        
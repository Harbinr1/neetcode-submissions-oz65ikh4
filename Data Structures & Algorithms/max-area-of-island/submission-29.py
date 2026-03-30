class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        maxArea = 0
        q = deque()

        def bfs(r,c):
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                i,j = q.popleft()

                for dr,dc in directions:
                    ni,nj = dr+i,dc+j

                    if 0 <= ni < ROWS and 0 <= nj < COLS:
                        if grid[ni][nj] == 1 and (ni,nj) not in visited:
                            area += 1
                            visited.add((ni,nj))
                            q.append((ni,nj))
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea,bfs(r,c))
        return maxArea

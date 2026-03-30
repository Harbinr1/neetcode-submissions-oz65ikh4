class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        maxArea = 0

        def bfs(r,c):
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                i,j = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr +i , dc+j
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1 and (nr,nc) not in visited:

                            area += 1
                            visited.add((nr,nc))
                            q.append((nr,nc))
                
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0  or (r,c)  in visited:
                    continue
                maxArea = max(maxArea,bfs(r,c))

        return maxArea 

            
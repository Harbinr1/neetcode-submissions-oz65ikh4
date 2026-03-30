class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        count = 0
        q = deque()
        def bfs(r,c):
            
            visited.add((r,c))
            q.append((r,c))

            while q:
                i,j = q.popleft()
                for dr,dc in directions:
                    ni,nr = dr +i,dc +j
                    if 0 <= ni < ROWS and 0 <= nr < COLS:
                        if grid[ni][nr] == '0' or (ni,nr) in visited:
                            continue
                        visited.add((ni,nr))
                        q.append((ni,nr)) 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0' or (r,c)  in visited:
                    continue
                count +=1 
                bfs(r,c)
        
        return count
        
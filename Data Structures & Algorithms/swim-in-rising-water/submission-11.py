class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        minHeap = [(grid[0][0],0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while minHeap:
            curT,r,c = heapq.heappop(minHeap)
            if r == ROWS -1 and c == COLS -1:
                return curT
            
            for dr,dc in directions:
                ni,nj = r + dr,dc + c
                if 0 <= ni < ROWS and 0 <=nj < COLS:
                    new_time = max(curT,grid[ni][nj])
                    if (ni,nj) in visited:
                        continue
                    visited.add((ni,nj))
                    heapq.heappush(minHeap,(new_time,ni,nj))
        
                
        
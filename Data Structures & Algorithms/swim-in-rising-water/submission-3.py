class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        minHeap = [(grid[0][0],0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        new_time = 0


        while minHeap:
            curr_time,r,c = heapq.heappop(minHeap)
            if r  == ROWS - 1 and c  == COLS - 1:
                return curr_time
            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr,dc in directions:
                ni,nj = (r + dr), (c + dc)
                if 0 <= ni < ROWS and 0 <= nj < COLS:
                    new_time = max(curr_time,grid[ni][nj])
                    heapq.heappush(minHeap,(new_time,ni,nj))
        


          

        
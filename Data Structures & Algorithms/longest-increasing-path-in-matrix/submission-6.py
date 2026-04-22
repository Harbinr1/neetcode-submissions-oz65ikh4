class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        overall_max = 0
        directions = ([1,0],[-1,0],[0,1],[0,-1])
        
        def dfs(i,j):
            current_path = 0
            if memo[i][j] != -1:
                return memo[i][j]

            for dr,dc in directions:
                ni,nj = dr+i,dc + j
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    current_path = max(dfs(ni,nj),current_path)
            memo[i][j] = 1 + current_path
            return memo[i][j]
                    
        
        for i in range(rows):
            for j in range(cols):
                current_path = dfs(i,j)
                overall_max = max(overall_max,current_path)
        
        return overall_max
            

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowSet = set()
        colSet = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        
        for r in rowSet:
            for c in range(COLS):
                matrix[r][c] = 0
        

        for c in colSet:
            for r in range(ROWS):
                matrix[r][c] = 0
                
        
        
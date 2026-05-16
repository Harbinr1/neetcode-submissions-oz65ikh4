class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        rowsZereos = set()
        colsZereos = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowsZereos.add(r)
                    colsZereos.add(c)
        
        for r in rowsZereos:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for c in colsZereos:
            for r in range(ROWS):
                matrix[r][c] = 0

                    

        
        
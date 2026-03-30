class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        lo = 0
        hi = (ROWS * COLS) - 1

        while lo <= hi:
            mid = (lo + hi ) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] > target:
                hi = mid - 1
            
            elif matrix[row][col] < target:
                lo = mid + 1
            
            else:
                return True
        return False
        
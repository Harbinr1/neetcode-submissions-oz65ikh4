class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)
                if value == ".":
                    continue
                elif value in rows[r] or value in cols[c] or value in box[box_index]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[box_index].add(board[r][c])
            
        return True



        
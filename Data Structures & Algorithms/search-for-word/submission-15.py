class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
            (r,c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r,c))

            for dr,dc in directions:
                ni,nj = dr+r,dc+c
                if dfs(ni,nj,i+1):
                    return True
            
            visited.remove((r,c))
            return False
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False

        dfs(0,0,0)

        
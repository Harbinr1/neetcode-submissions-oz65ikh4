class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r,c,node):
            char = board[r][c]
            if char == "#":
                return
            
            if node.endOfWord:
                res.append(node.word)
                node.endOfWord = False
            
            board[r][c] = "#"


            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = r + dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_char = board[nr][nc]
                    if next_char in node.children:
                        dfs(nr,nc,node.children[next_char])
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(r,c,trie.root.children[board[r][c]])
        return res
        
                        

        
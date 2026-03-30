class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited = set([beginWord])
        q = deque([beginWord])

        level = 1
        while q:
            for _ in range(len(q)):

                curr = q.popleft()



                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = curr[:i] + c + curr[i+1:]
                        if new_word in wordList and new_word not in visited:
                            if new_word == endWord:
                                return level + 1
                            q.append(new_word)
                            visited.add(new_word)
            level +=1
        return 0    
            
            
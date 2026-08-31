class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        level = 1
        visited = set([beginWord])


        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return level
                
                for word in wordList:
                    if word not in visited:
                        diff =0

                        for i in range(len(node)):
                            if word[i] != node[i]:
                                diff += 1

                        if diff == 1:
                            q.append(word)
                            visited.add(word)
            level +=1
        return 0
        
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = defaultdict(list)
        visited = set([beginWord])

        q = deque([beginWord])

        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
        

        level = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if endWord == node:
                    return level
                

                for i in range(len(node)):
                    pattern = node[:i] + "*" + node[i+1:]

                    for word in neighbors[pattern]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
            level += 1
        return 0 
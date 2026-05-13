class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        visited = set()
        processing = set()
        found = False
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    found = True
                    break
                j += 1

            if not found and  len(w1) > len(w2):
                return ""
                

        res = []
        def dfs(i):
            if i in visited:
                return True
            if i in processing:
                return False
            
            processing.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            processing.remove(i)
            visited.add(i)
            res.append(i)
            return True
        unique = set()
        
        for char in words:
            for c in char:
                if c not in unique:
                    unique.add(c)
                    if not dfs(c):
                        return ""
        return "".join(res[::-1])
        
        
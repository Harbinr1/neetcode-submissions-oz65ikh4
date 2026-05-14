class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dest = [float('inf')] * n
        dest[src] = 0
        for i in range(k + 1):
            temp = dest[::]

            for s,d,p in flights:
                if dest[s] == float('inf'):
                    continue
                if dest[s] + p < temp[d]:
                    temp[d] = dest[s] + p
            dest = temp
        
        return dest[dst] if dest[dst] != float('inf') else - 1
        
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        safe = []

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                safe.append(t)
        

        hasx = hasy = hasz = False

        for t in safe:
            if t[0] == target[0]:
                hasx = True
            if t[1] == target[1]:
                hasy = True
            if t[2] == target[2]:
                hasz = True
        
        return hasx and hasy and hasz

        
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        safe = []
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                safe.append(t)
        
        has_x = has_y = has_z = False
        for t in safe:
            if t[0] == target[0]:
                has_x = True
            if t[1] == target[1]:
                has_y = True
            if t[2] == target[2]:
                has_z = True
        return has_x and has_y and has_z
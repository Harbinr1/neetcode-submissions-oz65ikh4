class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # res = []
        # for t in triplets:
        #     if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
        #         res.append(t)
        

        # has_x = has_y = has_z = False
        # for t in res:
        #     if t[0] == target[0]:
        #         has_x = True
        #     if t[1] == target[1]:
        #         has_y = True
        #     if t[2] == target[2]:
        #         has_y = True
        # return has_x and has_y and has_z
        
        safe = []
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                safe.append(t)

        hasX = hasY = hasZ = False
        for t in safe:
            if t[0] == target[0]:
                hasX = True
            if t[1] == target[1]:
                hasY = True
            if t[2] == target[2]:
                hasZ = True
        
        return hasX and hasY and hasZ
                
        
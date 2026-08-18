class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)
        
        while l <= r:
            mid = (l+r) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/mid)
            
            if total_hours <= h:
                res = mid
                r = mid - 1
            elif total_hours > h:
                l = mid + 1

        return res

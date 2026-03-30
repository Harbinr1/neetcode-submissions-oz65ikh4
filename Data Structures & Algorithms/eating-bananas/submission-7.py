class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo <= hi:
            total_hours = 0
            mid = (lo + hi) // 2

            for pile in piles:
                total_hours += ((pile + mid - 1)// mid)
            

            if total_hours <= h:
                minK = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return minK


        
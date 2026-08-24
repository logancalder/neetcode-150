class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        lo, hi = 1, max(piles)

        while lo < hi:
            m = (lo + hi) // 2

            hours = 0
            for pile in piles:
                hours += (pile + m - 1) // m 
            
            if hours <= h:
                hi = m
            else:
                lo = m + 1
            
        return lo

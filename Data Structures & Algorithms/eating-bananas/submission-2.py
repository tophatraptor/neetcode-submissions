class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        lower = 1
        upper = sum(piles)
        while lower < upper:
            k = lower + (upper - lower) // 2
            time = 0
            for pile in piles:
                time += pile // k + (1 if (pile % k > 0) else 0)
            if time > h:
                lower = k + 1
            else:
                upper = k
        return lower
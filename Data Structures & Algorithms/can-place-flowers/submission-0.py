class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            is_valid = flowerbed[i] == 0
            if i > 0:
                is_valid = is_valid and flowerbed[i-1] == 0
            if i < len(flowerbed) - 1:
                is_valid = is_valid and flowerbed[i+1] == 0
            if is_valid:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False
"""
Greedy solution works

1 0 0 1 - can't place

1 0 0 0 0 1 - only one spot

1 0 0 0 0 0 1 - two spots
"""
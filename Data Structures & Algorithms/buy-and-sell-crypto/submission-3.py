class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = 100
        largest_diff = 0
        for x in prices:
            if x < min_so_far:
                min_so_far = x
            if  x - min_so_far > largest_diff:
                largest_diff = x - min_so_far
        return largest_diff
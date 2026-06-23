class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_so_far = prices[0]
        max_profit = 0
        for x in prices:
            if x < lowest_so_far:
                lowest_so_far = x
            if x - lowest_so_far > max_profit:
                max_profit = x - lowest_so_far
        return max_profit
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        profit_by_weight = [0 for _ in range(capacity + 1)]
        for i in range(1, len(profit_by_weight)):
            for j, w in enumerate(weight):
                if i-w < 0:
                    continue
                profit_by_weight[i] = max(profit_by_weight[i], profit_by_weight[i-w] + profit[j])
        return profit_by_weight[-1]

"""
Now, unbounded knapsack is *different* because we don't really need
to consider the state of each element. We just iterate over 
all possible elements, compare to the previous max, and update if our new
max is larger
"""
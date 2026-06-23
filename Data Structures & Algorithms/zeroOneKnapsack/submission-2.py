class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0 for _ in range(len(weight) + 1)] for _ in range(capacity + 1)]
        for i in range(1, capacity + 1):
            for j in range(1, len(weight) + 1):
                if i - weight[j-1] < 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = max(
                        dp[i][j], # Current value
                        dp[i][j-1], # Exclude J
                        dp[i-weight[j-1]][j-1] + profit[j-1] # Include j
                    )
        return dp[-1][-1]

"""

dp[i][j] means that for a capacity i, what is the maximum profit when considering the first j elements?

We have two options:
- Don't include j, which is the same as the max profit at dp[i-1][j-1]
- Include j, which 

This is the max(dp[i][j-1] + dp[i-j])

So we have a list of profits, a list of weights, and a total capacity

We can create a version called maximumProfitRec(cur_profit, cur_weight, profit, weight, capacity)

Then we can do the following:

def maximumProfitRec(cur_profit, cur_weight, profit, weight, capacity):
    if cur_weight > capacity:
        return 0
    if len(profit) == 0:
        return cur_profit
    next_profit, next_weight = profit[0], weight[0]
    return max(
        maximumProfitRec(cur_profit + next_profit, cur_weight + next_weight, profit[1:], weight[1:], capacity),
        maximumProfitRec(cur_profit, cur_weight, profit[1:], weight[1:], capacity)
    )

This will create 2^n iterations.

Soln: create a matrix of dimension [capacity, len(weights)]

for i in range(len(capacity)):
    for j in range(len(weights)):


dp[0] = 0s up through weight[0] then profit[0]
dp[x][0] = 0 since we can select no items of weight zero
"""
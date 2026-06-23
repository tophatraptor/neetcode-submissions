class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [max(costs) * len(days) for _ in days]
        for i in range(len(days)):
            # Iterate over 3 costs
            # 1 day ticket
            if i == 0:
                prev_cost = 0
            else:
                prev_cost = dp[i-1]
            dp[i] = min(dp[i], prev_cost + costs[0])

            # 7 day ticket
            for k in range(i, len(days)):
                if days[k] - days[i] < 7:
                    dp[k] = min(dp[k], prev_cost + costs[1])
                else:
                    break
            
            # 30 day ticket
            for k in range(i, len(days)):
                if days[k] - days[i] < 30:
                    dp[k] = min(dp[k], prev_cost + costs[2])
                else:
                    break
        return dp[-1]
            

# Recurrence
# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         if len(days) == 0:
#             return 0
#         return min(
#             # purchase 1
#             self.mincostTickets(days[:-1], costs) + costs[0],
#             # purchase 7 day
#             self.mincostTickets([x for x in days if x < days[-1] - 6], costs) + costs[1],
#             # purchase 30 day
#             self.mincostTickets([x for x in days if x < days[-1] - 29], costs) + costs[2],
#         )
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])
        
        prev_costs = costs[0]
        for i in range(1, len(costs)):
            result = [
                costs[i][0] + min(prev_costs[1], prev_costs[2]),
                costs[i][1] + min(prev_costs[0], prev_costs[2]),
                costs[i][2] + min(prev_costs[0], prev_costs[1]),
            ]
            prev_costs = result
        return min(result)

# Version 1
# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#         min_costs = []
#         min_costs.append(costs[0])
#         for i in range(1, len(costs)):
#             result = [
#                 costs[i][0] + min(min_costs[i-1][1], min_costs[i-1][2]),
#                 costs[i][1] + min(min_costs[i-1][0], min_costs[i-1][2]),
#                 costs[i][2] + min(min_costs[i-1][0], min_costs[i-1][1]),
#             ]
#             min_costs.append(result)
#         return min(min_costs[-1])
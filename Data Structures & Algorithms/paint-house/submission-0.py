class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        min_costs = []
        min_costs.append(costs[0])
        for i in range(1, len(costs)):
            result = [
                costs[i][0] + min(min_costs[i-1][1], min_costs[i-1][2]),
                costs[i][1] + min(min_costs[i-1][0], min_costs[i-1][2]),
                costs[i][2] + min(min_costs[i-1][0], min_costs[i-1][1]),
            ]
            min_costs.append(result)
        return min(min_costs[-1])
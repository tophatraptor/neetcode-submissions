import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            if first == second:
                continue
            if first > second:
                stones.append(first - second)
            else:
                stones.append(second - first)
        if len(stones) == 1:
            return stones[0]
        return 0
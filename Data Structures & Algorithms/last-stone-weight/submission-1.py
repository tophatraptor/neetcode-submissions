import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first == second:
                continue
            if first > second:
                heapq.heappush(stones, -(first - second))
            else:
                heapq.heappush(stones, -(second - first))
        if len(stones) == 1:
            return -stones[0]
        return 0
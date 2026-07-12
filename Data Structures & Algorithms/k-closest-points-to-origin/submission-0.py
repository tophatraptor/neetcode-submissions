import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # We want this to be a max heap, so append with neg distance
        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else:
                prev_distance, prev_point = heapq.heappop(heap)
                prev_distance = -prev_distance
                if dist < prev_distance:
                    heapq.heappush(heap, (-dist, point))
                else:
                    heapq.heappush(heap, (-prev_distance, prev_point))
        return [x[1] for x in heap]
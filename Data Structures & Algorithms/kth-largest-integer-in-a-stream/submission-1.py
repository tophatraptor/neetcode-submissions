class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.heapSize = k
        for x in nums:
            if len(self.heap) < self.heapSize:
                heapq.heappush(self.heap, x)
            else:
                top = heapq.heappop(self.heap)
                if x > top:
                    heapq.heappush(self.heap, x)
                else:
                    heapq.heappush(self.heap, top)

    def add(self, val: int) -> int:
        if len(self.heap) == self.heapSize:
            x = heapq.heappop(self.heap)
            if val > x:
                heapq.heappush(self.heap, val)
            else:
                heapq.heappush(self.heap, x)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
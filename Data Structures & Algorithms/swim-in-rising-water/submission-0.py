from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height = max(grid[0][0], grid[-1][-1])
        queue = deque()
        queue.append((0, 0))
        seen = set()
        point_heap = []
        n = len(grid)
        # Outer loop to handle re-filling the queue after
        # raising the level
        while True:
            while len(queue) > 0:
                r, c = queue.popleft()
                if (r, c) in seen:
                    continue
                if r == n-1 and c == n-1:
                    return height
                seen.add((r, c))
                neighbors = self.gen_neighbors(r, c, len(grid))
                for neighbor in neighbors:
                    if neighbor in seen:
                        continue
                    if grid[neighbor[0]][neighbor[1]] <= height:
                        queue.append(neighbor)
                    else:
                        heapq.heappush(point_heap, (grid[neighbor[0]][neighbor[1]], neighbor))
            # Now, empty queue (exhausted all reachable squares of a given height)
            # We need to expand by raising the height and adding the queue
            assert len(point_heap) > 0
            new_height = point_heap[0][0]
            height = new_height
            while len(point_heap) > 0 and point_heap[0][0] == new_height:
                new_height, coord = heapq.heappop(point_heap)
                queue.append(coord)
        return -1
                    

    def gen_neighbors(self, x, y, n):
        res = []
        if x > 0:
            res.append((x-1, y))
        if y > 0:
            res.append((x, y-1))
        if x < n-1:
            res.append((x+1, y))
        if y < n-1:
            res.append((x, y+1))
        return res

"""
So we need to identify a path from the top left (0, 0)
to the bottom right (-1, -1)

The issue is that there are cells of different heights, and
we need to identify the minimum height that will enable us to
traverse from the top left to the bottom right

In a naive solution, what we can do is straightforward: we
BFS from the top left until we add in the bottom right.

We have to instantiate our height to the max of top left
and bottom right, and we expand

In the happy path: we find a route directly via BFS.

Important question, however: What happens if we don't?

We have a whole set of squares that we can't traverse at our
given height. So we need to look back at all of the squares
that we could have traversed, and find a path forward
from the lowest weight.

So we need a structure that keeps track of squares we *could*
have visited, but did not, because their height exceeded
the current water level.
"""
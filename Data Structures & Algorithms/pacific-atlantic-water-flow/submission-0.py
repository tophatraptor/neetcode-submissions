from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        # At each coordinate, we define a list pair [pacific_reachable, atlantic_reachable]
        reachable = [[[0, 0] for c in range(num_cols)] for r in range(num_rows)]
        # Initialize reachability matrix
        pacific_coords = deque()
        atlantic_coords = deque()
        for r in range(num_rows):
            reachable[r][0][0] = 1
            pacific_coords.append((r, 0))
            reachable[r][-1][1] = 1
            atlantic_coords.append((r, num_cols - 1))
        for c in range(num_cols):
            reachable[0][c][0] = 1
            pacific_coords.append((0, c))
            reachable[-1][c][1] = 1
            atlantic_coords.append((num_rows - 1, c))
        
        while len(pacific_coords) > 0:
            r, c = pacific_coords.popleft()
            neighbors = self.genNeighbors(r, c, num_rows, num_cols)
            for nr, nc in neighbors:
                if reachable[nr][nc][0] > 0:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    reachable[nr][nc][0] = 1
                    pacific_coords.append((nr, nc))
        
        while len(atlantic_coords) > 0:
            r, c = atlantic_coords.popleft()
            neighbors = self.genNeighbors(r, c, num_rows, num_cols)
            for nr, nc in neighbors:
                if reachable[nr][nc][1] > 0:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    reachable[nr][nc][1] = 1
                    atlantic_coords.append((nr, nc))
        res = []
        for r in range(num_rows):
            for c in range(num_cols):
                if reachable[r][c][0] > 0 and reachable[r][c][1] > 0:
                    res.append([r, c])
        return res
    
    def genNeighbors(self, r, c, num_rows, num_cols):
        res = []
        if r > 0:
            res.append((r-1, c))
        if c > 0:
            res.append((r, c-1))
        if r < num_rows - 1:
            res.append((r + 1, c))
        if c < num_cols - 1:
            res.append((r, c + 1))
        return res

"""
A naive solution here would be to:
- Start at every grid
- DFS outwards to progressively determine whether or not a a particular set of
positions
- When we contact a "pacific" square (e.x. a square that already is reachable),
mark our square as pacific

Some notes:
- If we're not careful, we may spend time traversing the inside of the map unnecessarily

There's a key structural observation to observe: we can flood from the coast inwards.

We can start by marking all "coastal" squares as valid, then queueing up the squares
adjacent to them.
"""
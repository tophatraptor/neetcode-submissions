class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        total_area = 0
        tallest_after = [0 for _ in range(len(height))]
        tallest_seen = height[-1]
        for i in range(len(height) - 2, -1, -1):
            tallest_after[i] = tallest_seen
            if height[i] > tallest_seen:
                tallest_seen = height[i]
        # Start by moving left to the first nonzero element
        while left < len(height) and height[left] == 0:
            left += 1
        right = left + 1
        while left < len(height) and right < len(height):
            # We're going to start assuming that right is 1 to the left, so let's forward right to the next valid source
            while right < len(height) and height[right] < height[left] and height[right] != tallest_after[left]:
                right += 1
            # There's no valid bounding wall for left, so we return
            if right == len(height):
                return total_area
            # Otherwise, we've reached a valid "wall" for left
            water_height = min(height[left], height[right])
            for i in range(left + 1, right):
                total_area += water_height - height[i]
            # Now, we reset the values of left and right
            left = right
            right = left + 1
        return total_area
"""
Iterative solution:
- For a given wall, we need to make our way forward in the array until we identify the first wall that is as high as, if not higher than, our wall
WAIT, there's a catch - what if our wall is the tallest wall? We may be able to catch water after the fact.

The next wall we run into is going to be either:
- The first wall that is as tall as, or taller than us (if it's taller)
- The tallest wall before the end

- We will then make a pass over all non-wall segments between and sum min(left, right) - h over the interval
- We reset our left wall to the right wall and continue
"""
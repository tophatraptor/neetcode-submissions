class Solution:
    def trap(self, height: List[int]) -> int:
        forward_prefix = [0]
        for i in range(1, len(height)):
            forward_prefix.append(max(forward_prefix[i-1], height[i-1]))
        backward_prefix = [0 for _ in range(len(height))]
        for i in reversed(range(0, len(height) - 1)):
            backward_prefix[i] = max(backward_prefix[i+1], height[i+1])
        total = 0
        for i in range(len(height)):
            total += max(0, min(forward_prefix[i], backward_prefix[i]) - height[i])
        return total
        
"""
So we have a list of heights that represent an elevation map.

The height of the water at a given index i is going to be equal to
max(min(tallest_to_left, tallest_to_right) - cur_height, 0)

In O(n) time, O(n) space, we can generate an array that keeps track
of the tallest value *after* a particular index.

Then we yield the result. Edge cases to note, the edges of the map start at zero.

"""
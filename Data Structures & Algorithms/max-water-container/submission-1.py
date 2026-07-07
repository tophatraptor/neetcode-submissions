class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0
        while end > start:
            cur_area = min(heights[start], heights[end]) * (end - start)
            if cur_area > max_area:
                max_area = cur_area
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_area
"""
Height = min(heights[x], heights[y]) * (y - x)

O(n**2) solution is to iterate over all pairs of heights

When we consider two weights: if we decrease the width of the space between them,
that will always reduce the area contribution from width. Only way to net compensate
is to increase the height.
"""
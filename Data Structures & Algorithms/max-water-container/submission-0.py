class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            curr_area = min(heights[i], heights[j]) * (j-i)
            if curr_area > max_area:
                max_area = curr_area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area

"""
For whichever two bars we pick, the area we're going to encompass = min(bar1, bar2) * (bar2 - bar1)

One of two things is true, either we get more area by increasing the width of our container, or the height of our container

Therefore, by initializing pointers at the start and end of the array, we can iteratively trade off width against height

O(n**2) soln is to iterate over all values of bar1, bar2, and then pick the largest value.

The only way we can achieve a larger area is if we move forward bar2, such that bar2 is greater than bar1
"""
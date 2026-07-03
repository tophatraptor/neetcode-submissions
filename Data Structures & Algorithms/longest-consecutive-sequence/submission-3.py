import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        intervals = {}
        seen = set()
        for x in nums:
            if x in seen:
                continue
            else:
                seen.add(x)
            
            if x + 1 not in intervals and x - 1 not in intervals:
                intervals[x] = [x, x]
            elif x - 1 in intervals and x + 1 in intervals:
                # Example: [1, 3], [5, 7], we insert 4
                # We need to eliminate one of the intervals
                upper_interval = intervals[x + 1]
                lower, upper = upper_interval[0], upper_interval[1]
                intervals.pop(lower)
                # If lower == upper, we're popping a value no longer in the dictionary
                if lower != upper:
                    intervals.pop(upper)
                lower_interval = intervals[x - 1]
                if intervals[x-1][0] != intervals[x-1][1]:
                    intervals.pop(x - 1)
                lower_interval[1] = upper
                intervals[upper] = lower_interval
            elif x + 1 in intervals:
                if intervals[x+1][0] == intervals[x+1][1]:
                    cur_interval = intervals[x+1]
                else:
                    cur_interval = intervals.pop(x + 1)
                cur_interval[0] = x
                intervals[x] = cur_interval
            elif x - 1 in intervals:
                if intervals[x-1][0] == intervals[x-1][1]:
                    cur_interval = intervals[x-1]
                else:
                    cur_interval = intervals.pop(x - 1)
                cur_interval[1] = x
                intervals[x] = cur_interval
        max_diff = 0
        for x in intervals:
            lower, upper = intervals[x][0], intervals[x][1]
            if upper - lower + 1 > max_diff:
                max_diff = upper - lower + 1
        return max_diff

"""
My first thought: we can use a hashmap, that represents the longest sequence ending at that element

However, I see from the second example: that elements can be added out of order. New plan - we can represent the seen state as a series of
intervals, each of which represents the start and end. We put both elements in the same dictionary.

When we encounter a new element, one of a few things happens:
- We create a new interval, of length 0 (e.x. [1, 1] for value 1)
- We expand an existing interval by one. When we do, we pop the key corresponding to the side of the interval we're expanding.

After expanding an existing interval by one: We check both sides of the interval to see if we can merge two intervals into one.

If we can, then we will pop three elements:
    - Either our min or max (depending on if we expanded to the left or right)
    - Both elements of the other array
    - We will then expand our interval object all the way to the popped min or max, and add another key

Lastly: We will check to see what the length of this interval is, and keep it as a list of intervals.

This solution is O(n)

Some more naive solutions to take a step back:
- We sort the array, then it becomes trivial to identify which sequences are long in O(n)
- We heapify, which is O(n), then start popping.
"""
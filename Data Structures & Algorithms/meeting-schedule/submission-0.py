"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x: (x.start, x.end))
        for i in range(len(intervals) - 1):
            cur, next = intervals[i], intervals[i+1]
            if cur.end > next.start:
                return False
        return True

"""
n**2 solution: compare every soln to every other soln

nlogn soln: sort it, then any two that may overlap 
"""
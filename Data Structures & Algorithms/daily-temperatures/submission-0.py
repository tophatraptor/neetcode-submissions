class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, x in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < x:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

"""
For a given day, we want to return the *first* day after which
we have a warmer day.

Naive solution: O(n**2)

When we traverse forward, we can keep track of how 
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [[0 for _ in range(len(nums))] for _ in range(2)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        dp[1][0] = 0
        dp[1][1] = nums[1]

        for i in range(2, len(nums)):
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + nums[i])
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + nums[i])
        
        return max(dp[0][-2], dp[1][-1])
        
"""
So, in effect, at any given juncture, we need to decide whether to rob house
i, or house i-1, which is based on the cumulative optimals up until that point

We can express this problem as:

rob(i) = max(rob(i-1), rob(i-2) + i)

Which naturally has a recursive self-referential structure and exponential runtime
with a naive recursion.

This is solvable with a 1d DP.

The other thing to remember is that the very last house is adjacent to our first
house. This complicates things a bit; due to our max expression above, we don't
necessarily know whether or not the intermediary maximum that we tracked
involved robbing the first house or not. It additionally creates a circular
dependency, because rob(i-2) for the first house now depends on the value of
the last house.

Fundamentally, there are two ways to represent this solution:
- Either we rob the first house, and we definitely can't take the last cell
- Or we don't rob the first house, and we have the option of taking the last cell

We can calculate these separately, with a two-dimensional DP array.

The first array assumes we rob the first house
The second array explicitly assumes that we *do not* rob the first house.

We can build up both recurrence relationships as we move forward.

Then we compare the maximum at the end.
"""
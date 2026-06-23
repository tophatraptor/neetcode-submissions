class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k**2
        if n == 3:
            return k**3 - k
        dp = [0 for i in range(n)]
        dp[0] = k
        dp[1] = k**2
        dp[2] = k**3 - k
        # n rows x k columns
        # index i, j = the number of ways to paint the i-th post a given color
        # For any given n, k, we have k - 1 options where there is a different color before
        # We have one option which has k - 1 preceding options
        for i in range(3, n):
            dp[i] = (k-1) * dp[i-1] + (k-1) * dp[i-2]
        return dp[-1]

# Snapshot 1
# class Solution:
#     def numWays(self, n: int, k: int) -> int:
#         if n == 1:
#             return k
#         if n == 2:
#             return k**2
#         if n == 3:
#             return k**3 - k

#         dp = [[0 for i in range(k)] for j in range(n)]
#         dp[0] = [1 for i in range(k)]
#         dp[1] = [k**2 for i in range(k)]
#         dp[2] = [k**3 - k for i in range(k)]
#         # n rows x k columns
#         # index i, j = the number of ways to paint the i-th post a given color
#         # For any given n, k, we have k - 1 options where there is a different color before
#         # We have one option which has k - 1 preceding options
#         for i in range(3, n):
#             for j in range(k):
#                 dp[i][j] = sum([dp[i-1][x] for x in range(k) if x != j]) + sum([dp[i-2][x] for x in range(k) if x != j])
#                 # Number of ways beforehand to have a post at i-1 be a different color, and the number of ways to have the post
#                 # at i-2 be a different color, assuming previous color = same as current color
#         return sum(dp[-1])
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for j in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i == 0:
                    prev1 = 0
                else:
                    prev1 = dp[i-1][j]
                if j == 0:
                    prev2 = 0
                else:
                    prev2 = dp[i][j-1]
                if i == 0 or j == 0:
                    prev3 = 0
                else:
                    prev3 = dp[i-1][j-1]
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], prev3 + 1)
                else:
                    dp[i][j] = max(dp[i][j], prev1, prev2)
        return dp[-1][-1]
        # text1 rows
        # text2 columns
        # dp[i][j] is the LCS of the first i characters, inclusive, for text1 i and text2 j
        # If we have a match, we increase LCS by 1 and move both cursors back
        # Otherwise it's max lcs of clice(text1:-1 and slice of text2:-1)
        # We can represent this as max(dp[i-1][j]) and dp[i][j-1]

# We have two cursors that move forward, and either can be selected or not selected
# And we want the longest common subsequence of both, which smells to me of a dynamic programming problem
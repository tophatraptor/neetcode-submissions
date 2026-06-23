class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 for _ in range(amount + 1)]
        for c in coins:
            if c < len(dp):
                dp[c] = 1
        for i in range(len(dp)):
            if dp[i] > 0:
                for c in coins:
                    if i + c <= amount:
                        if dp[i + c] == -1:
                            dp[i + c] = dp[i] + 1
                        else:
                            dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1]
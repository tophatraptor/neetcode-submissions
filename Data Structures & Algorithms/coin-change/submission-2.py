class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] *(amount + 1) # So we can have dp[i] = minimum number of ways to make i
        for c in coins:
            if c <= amount:
                dp[c] = 1
        
        for i in range(1, len(dp)):
            if dp[i] == 0:
                continue
            for c in coins:
                if i + c <= amount:
                    if dp[i+c] == 0:
                        dp[i+c] = dp[i] + 1
                    else:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        if dp[-1] == 0:
            return -1
        return dp[-1]
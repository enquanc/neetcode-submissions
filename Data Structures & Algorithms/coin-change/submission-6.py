class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [float('inf')] * amount
        for i in range(1,amount+1):
            
            for c in coins:
                if c > i:
                    break
                if dp[i] > dp[i-c] +1:
                    dp[i] = dp[i-c] +1

        if dp[-1] == float("inf"): return -1
        return dp[-1]

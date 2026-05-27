class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1,n+1):
            min_len = float('inf')
            j = 1
            while j**2 <= i:
                if min_len > dp[i-j**2] + 1:
                    min_len = dp[i-j**2] + 1
                j += 1
            dp.append(min_len)
        
        return dp[-1]

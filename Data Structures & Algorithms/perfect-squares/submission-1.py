class Solution(object):
    def numSquares(self, n):
        # 一次把 dp 陣列開好，起點為 0，其他預設為無限大
        dp = [0] + [float('inf')] * n
        
        # 預先算好所有可能用到的平方數
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:  # 如果平方數已經大於當前數字，後面的平方數更大，直接跳出
                    break
                # 利用內建的 min() 函數，底層是用 C 語言執行，速度比純 Python 迴圈快
                if dp[i - square] + 1 < dp[i]:
                    dp[i] = dp[i - square] + 1
                    
        return dp[-1]
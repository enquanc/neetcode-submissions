class Solution:
    def numDecodings(self, s: str) -> int:
        # 提早處理空字串或開頭為 "0" 的必死局
        if not s or s[0] == "0":
            return 0
            
        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            # 1. 單獨解碼檢查 (只要當前不是 "0" 就可以繼承前一步)
            if s[i] != "0":
                dp[i] += dp[i-1]
            
            # 2. 合併解碼檢查 (獨立於單獨解碼，必須每次都檢查)
            # 抓取前一位到當前位的雙位數字串
            two_digit = int(s[i-1 : i+1]) 
            
            if 10 <= two_digit <= 26:
                if i == 1:
                    # 如果是前兩個字元合法，直接 +1 種方法
                    dp[i] += 1 
                else:
                    # 如果是後面的字元，繼承前兩步的方法數
                    dp[i] += dp[i-2] 
                    
        return dp[-1]
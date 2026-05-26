class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counts = 0
        
        # 定義一個內部輔助函式來處理擴展邏輯
        def count_palindromes(left: int, right: int) -> int:
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(n):
            # 奇數長度 (以 i 為中心)
            counts += count_palindromes(i, i)
            # 偶數長度 (以 i 和 i+1 為中心)
            counts += count_palindromes(i, i + 1)
            
        return counts
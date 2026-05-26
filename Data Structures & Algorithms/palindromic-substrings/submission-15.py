class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counts = 0
        r = 2
        for i in range(n):
            left = i
            right = i 
            while left >= 0 and right <= n-1:
                if s[left] != s[right]:
                    break
                counts += 1
                left -= 1
                right += 1

            left = i
            right = i+1
            while left >= 0 and right <= n-1:
                if s[left] != s[right]:
                    break
                counts += 1
                left -= 1
                right += 1

        return counts
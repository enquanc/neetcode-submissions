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

    # def count_palindromes(left: int, right: int) -> int:
    #     local_count = 0
    #     while left >= 0 and right < n and s[left] == s[right]:
    #         local_count += 1
    #         left -= 1
    #         right += 1
    #     return local_count
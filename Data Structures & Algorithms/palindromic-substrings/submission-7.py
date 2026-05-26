class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counts = n
        r = 2
        while r <= n:
            for i in range(0, n - r + 1):
                if self.check_palid(s[i:i+r]):
                    counts += 1
            r += 1
        return counts

    def check_palid(self, string):
        left = 0
        right = len(string) - 1
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True
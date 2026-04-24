class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]

        def check_pad(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]
            
        for i in range(len(s)):
            
            # odd case
            if max_len < len(check_pad(i,i)):
                max_len = len(check_pad(i,i))
                max_str = check_pad(i,i)
            # even case 
            if max_len < len(check_pad(i-1,i)):
                max_len = len(check_pad(i-1,i))
                max_str = check_pad(i-1,i)

        return max_str
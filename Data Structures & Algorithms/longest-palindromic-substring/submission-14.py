class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]

        # def check_pad(i, pad):
            
        for i in range(len(s)):
            pad = 1
            # odd case
            while i - pad >= 0 and i + pad <  len(s):
                if s[i - pad] == s[i + pad]:
                    pad += 1
                else:
                    break
            if max_len < 1+2*(pad-1):
                max_len = 2*(pad-1)
                max_str = s[i-pad+1:i+pad]

            pad = 1
            # even case right padding
            while i - pad >= 0 and i + pad -1 <  len(s):
                if s[i - pad] == s[i + pad -1]:
                    pad += 1
                else:
                    break
            if max_len < 2*(pad-1):
                max_len = 2*(pad-1)
                max_str = s[i-pad+1:i+pad-1]

            pad = 1
            # even case left padding
            while i - pad -1 >= 0 and i + pad <  len(s):
                if s[i - pad -1] == s[i + pad]:
                    pad += 1
                else:
                    break

            if max_len < 2*(pad-1):
                max_len = 2*(pad-1)
                max_str = s[i-pad:i+pad]

        return max_str
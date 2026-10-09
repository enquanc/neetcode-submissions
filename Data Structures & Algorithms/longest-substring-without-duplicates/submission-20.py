class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        now = {}
        MAX = 0

        for i in range(len(s)):
            if s[i] in now and left <= now[s[i]]:
                left = now[s[i]] + 1
            now[s[i]] = i
            if MAX < i - left + 1:
                MAX = i - left + 1 
        return MAX

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sw = []
        for i in s:
            if i not in sw:
                sw.append(i)
            else:
                for j in range(len(sw)):
                    if sw[j] == i:
                        sw = sw[j+1:]
                        sw.append(i)
                        break
            if max_len < len(sw):
                max_len = len(sw)
                
        return max_len

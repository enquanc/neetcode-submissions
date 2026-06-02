class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0

        max_w = 1
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

            if len(sw) > max_w:
                max_w = len(sw)

        return max_w
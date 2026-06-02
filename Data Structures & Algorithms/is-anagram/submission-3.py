class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for j in t:
            if j in count:
                count[j] -= 1
            else:
                return False
        
        for v in count.values():
            if v != 0:
                return False
        return True
        
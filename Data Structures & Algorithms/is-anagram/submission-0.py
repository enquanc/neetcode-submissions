class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts = {}

        for i in s:
            if i in counts:
                counts[i] += 1
                continue
            counts[i] = 1

        for j in t:
            if j in counts:
                counts[j] -= 1
                continue
            return False
        
        for val in counts.values():
            if val != 0:
                return False
        return True

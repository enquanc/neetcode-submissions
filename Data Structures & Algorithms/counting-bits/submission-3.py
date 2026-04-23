class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            counts = 0
            m = i
            while m:
                m &= (m-1)
                counts += 1
            result.append(counts)
        return result
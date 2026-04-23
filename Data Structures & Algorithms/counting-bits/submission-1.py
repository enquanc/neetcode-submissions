class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        while n != -1:
            counts = 0
            m = n
            while m:
                m &= (m-1)
                counts += 1
            n -= 1
            result.append(counts)
        return result[::-1]
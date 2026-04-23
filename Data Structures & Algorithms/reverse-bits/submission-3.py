class Solution:
    def reverseBits(self, n: int) -> int:
        index = []
        i = 0
        while n != 0:
            if n & 1:
                index.append(i)
            n = n >> 1
            i += 1
        result = 0

        for val in index:
            result += 1 << (31-val)
        return result
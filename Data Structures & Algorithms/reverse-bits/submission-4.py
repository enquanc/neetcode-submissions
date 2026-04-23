class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        result = 0
        while n != 0:
            if n & 1:
                result += 1 << (31-i)
            n = n >> 1
            i += 1
        return result
class Solution:
    def hammingWeight(self, n: int) -> int:
        counts = 0
        while n != 0:
            if n % 2 == 1:
                counts += 1
            n = n >> 1
        return counts
class Solution:
    def hammingWeight(self, n: int) -> int:
        counts = 0
        while n:
            n &= (n - 1)  # 神奇的一行：直接消去最右邊的 1
            counts += 1
        return counts
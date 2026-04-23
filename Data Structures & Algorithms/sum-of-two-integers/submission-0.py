class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 建立 32-bit 遮罩，等於 2進位的 32 個 1
        MASK = 0xFFFFFFFF
        # 32-bit 正數的最大值
        MAX_INT = 0x7FFFFFFF

        # 當進位 b 不為 0 時持續運算
        while b != 0:
            # a ^ b 是無進位加法
            # (a & b) << 1 是進位
            # Python 特性：利用平行賦值，且每次都要加上 & MASK 限制在 32-bit 內
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 如果 a 小於等於 32-bit 最大正數，代表結果是正數，直接回傳
        # 如果 a 大於 MAX_INT，代表第 32 個位元是 1，在 32-bit 系統中是負數
        # 此時需要還原成 Python 無限精度的負數表示法
        return a if a <= MAX_INT else ~(a ^ MASK)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. 預先分配空間，預設值為 1
        res = [1] * n
        
        # 2. 第一遍遍歷：計算「左側乘積」 (Prefix Product)
        # res[i] 儲存 nums[i] 左邊所有數字的乘積
        prefix_total = 1
        for i in range(n):
            res[i] = prefix_total
            prefix_total *= nums[i]
            
        # 3. 第二遍遍歷：乘以「右側乘積」 (Suffix Product)
        # 用一個變數 suffix_total 同步維護右邊傳過來的乘積
        suffix_total = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_total
            suffix_total *= nums[i]
            
        return res
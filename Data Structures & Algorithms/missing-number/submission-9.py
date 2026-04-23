class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums) # 先把最大的 n 放進來
        
        # 把索引值 i (代表 0~n-1) 和陣列裡的值 nums[i] 全部做 XOR
        for i, num in enumerate(nums):
            result ^= i ^ num
            
        return result
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # 轉換成 set，查詢變 O(1)
        max_l = 0
        
        for n in num_set:
            # 判斷 n 是否為序列的「起點」
            # 如果 n-1 不在 set 裡，代表沒有比它更小的，它是起點
            if (n - 1) not in num_set:
                length = 1
                # 從起點開始往後找連續數字
                while (n + length) in num_set:
                    length += 1
                
                max_l = max(max_l, length)
                
        return max_l
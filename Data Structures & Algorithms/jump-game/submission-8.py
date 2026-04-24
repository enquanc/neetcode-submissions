class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 記錄目前能到達的最遠索引值
        
        for i, jump in enumerate(nums):
            # 如果我們目前站的位置 i，已經超過了我們能抵達的最遠距離，代表我們卡死在前面了
            if i > max_reach:
                return False
            
            # 更新最遠能抵達的距離
            max_reach = max(max_reach, i + jump)
            
            # 如果最遠距離已經涵蓋了終點，就可以提早收工
            if max_reach >= len(nums) - 1:
                return True
                
        return True
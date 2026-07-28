class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_prod = -float('inf')
        min_prod = float('inf')
        
 

        curr_max = 1
        curr_min = 1
        for i in range(len(nums)):
            new_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            new_min = min(nums[i], curr_max * nums[i], curr_min * nums[i])

            curr_max = new_max 
            curr_min = new_min
            
            if curr_max > max_prod:
                max_prod = curr_max
            if curr_min > min_prod:
                min_prod = curr_min

        return max_prod
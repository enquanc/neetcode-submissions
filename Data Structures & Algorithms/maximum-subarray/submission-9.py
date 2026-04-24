class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_val = 0
        max_neg = -1001
        for i in nums:
            current_sum += i
            if current_sum < 0:
                current_sum = 0
            max_val = max(max_val, current_sum)

            if i <= 0:
                max_neg = max(i, max_neg)
        if max_val == 0:
            return max_neg
        return max_val
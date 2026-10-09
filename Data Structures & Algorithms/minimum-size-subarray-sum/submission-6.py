class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        total = 0
        MIN = float("inf")

        for i in range(len(nums)):
            total += nums[i]
            if target <= total:
                while target <= total:
                    total -= nums[start]
                    start += 1
                if i - start + 2 < MIN: # 1 for len 1 for last one number
                    MIN = i -start + 2
        if MIN == float("inf"):
            return 0
        return MIN
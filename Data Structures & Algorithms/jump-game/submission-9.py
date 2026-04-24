class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        path = [0] * n
        i = 0
        while i >= 0:
            if i == (n-1):
                return True
            if nums[i] != 0 and not path[i]:
                path[i] = 1
                i = min(i+nums[i], n-1)
            else:
                path[i] = 1
                i -= 1

        return False
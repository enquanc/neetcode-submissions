class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0                      # 下一個非零該放的位置
        for i in range(len(nums)):     # i 負責掃描
            if nums[i] != 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        p_z = 0
        p_nz = 0

        while p_z < n and p_nz < n:
            if nums[p_z] == 0 and nums[p_nz] != 0:
                if p_nz < p_z:
                    p_nz += 1
                    continue
                nums[p_z], nums[p_nz] = nums[p_nz], nums[p_z]
                p_z += 1
                p_nz += 1
            elif nums[p_z] != 0:
                p_z += 1
            elif nums[p_nz] == 0:
                p_nz += 1
            
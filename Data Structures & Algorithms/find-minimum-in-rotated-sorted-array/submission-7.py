class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        mid = (left+right) // 2
        while right > left:
            if nums[right] > nums[mid]:
                right = mid
                mid = (left+right) // 2
            elif nums[right] <= nums[mid]:
                left = mid+1
                mid = (left+right) // 2
        return nums[mid]
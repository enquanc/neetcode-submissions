class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        output = []

        for i in range(n-2):
            left =  i + 1
            right = n - 1
            target = 0 - nums[i]
            
            if i !=0 and nums[i] == nums[i-1]:
                continue
            if target < 0:
                break

            while left < right:
                total = nums[left] + nums[right]
                if  total == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif total > target:
                    right -= 1
                elif total < target:
                    left += 1

        return output
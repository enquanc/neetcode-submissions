class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        output = []
        
        temp = 1
        for i in nums:
            left.append(temp)
            temp = temp * i
        
        temp = 1
        nums = nums[::-1]
        for j in nums:
            right.append(temp)
            temp = temp * j
        right = right[::-1]


        for k in range(len(nums)):
            output.append(left[k] * right[k])
        
        return output

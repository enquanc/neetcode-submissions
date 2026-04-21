class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre_list = []


        total = 1
        for i in nums:
            pre_list.append(total)
            total = total * i

        # pre_list = pre_list[::-1]

        total = 1
        for j in range(len(nums)-1, -1, -1):
            pre_list[j] = pre_list[j] * total
            total = total * nums[j]

        
        # pre_list = pre_list[::-1]
        return pre_list  
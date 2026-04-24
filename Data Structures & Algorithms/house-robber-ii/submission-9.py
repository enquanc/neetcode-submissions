class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return nums[0]

        def rob_sub(arr):
            case1 = 0
            case2 = 0
            current = 0
            for i in range(len(arr)):
                # case1 : rob
                # case2 : no rob
                current = max(case1 + arr[i], case2)

                # new case1 can rob, be old case2
                case1 = case2
                case2 = current

            return current
        
        # no rob first
        return max(rob_sub(nums[:-1]), rob_sub(nums[1:]))
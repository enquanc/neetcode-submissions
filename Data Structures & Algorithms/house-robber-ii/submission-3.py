class Solution:
    def rob(self, nums: List[int]) -> int:
        case1 = 0
        case2 = 0

        current_A = 0
        current_B = 0
        use_first = True
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)-1):
            # case1 : rob
            # case2 : no rob
            current_A = max(case1 + nums[i], case2)

            # new case1 can rob, be old case2
            case1 = case2
            case2 = current_A

        case1 = 0
        case2 = 0
        for i in range(1, len(nums)):
            # case1 : rob
            # case2 : no rob
            current_B = max(case1 + nums[i], case2)

            # new case1 can rob, be old case2
            case1 = case2
            case2 = current_B

        return max(current_A, current_B)
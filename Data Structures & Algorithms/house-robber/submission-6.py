class Solution:
    def rob(self, nums: List[int]) -> int:
        case1 = 0
        case2 = 0

        for i in range(len(nums)):

            # case1 : rob
            # case2 : no rob
            current = max(case1 + nums[i], case2)

            # 這樣下個case1才能再搶，所以等於沒搶的case2
            case1 = case2
            
            case2 = current

        return current
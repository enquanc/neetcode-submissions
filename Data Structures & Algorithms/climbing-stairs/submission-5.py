class Solution:
    def climbStairs(self, n: int) -> int:
        # def climb(t):
        #     if t == 1 :
        #         return 1
        #     elif t == 2:
        #         return 2
        #     return climb(t-1) + climb(t-2)
        steps = []
        for i in range(n):
            
            if i == 0:
                steps.append(1)
            elif i ==1:
                steps.append(2)
            else:
                steps.append(steps[-1]+steps[-2])

        return steps[-1]
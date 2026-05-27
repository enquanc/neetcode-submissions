class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        for i in range(n):
            if i == 0:
                steps.append(1)
            elif i ==1:
                steps.append(2)
            else:
                steps.append(steps[-1]+steps[-2])

        return steps[-1]
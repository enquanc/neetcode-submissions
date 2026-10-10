class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for cur in intervals[1:]:
            if cur[0] <= result[-1][1]:                  # 重疊：cur 的起點和 result[-1] 的終點比較
                result[-1][1] = max(cur[1], result[-1][1])                  # 更新 result[-1] 的終點
            else:
                result.append(cur)                  # 不重疊
        return result
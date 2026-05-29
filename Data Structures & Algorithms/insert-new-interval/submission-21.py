class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        result = []
        i = 0
        while i < len(intervals):
            # check start
            if intervals[i][1] < start:
                result.append(intervals[i])
        
            # check end
            elif intervals[i][0] > end:
                result.append([start,end])
                result = result + intervals[i:]
                return result

            # check overlap
            else:
                start = min(intervals[i][0], start)
                end = max(intervals[i][1], end)

            i += 1
        
        result.append([start,end])
        return result

            